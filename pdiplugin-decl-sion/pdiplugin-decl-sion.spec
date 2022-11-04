Name:           pdiplugin-decl-sion
Version:        master
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        SIONlib plugin for the PDI Data Interface
Url:            https://gitlab.maisondelasimulation.fr/pdidev/pdi
Source0:        https://gitlab.maisondelasimulation.fr/pdidev/pdi/-/archive/%{version}/pdi-%{version}.tar.bz2
BuildRequires:  gcc, gcc-c++, make, cmake >= 3.10
BuildRequires:  pdi-devel = %{version}

%description
The PDI decl-sion plugin interfaces PDI with SIONlib.

%package openmpi
Summary: SIONlib plugin for the PDI Data Interface, OpenSIONlib version
BuildRequires: sionlib-openmpi-devel >= 1.7.6

%description openmpi
The PDI decl-sion plugin interfaces PDI with SIONlib.

%package mpich
Summary: SIONlib plugin for the PDI Data Interface, MPich version
BuildRequires: sionlib-mpich-devel >= 1.7.6

%description mpich
The PDI decl-sion plugin interfaces PDI with SIONlib.

%prep
%autosetup -n pdi-%{version}

%build
for MPI_VERSION in openmpi mpich
do
mkdir build-${MPI_VERSION}
module load mpi/${MPI_VERSION}-%{_arch}
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DINSTALL_PDIPLUGINDIR=${MPI_LIB}/pdi/plugins_%{version}/ \
	-S plugins/decl_sion \
	-B build-${MPI_VERSION}
%make_build -C build-${MPI_VERSION}
done

%install
rm -rf $RPM_BUILD_ROOT
for MPI_VERSION in openmpi mpich
do
module load mpi/${MPI_VERSION}-%{_arch}
%make_install -C build-${MPI_VERSION}
module purge
done

%clean
rm -rf $RPM_BUILD_ROOT

%post   openmpi -p /sbin/ldconfig

%postun openmpi -p /sbin/ldconfig

%post   mpich -p /sbin/ldconfig

%postun mpich -p /sbin/ldconfig

%files openmpi
%license LICENSE
%doc README.md
%{_libdir}/openmpi/lib/pdi/*/lib*.so

%files mpich
%license LICENSE
%doc README.md
%{_libdir}/mpich/lib/pdi/*/lib*.so

%changelog
* Fri Nov 04 2022 - Pending release on master <julien.bigot@cea.fr>
- Upstream release master
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
- Initial Release
