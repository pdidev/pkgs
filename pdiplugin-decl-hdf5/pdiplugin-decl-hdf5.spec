%global _vpath_builddir .
Name:           pdiplugin-decl-hdf5
Version:        master
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        Decl'HDF5 plugin for the Portable Data Interface library
Url:            https://gitlab.maisondelasimulation.fr/pdidev/pdi
Source0:        https://gitlab.maisondelasimulation.fr/pdidev/pdi/-/archive/pdi_plugin_path_install/pdi-pdi_plugin_path_install.tar.gz
BuildRequires:  cmake >= 3.10, gcc, gcc-c++, gcc-gfortran
BuildRequires:  make
BuildRequires:  pdi-devel = %{version}, hdf5-devel >= 1.8

%description
The Decl'HDF5 PDI plugin enables one to read and write data from HDF5 files in a
declarative way. Decl'HDF5 does not support the full HDF5 feature set but offers
a simple declarative interface to access a large subset of it.

%package openmpi
Summary: Decl'HDF5 plugin for the Portable Data Interface library, OpenMPI version
BuildRequires:  hdf5-openmpi-devel >= 1.8

%description openmpi
The Decl'HDF5 PDI plugin enables one to read and write data from HDF5 files in a
declarative way. Decl'HDF5 does not support the full HDF5 feature set but offers
a simple declarative interface to access a large subset of it.

%package mpich
Summary: Decl'HDF5 plugin for the Portable Data Interface library, MPich version
BuildRequires:  hdf5-mpich-devel >= 1.8

%description mpich
The Decl'HDF5 PDI plugin enables one to read and write data from HDF5 files in a
declarative way. Decl'HDF5 does not support the full HDF5 feature set but offers
a simple declarative interface to access a large subset of it.

%prep
%autosetup -n pdi-%{version}

%build
mkdir build
pushd build
%cmake3 \
	-DCMAKE_BUILD_TYPE=Release \
	-DBUILD_TESTING=OFF \
	-DBUILD_HDF5_PARALLEL=OFF \
	../plugins/decl_hdf5
%make_build
popd
mkdir build-openmpi
pushd build-openmpi
module load mpi/openmpi-%{_arch}
%cmake3 \
	-DCMAKE_BUILD_TYPE=Release \
	-DBUILD_TESTING=OFF \
	-DBUILD_HDF5_PARALLEL=ON \
	-DCMAKE_INSTALL_LIBDIR=%{_libdir}/openmpi/lib \
	../plugins/decl_hdf5	
%make_build
module purge
popd
mkdir build-mpich
pushd build-mpich
module load mpi/mpich-%{_arch}
%cmake3 \
	-DCMAKE_BUILD_TYPE=Release \
	-DBUILD_TESTING=OFF \
	-DBUILD_HDF5_PARALLEL=ON \
	-DCMAKE_INSTALL_LIBDIR=%{_libdir}/mpich/lib \
	../plugins/decl_hdf5
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
%{_libdir}/pdi/plugins/*/lib*.so

%files openmpi
%license LICENSE
%doc README.md
%{_libdir}/openmpi/lib/pdi/plugins/*/lib*.so

%files mpich
%license LICENSE
%doc README.md
%{_libdir}/mpich/lib/pdi/plugins/*/lib*.so

%changelog
* Fri Oct 16 2020 - Pending release on master <julien.bigot@cea.fr>
- Pending release on master
* Thu Oct 15 2020 - Julien Bigot <julien.bigot@cea.fr>
- Version bump to 0.6.2
* Mon May 11 2020 - Julien Bigot <julien.bigot@cea.fr>
- Initial Release
