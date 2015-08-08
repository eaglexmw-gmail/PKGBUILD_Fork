# $Id$
# Maintainer:
# Contributor: Tobias Powalowski <tpowa@archlinux.org>
# Contributor: red_over_blue,Ben <ben@benmazer.net>,Kritoke <kritoke@gamebox.net>

pkgname=qscintilla-qt3
pkgver=1.7.1
pkgrel=3
pkgdesc="A port to Qt3 of Neil Hodgson's Scintilla C++ editor class"
arch=('i686' 'x86_64')
url="http://www.riverbankcomputing.co.uk/software/qscintilla/intro/"
license=('GPL2')
#depends=('qt3')
options=('staticlibs')
source=(http://www.riverbankcomputing.co.uk/static/Downloads/QScintilla1/QScintilla-1.71-gpl-$pkgver.tar.gz)
md5sums=('dfa047b45d4f09ae8d4a8a431ba88a5a')

build() {
  #. /etc/profile.d/qt3.sh
  cd $srcdir/QScintilla-1.71-gpl-$pkgver
  cd qt
  echo [STARTING sed on qscintilla.pro]
  sed -i "s%DESTDIR.*%DESTDIR=$pkgdir/usr/local/qt/qt3/lib%g" qscintilla.pro

  /usr/local/qt/qt3/bin/qmake qscintilla.pro

  sed -i 's|-$(DEL_FILE) $(TARGETA)|echo &|g' Makefile
  sed -i 's|../../../pkg/qscintilla-qt3/usr/local/qt/qt3/lib/lib|lib|g' Makefile

  make staticlib
}

package() {
  cd $srcdir/QScintilla-1.71-gpl-$pkgver
  cd qt

  make INSTALL_ROOT=$pkgdir install

  #mkdir $pkgdir/usr/local/qt/qt3/lib
  cp *.a $pkgdir/usr/local/qt/qt3/lib

  # installind includes
  for i in qextscintilla*.h; do
    install -m 644 -D $i $pkgdir/usr/local/qt/qt3/include/$i
  done
  
  for i in qscintilla*.qm
  do
    install -m 644 -D $i $pkgdir/usr/local/qt/qt3/translations/$i
  done
}
