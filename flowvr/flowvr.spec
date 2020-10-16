%global _vpath_builddir .
Name:           flowvr
Version:        2.3.2
Release:        0
License:        LGPLv2
Group:          Development/Libraries/C and C++
Summary:        the FlowVR in situ and in transit processing middleware
Url:            http://flowvr.sourceforge.net/FlowVRDoc.html
Source0:        https://gitlab.inria.fr/flowvr/flowvr-ex/-/archive/f3938ecc7aa8d7ea5211554480a5a99237c61fbb/flowvr-ex-f3938ecc7aa8d7ea5211554480a5a99237c61fbb.tar.gz
BuildRequires:  cmake >= 3.5, gcc, gcc-c++, gcc-gfortran
BuildRequires:  make
BuildRequires:  doxygen
BuildRequires:  freeglut-devel
BuildRequires:  glew-devel
BuildRequires:  graphviz
BuildRequires:  graphviz-devel
BuildRequires:  hwloc-devel
BuildRequires:  libXi-devel
BuildRequires:  libxml2-devel
BuildRequires:  libXmu-devel
BuildRequires:  libxslt-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  openmpi-devel
BuildRequires:  python3-devel
BuildRequires:  swig

%description
FlowVR is an open source middleware to augment parallel simulations running on
thousands of cores with in situ processing capabilities and live steering.
FlowVR offers a very flexible environment while enabling high performance
asynchronous in situ and in transit processing.

%prep
%autosetup -n flowvr-ex-f3938ecc7aa8d7ea5211554480a5a99237c61fbb

%build
%cmake3 \
	-DOpenGL_GL_PREFERENCE=LEGACY \
	-DCMAKE_BUILD_TYPE=Release \
	-DBUILD_FLOWVRD_MPI_PLUGIN=OFF \
	-DBUILD_FLOWVR_CONTRIB=OFF \
	-DBUILD_FLOWVR_DOXYGEN=ON \
	-DBUILD_FLOWVR_GLGRAPH=OFF \
	-DBUILD_FLOWVR_GLTRACE=ON \
	-DCMAKE_INSTALL_PREFIX=/opt/flowvr \
	.
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install
# We remove this as it is not python3 compatible
rm %{buildroot}/opt/flowvr/lib/flowvr/python/spy_module.py
mkdir -p %{buildroot}/etc
cd %{buildroot}/etc

%clean
rm -rf $RPM_BUILD_ROOT

%post
ln -s %{base_install_dir}/opt/flowvr/bin/flowvr-suite-config.sh %{base_install_dir}/etc/profile.d/flowvr-suite-config.sh

%files
/opt/flowvr
%license flowvr/flowvr-base/COPYING
%doc /opt/flowvr/share/flowvr/doc/*
%ghost /etc/profile.d/flowvr-suite-config.sh

%changelog
* Fri Oct 16 2020 - Pending release on master <julien.bigot@cea.fr>
- Initial Release
