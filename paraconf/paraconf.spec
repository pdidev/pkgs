%define _sover  1
Name:           paraconf
Version:        1.2.1
Release:        1
License:        MIT
Summary:        A library that provides a simple query language to access a Yaml tree on top of libyaml
Url:            https://github.com/pdidev/%{name}
Source0:        https://github.com/pdidev/%{name}/archive/%{version}.tar.gz
BuildRequires:  gcc, gcc-c++, gcc-gfortran, make, cmake >= 3.22
BuildRequires:  pkgconfig(yaml-0.1)

%description
Paraconf is a library that provides a simple query language to
access a Yaml tree on top of libyaml.

%package     -n lib%{name}%{_sover}
Summary:        A simple query language to access a Yaml tree on top of libyaml

%description -n lib%{name}%{_sover}
Paraconf is a library that provides a simple query language to
access a Yaml tree on top of libyaml.

%package     -n lib%{name}-f90.%{_sover}
Summary:        Fortran interface of Paraconf
Requires:       lib%{name}%{_sover}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n lib%{name}-f90.%{_sover}
Paraconf is a library that provides a simple query language to
access a Yaml tree on top of libyaml.

%package devel
Summary:        Development files for %{name}
Requires:       lib%{name}-f90.%{_sover}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       libyaml-devel
Requires:       gcc-gfortran%{_isa}

%description devel
The %{name}-devel package contains C/C++/F90 header files for developing
applications that use %{name}.

%prep
%autosetup

%build
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DINSTALL_FMODDIR=%{_fmoddir} \
	-DPARACONF_BUILD_EXAMPLE=OFF
%cmake_build

%install
%cmake_install

%files devel
%license LICENSES/MIT.txt
%doc README.md

%{_includedir}/*
%{_fmoddir}/*.mod
%{_libdir}/lib%{name}*.so
%{_datadir}/paraconf/


%files -n lib%{name}%{_sover}
%{_libdir}/lib%{name}.so.%{_sover}*	


%files -n lib%{name}-f90.%{_sover}
%{_libdir}/lib%{name}_f90.so.%{_sover}*


%changelog
* Wed Nov 04 2026 - Julien Bigot <julien.bigot@cea.fr>
- own the directories the package installs, and only those; drop obsolete Group tags, buildroot cleanup and ldconfig scriptlets
- fix the copy-pasted summaries and descriptions of the library packages
* Mon Oct 19 2026 - Julien Bigot <julien.bigot@cea.fr>
- Version bump to 1.2.1
* Fri Jun 12 2026 - Julien Bigot <julien.bigot@cea.fr>
- Version bump to 1.1.1
* Fri Jan 30 2026 - Julien Bigot <julien.bigot@cea.fr>
- Version bump to 1.0.3
* Wed Dec 17 2025 - Julien Bigot <julien.bigot@cea.fr>
- Version bump to 1.0.1
* Wed Mar 08 2023 - Julien Bigot <julien.bigot@cea.fr>
- Version bump to 1.0.0
* Wed Oct 12 2022 - Julien Bigot <julien.bigot@cea.fr>
- Version bump to 0.4.16
* Sat Mar 05 2022 - Julien Bigot <julien.bigot@cea.fr>
- updated cmake invocation to be compatible with Fedora 36+
* Mon Jan 03 2022 - Julien Bigot <julien.bigot@cea.fr>
- Version bump to 0.4.15
* Mon May 11 2020 - Julien Bigot <julien.bigot@cea.fr>
- Version bump to 0.4.9
* Thu Feb 6 2020 - Karol Sierociński ksiero@man.poznan.pl
- Initial Release
