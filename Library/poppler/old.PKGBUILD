# $Id$
# Maintainer: Jan de Groot <jgc@archlinux.org>

pkgbase=poppler
pkgname=('poppler' 'poppler-glib' 'poppler-qt')
pkgver=0.22.5
pkgrel=1
arch=(i686 x86_64)
license=('GPL')
makedepends=('libjpeg' 'gcc-libs' 'cairo' 'fontconfig' 'openjpeg' 'gtk2' 'qt4' 'pkgconfig' 'lcms2' 'gobject-introspection' 'icu')
options=('!libtool' '!emptydirs')
url="http://poppler.freedesktop.org/"
_testtag=0d2bfd4af4c76a3bac27ccaff793d9129df7b57a
source=(http://poppler.freedesktop.org/${pkgbase}-${pkgver}.tar.gz
        http://cgit.freedesktop.org/poppler/test/snapshot/test-${_testtag}.tar.bz2)
md5sums=('1cd27460f7e3379d1eb109cfd7bcdb39'
         '9dc64c254a31e570507bdd4ad4ba629a')

build() {

  cd "${srcdir}"
  ln -sf test-${_testtag} test
  cd ${pkgbase}-${pkgver}

  sed -i -e '/AC_PATH_XTRA/d' configure.ac
  sed -i "s:AM_CONFIG_HEADER:AC_CONFIG_HEADERS:" configure.ac
  autoreconf -fi

  ./configure --prefix=/usr --sysconfdir=/etc \
      --localstatedir=/var \
      --enable-cairo-output \
      --enable-xpdf-headers \
      --enable-libjpeg --enable-zlib \
      --enable-poppler-qt4 \
      --enable-poppler-glib
  make
}

check() {
  cd "${srcdir}/${pkgbase}-${pkgver}"
  LANG=en_US.UTF8 make check
}

package_poppler() {
  pkgdesc="PDF rendering library based on xpdf 3.0"
  depends=('libjpeg' 'gcc-libs' 'cairo' 'fontconfig' 'openjpeg' 'lcms2')
  optdepends=('poppler-data: encoding data to display PDF documents containing CJK characters')
  conflicts=("poppler-qt3<${pkgver}")

  cd "${srcdir}/${pkgbase}-${pkgver}"
  sed -e 's/^glib_subdir =.*/glib_subdir =/' \
      -e 's/^qt4_subdir =.*/qt4_subdir =/' -i Makefile
  make DESTDIR="${pkgdir}" install

  rm -f "${pkgdir}"/usr/lib/pkgconfig/poppler-{glib,qt4}.pc
}

package_poppler-glib() {
  pkgdesc="Poppler glib bindings"
  depends=("poppler=${pkgver}" 'glib2')

  cd "${srcdir}/${pkgbase}-${pkgver}/poppler"
  make DESTDIR="${pkgdir}" install-libLTLIBRARIES
  cd "${srcdir}/${pkgbase}-${pkgver}/glib"
  make DESTDIR="${pkgdir}" install
  install -m755 -d "${pkgdir}/usr/lib/pkgconfig"
  install -m644 ../poppler-glib.pc "${pkgdir}/usr/lib/pkgconfig/"
  rm -f "${pkgdir}"/usr/lib/libpoppler.*
  rm -f "${pkgdir}/usr/bin/poppler-glib-demo"
}

package_poppler-qt() {
  pkgdesc="Poppler Qt bindings"
  depends=("poppler=${pkgver}" 'qt4')

  cd "${srcdir}/${pkgbase}-${pkgver}/poppler"
  make DESTDIR="${pkgdir}" install-libLTLIBRARIES
  cd "${srcdir}/${pkgbase}-${pkgver}/qt4"
  make DESTDIR="${pkgdir}" install
  install -m755 -d "${pkgdir}/usr/lib/pkgconfig"
  install -m644 ../poppler-qt4.pc "${pkgdir}/usr/lib/pkgconfig/"
  rm -f "${pkgdir}"/usr/lib/libpoppler.*
}
