%global _vpath_builddir .
Name:           pdiplugin-mpi
Version:        master
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        MPI plugin for the PDI Data Interface
Url:            https://gitlab.maisondelasimulation.fr/pdidev/pdi
Source0:        https://gitlab.maisondelasimulation.fr/pdidev/pdi/-/archive/master/pdi-master.tar.gz
BuildRequires:  cmake >= 3.10, gcc, gcc-c++, gcc-gfortran
BuildRequires:  make
BuildRequires:  pdi-devel = %{version}, openmpi-devel

%description
The PDI mpi plugin interfaces PDI with MPI.

%package openmpi
Summary: MPI plugin for the PDI Data Interface, OpenMPI version
BuildRequires:  hdf5-openmpi-devel >= 1.8

%description openmpi
The PDI mpi plugin interfaces PDI with MPI.

%package mpich
Summary: MPI plugin for the PDI Data Interface. MPich version
BuildRequires:  hdf5-mpich-devel >= 1.8

%description mpich
The PDI mpi plugin interfaces PDI with MPI.

%prep
%autosetup -n pdi-%{version}

%build
mkdir build-openmpi
pushd build-openmpi
module load mpi/openmpi-%{_arch}
%cmake3 \
	-DCMAKE_BUILD_TYPE=Release \
	-DINSTALL_PDIPLUGINDIR=%{_libdir}/openmpi/lib/pdi/plugins_%{version}/ \
	../plugins/mpi
%make_build
module purge
popd
mkdir build-mpich
pushd build-mpich
module load mpi/mpich-%{_arch}
%cmake3 \
	-DCMAKE_BUILD_TYPE=Release \
	-DINSTALL_PDIPLUGINDIR=%{_libdir}/mpich/lib/pdi/plugins_%{version}/ \
	../plugins/mpi
%make_build
module purge
popd

%install
rm -rf $RPM_BUILD_ROOT
module load mpi/openmpi-%{_arch}
%make_install -C build-openmpi
module purge
module load mpi/mpich-%{_arch}
%make_install -C build-mpich
module purge

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
* Thu Nov 26 2020 - Pending release on master <julien.bigot@cea.fr>
- Pending release on master
* Wed Nov 25 2020 - Julien Bigot <julien.bigot@cea.fr>
- Version bump to 0.6.5
* Tue Oct 20 2020 - Julien Bigot <julien.bigot@cea.fr>
- Version bump to 0.6.3
* Thu Oct 15 2020 - Julien Bigot <julien.bigot@cea.fr>
- Version bump to 0.6.2
* Mon May 11 2020 - Julien Bigot <julien.bigot@cea.fr>
- Initial Release
