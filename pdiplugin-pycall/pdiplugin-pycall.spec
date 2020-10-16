%global _vpath_builddir .
Name:           pdiplugin-pycall
Version:        0.6.2
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        Trace plugin for the Portable Data Interface library
Url:            https://gitlab.maisondelasimulation.fr/pdidev/pdi
Source0:        https://gitlab.maisondelasimulation.fr/pdidev/pdi/-/archive/%{version}/pdi-%{version}.tar.gz
BuildRequires:  cmake >= 3.5, gcc, gcc-c++
BuildRequires:  make
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
%{_libdir}/lib*.so

%changelog
* Thu Oct 15 2020 - Julien Bigot <julien.bigot@cea.fr>
- Version bump to 0.6.2
* Mon May 11 2020 - Julien Bigot <julien.bigot@cea.fr>
- Initial Release
