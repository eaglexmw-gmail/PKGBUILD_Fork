# $Id$
# Maintainer: Eric Belanger <eric@archlinux.org>

pkgname=wxgtk
pkgver=2.8.12
pkgrel=4
pkgdesc="GTK+ implementation of wxWidgets API for GUI"
arch=('i686' 'x86_64')
url="http://wxwidgets.org"
license=('custom:wxWindows')
depends=('gtk2' 'libgl' 'libxxf86vm')
makedepends=('mesa')
source=(http://downloads.sourceforge.net/wxwindows/wxGTK-${pkgver}.tar.bz2)
#source=(http://downloads.sourceforge.net/wxpython/wxPython-src-${pkgver}.tar.bz2)
md5sums=('08f81ab60647308058f6ce99712b14f8')

build() {
  cd "${srcdir}/wxGTK-${pkgver}"
  ./configure --prefix=/usr/local --libdir=/usr/local/lib --with-gtk=2 --with-opengl --enable-unicode \
    --enable-graphics_ctx --disable-optimize --enable-mediactrl --with-regex=builtin \
    --with-libpng=sys --with-libxpm=sys --with-libjpeg=sys --with-libtiff=sys \
    --with-sdl --disable-precomp-headers

  make
  make -C locale allmo
  cd contrib/src
  make
}

package() {
  cd "${srcdir}/wxGTK-${pkgver}"
  make DESTDIR="${pkgdir}" install
  cd contrib/src
  make DESTDIR="${pkgdir}" install
  install -D -m644 ../../docs/licence.txt "${pkgdir}/usr/local/share/licenses/${pkgname}/LICENSE"
}
