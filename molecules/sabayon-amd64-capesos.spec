# Use abs path, otherwise daily builds automagic won't work
%env %import ${SABAYON_MOLECULE_HOME:-/sabayon}/molecules/xfce-capes.common
%env %import ${SABAYON_MOLECULE_HOME:-/sabayon}/molecules/amd64.common

%env release_version: ${SABAYON_RELEASE:-LATEST}
release_desc: amd64 capesos


%env source_iso: ${SABAYON_MOLECULE_HOME:-/sabayon}/iso/Sabayon_Linux_${ISO_TAG:-LATEST}_amd64_SpinBase.iso
%env destination_iso_image_name: Sabayon_Linux_${SABAYON_RELEASE:-LATEST}_amd64_capesos.iso
packages_to_add:
#system
  app-misc/capesos-skel
  x11-themes/capesos-artwork-wallpapers
  x11-themes/Humanity-Dark-Aqua-icon-theme
  x11-themes/capesos-artwork-lightdm-slick-greeter
  x11-themes/capesos-artwork-grub
  x11-themes/capesos-artwork-isolinux
  x11-themes/capesos-artwork-core
  x11-themes/capesos-artwork-plymouth
#logiciels_commun
  x11-apps/capesos-screencapture
  x11-misc/blackscreen
  app-docs/zeal
  app-doc/zeal-icon-capesos
  gnome-base/nautilus
  app-editors/vim
  www-client/chromium
  app-office/libreoffice-icon-capesos
  app-editors/atom
  net-analyzer/zabbix  

#logiciels_info?
  dev-db/sqlitebrowser-icon-capesos

#logiciels_math
    sci-mathematics/giac
    sci-mathematics/xcas-icon-capesos
    gnome-extra/gnome-calculator
    gnome-extra/gnome-calculator-capesos-icon
    sci-calculators/Numworks
    sci-mathematics/geogebra
    app-doc/ressources-officielles-math
    dev-python/Pyzo
    sci-mathematics/scratch3-ac-grenoble
    app-text/lecteur_pdf
    sci-mathematics/scilab
    #Python
    dev-lang/python:2.7::capesos
    app-doc/python2-dash-docset
    dev-lang/python:3.6::capesos
    app-doc/python3-dash-docset
    dev-python/notebook-capesos-icon
    dev-python/numpy
    app-doc/numpy-dash-docset
    sci-libs/scipy
    app-doc/scipy-dash-docset
    dev-python/matplotlib
    app-doc/matplotlib-dash-docset
    dev-python/pillow
    dev-python/imageio

#outils-session
    app-misc/login-script
    app-admin/lsyncd
    net-vpn/openvpn
    net-misc/capesos-primitiveComm
    net-misc/mkhosts
    net-misc/test-vpn
    net-misc/capesos-vpn-config-client
    net-misc/mkhosts
    net-misc/gestion-doc-candidat-serveur

