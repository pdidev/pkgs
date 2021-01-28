%global _vpath_builddir .
Name:           pdiplugin-set-value
Version:        1.0.0
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        Set Value plugin for the PDI Data Interface
Url:            https://gitlab.maisondelasimulation.fr/pdidev/pdi
Source0:        https://gitlab.maisondelasimulation.fr/pdidev/pdi/-/archive/%{version}/pdi-%{version}.tar.bz2
BuildRequires:  gcc, gcc-c++, make, cmake >= 3.5
BuildRequires:  pdi-devel = %{version}

%description
The PDI Set Value plugin supports setting PDI metadata values from PDI itself.

%prep
%autosetup -n pdi-%{version}

%build
%cmake3 \
	-DCMAKE_BUILD_TYPE=Release \
	plugins/set_value
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
* Thu Jan 28 2021 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.0.0
