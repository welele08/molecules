# Path to molecules.git dir
SABAYON_MOLECULE_HOME="${SABAYON_MOLECULE_HOME:-/sabayon}"
. "${SABAYON_MOLECULE_HOME}/scripts/iso_build.include"

(
    flock --timeout 7200 -x 9
    if [ "${?}" != "0" ]; then
        echo "[cleanup] cannot acquire lock, stale process holding it?" >&2
        exit 1
    fi
    "${SABAYON_MOLECULE_HOME}/scripts/cleanup_pkgcache.sh"
) 9> "${ISO_BUILD_LOCK}"

exit ${?}