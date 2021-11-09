%global _vpath_builddir .
Name:           pdiplugin-flowvr
Version:        master
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
* Tue Nov 09 2021 - Pending release on master <julien.bigot@cea.fr>
- Upstream release master
* Tue Nov 09 2021 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.4.0
* Tue Aug 03 2021 - Karol Sierociński <ksiero@man.poznan.pl>
- Upstream release 1.3.1
* Sun Aug 01 2021 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.3.0
* Tue Jul 20 2021 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.2.2
* Fri Jun 18 2021 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.2.1
* Wed Jun 16 2021 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.2.0
* Sat Mar 27 2021 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.1.0
* Sat Feb 27 2021 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.0.1
* Fri Oct 16 2020 - Upstream release 1.0.0 <julien.bigot@cea.fr>
- Initial Release
