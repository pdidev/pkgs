%define _sover  0
Name:           pdi
Version:        0.6.1
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        the Portable Data Interface library
Url:            https://gitlab.maisondelasimulation.fr/pdidev/pdi
Source0:        https://gitlab.maisondelasimulation.fr/pdidev/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
%if 0%{?centos_ver} > 0 && 0%{?centos_ver} < 800
BuildRequires:  devtoolset-6, cmake3 >= 3.5
%else
BuildRequires:  cmake >= 3.10, gcc, gcc-c++, gcc-gfortran
BuildRequires:  gtest-devel >= 1.8.0 , gmock-devel >= 1.8.0,
%endif
BuildRequires:  make
BuildRequires:  zpp, paraconf-devel >= 0.4.0, spdlog-devel >= 1.3.1
BuildRequires:  pybind11-devel >= 2.3.0, python3-devel, python3-numpy

%description
PDI is a library that aims to decouple high-performance simulation
codes from Input/Output concerns.

%package devel
Summary:        Development files for %{name}
Requires:       lib%{name}-f90.%{_sover}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       python3-%{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       paraconf-devel >= 0.4.0
Requires:       spdlog-devel >= 1.3.1
Requires:       pybind11-devel >= 2.3.0
Requires:       python3-devel, python3-numpy

%description devel
The %{name}-devel package contains C/C++ header files for developing
applications or plugins that use %{name}.

%package     -n lib%{name}%{_sover}
Summary:        the Portable Data Interface library

%description -n lib%{name}%{_sover}
PDI is a library that aims to decouple high-performance simulation
codes from Input/Output concerns.

%package     -n lib%{name}-f90.%{_sover}
Summary:        the Portable Data Interface library
Requires:       lib%{name}%{_sover}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n lib%{name}-f90.%{_sover}
PDI is a library that aims to decouple high-performance simulation
codes from Input/Output concerns.

%package     -n lib%{name}-python.%{_sover}
Summary:        the Portable Data Interface library

%description -n lib%{name}-python.%{_sover}
PDI is a library that aims to decouple high-performance simulation
codes from Input/Output concerns.

%package     -n python3-%{name}
Summary:        the Portable Data Interface library
Requires:       lib%{name}-python.%{_sover}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-%{name}
PDI is a library that aims to decouple high-performance simulation
codes from Input/Output concerns.

%prep
%autosetup

%build
%if 0%{?centos_ver} > 0 && 0%{?centos_ver} < 800
set +e
source scl_source enable devtoolset-6
set -e
%endif
%cmake3 \
	-DBUILD_DOCUMENTATION=OFF \
	-DBUILD_PYTHON=ON \
	-DINSTALL_FMODDIR=%{_fmoddir} \
	-DINSTALL_FINCLUDEDIR=%{_fmoddir} \
	-DCMAKE_BUILD_TYPE=Release \
	pdi
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%post   -n lib%{name}%{_sover} -p /sbin/ldconfig

%postun -n lib%{name}%{_sover} -p /sbin/ldconfig

%post   -n lib%{name}-f90.%{_sover} -p /sbin/ldconfig

%postun -n lib%{name}-f90.%{_sover} -p /sbin/ldconfig

%post   -n lib%{name}-python.%{_sover} -p /sbin/ldconfig

%postun -n lib%{name}-python.%{_sover} -p /sbin/ldconfig

%files devel
%license LICENSE
%doc README.md
%{_bindir}/*
%{_includedir}/
%{_fmoddir}/*
%{_libdir}/lib*.so
%{_datadir}/%{name}

%files -n lib%{name}%{_sover}
%{_libdir}/lib%{name}.so.%{_sover}*

%files -n lib%{name}-f90.%{_sover}
%{_libdir}/lib%{name}_f90.so.%{_sover}*

%files -n lib%{name}-python.%{_sover}
%{_libdir}/lib%{name}_python.so.%{_sover}*

%files -n python3-%{name}
%{python3_sitearch}/pdi/*

%changelog
* Tue Feb 18 2020 - Karol Sierociński ksiero@man.poznan.pl
- Initial Release
