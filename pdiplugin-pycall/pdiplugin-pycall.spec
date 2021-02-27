%global _vpath_builddir .
Name:           pdiplugin-pycall
Version:        1.0.1
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        Trace plugin for the PDI Data Interface
Url:            https://gitlab.maisondelasimulation.fr/pdidev/pdi
Source0:        https://gitlab.maisondelasimulation.fr/pdidev/pdi/-/archive/%{version}/pdi-%{version}.tar.bz2
BuildRequires:  gcc, gcc-c++, make, cmake >= 3.5
BuildRequires:  pdi-devel = %{version}

%description
The PDI pycall plugin enables one to call a user-defined python function when a
specified event occur or certain data becomes available.

%prep
%autosetup -n pdi-%{version}

%build
%cmake3 \
	-DBUILD_TESTING=OFF \
	-DCMAKE_BUILD_TYPE=Release \
	plugins/pycall
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
- Initial Release
