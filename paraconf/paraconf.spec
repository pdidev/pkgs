%global _vpath_builddir .
%define _sover  0
Name:           paraconf
Version:        0.4.9
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        A library that provides a simple query language to access a Yaml tree on top of libyaml
Url:            https://github.com/pdidev/%{name}
Source0:        https://github.com/pdidev/%{name}/archive/%{version}.tar.gz
BuildRoot:      %{_tmppath}/%name-root
BuildRequires:  gcc, gcc-gfortran, make, cmake >= 3.5
BuildRequires:  pkgconfig(yaml-0.1)

%description
Paraconf is a library that provides a simple query language to
access a Yaml tree on top of libyaml.

%package     -n lib%{name}%{_sover}
Summary:        C++ logging library

%description -n lib%{name}%{_sover}
Paraconf is a library that provides a simple query language to
access a Yaml tree on top of libyaml.
applications that use %{name}.

%package     -n lib%{name}-f90.%{_sover}
Summary:        C++ logging library
Requires:       lib%{name}%{_sover} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n lib%{name}-f90.%{_sover}
Paraconf is a library that provides a simple query language to
access a Yaml tree on top of libyaml.

%package devel
Summary:        Development files for %{name}
Requires:       lib%{name}-f90.%{_sover} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       libyaml-devel
Requires:       gcc-gfortran%{_isa}

%description devel
The %{name}-devel package contains C/C++/F90 header files for developing
applications that use %{name}.

%prep
%autosetup

%build
%cmake3 \
	-DCMAKE_BUILD_TYPE=Release \
	-DINSTALL_FMODDIR=%{_fmoddir} \
	-DINSTALL_FINCLUDEDIR=%{_fmoddir} \
	paraconf
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


%files devel
%license LICENSE
%doc README.md

%{_includedir}/*
%{_fmoddir}/*.mod
%{_libdir}/lib%{name}*.so
%{_datadir}/paraconf/cmake/


%files -n lib%{name}%{_sover}
%{_libdir}/lib%{name}.so.%{_sover}*


%files -n lib%{name}-f90.%{_sover}
%{_libdir}/lib%{name}_f90.so.%{_sover}*


%changelog
* Mon May 11 2020 - Julien Bigot <julien.bigot@cea.fr>
- Version bump to 0.4.9
* Thu Feb 6 2020 - Karol Sierociński ksiero@man.poznan.pl
- Initial Release
