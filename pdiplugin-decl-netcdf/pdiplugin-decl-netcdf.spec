Name:           pdiplugin-decl-netcdf
Version:        1.6.0
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        Decl'NetCDF plugin for the PDI Data Interface
Url:            https://gitlab.maisondelasimulation.fr/pdidev/pdi
Source0:        https://gitlab.maisondelasimulation.fr/pdidev/pdi/-/archive/%{version}/pdi-%{version}.tar.bz2
BuildRequires:  gcc, gcc-c++, make, cmake >= 3.10
BuildRequires:  pdi-devel = %{version}, netcdf-devel >= 4.6
BuildRequires:  gtest-devel >= 1.8.0 , gmock-devel >= 1.8.0

%description
The Decl'NetCDF PDI plugin enables one to read and write data from NetCDF files in a
declarative way. Decl'NetCDF does not support the full NetCDF feature set but offers
a simple declarative interface to access a large subset of it.

%package openmpi
Summary: Decl'NetCDF plugin for the PDI Data Interface, OpenMPI version
BuildRequires: netcdf-openmpi-devel >= 4.6

%description openmpi
The Decl'NetCDF PDI plugin enables one to read and write data from NetCDF files in a
declarative way. Decl'NetCDF does not support the full NetCDF feature set but offers
a simple declarative interface to access a large subset of it.

%package mpich
Summary: Decl'NetCDF plugin for the PDI Data Interface, MPich version
BuildRequires: netcdf-mpich-devel >= 4.6

%description mpich
The Decl'NetCDF PDI plugin enables one to read and write data from NetCDF files in a
declarative way. Decl'NetCDF does not support the full NetCDF feature set but offers
a simple declarative interface to access a large subset of it.

%prep
%autosetup -n pdi-%{version}

%build
mkdir build
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DBUILD_TESTING=OFF \
	-DBUILD_NETCDF_PARALLEL=OFF \
	-S plugins/decl_netcdf \
	-B build
%make_build -C build

for MPI_VERSION in openmpi mpich
do
mkdir build-${MPI_VERSION}
module load mpi/${MPI_VERSION}-%{_arch}
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DBUILD_TESTING=OFF \
	-DBUILD_NETCDF_PARALLEL=ON \
	-DINSTALL_PDIPLUGINDIR=${MPI_LIB}/pdi/plugins_%{version}/ \
	-S plugins/decl_netcdf \
	-B build-${MPI_VERSION}
%make_build -C build-${MPI_VERSION}
module purge
done


%install
rm -rf $RPM_BUILD_ROOT
%make_install -C build

for MPI_VERSION in openmpi mpich
do
module load mpi/${MPI_VERSION}-%{_arch}
%make_install -C build-${MPI_VERSION}
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
