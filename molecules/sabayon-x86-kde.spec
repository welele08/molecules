# Use abs path, otherwise daily builds automagic won't work
%env %import ${SABAYON_MOLECULE_HOME:-/sabayon}/molecules/kde.common

prechroot: linux32

# Release Version
%env release_version: ${SABAYON_RELEASE:-11}

# Release Version string description
release_desc: x86 KDE

# Path to source ISO file (MANDATORY)
%env source_iso: ${SABAYON_MOLECULE_HOME:-/sabayon}/iso/Sabayon_Linux_SpinBase_DAILY_x86.iso

# Destination ISO image name, call whatever you want.iso, not mandatory
%env destination_iso_image_name: Sabayon_Linux_${SABAYON_RELEASE:-11}_x86_KDE.iso
