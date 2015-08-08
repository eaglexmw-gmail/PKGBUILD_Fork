# $Id$
# Maintainer: Andreas Radke <andyrtr@archlinux.org>

pkgbase=webkitgtk
pkgname=(webkitgtk webkitgtk2)
pkgver=2.4.7
pkgrel=1
pkgdesc="GTK+ Web content engine library"
arch=(i686 x86_64)
url="http://webkitgtk.org/"
license=(custom)
#depends=(libxt libxslt sqlite libsoup enchant libgl geoclue2 gst-plugins-base-libs libsecret libwebp harfbuzz-icu)
depends=(libxt sqlite libsoup libgl)
#makedepends=(gtk3 gtk2 gperf python2 mesa ruby)
makedepends=(gtk3 gtk2 gperf mesa ruby)
optdepends=('gst-plugins-base: free media decoding'
            'gst-plugins-good: media decoding'
            'gst-libav: nonfree media decoding')
options=(!emptydirs staticlibs)
source=(http://webkitgtk.org/releases/$pkgbase-${pkgver}.tar.xz
        fix-pretty-quotes.patch)
sha256sums=('f5cf26e39abf1d6b2d25f1398348fef6bbe6c03fb4f99e11c569091c05197d38'
            '56316228bbbf0b7ebcbe210a35120f4e72cb9c1b680dd82cc2bde0f4549245e6')

prepare() {
  mkdir build-gtk{,2} path

  ln -s /usr/local/python2/bin/python2 path/python

  cd $pkgbase-$pkgver
  patch -Np0 -i ../fix-pretty-quotes.patch
  
  # :#!/usr/bin/env python
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/WebKit2/Scripts/generate-messages-header.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/WebKit2/Scripts/generate-message-receiver.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/JavaScriptCore/inspector/scripts/inline-and-minify-stylesheets-and-scripts.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/JavaScriptCore/inspector/scripts/CodeGeneratorInspector.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/WebCore/html/parser/create-html-entity-table
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Tools/gtk/check-for-webkitdom-api-breaks
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Tools/gtk/generate-inspector-gresource-manifest.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Tools/gtk/webkitdom.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Tools/gtk/common.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Tools/gtk/generate-gtkdoc
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Tools/gtk/generate-feature-defines-files

}

_build() (
  _ver="$1"; shift
  cd build-${_ver}

  ../$pkgbase-$pkgver/configure --prefix=/usr \
    --libexecdir=/usr/lib/webkit${_ver} \
    --disable-webkit2 \
    --disable-gtk-doc \
    --enable-static --disable-shared --disable-glibtest \
    "$@"

  #  --enable-introspection \

  # https://bugzilla.gnome.org/show_bug.cgi?id=655517
  sed -i 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool

  sed -i 's|AR_FLAGS = cruT|AR_FLAGS = cru|g' ./GNUmakefile

  # for gtk-3.0
  sed -i 's|libwebkitgtk-3.0.la \\|libwebkitgtk-3.0.la -lstdc++ \\|g' ./GNUmakefile

  # for gtk-2.0
  sed -i 's|libwebkitgtk-1.0.la \\|libwebkitgtk-1.0.la -lstdc++ \\|g' ./GNUmakefile

  sed -i 's| -lgstaudio-1.0 | -lgstaudio-1.0 -lorc-0.4 -lm -lrt -lpthread |g' ./GNUmakefile
  sed -i 's| -lgstvideo-1.0 | -lgstvideo-1.0 -lorc-0.4 -lm -lrt -lpthread |g' ./GNUmakefile
  sed -i 's| -lXt | -lXt -lSM -lICE |g' ./GNUmakefile

  sed -i 's|AR_FLAGS="cruT"|AR_FLAGS="cru"|g' ./libtool

  make all stamp-po
)

build() {
  PATH="$srcdir/path:$PATH"

  _build gtk
  _build gtk2 --with-gtk=2.0
}

package_webkitgtk() {
  depends+=(gtk3)
  optdepends+=('gtk2: Netscape plugin support')
  provides=("webkitgtk3=${pkgver}" "libwebkit3=${pkgver}")
  conflicts=(webkitgtk3 libwebkit3)
  replaces=(webkitgtk3 libwebkit3)

  make -C build-gtk -j1 DESTDIR="$pkgdir" install
  install -Dm644 $pkgbase-$pkgver/Source/WebKit/LICENSE \
    "$pkgdir/usr/share/licenses/webkitgtk/LICENSE"
}

package_webkitgtk2() {
  pkgdesc+=" for GTK2"
  depends+=(gtk2)
  provides=("libwebkit=${pkgver}")
  conflicts=(libwebkit)
  replaces=(libwebkit)

  make -C build-gtk2 -j1 DESTDIR="$pkgdir" install
  install -Dm644 $pkgbase-$pkgver/Source/WebKit/LICENSE \
    "$pkgdir/usr/share/licenses/webkitgtk2/LICENSE"
}
