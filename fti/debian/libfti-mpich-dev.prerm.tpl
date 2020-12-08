#!
set -e

PKG_VERSION="#PKG_VERSION#"

case "$1" in
*)
	update-alternatives \
		--remove \
		FTIConfig.cmake \
		/usr/share/FTI/mpich/cmake
;;
esac

#DEBHELPER#
