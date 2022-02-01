%global _vpath_builddir .
%define _sover  1
Name:           sionlib
Version:        %{_sover}.7.7
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Summary:        a parallel input output library
Url:            https://www.fz-juelich.de/ias/jsc/EN/Expertise/Support/Software/SIONlib/_node.html
Source0:        https://apps.fz-juelich.de/jsc/%{name}/download.php?version=%{version}
BuildRequires:  gcc, gcc-c++, make

%description
SIONlib is a library for writing and reading binary data to/from several
thousands of processors into one or a small number of physical files. For
parallel access to files only the open and close functions are collective while
writing and reading file can be done asynchronously. SIONlib provides a SIONlib
file handle which substitutes the C file pointer.

%package headers
Summary: a parallel input output library, OpenMPI version
BuildArch: noarch

%description headers
SIONlib is a library for writing and reading binary data to/from several
thousands of processors into one or a small number of physical files. For
parallel access to files only the open and close functions are collective while
writing and reading file can be done asynchronously. SIONlib provides a SIONlib
file handle which substitutes the C file pointer.

%package openmpi-devel
Summary: a parallel input output library, OpenMPI version
BuildRequires: openmpi-devel
Requires: openmpi-devel, %{name}-headers = %{?epoch:%{epoch}:}%{version}-%{release}

%description openmpi-devel
SIONlib is a library for writing and reading binary data to/from several
thousands of processors into one or a small number of physical files. For
parallel access to files only the open and close functions are collective while
writing and reading file can be done asynchronously. SIONlib provides a SIONlib
file handle which substitutes the C file pointer.

%package mpich-devel
Summary: a parallel input output library, MPich version
BuildRequires: mpich-devel
Requires: mpich-devel

%description mpich-devel
SIONlib is a library for writing and reading binary data to/from several
thousands of processors into one or a small number of physical files. For
parallel access to files only the open and close functions are collective while
writing and reading file can be done asynchronously. SIONlib provides a SIONlib
file handle which substitutes the C file pointer.

%prep
%autosetup -n sionlib
patch -p1 << 'EOF'
--- sionlib.orig/src/utils/Makefile
+++ sionlib/src/utils/Makefile
@@ -76,9 +76,8 @@ sionversion: sionversion.o ../lib/lib$(S
 
 ###### sionconfig ######
 install-config: sionconfig.in
-	AINSTDIR=`(cd $(PREFIX) && pwd)`; \
 	sed -e "s!@ARCH@!$(ARCH)!" \
-		-e "s!@INSTDIR@!$$AINSTDIR!" \
+		-e "s!@INSTDIR@!$(PREFIX)!" \
 		-e "s!@LIBNAME@!$(SION_LIBNAME_PAR)!" \
 		-e "s!@LIBSERNAME@!$(SION_LIBNAME_SER)!" \
 		-e "s!@HINTSLIB@!$(HINTSLIB)!" \
@@ -89,8 +88,8 @@ install-config: sionconfig.in
 		-e "s!@SIONFWD_LIBS@!$(SIONFWD_LIBS)!" \
 		-e "s!@IME_LIBS@!$(IMELIB_LIBPATH) $(IMELIB_LIB)!" \
 		-e "s!@IME_CFLAGS@!-D_SION_IME_NATIVE!" \
-		sionconfig.in > $(PREFIX)/bin/sionconfig
-	chmod 755 $(PREFIX)/bin/sionconfig; \
+		sionconfig.in > $(BINDIR)/sionconfig
+	chmod 755 $(BINDIR)/sionconfig; \
 
 
 install: all
EOF

%build
for MPI_VERSION in openmpi mpich
do
module load mpi/${MPI_VERSION}-%{_arch}
./configure \
	--prefix="$(dirname ${MPI_BIN})" \
	--compiler=gnu \
	--disable-fortran \
	--disable-parutils \
	--mpi=${MPI_VERSION/mpich/mpich3}
%make_build -C build-linux-gomp*-${MPI_VERSION/mpich/mpich3}
module purge
done

%install
rm -rf $RPM_BUILD_ROOT
for MPI_VERSION in openmpi mpich
do
module load mpi/${MPI_VERSION}-%{_arch}
%{__make} \
	BINDIR=%{?buildroot}${MPI_BIN} \
	LIBDIR=%{?buildroot}${MPI_LIB} \
	INCDIR=%{?buildroot}%{_includedir} \
	-C build-linux-gomp*-${MPI_VERSION/mpich/mpich3}/build \
	-f RealMakefile \
	install-path install-libs install-parlibs install-utils install-config
module purge
done

%clean
rm -rf $RPM_BUILD_ROOT

%files headers
%{_includedir}/sion*

%files openmpi-devel
%license LICENSE
%{_libdir}/openmpi/lib/libsion*.a
%{_libdir}/openmpi/bin/sion*

%files mpich-devel
%license LICENSE
%{_libdir}/mpich/lib/libsion*.a
%{_libdir}/mpich/bin/sion*

%changelog
* Tue Feb 01 2022 - Julien Bigot <julien.bigot@cea.fr>
- Upstream update to 1.7.7
* Mon Dec 14 2020 - Julien Bigot <julien.bigot@cea.fr>
- Initial Release
