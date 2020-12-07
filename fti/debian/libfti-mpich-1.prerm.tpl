#!
set -e

PKG_VERSION="#PKG_VERSION#"

case "$1" in
*)
	update-alternatives \
		--remove \
		libfti.so-$(dpkg-architecture -qDEB_HOST_MULTIARCH) \
		/usr/lib/$(dpkg-architecture -qDEB_HOST_MULTIARCH)/fti/mpich/libfti.so
;;
esac

#DEBHELPER#
