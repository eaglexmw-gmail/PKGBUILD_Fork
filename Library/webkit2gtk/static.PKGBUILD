# $Id$
# Maintainer: Eric Bélanger <eric@archlinux.org>

pkgname=webkit2gtk
pkgver=2.6.4
pkgrel=1
pkgdesc="GTK+ Web content engine library"
arch=('i686' 'x86_64')
url="http://webkitgtk.org/"
license=('custom')
#depends=('libxt' 'libxslt' 'enchant' 'geoclue2' 'gst-plugins-base-libs'
#	 'libsecret' 'libwebp' 'harfbuzz-icu' 'gtk3')
depends=('libxt' 'libxslt' 'gtk3')
#makedepends=('gtk2' 'gperf' 'gobject-introspection' 'python2' 'ruby' 'gtk-doc' 'cmake' 'python')
makedepends=('gtk2' 'gperf' 'ruby' 'cmake')
optdepends=('gtk2: Netscape plugin support'
            'gst-plugins-base: free media decoding'
            'gst-plugins-good: media decoding'
            'gst-libav: nonfree media decoding')
options=('!emptydirs' 'staticlibs')
source=(http://webkitgtk.org/releases/webkitgtk-${pkgver}.tar.xz
        fix-pretty-quotes.patch)
sha256sums=('beef5e24edd9b9cade22d80bf373c74d236f996fe30f49f8697a70f267772e9b'
            '56316228bbbf0b7ebcbe210a35120f4e72cb9c1b680dd82cc2bde0f4549245e6')

prepare() {
  mkdir build

  cd webkitgtk-$pkgver
  patch -p0 -i ../fix-pretty-quotes.patch

  #sed -i '1s/python$/&2/' Tools/gtk/generate-gtkdoc
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/WebKit2/Scripts/generate-messages-header.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/WebKit2/Scripts/generate-message-receiver.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/JavaScriptCore/replay/scripts/CodeGeneratorReplayInputs.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/JavaScriptCore/replay/scripts/CodeGeneratorReplayInputsTemplates.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/JavaScriptCore/inspector/scripts/codegen/generator.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/JavaScriptCore/inspector/scripts/codegen/generate_backend_commands.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/JavaScriptCore/inspector/scripts/codegen/generate_frontend_dispatcher_implementation.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/JavaScriptCore/inspector/scripts/codegen/generate_frontend_dispatcher_header.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/JavaScriptCore/inspector/scripts/codegen/generate_backend_dispatcher_implementation.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/JavaScriptCore/inspector/scripts/codegen/models.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/JavaScriptCore/inspector/scripts/codegen/generate_backend_dispatcher_header.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/JavaScriptCore/inspector/scripts/codegen/generate_protocol_types_header.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/JavaScriptCore/inspector/scripts/codegen/generate_protocol_types_implementation.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/JavaScriptCore/inspector/scripts/codegen/generator_templates.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/JavaScriptCore/inspector/scripts/inline-and-minify-stylesheets-and-scripts.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/JavaScriptCore/inspector/scripts/generate-inspector-protocol-bindings.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/WebCore/make-file-arrays.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/WebCore/css/makeSelectorPseudoElementsMap.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/WebCore/css/makeSelectorPseudoClassAndCompatibilityElementMap.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/WebCore/html/parser/create-html-entity-table
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/WebCore/Scripts/make-js-file-arrays.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Source/WebCore/platform/network/create-http-header-name-table
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Tools/gtk/jhbuildrc
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Tools/gtk/check-for-webkitdom-api-breaks
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Tools/gtk/generate-inspector-gresource-manifest.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Tools/gtk/webkitdom.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Tools/gtk/common.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Tools/gtk/generate-gtkdoc
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Tools/gtk/ycm_extra_conf.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Tools/gtk/make-dist.py
  sed -i 's|/usr/bin/env python|/usr/local/python2/bin/python2|g' ./Tools/Scripts/run-gtk-tests

  
  sed -i 's| SHARED| STATIC|g' ./CMakeLists.txt
  sed -i 's|ruT|ru|g' ./Source/cmake/OptionsCommon.cmake

  rm -r Source/ThirdParty/gtest/
  rm -r Source/ThirdParty/qunit/
}

build() {
  cd build
  export PATH="$PATH:/usr/local/python2/bin"
  cmake -DPORT=GTK -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_SKIP_RPATH=ON -DCMAKE_INSTALL_PREFIX=/usr \
        -DLIB_INSTALL_DIR=/usr/lib -DLIBEXEC_INSTALL_DIR=/usr/lib/webkit2gtk-4.0 \
        -DENABLE_GTKDOC=OFF ../webkitgtk-$pkgver

  make cmake_check_build_system

  sed -i '1029,1030 d' ./CMakeFiles/Makefile2
  sed -i '932,933 d' ./CMakeFiles/Makefile2

  sed -i 's|libharfbuzz.a |libharfbuzz.a -lgraphite2 |g' ./Source/WebKit2/CMakeFiles/NetworkProcess.dir/link.txt
  sed -i 's|libgstaudio-1.0.a |libgstaudio-1.0.a -lorc-0.4 |g' ./Source/WebKit2/CMakeFiles/NetworkProcess.dir/link.txt
  sed -i 's|libWebCorePlatformGTK.a |libWebCorePlatformGTK.a -L../../lib/ -lWebCoreGTK |g' ./Source/WebKit2/CMakeFiles/NetworkProcess.dir/link.txt

  sed -i 's|libharfbuzz.a |libharfbuzz.a -lgraphite2 |g' ./Source/WebKit2/CMakeFiles/PluginProcess.dir/link.txt
  sed -i 's|libgstaudio-1.0.a |libgstaudio-1.0.a -lorc-0.4 |g' ./Source/WebKit2/CMakeFiles/PluginProcess.dir/link.txt
  sed -i 's|libWebCorePlatformGTK.a |libWebCorePlatformGTK.a -L../../lib/ -lWebCoreGTK |g' ./Source/WebKit2/CMakeFiles/PluginProcess.dir/link.txt

  sed -i 's|libharfbuzz.a |libharfbuzz.a -lgraphite2 |g' ./Source/WebKit2/CMakeFiles/WebKitPluginProcess2.dir/link.txt
  sed -i 's|libgstaudio-1.0.a |libgstaudio-1.0.a -lorc-0.4 |g' ./Source/WebKit2/CMakeFiles/WebKitPluginProcess2.dir/link.txt
  sed -i 's|libWebCorePlatformGTK.a |libWebCorePlatformGTK.a -L../../lib/ -lWebCoreGTK |g' ./Source/WebKit2/CMakeFiles/WebKitPluginProcess2.dir/link.txt

  sed -i 's|libharfbuzz.a |libharfbuzz.a -lgraphite2 |g' ./Source/WebKit2/CMakeFiles/WebProcess.dir/link.txt
  sed -i 's|libgstaudio-1.0.a |libgstaudio-1.0.a -lorc-0.4 |g' ./Source/WebKit2/CMakeFiles/WebProcess.dir/link.txt
  sed -i 's|libWebCorePlatformGTK.a |libWebCorePlatformGTK.a -L../../lib/ -lWebCoreGTK |g' ./Source/WebKit2/CMakeFiles/WebProcess.dir/link.txt

  sed -i '165,168 d' ./Source/WebKit2/cmake_install.cmake
  sed -i '150,153 d' ./Source/WebKit2/cmake_install.cmake

  make
}

package() {
  cd build
  make DESTDIR="$pkgdir" install

  cp -f ./lib/*.a $pkgdir/usr/lib/

  install -m755 -d "$pkgdir/usr/share/licenses/webkit2gtk"
  cd "$srcdir/webkitgtk-$pkgver/Source"
  for f in $(find -name 'COPYING*' -or -name 'LICENSE*'); do
    echo $f >> "$pkgdir/usr/share/licenses/webkit2gtk/LICENSE"
    cat $f >> "$pkgdir/usr/share/licenses/webkit2gtk/LICENSE"
    echo "" >> "$pkgdir/usr/share/licenses/webkit2gtk/LICENSE"
  done
}
