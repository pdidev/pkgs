Name:           pdiplugin-trace
Version:        main
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        Trace plugin for the PDI Data Interface
Url:            https://github.com/pdidev/pdi
Source0:        https://github.com/pdidev/pdi/archive/refs/heads/main.tar.gz
BuildRequires:  gcc, gcc-c++, make, cmake >= 3.16.3
BuildRequires:  pdi-devel = %{version}

%description
The PDI trace plugin generates a trace of what happens in PDI data store.

%prep
%autosetup -n pdi-%{version}

%build
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-S plugins/trace
%cmake_build

%install
rm -rf $RPM_BUILD_ROOT
%cmake_install

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_libdir}/pdi/*/lib*.so

%changelog
* Wed Dec 24 2025 - Pending release on main <julien.bigot@cea.fr>
- Upstream release main
* Fri Jun 13 2025 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.9.2
* Wed May 07 2025 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.9.1
* Mon Apr 07 2025 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.9.0
* Tue Feb 25 2025 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.8.3
* Thu Feb 20 2025 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.8.2
* Sun Feb 09 2025 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.8.1
* Thu Dec 05 2024 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.8.0
* Sun Jul 21 2024 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.7.1
* Thu Mar 09 2023 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.6.0
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
