Name:           pdiplugin-decl-netcdf
Version:        1.12.0
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        Decl'NetCDF plugin for the PDI Data Interface
Url:            https://github.com/pdidev/pdi
Source0:        https://github.com/pdidev/pdi/archive/refs/tags/%{version}.tar.gz
BuildRequires:  gcc, gcc-c++, make, cmake >= 3.22
BuildRequires:  pdi-devel = %{version}, netcdf-devel >= 4.8.1

%description
The Decl'NetCDF PDI plugin enables one to read and write data from NetCDF files in a
declarative way. Decl'NetCDF does not support the full NetCDF feature set but offers
a simple declarative interface to access a large subset of it.

%package openmpi
Summary: Decl'NetCDF plugin for the PDI Data Interface, OpenMPI version
BuildRequires: netcdf-openmpi-devel >= 4.8.1

%description openmpi
The Decl'NetCDF PDI plugin enables one to read and write data from NetCDF files in a
declarative way. Decl'NetCDF does not support the full NetCDF feature set but offers
a simple declarative interface to access a large subset of it.

%package mpich
Summary: Decl'NetCDF plugin for the PDI Data Interface, MPich version
BuildRequires: netcdf-mpich-devel >= 4.8.1

%description mpich
The Decl'NetCDF PDI plugin enables one to read and write data from NetCDF files in a
declarative way. Decl'NetCDF does not support the full NetCDF feature set but offers
a simple declarative interface to access a large subset of it.

%prep
%global _vpath_srcdir plugins/decl_netcdf
%global _vpath_builddir build-${MPI_VERSION}
%autosetup -n pdi-%{version}

%build
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DBUILD_TESTING=OFF \
	-DBUILD_NETCDF_PARALLEL=OFF \
%cmake_build

for MPI_VERSION in openmpi mpich
do
module load mpi/${MPI_VERSION}-%{_arch}
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DBUILD_TESTING=OFF \
	-DBUILD_NETCDF_PARALLEL=ON \
	-DINSTALL_PDIPLUGINDIR=${MPI_LIB}/pdi/plugins_%{version}/ \
%cmake_build
module purge
done


%install
%cmake_install

for MPI_VERSION in openmpi mpich
do
module load mpi/${MPI_VERSION}-%{_arch}
%cmake_install
module purge
done

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post   openmpi -p /sbin/ldconfig

%postun openmpi -p /sbin/ldconfig

%post   mpich -p /sbin/ldconfig

%postun mpich -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_libdir}/pdi/*/lib*.so

%files openmpi
%license LICENSE
%doc README.md
%{_libdir}/openmpi/lib/pdi/*/lib*.so

%files mpich
%license LICENSE
%doc README.md
%{_libdir}/mpich/lib/pdi/*/lib*.so

%changelog
* Tue Jun 23 2026 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.11.1
* Wed Apr 22 2026 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.11.0
* Wed Apr 22 2026 - Julien Bigot <julien.bigot@.cea.fr>
- Fix direct use of make that breaks with ninja
* Tue Feb 10 2026 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.10.1
* Sat Jan 31 2026 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release 1.10.0
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
- Fixed package build wrt. modules
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
