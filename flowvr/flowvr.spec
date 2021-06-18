%global _vpath_builddir .
Name:           flowvr
Version:        2.3.2
Release:        0
License:        LGPLv2
Group:          Development/Libraries/C and C++
Summary:        the FlowVR in situ and in transit processing middleware
Url:            http://flowvr.sourceforge.net/FlowVRDoc.html
Source0:        https://gitlab.inria.fr/%{name}/%{name}-ex/-/archive/v%{version}/%{name}-ex-v%{version}.tar.gz
BuildRequires:  gcc, gcc-c++, make, cmake >= 3.5
BuildRequires:  chrpath
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
Requires:  hwloc-devel
Requires:  openmpi-devel
Requires:  python3-yaml

%description
FlowVR is an open source middleware to augment parallel simulations running on
thousands of cores with in situ processing capabilities and live steering.
FlowVR offers a very flexible environment while enabling high performance
asynchronous in situ and in transit processing.

%prep
%autosetup -n %{name}-ex-v%{version}

%build
%cmake3 \
	-DOpenGL_GL_PREFERENCE=LEGACY \
	-DCMAKE_BUILD_TYPE=Release \
	-DBUILD_FLOWVRD_MPI_PLUGIN=OFF \
	-DBUILD_FLOWVR_CONTRIB=OFF \
	-DBUILD_FLOWVR_DOXYGEN=ON \
	-DBUILD_FLOWVR_GLGRAPH=OFF \
	-DBUILD_FLOWVR_GLTRACE=ON \
	-DCMAKE_INSTALL_PREFIX=/opt/%{name} \
	.
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install
# remove rpath from the libs as it is wrong
chrpath -d %{buildroot}/opt/%{name}/lib/flowvr/python/*.so
# We remove this as it is not python3 compatible
rm %{buildroot}/opt/%{name}/lib/flowvr/python/spy_module.py
# Link from /opt to the expected locations
mkdir -p %{buildroot}%{_bindir}
for N in flowvr flowvrd flowvr-fdump flowvr-gltrace flowvr-kill flowvr-run-env flowvr-run-ssh flowvr-setup-shmem flowvr-shmdump flowvr-stats flowvr-term
do
	%{__ln_s} -f "/opt/%{name}/bin/${N}" "%{buildroot}%{_bindir}/${N}"
done
mkdir -p %{buildroot}%{_includedir}
cd %{buildroot}/opt/%{name}/include
for N in *
do
	%{__ln_s} -f "/opt/%{name}/include/${N}" "%{buildroot}%{_includedir}/${N}"
done
mkdir -p %{buildroot}%{_libdir}
cd %{buildroot}/opt/%{name}/lib
for N in *
do
	%{__ln_s} -f "/opt/%{name}/lib/${N}" "%{buildroot}%{_libdir}/${N}"
done
mkdir -p %{buildroot}%{python3_sitelib}
cd %{buildroot}/opt/%{name}/lib/flowvr/python/
for N in *
do
	%{__ln_s} -f "/opt/%{name}/lib/flowvr/python/${N}" "%{buildroot}%{python3_sitelib}/${N}"
done
mkdir -p %{buildroot}%{_docdir}
%{__ln_s} -f "/opt/%{name}/share/flowvr/doc/FlowVR" "%{buildroot}%{_docdir}/%{name}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%docdir /opt/%{name}/share/flowvr/doc/
%docdir /opt/%{name}/share/flowvr/examples/
/opt/%{name}
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{python3_sitelib}/*
%doc %{_docdir}/%{name}
%license flowvr/flowvr-base/COPYING

%changelog
* Wed Nov 25 2020 - Julien Bigot <julien.bigot@cea.fr>
- Initial Release
