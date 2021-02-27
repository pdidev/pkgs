%global _vpath_builddir .
Name:           pdiplugin-flowvr
Version:        1.0.1
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        FlowVR plugin for the PDI Data Interface
Url:            https://gitlab.maisondelasimulation.fr/pdidev/pdi
Source0:        https://gitlab.maisondelasimulation.fr/pdidev/pdi/-/archive/%{version}/pdi-%{version}.tar.bz2
BuildRequires:  gcc, gcc-c++, make, cmake >= 3.5
BuildRequires:  flowvr
BuildRequires:  freeglut-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  pdi-devel = %{version}
BuildRequires:  python3-yaml

%description
The PDI FlowVR plugin supports application coupling through the FlowVR software.

%prep
%autosetup -n pdi-%{version}

%build
. /opt/flowvr/bin/flowvr-suite-config.sh
%cmake3 \
	-DCMAKE_BUILD_TYPE=Release \
	plugins/flowvr
%make_build

%install
. /opt/flowvr/bin/flowvr-suite-config.sh
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
%{python3_sitearch}/pdi_flowvr

%changelog
* Sat Feb 27 2021 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.0.1
* Fri Oct 16 2020 - Upstream release 1.0.0 <julien.bigot@cea.fr>
- Initial Release
