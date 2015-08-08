# Contributor: furester <xfurester@hotmail.com> 
# Contributor: Firmicus <firmicus gmx net> 
# Contributor: Paulo Matias <matiasΘarchlinux-br·org>
# Maintainer: Daniel J Griffiths <ghost1227@archlinux.us>

pkgname=texmaker
pkgver=3.3.4
pkgrel=1
pkgdesc='Free cross-platform latex editor'
arch=('i686' 'x86_64')
url="http://www.xm1math.net/texmaker/index.html"
license=('GPL')
source=("http://www.xm1math.net/texmaker/${pkgname}-${pkgver}.tar.bz2")
md5sums=('6010c540bb3d0d3571bf523601bc1a48')

build() {
	cd ${pkgname}-${pkgver}

	export INSTALL_ROOT=${pkgdir}

        #sed -i 's/ -lpoppler-qt4/ -Wl,-Bstatic,-lpoppler-qt4/g' texmaker.pro
        sed -i 's/+= qt warn_off release/+= qt warn_on release static/g' texmaker.pro

	qmake -unix PREFIX=//usr//local//texmaker texmaker.pro

        # sed -i 's/-lpoppler-qt4 -lz -lQtWebKit -lQtXml -lQtGui -lQtNetwork -lQtCore -lpthread/-lpoppler-qt4 -lpoppler -llcms -lopenjpeg -lz -lQtWebKit -pthread -pthread -pthread -pthread -lsqlite3 -pthread -pthread -pthread -pthread -pthread -pthread -pthread -pthread -pthread -pthread -pthread -pthread -pthread -pthread -lQtXml -pthread -pthread -pthread -pthread -L\/usr\/X11R6\/lib -pthread -pthread -pthread -pthread -pthread -pthread -pthread -pthread -lQtNetwork -pthread -pthread -pthread -pthread -lssl -lcrypto -pthread -pthread -lQtGui -ljpeg -lmng -ltiff -pthread -pthread -pthread -lpng -pthread -lgobject-2.0 -lSM -lICE -lXrender -lfontconfig -lfreetype -lXext -lX11 -lQtCore -lz -lm -ldl -pthread -lgthread-2.0 -lrt -lglib-2.0 -lpthread -lXrender -lfontconfig -lfreetype -lXext -lX11 -lm /g' Makefile
        sed -i 's|-I/usr/include/poppler/qt4|-I/usr/local/include/poppler/qt4|g' Makefile
        sed -i 's/-lpoppler-qt4 /-lpoppler-qt4 -lpoppler -llcms -lopenjpeg /g' Makefile
        sed -i 's/-lQtWebKit /-lQtWebKit -ljscore -pthread -pthread -pthread -pthread -lsqlite3 -pthread -pthread -pthread -pthread -pthread -pthread -pthread -pthread -pthread -pthread -pthread -pthread -pthread -pthread /g' Makefile
        sed -i 's/-lQtXml /-lQtXml -pthread -pthread -pthread -pthread -L\/usr\/X11R6\/lib -pthread -pthread -pthread -pthread -pthread -pthread -pthread -pthread /g' Makefile
        sed -i 's/-lQtGui /-lQtGui -ljpeg -lmng -ltiff -pthread -pthread -pthread -lpng14 -pthread -lgobject-2.0 -lSM -lICE -lXrender -lfontconfig -lfreetype -lXext -lX11 /g' Makefile
        sed -i 's/-lQtNetwork /-lQtNetwork -pthread -pthread -pthread -pthread -lssl -lcrypto -pthread -pthread /g' Makefile
        sed -i 's/-lQtCore /-lQtCore -lz -lm -ldl -pthread -lgthread-2.0 -lrt -lglib-2.0 -lpthread -lXrender -lfontconfig -lfreetype -lXext -lX11 -lm /g' Makefile

	make
}

package() {
	cd ${pkgname}-${pkgver}

	export INSTALL_PATH=${pkgdir}
	make install
        mv ${pkgdir}/usr/share/* ${pkgdir}/usr/local/texmaker/share/
        rmdir ${pkgdir}/usr/share/
}
