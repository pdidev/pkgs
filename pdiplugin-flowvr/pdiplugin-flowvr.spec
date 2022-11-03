Name:           pdiplugin-flowvr
Version:        1.5.5
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        FlowVR plugin for the PDI Data Interface
Url:            https://gitlab.maisondelasimulation.fr/pdidev/pdi
Source0:        https://gitlab.maisondelasimulation.fr/pdidev/pdi/-/archive/%{version}/pdi-%{version}.tar.bz2
BuildRequires:  gcc, gcc-c++, make, cmake >= 3.10
BuildRequires:  flowvr >= 2.3.2
BuildRequires:  freeglut-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  pdi-devel = %{version}
BuildRequires:  python3-yaml >= 3.12

%description
The PDI FlowVR plugin supports application coupling through the FlowVR software.

%prep
%autosetup -n pdi-%{version}

%build
. /opt/flowvr/bin/flowvr-suite-config.sh
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-S plugins/flowvr
%cmake_build

%install
rm -rf $RPM_BUILD_ROOT
. /opt/flowvr/bin/flowvr-suite-config.sh
%cmake_install

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
* Thu Nov 03 2022 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.5.5
* Sat Jun 11 2022 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.5.4
* Tue May 31 2022 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.5.3
* Fri Apr 01 2022 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.5.1
* Wed Mar 30 2022 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.5.0
* Sat Mar 05 2022 - Julien Bigot <julien.bigot@cea.fr>
- updated cmake invocation to be compatible with Fedora 36+
* Wed Dec 01 2021 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.4.3
* Mon Nov 15 2021 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.4.1
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
