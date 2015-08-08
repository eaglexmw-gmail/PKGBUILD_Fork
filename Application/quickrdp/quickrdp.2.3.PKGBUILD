# Maintainer: Phillip Smith <fukawi2@NO-SPAM.gmail.com>
# http://github.com/fukawi2/aur-packages

pkgname=quickrdp
pkgver=2.3
pkgrel=1
pkgdesc="Connection manager program for your remote desktop, telnet, SSH or VNC connections."
arch=('i686' 'x86_64')  # untested on i686; please let me know if it works
url="http://quickrdp.sourceforge.net/"
license=('GPL3')
#depends=('wxgtk' 'curl')
depends=('curl')
optdepends=('rdesktop: remote desktop support')
source=("http://downloads.sourceforge.net/$pkgname/$pkgname-$pkgver-src.tar.gz")

build() {
  cd "$srcdir/$pkgname-$pkgver"
  sed -i 's|/usr/share|/usr/local/quickrdp/share|g' Makefile
  sed -i 's|rdesktop |/usr/local/rdesktop/bin/rdesktop |g' src/Settings.cpp
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make DESTDIR="$pkgdir" install
}

# vim:set ts=2 sw=2 et:
md5sums=('da6b56360ea4eabd673e44cf1907402a')
