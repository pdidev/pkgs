Name:           pdiplugin-trace
Version:        0.6.1
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        Trace plugin for the Portable Data Interface library
Url:            https://gitlab.maisondelasimulation.fr/pdidev/pdi
Source0:        https://gitlab.maisondelasimulation.fr/pdidev/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
%if 0%{?centos_version} > 0 && 0%{?centos_version} < 800
BuildRequires:  devtoolset-6
BuildRequires:  cmake3 >= 3.5
%else
BuildRequires:  cmake >= 3.5
%endif
BuildRequires:  pdi-devel = %(version)

%description
The PDI trace plugin generates a trace of what happens in PDI data store.

%package
Summary:        Trace plugin for the Portable Data Interface library

%description
The PDI trace plugin generates a trace of what happens in PDI data store.

%prep
%setup -q -n pdi-%{version}

%build
%if 0%{?centos_version} > 0 && 0%{?centos_version} < 800
set +e
source scl_source enable devtoolset-6
set -e
%endif
%cmake3 \
  plugins/trace
%make_build

%install
%make_install

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Thu, 27 Feb 2020 17:15:00 +0100 - Julien Bigot <julien.bigot@cea.fr>
- Initial Release
