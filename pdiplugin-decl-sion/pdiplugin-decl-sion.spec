%global _vpath_builddir .
Name:           pdiplugin-decl-sion
Version:        master
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        SIONlib plugin for the PDI Data Interface
Url:            https://gitlab.maisondelasimulation.fr/pdidev/pdi
Source0:        https://gitlab.maisondelasimulation.fr/pdidev/pdi/-/archive/%{version}/pdi-%{version}.tar.bz2
BuildRequires:  gcc, gcc-c++, make, cmake >= 3.5
BuildRequires:  pdi-devel = %{version}

%description
The PDI decl-sion plugin interfaces PDI with SIONlib.

%package openmpi
Summary: SIONlib plugin for the PDI Data Interface, OpenSIONlib version
BuildRequires: sionlib-openmpi-devel

%description openmpi
The PDI decl-sion plugin interfaces PDI with SIONlib.

%package mpich
Summary: SIONlib plugin for the PDI Data Interface, MPich version
BuildRequires: sionlib-mpich-devel

%description mpich
The PDI decl-sion plugin interfaces PDI with SIONlib.

%prep
%autosetup -n pdi-%{version}

%build
for MPI_VERSION in openmpi mpich
do
mkdir build-${MPI_VERSION}
pushd build-${MPI_VERSION}
module load mpi/${MPI_VERSION}-%{_arch}
ls ${MPI_BIN}
%cmake3 \
	-DCMAKE_BUILD_TYPE=Release \
	-DINSTALL_PDIPLUGINDIR=${MPI_LIB}/pdi/plugins_%{version}/ \
	../plugins/decl_sion
%make_build
module purge
popd
done

%install
rm -rf $RPM_BUILD_ROOT
for MPI_VERSION in openmpi mpich
do
module load mpi/${MPI_VERSION}-%{_arch}
%make_install -C build-${MPI_VERSION}
module purge
done

%clean
rm -rf $RPM_BUILD_ROOT

%post   openmpi -p /sbin/ldconfig

%postun openmpi -p /sbin/ldconfig

%post   mpich -p /sbin/ldconfig

%postun mpich -p /sbin/ldconfig

%files openmpi
%license LICENSE
%doc README.md
%{_libdir}/openmpi/lib/pdi/*/lib*.so

%files mpich
%license LICENSE
%doc README.md
%{_libdir}/mpich/lib/pdi/*/lib*.so

%changelog
* Sat Feb 27 2021 - Pending release on master <julien.bigot@cea.fr>
- Upstream release master
* Thu Jan 28 2021 - Julien Bigot <julien.bigot@.cea.fr>
- Initial Release
