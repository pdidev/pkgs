Name:           pdiplugin-timer
Version:        main
Release:        0
License:        BSD-3-Clause
Summary:        Timer plugin for the PDI Data Interface
Url:            https://github.com/pdidev/pdi
Source0:        https://github.com/pdidev/pdi/archive/refs/heads/main.tar.gz
BuildRequires:  gcc, gcc-c++, make, cmake >= 3.22
BuildRequires:  pdi-devel = %{version}

%description
The PDI timer plugin measures the time spent by PDI and its plugins.

%prep
%autosetup -n pdi-%{version}

%build
%cmake \
	-DBUILD_TESTING=OFF \
	-DCMAKE_BUILD_TYPE=Release \
	-S plugins/timer
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/pdi/plugins_%{version}/lib*.so

%changelog
* Thu Nov 05 2026 - Pending release on main <julien.bigot@cea.fr>
- Upstream release main
* Wed Nov 04 2026 - Julien Bigot <julien.bigot@cea.fr>
- Initial release
