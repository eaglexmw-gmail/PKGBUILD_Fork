# $Id$
# Maintainer: Jan de Groot <jgc@archlinux.org>

pkgbase=poppler
pkgname=('poppler' 'poppler-glib' 'poppler-qt')
pkgver=0.16.7
pkgrel=2
arch=(i686 x86_64)
license=('GPL')
makedepends=('libjpeg' 'gcc-libs' 'cairo' 'libxml2' 'fontconfig' 'openjpeg' 'gtk2' 'pkgconfig' 'lcms')
options=('!libtool')
url="http://poppler.freedesktop.org/"
source=(http://poppler.freedesktop.org/${pkgbase}-${pkgver}.tar.gz)
md5sums=('3afa28e3c8c4f06b0fbca3c91e06394e')

build() {
  cd "${srcdir}/${pkgbase}-${pkgver}"
  sed -i -e '/AC_PATH_XTRA/d' configure.ac
  autoreconf
  ./configure --prefix=/usr --sysconfdir=/etc \
      --localstatedir=/var --disable-shared \
      --enable-cairo-output \
      --enable-xpdf-headers \
      --enable-libjpeg --enable-zlib \
      --enable-poppler-qt4 \
      --enable-poppler-glib
  make
}

package_poppler() {
  pkgdesc="PDF rendering library based on xpdf 3.0"
  depends=('libjpeg' 'gcc-libs' 'cairo' 'libxml2' 'fontconfig' 'openjpeg' 'lcms' 'poppler-data')
  conflicts=("poppler-qt3<${pkgver}")

  cd "${srcdir}/${pkgbase}-${pkgver}"
  sed -e 's/^glib_subdir =.*/glib_subdir =/' \
      -e 's/^qt4_subdir =.*/qt4_subdir =/' -i Makefile
  make DESTDIR="${pkgdir}" install

  rm -f "${pkgdir}"/usr/lib/pkgconfig/poppler-{glib,qt4}.pc
}

package_poppler-glib() {
  pkgdesc="Poppler glib bindings"
  depends=("poppler=${pkgver}" 'gtk2')

  cd "${srcdir}/${pkgbase}-${pkgver}/poppler"
  make DESTDIR="${pkgdir}" install-libLTLIBRARIES
  cd "${srcdir}/${pkgbase}-${pkgver}/glib"
  make DESTDIR="${pkgdir}" install
  install -m755 -d "${pkgdir}/usr/lib/pkgconfig"
  install -m644 ../poppler-glib.pc "${pkgdir}/usr/lib/pkgconfig/"
  rm -f "${pkgdir}"/usr/lib/libpoppler.*
}

package_poppler-qt() {
  pkgdesc="Poppler Qt bindings"
  depends=("poppler=${pkgver}")

  cd "${srcdir}/${pkgbase}-${pkgver}/poppler"
  make DESTDIR="${pkgdir}" install-libLTLIBRARIES
  cd "${srcdir}/${pkgbase}-${pkgver}/qt4"
  make DESTDIR="${pkgdir}" install
  install -m755 -d "${pkgdir}/usr/lib/pkgconfig"
  install -m644 ../poppler-qt4.pc "${pkgdir}/usr/lib/pkgconfig/"
  rm -f "${pkgdir}"/usr/lib/libpoppler.*
}
