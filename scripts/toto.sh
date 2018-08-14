#!/bin/sh

date >>/var/log/toto
# Path to molecules.git dir
SABAYON_MOLECULE_HOME="${SABAYON_MOLECULE_HOME:-/sabayon}"
export SABAYON_MOLECULE_HOME

PKGS_DIR="${SABAYON_MOLECULE_HOME}/pkgcache"
CHROOT_PKGS_DIR="${CHROOT_DIR}/var/lib/entropy/client/packages"

[[ ! -d "${PKGS_DIR}" ]] && mkdir -p "${PKGS_DIR}"
[[ ! -d "${CHROOT_PKGS_DIR}" ]] && mkdir -p "${CHROOT_PKGS_DIR}"

# make sure it's all clean before mounting
echo "Mounting bind to ${CHROOT_PKGS_DIR}"
mkdir -p "${CHROOT_PKGS_DIR}" || exit 1
mount --bind "${PKGS_DIR}" "${CHROOT_PKGS_DIR}" || exit 1

content=$(ls -1 "${CHROOT_DIR}/proc" | wc -l)
if [ "${content}" -le 3 ]; then
	echo "Mounting /proc ..."
	mount -t proc proc "${CHROOT_DIR}/proc"
fi

echo "cp capesos repo file to ${CHROOT_DIR}/etc/entropy/repositories.conf.d/"
cp /etc/entropy/repositories.conf.d/capesos ${CHROOT_DIR}/etc/entropy/repositories.conf.d/
exit 0
