#!/bin/sh
set -e

SRCDIR="$(dirname "$0")"

. /etc/os-release
# The suite to point at is the one this package is built for, as its changelog names it.
# /etc/os-release and /etc/debian_version tell neither testing from unstable: both say forky and forky/sid.
SUITE="$(dpkg-parsechangelog -l "${SRCDIR}/debian/changelog" -S Distribution)"
sed "s/#VERSION_CODENAME#/${SUITE}/g;s/#ID#/${ID}/g" "${SRCDIR}/pdi.sources.in" > pdi.sources
