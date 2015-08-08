# $Id$
# Maintainer : Martin Wimpress <code@flexion.org>

#pkgname=gnome-main-menu
pkgbase=gnome-main-menu
pkgname=(${pkgbase}-gtk3)
pkgver=1.8.0
pkgrel=2
pkgdesc="A mate-panel applet similar to the traditional main-menu, but with a few additions."
url="http://mate-desktop.org"
arch=('i686' 'x86_64')
license=('GPL')
# depends=('caja' 'libunique' 'mate-control-center' 'mate-desktop' 'mate-panel')
makedepends=('mate-common' 'yelp-tools')
optdepends=('yelp: for reading help documents')
source=("http://pub.mate-desktop.org/releases/1.8/${pkgbase}-${pkgver}.tar.xz")
sha1sums=('287e904506ae2796e84b556f76e3b12274c1c89f')
install=${pkgbase}.install

if [ "$CARCH" = "x86_64" ]; then
  dstdir=mate64
elif [ "$CARCH" = "i686" ]; then
  dstdir=mate
fi

prepare() {
    cd "${srcdir}/${pkgbase}-${pkgver}"

    # Replace libslab with libmate-slab
    sed -i 's|libslab|mate-slab|' configure.ac
    sed -i 's|libslab/slab.h|libmate-slab/slab.h|' */src/*

    # Update disable-log-out key location
    sed -i 's|org.mate.panel|org.mate.lockdown|' main-menu/src/main-menu-ui.c

    autoreconf -fi
}

build() {
    cd "${srcdir}/${pkgbase}-${pkgver}"

    export PKG_CONFIG_PATH=${PKG_CONFIG_PATH}:/usr/local/${dstdir}/mate_gtk+3.0/lib/pkgconfig/

    ./configure \
        --prefix=/usr/local/${dstdir}/mate_gtk+3.0 \
        --libexecdir=/usr/local/${dstdir}/mate_gtk+3.0/lib/${pkgbase} \
        --sysconfdir=/usr/local/${dstdir}/mate_gtk+3.0/etc \
        --localstatedir=/var \
        --enable-caja-extension \
        --disable-static
    make
}

package() {
    cd "${srcdir}/${pkgbase}-${pkgver}"
    make DESTDIR="${pkgdir}" install
}
