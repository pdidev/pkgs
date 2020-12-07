#!
set -e

. /usr/share/mpi-default-dev/debian_defaults
if [ openmpi = "${ARCH_DEFAULT_MPI_IMPL}" ]
then
	PRIORITY=30
else
	PRIORITY=20
fi

case "$1" in
configure)
	update-alternatives \
		--install \
		/usr/share/FTI/cmake \
		FTIConfig.cmake \
		/usr/share/FTI/openmpi/cmake \
		"${PRIORITY}"
;;
*)
	# nothing to do
;;
esac

#DEBHELPER#
