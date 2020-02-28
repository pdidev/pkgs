Name:           pdiplugin-decl-hdf5
Version:        0.6.1
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        Decl'HDF5 plugin for the Portable Data Interface library
Url:            https://gitlab.maisondelasimulation.fr/pdidev/pdi
Source0:        https://gitlab.maisondelasimulation.fr/pdidev/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%name-root
%if 0%{?centos_version} > 0 && 0%{?centos_version} < 800
BuildRequires:  devtoolset-6
BuildRequires:  cmake3 >= 3.5
%else
BuildRequires:  cmake >= 3.5
%endif
BuildRequires:  pdi-devel = %(version)

%description
The Decl'HDF5 PDI plugin enables one to read and write data from HDF5 files in a
declarative way. Decl'HDF5 does not support the full HDF5 feature set but offers
a simple declarative interface to access a large subset of it.

%package
Summary:        Decl'HDF5 plugin for the Portable Data Interface library

%description
The Decl'HDF5 PDI plugin enables one to read and write data from HDF5 files in a
declarative way. Decl'HDF5 does not support the full HDF5 feature set but offers
a simple declarative interface to access a large subset of it.

%prep
%autosetup -n pdi-%{version}
mkdir -p %{_target_platform}

%build
%if 0%{?centos_version} > 0 && 0%{?centos_version} < 800
set +e
source scl_source enable devtoolset-6
set -e
%endif
pushd %{_target_platform}
    %cmake3 plugins/decl_hdf5
popd
%make_build -C %{_target_platform}

%install
rm -rf $RPM_BUILD_ROOT
%make_install -C %{_target_platform}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Thu Feb 27 2020 - Julien Bigot <julien.bigot@cea.fr>
- Initial Release
