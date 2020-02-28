%define _sover  0
Name:           libparaconf
Version:        0.4.3
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        A library that provides a simple query language to access a Yaml tree on top of libyaml
Url:            https://gitlab.maisondelasimulation.fr/jbigot/libparaconf
Source0:        https://gitlab.maisondelasimulation.fr/jbigot/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%name-root
%if 0%{?centos_version} > 0 && 0%{?centos_version} < 800

BuildRequires:  cmake3 >= 3.2
%else
BuildRequires:  cmake >= 3.2
%endif
BuildRequires:  libyaml-devel

%description
Paraconf is a library that provides a simple query language to
access a Yaml tree on top of libyaml.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{_sover}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       libyaml-devel

%description devel
The %{name}-devel package contains C++ header files for developing
applications that use %{name}.

%package     -n %{name}%{_sover}
Summary:        C++ logging library

%description -n %{name}%{_sover}
Paraconf is a library that provides a simple query language to
access a Yaml tree on top of libyaml.

%prep
%autosetup
mkdir -p %{_target_platform}

%build
pushd %{_target_platform}
    %cmake3 \
    -DBUILD_FORTRAN=OFF \
    -DCMAKE_BUILD_TYPE=Release \
    ../paraconf
popd
%make_build -C %{_target_platform}

%install
rm -rf $RPM_BUILD_ROOT
%make_install -C %{_target_platform}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -n %{name}%{_sover} -p /sbin/ldconfig

%postun -n %{name}%{_sover} -p /sbin/ldconfig

%files devel
%license LICENSE
%doc README.md

%{_includedir}/
%{_libdir}/%{name}.so
%{_datadir}/paraconf/cmake/

%files -n %{name}%{_sover}
%{_libdir}/%{name}.so.%{_sover}*

%changelog
* Tue Feb 6 2020 - Karol Sierociński ksiero@man.poznan.pl
- Initial Release
