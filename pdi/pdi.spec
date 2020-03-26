%define _sover  0
Name:           pdi
Version:        0.6.1
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        the Portable Data Interface library
Url:            https://gitlab.maisondelasimulation.fr/pdidev/pdi
Source0:        https://gitlab.maisondelasimulation.fr/pdidev/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%name-root
%if 0%{?centos_version} > 0 && 0%{?centos_version} < 800
BuildRequires:  devtoolset-6
BuildRequires:  cmake3 >= 3.5
%else
BuildRequires:  cmake >= 3.5
%endif
BuildRequires:  paraconf-devel >= 0.4.0, spdlog-devel >= 1.3.1

%description
PDI is a library that aims to decouple high-performance simulation
codes from Input/Output concerns.

%package devel
Summary:        Development files for %{name}
Requires:       lib%{name}%{_sover}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       paraconf-devel >= 0.4.0, spdlog-devel >= 1.3.1

%description devel
The %{name}-devel package contains C/C++ header files for developing
applications or plugins that use %{name}.

%package     -n lib%{name}%{_sover}
Summary:        the Portable Data Interface library

%description -n lib%{name}%{_sover}
PDI is a library that aims to decouple high-performance simulation
codes from Input/Output concerns.

%prep
%autosetup
mkdir -p %{_target_platform}

%build
%if 0%{?centos_version} > 0 && 0%{?centos_version} < 800
set +e
source scl_source enable devtoolset-6
set -e
%endif
pushd %{_target_platform}
    %cmake3 \
    -DBUILD_DOCUMENTATION=OFF \
    -DBUILD_TESTING=OFF \
    -DBUILD_FORTRAN=OFF \
    ../pdi
popd
%make_build -C %{_target_platform}

%install
rm -rf $RPM_BUILD_ROOT
%make_install -C %{_target_platform}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -n lib%{name}%{_sover} -p /sbin/ldconfig

%postun -n lib%{name}%{_sover} -p /sbin/ldconfig

%files devel
%license LICENSE
%doc README.md
%{_bindir}/*
%{_includedir}/
%{_libdir}/lib%{name}.so
%{_datadir}/%{name}/cmake
%{_datadir}/%{name}/env.bash

%files -n lib%{name}%{_sover}
%{_libdir}/lib%{name}.so.%{_sover}*

%changelog
* Tue Feb 18 2020 - Karol Sierociński ksiero@man.poznan.pl
- Initial Release
