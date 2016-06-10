# Use abs path, otherwise daily builds automagic won't work
%env %import ${SABAYON_MOLECULE_HOME:-/sabayon}/molecules/lxqt.common
%env %import ${SABAYON_MOLECULE_HOME:-/sabayon}/molecules/amd64.common

%env release_version: ${SABAYON_RELEASE:-LATEST}
release_desc: amd64 LXQt Development

%env source_iso: ${SABAYON_MOLECULE_HOME:-/sabayon}/iso/Sabayon_Linux_${ISO_TAG:-LATEST}_amd64_SpinBase-dev.iso
%env destination_iso_image_name: Sabayon_Linux_${SABAYON_RELEASE:-LATEST}_amd64_LXQt-dev.iso
