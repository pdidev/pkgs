Name:           spdlog
Version:        1.5.0
Release:        0
License:        MIT

Summary:        Super fast C++ logging library
Url:            https://github.com/gabime/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%name-root
%if 0%{?centos_version} > 0 && 0%{?centos_version} < 800

BuildRequires:  cmake3 >= 3.2
%else
BuildRequires:  cmake >= 3.2
%endif
#BuildRequires:  fmt-devel >= 6.1.2
BuildRequires:  gcc, gcc-c++

%description
This is a packaged version of the gabime/spdlog C++ logging
library available at Github.
 
%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       libstdc++-devel%{?_isa}
#Requires:       fmt-devel%{?_isa}

%description devel
The %{name}-devel package contains C++ header files for developing
applications that use %{name}.

%prep
%autosetup -p1
mkdir -p %{_target_platform}
find . -name '.gitignore' -exec rm {} \;
sed -i -e "s,\r,," README.md

%build
pushd %{_target_platform}
    %cmake3 \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DCMAKE_BUILD_TYPE=Release \
    -DSPDLOG_BUILD_SHARED=ON \
    -DSPDLOG_BUILD_EXAMPLE=ON \
    -DSPDLOG_BUILD_EXAMPLE_HO=OFF \
    -DSPDLOG_BUILD_TESTS=ON \
    -DSPDLOG_BUILD_TESTS_HO=OFF \
    ..
popd
%make_build -C %{_target_platform}

%install
%make_install -C %{_target_platform}

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.1*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}.pc
