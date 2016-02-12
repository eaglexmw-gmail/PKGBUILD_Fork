# $Id$
# Maintainer: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>

pkgbase=gstreamer-vaapi
# pkgname=(gst-vaapi gstreamer0.10-vaapi)
pkgname=(gst-vaapi)
pkgver=0.7.0
pkgrel=1
pkgdesc="GStreamer Multimedia Framework VA Plugins"
arch=(i686 x86_64)
license=(LGPL)
url="http://www.freedesktop.org/software/vaapi/releases/gstreamer-vaapi/"
#makedepends=(gst-plugins-base gst-plugins-bad gstreamer0.10-base-plugins gstreamer0.10-bad-plugins
#             libva libxrandr libvpx)
makedepends=(libxrandr)
options=(!emptydirs)

#source=(git://gitorious.org/vaapi/${pkgbase}.git#commit=5ffa82b)
source=($url/$pkgbase-$pkgver.tar.bz2)
sha1sums=('053a7af120c72fda0b46450c4a94a752abf64a74')

prepare() {
  mkdir build build-0.10
  sed -i "s| tests | |g" ./gstreamer-vaapi-0.7.0/Makefile.am
  cd $pkgbase-$pkgver/
  autoreconf

  export OLD_PKG_CONFIG_PATH=${PKG_CONFIG_PATH}
}

_build() (
  cd $pkgbase-$pkgver
  autoreconf
  cd ../"$1"; shift
  ../$pkgbase-$pkgver/configure --prefix=/usr \
    --enable-static \
    --disable-builtin-libvpx --disable-gtk-doc --disable-shared \
    "$@"
  # --enable-static-plugins  --enable-introspection=yes
  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
  make
)

build() {
  _build build
  # _build build-0.10 --with-gstreamer-api=0.10 --disable-wayland
}

#check() {
  #make -C build -k check
  #make -C build-0.10 -k check
#}

package_gst-vaapi() {
  depends=(gst-plugins-base gst-plugins-bad libva libxrandr libvpx)
  export PKG_CONFIG_PATH=/usr/local/gstreamer/$dstdir1/lib/pkgconfig:${PKG_CONFIG_PATH}
  make -C build DESTDIR="$pkgdir" install
}

package_gstreamer0.10-vaapi() {
  depends=(gstreamer0.10-base-plugins gstreamer0.10-bad-plugins libva libxrandr libvpx)
  export PKG_CONFIG_PATH=/usr/local/gstreamer/$dstdir0/lib/pkgconfig:${PKG_CONFIG_PATH}
  make -C build-0.10 DESTDIR="$pkgdir" install
}
