%global _vpath_builddir .
Name:           pdiplugin-mpi
Version:        0.6.1
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        MPI plugin for the Portable Data Interface library
Url:            https://gitlab.maisondelasimulation.fr/pdidev/pdi
Source0:        https://gitlab.maisondelasimulation.fr/pdidev/pdi/-/archive/%{version}/pdi-%{version}.tar.gz
%if 0%{?centos_ver} > 0 && 0%{?centos_ver} < 800
BuildRequires:  devtoolset-6, cmake3 >= 3.5
%else
BuildRequires:  cmake >= 3.10, gcc, gcc-c++, gcc-gfortran
%endif
BuildRequires:  make
BuildRequires:  pdi-devel = %{version}, openmpi-devel

%description
The PDI mpi plugin interfaces PDI with MPI.

%package openmpi
Summary: MPI plugin for the Portable Data Interface library, OpenMPI version
BuildRequires:  hdf5-openmpi-devel >= 1.8

%description openmpi
The PDI mpi plugin interfaces PDI with MPI.

%package mpich
Summary: MPI plugin for the Portable Data Interface library. MPich version
BuildRequires:  hdf5-mpich-devel >= 1.8

%description mpich
The PDI mpi plugin interfaces PDI with MPI.

%prep
%autosetup -n pdi-%{version}

%build
module load mpi/openmpi-%{_arch}
%if 0%{?centos_ver} > 0 && 0%{?centos_ver} < 800
set +e
source scl_source enable devtoolset-6
set -e
%endif
mkdir build-openmpi
pushd build-openmpi
module load mpi/openmpi-%{_arch}
%cmake3 \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_LIBDIR=%{_libdir}/openmpi/lib \
	../plugins/mpi
%make_build
module purge
popd
mkdir build-mpich
pushd build-mpich
module load mpi/mpich-%{_arch}
%cmake3 \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_LIBDIR=%{_libdir}/mpich/lib \
	../plugins/mpi
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
%{_libdir}/openmpi/lib/lib*.so

%files mpich
%license LICENSE
%doc README.md
%{_libdir}/mpich/lib/lib*.so

%changelog
* Mon May 11 2020 - Julien Bigot <julien.bigot@cea.fr>
- Initial Release
