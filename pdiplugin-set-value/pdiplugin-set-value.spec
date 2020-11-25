%global _vpath_builddir .
Name:           pdiplugin-set-value
Version:        master
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        Set Value plugin for the PDI Data Interface
Url:            https://gitlab.maisondelasimulation.fr/pdidev/pdi
Source0:        https://gitlab.maisondelasimulation.fr/pdidev/pdi/-/archive/master/pdi-master.tar.gz
BuildRequires:  cmake >= 3.5, gcc, gcc-c++
BuildRequires:  make
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
* Thu Nov 26 2020 - Pending release on master <julien.bigot@cea.fr>
- Pending release on master
