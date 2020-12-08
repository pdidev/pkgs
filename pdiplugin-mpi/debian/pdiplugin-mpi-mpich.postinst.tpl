#!
set -e

. /usr/share/mpi-default-dev/debian_defaults
if [ mpich = "${ARCH_DEFAULT_MPI_IMPL}" ]
then
	PRIORITY=30
else
	PRIORITY=10
fi
PKG_VERSION="#PKG_VERSION#"

case "$1" in
configure)
	update-alternatives \
		--install \
		/usr/lib/$(dpkg-architecture -qDEB_HOST_MULTIARCH)/pdi/plugins_${PKG_VERSION}/libpdi_mpi_plugin.so \
		pdi-${PKG_VERSION}_mpi_plugin.so-$(dpkg-architecture -qDEB_HOST_MULTIARCH) \
		/usr/lib/$(dpkg-architecture -qDEB_HOST_MULTIARCH)/pdiplugin-mpi-mpich/pdi/plugins_${PKG_VERSION}/libpdi_mpi_plugin.so \
		"${PRIORITY}"
;;
*)
	# nothing to do
;;
esac

#DEBHELPER#