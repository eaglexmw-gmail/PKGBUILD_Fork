# $Id$
# Contributor: Alexander Fehr <pizzapunk gmail com>
# Maintainer: Daniel J Griffiths <ghost1227@archlinux.us>

pkgname=filezilla
pkgver=3.5.1
pkgrel=1
pkgdesc="Fast and reliable FTP, FTPS and SFTP client"
arch=('i686' 'x86_64')
url="http://filezilla-project.org/"
license=('GPL')
# depends=('dbus-core' 'wxgtk' 'hicolor-icon-theme' 'sqlite3')
depends=('dbus-core' 'hicolor-icon-theme' 'sqlite3')
source=("http://downloads.sourceforge.net/project/filezilla/FileZilla_Client/${pkgver}/FileZilla_${pkgver}_src.tar.bz2"
        gnutls.patch)
md5sums=('8afb7aee4ba72b6363dcfe469bc7fbef'
         'SKIP')

build() {
  cd ${pkgname}-${pkgver}

  patch -p1 -i ../gnutls.patch

   ./autogen.sh
  ./configure \
    --prefix=/usr/local/filezilla \
    --disable-manualupdatecheck \
    --disable-autoupdatecheck \
    --disable-static \
    --with-tinyxml=builtin

  make
}

package() {
  cd ${pkgname}-${pkgver}

  make DESTDIR=${pkgdir} install
}
