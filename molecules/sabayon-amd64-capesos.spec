# Use abs path, otherwise daily builds automagic won't work
%env %import ${SABAYON_MOLECULE_HOME:-/sabayon}/molecules/xfce-capes.common
%env %import ${SABAYON_MOLECULE_HOME:-/sabayon}/molecules/amd64.common

%env release_version: ${SABAYON_RELEASE:-LATEST}
release_desc: amd64 Xfce


%env source_iso: ${SABAYON_MOLECULE_HOME:-/sabayon}/iso/Sabayon_Linux_${ISO_TAG:-LATEST}_amd64_SpinBase.iso
%env destination_iso_image_name: Sabayon_Linux_${SABAYON_RELEASE:-LATEST}_amd64_Xfce.iso
packages_to_add:
    sci-mathematics/giac
    app-misc/capesos-skel
    x11-themes/capesos-artwork-wallpapers
    x11-themes/Humanity-Dark-Aqua-icon-theme
    x11-themes/capesos-artwork-lightdm-slick-greeter
    x11-themes/capesos-artwork-grub
    x11-themes/capesos-artwork-isolinux
    x11-themes/capesos-artwork-core
    x11-themes/capesos-artwork-plymouth
    x11-apps/capesos-screencapture
    x11-misc/blackscreen
    gnome-extra/gnome-calculator
    app-docs/zeal
    app-editors/atom
    dev-python/notebook-capesos-icon
    gnome-base/nautilus
    gnome-extra/gnome-calculator-capesos-icon
    sci-mathematics/xcas-icon-capesos
    sci-mathematics/geogebra
    app-doc/zeal-icon-capesos
    dev-db/sqlitebrowser-icon-capesos
    app-editors/vim
    www-client/chromium
    app-office/libreoffice-icon-capesos
    app-doc/ressources-officielles-math
    sci-calculators/Numworks
    dev-python/Pyzo
    sci-mathematics/scratch3-ac-grenoble
    app-text/lecteur_pdf
    sci-mathematics/scilab
    net-analyzer/zabbix
    dev-python/numpy
    sci-libs/scipy
    dev-python/matplotlib
    dev-python/pillow
    dev-python/imageio
    app-doc/matplotlib-dash-docset
    app-doc/python2-dash-docset
    app-doc/python3-dash-docset
    app-doc/scipy-dash-docset
    app-doc/numpy-dash-docset
    app-admin/lsyncd
    dev-lang/python:2.7::capesos
    dev-lang/python:3.6::capesos
    net-vpn/openvpn
