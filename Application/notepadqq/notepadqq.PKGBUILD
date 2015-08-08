# Maintainer: twa022 <twa022 at gmail dot com>
# Contributor: Zom <zom[at]eevul[dot]org>

pkgname=notepadqq
pkgver=0.41.1
_codemirrorver=4.7.0
pkgrel=1
pkgdesc="A Linux clone of Notepad++"
arch=('i686' 'x86_64')
url="http://notepadqq.sourceforge.net/wp/"
license=('GPL3')
#depends=('qt5-webkit' 'qt5-svg')
makedepends=('')
source=("${pkgname}-${pkgver}.tar.gz"::https://github.com/notepadqq/${pkgname}/archive/v${pkgver}.tar.gz
        codemirror-${_codemirrorver}.tar.gz::https://github.com/notepadqq/CodeMirror/archive/${_codemirrorver}.tar.gz)
sha256sums=('e4ca0908475230b5f0cfff20dbf9cdb18c36c1c564201614f070ea822b834372'
            '7fe7bfc906ef0a7108330f9a3d003459ed545f7a4a6cfc2d6193dd799784b5f2')

build() {
  cd ${srcdir}/notepadqq-${pkgver}
  cp -R ${srcdir}/CodeMirror-${_codemirrorver}/* ${srcdir}/notepadqq-${pkgver}/src/editor/libs/codemirror/

  #sed -i 's|webkitwidgets|webkit|g' src/ui/ui.pro
  #patch -p1 -i ../qt_4_2.patch
  #CXXFLAGS="${CXXFLAGS} -std=c++11"

  sed -i '7 a QT += dbus' src/ui/ui.pro
  sed -i '8 a CONFIG += no_lflags_merge ' src/ui/ui.pro

  ./configure --qmake-path qmake-qt5 --prefix=/usr/local/notepadqq
  #./configure --qmake-path qmake --prefix=/usr/local/notepadqq
  make
}

package() {
  cd ${srcdir}/notepadqq-${pkgver}/src/ui

  make INSTALL_ROOT="$pkgdir" install

  install -Dm644 "${pkgdir}/usr/local/notepadqq/share/icons/hicolor/scalable/apps/${pkgname}.svg" "${pkgdir}/usr/local/notepadqq/share/pixmaps/${pkgname}.svg"
}
