%global _vpath_builddir .
%define _sover  1
Name:           fti
Version:        1.5.1
Release:        0
License:        LGPLv2
Group:          Development/Libraries/C and C++
Summary:        a library for fast and efficient multilevel checkpointing
Url:            https://github.com/leobago/%{name}
Source0:        https://github.com/leobago/%{name}/archive/v%{version}.tar.gz
BuildRequires:  gcc, gcc-c++, make, cmake >= 3.4
BuildRequires:  openssl-devel

%description
FTI stands for Fault Tolerance Interface and is a library that aims to give
computational scientists the means to perform fast and efficient multilevel
checkpointing in large scale supercomputers

%package headers
Summary: a library for fast and efficient multilevel checkpointing, OpenMPI version
BuildRequires: openmpi-devel
Requires: openssl-devel
Requires: openmpi-devel

%description headers
FTI stands for Fault Tolerance Interface and is a library that aims to give
computational scientists the means to perform fast and efficient multilevel
checkpointing in large scale supercomputers

%package openmpi-devel
Summary: a library for fast and efficient multilevel checkpointing, OpenMPI version
BuildRequires: openmpi-devel
Requires: openssl-devel
Requires: openmpi-devel
Requires: %{name}-headers = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: lib%{name}-openmpi-%{_sover}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description openmpi-devel
FTI stands for Fault Tolerance Interface and is a library that aims to give
computational scientists the means to perform fast and efficient multilevel
checkpointing in large scale supercomputers

%package -n lib%{name}-openmpi-%{_sover}
Summary: a library for fast and efficient multilevel checkpointing, OpenMPI version
BuildRequires:  openmpi-devel

%description -n lib%{name}-openmpi-%{_sover}
FTI stands for Fault Tolerance Interface and is a library that aims to give
computational scientists the means to perform fast and efficient multilevel
checkpointing in large scale supercomputers

%package mpich-devel
Summary: a library for fast and efficient multilevel checkpointing, MPich version
BuildRequires: mpich-devel
Requires: openssl-devel
Requires: mpich-devel
Requires: %{name}-headers = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: lib%{name}-mpich-%{_sover}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description mpich-devel
FTI stands for Fault Tolerance Interface and is a library that aims to give
computational scientists the means to perform fast and efficient multilevel
checkpointing in large scale supercomputers

%package -n lib%{name}-mpich-%{_sover}
Summary: a library for fast and efficient multilevel checkpointing, MPich version
BuildRequires:  mpich-devel

%description -n lib%{name}-mpich-%{_sover}
FTI stands for Fault Tolerance Interface and is a library that aims to give
computational scientists the means to perform fast and efficient multilevel
checkpointing in large scale supercomputers

%prep
%autosetup

%build
for MPI_VERSION in openmpi mpich
do
mkdir -p build-${MPI_VERSION}
pushd build-${MPI_VERSION}
module load mpi/${MPI_VERSION}-%{_arch}
%cmake3 \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_LIBDIR=${MPI_LIB} \
	-DINSTALL_CMAKEDIR=${MPI_BIN}/../share/FTI/cmake \
	-DENABLE_OPENSSL=ON \
	..
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

%files headers
%license LICENSE
%doc README.md
%{_includedir}/*

%files openmpi-devel
%license LICENSE
%doc README.md
%{_libdir}/openmpi/share/FTI
%{_libdir}/openmpi/lib/*.a

%files -n lib%{name}-openmpi-%{_sover}
%license LICENSE
%doc README.md
%{_libdir}/openmpi/lib/*.so

%files mpich-devel
%license LICENSE
%doc README.md
%{_libdir}/mpich/share/FTI
%{_libdir}/mpich/lib/*.a

%files -n lib%{name}-mpich-%{_sover}
%license LICENSE
%doc README.md
%{_libdir}/mpich/lib/*.so

%changelog
* Wed Nov 25 2020 - Julien Bigot <julien.bigot@cea.fr>
- Initial Release
