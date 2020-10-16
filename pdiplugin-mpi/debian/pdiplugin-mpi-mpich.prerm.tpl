#!
set -e

PKG_VERSION="#PKG_VERSION#"

case "$1" in
*)
	update-alternatives \
		--remove \
		pdi-${PKG_VERSION}_mpi_plugin.so-$(dpkg-architecture -qDEB_HOST_MULTIARCH) \
		/usr/lib/$(dpkg-architecture -qDEB_HOST_MULTIARCH)/pdiplugin-mpi-mpich/pdi/plugins_${PKG_VERSION}/libpdi_mpi_plugin.so
;;
esac

#DEBHELPER#
