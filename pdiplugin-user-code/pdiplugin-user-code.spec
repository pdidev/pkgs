Name:           pdiplugin-user-code
Version:        0.6.1
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        user-code plugin for the Portable Data Interface library
Url:            https://gitlab.maisondelasimulation.fr/pdidev/pdi
Source0:        https://gitlab.maisondelasimulation.fr/pdidev/pdi/-/archive/%{version}/pdi-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%name-root
%if 0%{?centos_version} > 0 && 0%{?centos_version} < 800
BuildRequires:  devtoolset-6
BuildRequires:  cmake3 >= 3.5
%else
BuildRequires:  cmake >= 3.5
%endif
BuildRequires:  pdi-devel = %{version}

%description
The PDI user-code plugin enables one to call a user-defined function when a
specified event occur or certain data becomes available.

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
    %cmake3 \
    -DBUILD_TESTING=OFF \
    -DBUILD_FORTRAN=OFF \
    ../plugins/user_code
popd
%make_build -C %{_target_platform}

%install
rm -rf $RPM_BUILD_ROOT
%make_install -C %{_target_platform}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so

%changelog
* Thu Feb 27 2020 - Julien Bigot <julien.bigot@cea.fr>
- Initial Release
