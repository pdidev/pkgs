%global _vpath_builddir .
%define _sover  1
Name:           pdi
Version:        1.2.1
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        the PDI Data Interface
Url:            https://gitlab.maisondelasimulation.fr/pdidev/pdi
Source0:        https://gitlab.maisondelasimulation.fr/pdidev/pdi/-/archive/%{version}/pdi-%{version}.tar.bz2
BuildRequires:  gcc, gcc-c++, gcc-gfortran, make, cmake >= 3.10
BuildRequires:  gtest-devel >= 1.8.0 , gmock-devel >= 1.8.0
BuildRequires:  zpp, paraconf-devel >= 0.4.0, spdlog-devel >= 1.3.1
BuildRequires:  pybind11-devel >= 2.3.0, python3-devel >= 3.5, python3-numpy

%description
PDI is a library that aims to decouple high-performance simulation
codes from Input/Output concerns.

%package devel
Summary:        Development files for %{name}
Requires:       gcc-gfortran%{_isa}
Requires:       lib%{name}-f90.%{_sover}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       paraconf-devel >= 0.4.0
Requires:       pybind11-devel >= 2.3.0
Requires:       python3-%{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       python3-devel >= 3.5, python3-numpy
Requires:       spdlog-devel >= 1.3.1

%description devel
The %{name}-devel package contains C/C++ header files for developing
applications or plugins that use %{name}.

%package     -n lib%{name}%{_sover}
Summary:        the PDI Data Interface

%description -n lib%{name}%{_sover}
PDI is a library that aims to decouple high-performance simulation
codes from Input/Output concerns.

%package     -n lib%{name}-f90.%{_sover}
Summary:        the PDI Data Interface
Requires:       lib%{name}%{_sover}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n lib%{name}-f90.%{_sover}
PDI is a library that aims to decouple high-performance simulation
codes from Input/Output concerns.

%package     -n lib%{name}-pysupport.%{_sover}
Summary:        the PDI Data Interface

%description -n lib%{name}-pysupport.%{_sover}
PDI is a library that aims to decouple high-performance simulation
codes from Input/Output concerns.

%package     -n python3-%{name}
Summary:        the PDI Data Interface
Requires:       lib%{name}-pysupport.%{_sover}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-%{name}
PDI is a library that aims to decouple high-performance simulation
codes from Input/Output concerns.

%prep
%autosetup

%build
%cmake3 \
	-DBUILD_DOCUMENTATION=OFF \
	-DBUILD_PYTHON=ON \
	-DINSTALL_FMODDIR=%{_fmoddir} \
	-DINSTALL_PDIPLUGINDIR=%{_libdir}/pdi/plugins_%{version}/ \
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

%post   -n lib%{name}-pysupport.%{_sover} -p /sbin/ldconfig

%postun -n lib%{name}-pysupport.%{_sover} -p /sbin/ldconfig

%files devel
%license LICENSE
%doc README.md
%{_bindir}/*
%{_includedir}/
%{_fmoddir}/*
%{_libdir}/lib*.so
%{_datadir}/%{name}

%files -n lib%{name}%{_sover}
%{_libdir}/lib%{name}.so.*

%files -n lib%{name}-f90.%{_sover}
%{_libdir}/lib%{name}_f90.so.*

%files -n lib%{name}-pysupport.%{_sover}
%{_libdir}/lib%{name}_pysupport.so.*

%files -n python3-%{name}
%{python3_sitearch}/pdi/*

%changelog
* Fri Jun 18 2021 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.2.1
* Wed Jun 16 2021 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.2.0
* Sat Mar 27 2021 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.1.0
* Sat Feb 27 2021 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.0.1
* Thu Jan 28 2021 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.0.0
* Wed Nov 25 2020 - Julien Bigot <julien.bigot@cea.fr>
- Version bump to 0.6.5
* Tue Oct 20 2020 - Julien Bigot <julien.bigot@cea.fr>
- Version bump to 0.6.3
* Thu Oct 15 2020 - Julien Bigot <julien.bigot@cea.fr>
- Version bump to 0.6.2
* Mon May 11 2020 - Julien Bigot <julien.bigot@cea.fr>
- Version bump to 0.6.1
- Added support for Fortran & Python
* Tue Feb 18 2020 - Karol Sierociński ksiero@man.poznan.pl
- Initial Release
