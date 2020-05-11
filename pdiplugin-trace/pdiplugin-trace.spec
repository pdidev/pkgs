Name:           pdiplugin-trace
Version:        0.6.1
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        Trace plugin for the Portable Data Interface library
Url:            https://gitlab.maisondelasimulation.fr/pdidev/pdi
Source0:        https://gitlab.maisondelasimulation.fr/pdidev/pdi/-/archive/%{version}/pdi-%{version}.tar.gz
%if 0%{?centos_ver} > 0 && 0%{?centos_ver} < 800
BuildRequires:  devtoolset-6, cmake3 >= 3.5
%else
BuildRequires:  cmake >= 3.5, gcc, gcc-c++
%endif
BuildRequires:  make
BuildRequires:  pdi-devel = %{version}

%description
The PDI trace plugin generates a trace of what happens in PDI data store.

%prep
%autosetup -n pdi-%{version}

%build
%if 0%{?centos_ver} > 0 && 0%{?centos_ver} < 800
set +e
source scl_source enable devtoolset-6
set -e
%endif
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
%{_libdir}/lib*.so

%changelog
* Mon May 11 2020 - Julien Bigot <julien.bigot@cea.fr>
- Initial Release
