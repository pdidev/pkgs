#!
set -e

PKG_VERSION="#PKG_VERSION#"

case "$1" in
*)
	update-alternatives \
		--remove \
		pdi-${PKG_VERSION}_decl_hdf5_plugin.so-$(dpkg-architecture -qDEB_HOST_MULTIARCH) \
		/usr/lib/$(dpkg-architecture -qDEB_HOST_MULTIARCH)/pdiplugin-decl-hdf5/pdi/plugins_${PKG_VERSION}/libpdi_decl_hdf5_plugin.so
;;
esac

#DEBHELPER#
