#!

SRCDIR="$(dirname "$0")"

. /etc/os-release
if [ "x${ID}" = 'xdebian' ] && grep -qs sid /etc/debian_version
then
	VERSION_CODENAME=sid
fi
sed "s/#VERSION_CODENAME#/${VERSION_CODENAME}/g;s/#ID#/${ID}/g" "${SRCDIR}/pdi.sources.in" > pdi.sources
