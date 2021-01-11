%global _vpath_builddir .
Name:           pdiplugin-decl-netcdf
Version:        fix_serial_netcdf
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        Decl'NetCDF plugin for the PDI Data Interface
Url:            https://gitlab.maisondelasimulation.fr/pdidev/pdi
Source0:        https://gitlab.maisondelasimulation.fr/pdidev/pdi/-/archive/%{version}/pdi-%{version}.tar.gz
BuildRequires:  gcc, gcc-c++, make, cmake >= 3.5
BuildRequires:  pdi-devel = master, netcdf-devel >= 1.8

%description
The Decl'NetCDF PDI plugin enables one to read and write data from NetCDF files in a
declarative way. Decl'NetCDF does not support the full NetCDF feature set but offers
a simple declarative interface to access a large subset of it.

%package openmpi
Summary: Decl'NetCDF plugin for the PDI Data Interface, OpenMPI version
BuildRequires: netcdf-openmpi-devel >= 1.8

%description openmpi
The Decl'NetCDF PDI plugin enables one to read and write data from NetCDF files in a
declarative way. Decl'NetCDF does not support the full NetCDF feature set but offers
a simple declarative interface to access a large subset of it.

%package mpich
Summary: Decl'NetCDF plugin for the PDI Data Interface, MPich version
BuildRequires: netcdf-mpich-devel >= 1.8

%description mpich
The Decl'NetCDF PDI plugin enables one to read and write data from NetCDF files in a
declarative way. Decl'NetCDF does not support the full NetCDF feature set but offers
a simple declarative interface to access a large subset of it.

%prep
%autosetup -n pdi-%{version}

%build
mkdir build
pushd build
%cmake3 \
	-DCMAKE_BUILD_TYPE=Release \
	-DBUILD_TESTING=OFF \
	../plugins/decl_netcdf
%make_build
popd
mkdir build-openmpi
pushd build-openmpi
module load mpi/openmpi-%{_arch}
%cmake3 \
	-DCMAKE_BUILD_TYPE=Release \
	-DBUILD_TESTING=OFF \
	-DINSTALL_PDIPLUGINDIR=%{_libdir}/openmpi/lib/pdi/plugins_%{version}/ \
	../plugins/decl_netcdf	
%make_build
module purge
popd
mkdir build-mpich
pushd build-mpich
module load mpi/mpich-%{_arch}
%cmake3 \
	-DCMAKE_BUILD_TYPE=Release \
	-DBUILD_TESTING=OFF \
	-DINSTALL_PDIPLUGINDIR=%{_libdir}/mpich/lib/pdi/plugins_%{version}/ \
	../plugins/decl_netcdf
%make_build
module purge
popd


%install
rm -rf $RPM_BUILD_ROOT
%make_install -C build
module load mpi/openmpi-%{_arch}
%make_install -C build-openmpi
module purge
module load mpi/mpich-%{_arch}
%make_install -C build-mpich
module purge

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
* Thu Nov 26 2020 - Pending release on master <julien.bigot@cea.fr>
- Initial Release