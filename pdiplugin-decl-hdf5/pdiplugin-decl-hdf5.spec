%global _vpath_builddir .
Name:           pdiplugin-decl-hdf5
Version:        v1.0
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        Decl'HDF5 plugin for the PDI Data Interface
Url:            https://gitlab.maisondelasimulation.fr/pdidev/pdi
Source0:        https://gitlab.maisondelasimulation.fr/pdidev/pdi/-/archive/%{version}/pdi-%{version}.tar.bz2
BuildRequires:  gcc, gcc-c++, make, cmake >= 3.5
BuildRequires:  pdi-devel = %{version}, hdf5-devel >= 1.8

%description
The Decl'HDF5 PDI plugin enables one to read and write data from HDF5 files in a
declarative way. Decl'HDF5 does not support the full HDF5 feature set but offers
a simple declarative interface to access a large subset of it.

%package openmpi
Summary: Decl'HDF5 plugin for the PDI Data Interface, OpenMPI version
BuildRequires:  hdf5-openmpi-devel >= 1.8

%description openmpi
The Decl'HDF5 PDI plugin enables one to read and write data from HDF5 files in a
declarative way. Decl'HDF5 does not support the full HDF5 feature set but offers
a simple declarative interface to access a large subset of it.

%package mpich
Summary: Decl'HDF5 plugin for the PDI Data Interface, MPich version
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
	-DINSTALL_PDIPLUGINDIR=%{_libdir}/openmpi/lib/pdi/plugins_%{version}/ \
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
	-DINSTALL_PDIPLUGINDIR=%{_libdir}/mpich/lib/pdi/plugins_%{version}/ \
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
* Sat Feb 27 2021 - Julien Bigot <julien.bigot@.cea.fr>
- Upstream release v1.0
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
