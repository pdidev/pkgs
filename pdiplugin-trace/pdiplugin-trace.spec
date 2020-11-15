%global _vpath_builddir .
Name:           pdiplugin-trace
Version:        prerelease
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        Trace plugin for the PDI Data Interface
Url:            https://gitlab.maisondelasimulation.fr/pdidev/pdi
Source0:        https://gitlab.maisondelasimulation.fr/pdidev/pdi/-/archive/prerelease/pdi-prerelease.tar.gz
BuildRequires:  cmake >= 3.5, gcc, gcc-c++
BuildRequires:  make
BuildRequires:  pdi-devel = %{version}

%description
The PDI trace plugin generates a trace of what happens in PDI data store.

%prep
%autosetup -n pdi-%{version}

%build
%cmake3 \
	-DCMAKE_BUILD_TYPE=Release \
	plugins/trace
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
* Fri Oct 16 2020 - Pending release on prerelease <julien.bigot@cea.fr>
- Pending release on prerelease
* Thu Oct 15 2020 - Julien Bigot <julien.bigot@cea.fr>
- Version bump to 0.6.2
* Mon May 11 2020 - Julien Bigot <julien.bigot@cea.fr>
- Initial Release
