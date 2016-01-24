# $Id$
# Maintainer : Martin Wimpress <code@flexion.org>

_ver=1.12
# pkgname=libmatemixer
pkgbase=libmatemixer
pkgname=(${pkgbase}-gtk3)
pkgver=${_ver}.1
pkgrel=1
pkgdesc="Mixer library for MATE Desktop"
url="http://mate-desktop.org"
arch=('i686' 'x86_64')
license=('LGPL')
#depends=('alsa-lib' 'libpulse')
depends=('alsa-lib')
makedepends=('mate-common')
source=("http://pub.mate-desktop.org/releases/${_ver}/${pkgbase}-${pkgver}.tar.xz")
sha1sums=('37c5b081e80db36210834e123643e2f7a12f176d')

if [ "$CARCH" = "x86_64" ]; then
  dstdir=mate64
elif [ "$CARCH" = "i686" ]; then
  dstdir=mate
fi

build() {
    cd "${srcdir}/${pkgbase}-${pkgver}"
    ./configure \
        --prefix=/usr/local/${dstdir}/mate_gtk+3.0 \
        --sysconfdir=/usr/local/${dstdir}/mate_gtk+3.0/etc \
        --localstatedir=/var \
        --disable-static --disable-pulseaudio
    make
}

package() {
    cd "${srcdir}/${pkgbase}-${pkgver}"
    make DESTDIR="${pkgdir}" install
}
