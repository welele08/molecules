#!/bin/sh

# Path to molecules.git dir
SABAYON_MOLECULE_HOME="${SABAYON_MOLECULE_HOME:-/sabayon}"
export SABAYON_MOLECULE_HOME
#cp "${SABAYON_MOLECULE_HOME}/remaster/capesos/etc/xdg/menus/xfce-applications.menu" "${CHROOT_DIR}/etc/xdg/menus/"
cp -r "${SABAYON_MOLECULE_HOME}/remaster/capesos/etc" "${CHROOT_DIR}"|| exit 1
cp -r "${SABAYON_MOLECULE_HOME}/remaster/capesos/usr" "${CHROOT_DIR}"|| exit 1
PKGS_DIR="${SABAYON_MOLECULE_HOME}/pkgcache"
CHROOT_PKGS_DIR="${CHROOT_DIR}/var/lib/entropy/client/packages"

echo "================================================="
echo "REMASTER_POST.SH ARGS: $@"
echo "================================================="
if [ $# -gt 0 ] ; then
  if [ -f "$1" ] ; then
    echo "================================================="
    echo "REMASTER_POST.SH ARGS: Executing $1..."
    echo "================================================="
    . $1
    echo "================================================="
  fi
fi

# load common stuff
. "${SABAYON_MOLECULE_HOME}"/scripts/remaster_post_common.sh

# make sure to not leak /proc
umount "${CHROOT_DIR}/proc" &> /dev/null
umount "${CHROOT_DIR}/proc" &> /dev/null
umount "${CHROOT_DIR}/proc" &> /dev/null

echo "Umounting bind to ${CHROOT_PKGS_DIR}"
umount "${CHROOT_PKGS_DIR}" || exit 1

exit 0
