#!

SRCDIR="$(dirname "$0")"

. /etc/os-release
sed "s/#VERSION_CODENAME#/${VERSION_CODENAME}/g;s/#ID#/${ID}/g" "${SRCDIR}/pdi.sources.in" > pdi.sources
