%global _vpath_builddir .
Name:           pdiplugin-fti
Version:        master
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        FTI plugin for the PDI Data Interface
Url:            https://gitlab.maisondelasimulation.fr/pdidev/pdi
Source0:        https://gitlab.maisondelasimulation.fr/pdidev/pdi/-/archive/%{version}/pdi-%{version}.tar.bz2
BuildRequires:  gcc, gcc-c++, make, cmake >= 3.5
BuildRequires:  pdi-devel = %{version}

%description
The PDI fti plugin interfaces PDI with FTI.

%package openmpi
Summary: FTI plugin for the PDI Data Interface, OpenFTI version
BuildRequires: fti-openmpi-devel

%description openmpi
The PDI fti plugin interfaces PDI with FTI.

%package mpich
Summary: FTI plugin for the PDI Data Interface, MPich version
BuildRequires: fti-mpich-devel

%description mpich
The PDI fti plugin interfaces PDI with FTI.

%prep
%autosetup -n pdi-%{version}

%build
mkdir build-openmpi
pushd build-openmpi
module load mpi/openmpi-%{_arch}
%cmake3 \
	-DCMAKE_BUILD_TYPE=Release \
	-DINSTALL_PDIPLUGINDIR=%{_libdir}/openmpi/lib/pdi/plugins_%{version}/ \
	../plugins/fti
%make_build
module purge
popd
mkdir build-mpich
pushd build-mpich
module load mpi/mpich-%{_arch}
%cmake3 \
	-DCMAKE_BUILD_TYPE=Release \
	-DINSTALL_PDIPLUGINDIR=%{_libdir}/mpich/lib/pdi/plugins_%{version}/ \
	../plugins/fti
%make_build
module purge
popd

%install
rm -rf $RPM_BUILD_ROOT
module load mpi/openmpi-%{_arch}
%make_install -C build-openmpi
module purge
module load mpi/mpich-%{_arch}
%make_install -C build-mpich
module purge

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
* Sat Mar 27 2021 - Pending release on master <julien.bigot@cea.fr>
- Upstream release master
* Sat Feb 27 2021 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.0.1
* Thu Jan 28 2021 - Julien Bigot <julien.bigot@.cea.fr>
- Initial Release
