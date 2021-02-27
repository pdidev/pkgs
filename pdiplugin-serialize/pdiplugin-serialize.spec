%global _vpath_builddir .
Name:           pdiplugin-serialize
Version:        v1.0
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        Serialize plugin for the PDI Data Interface
Url:            https://gitlab.maisondelasimulation.fr/pdidev/pdi
Source0:        https://gitlab.maisondelasimulation.fr/pdidev/pdi/-/archive/%{version}/pdi-%{version}.tar.bz2
BuildRequires:  gcc, gcc-c++, make, cmake >= 3.5
BuildRequires:  pdi-devel = %{version}

%description
The PDI serialize plugin supports serialization of complex types into a
representation all I/O libraries should support.

%prep
%autosetup -n pdi-%{version}

%build
%cmake3 \
	-DCMAKE_BUILD_TYPE=Release \
	plugins/serialize
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_libdir}/pdi/*/lib*.so

%changelog
* Sat Feb 27 2021 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release v1.0
* Thu Jan 28 2021 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.0.0
