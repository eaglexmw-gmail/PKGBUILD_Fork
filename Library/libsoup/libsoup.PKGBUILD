# $Id$
# Maintainer: Jan de Groot <jgc@archlinux.org>

pkgname=libsoup
pkgver=2.44.2
pkgrel=1
pkgdesc="GNOME HTTP Library"
arch=(i686 x86_64)
license=(LGPL)
url="http://www.gnome.org"
#depends=(glib2 libxml2 glib-networking sqlite)
depends=(glib2 libxml2 sqlite)
makedepends=(intltool gobject-introspection python)
#checkdepends=(apache php php-apache)
provides=("libsoup-gnome=$pkgver-$pkgrel")
conflicts=(libsoup-gnome)
replaces=(libsoup-gnome)
options=('staticlibs' '!emptydirs')
source=(http://ftp.gnome.org/pub/gnome/sources/$pkgname/${pkgver%.*}/$pkgname-$pkgver.tar.xz)
sha256sums=('e7e4b5ab74a6c00fc267c9f5963852d28759ad3154dab6388e2d6e1962d598f3')

build() {
  cd $pkgname-$pkgver
  ./configure --prefix=/usr --sysconfdir=/etc \
      --localstatedir=/var --enable-static --disable-tls-check
  make
}

package() {
  cd $pkgname-$pkgver
  make DESTDIR="$pkgdir" install
}
