#!
set -e

. /usr/share/mpi-default-dev/debian_defaults
if [ openmpi = "${ARCH_DEFAULT_MPI_IMPL}" ]
then
	PRIORITY=30
else
	PRIORITY=20
fi
PKG_VERSION="#PKG_VERSION#"

case "$1" in
configure)
	update-alternatives \
		--install \
		/usr/lib/$(dpkg-architecture -qDEB_HOST_MULTIARCH)/fti/openmpi/libfti.so.${PKG_VERSION}
		libfti.so.${PKG_VERSION}-$(dpkg-architecture -qDEB_HOST_MULTIARCH)
		/usr/lib/$(dpkg-architecture -qDEB_HOST_MULTIARCH)/libfti.so.${PKG_VERSION}
		"${PRIORITY}"
;;
*)
	# do nothing
;;
esac

#DEBHELPER#
