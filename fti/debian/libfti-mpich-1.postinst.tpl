#!
set -e

. /usr/share/mpi-default-dev/debian_defaults
if [ mpich = "${ARCH_DEFAULT_MPI_IMPL}" ]
then
	PRIORITY=30
else
	PRIORITY=10
fi

case "$1" in
configure)
	update-alternatives \
		--install \
		/usr/lib/$(dpkg-architecture -qDEB_HOST_MULTIARCH)/libfti.so \
		libfti.so-$(dpkg-architecture -qDEB_HOST_MULTIARCH) \
		/usr/lib/$(dpkg-architecture -qDEB_HOST_MULTIARCH)/fti/mpich/libfti.so \
		"${PRIORITY}"
;;
*)
	# nothing to do
;;
esac

#DEBHELPER#
