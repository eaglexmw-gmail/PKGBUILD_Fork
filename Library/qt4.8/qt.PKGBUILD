# $Id$
# Maintainer: Andrea Scarpino <andrea@archlinux.org>
# Contributor: Pierre Schmitz <pierre@archlinux.de>

pkgbase=qt
pkgname=('qt')
pkgver=4.8.0
pkgrel=2
arch=('i686' 'x86_64')
url='http://qt-project.org/'
license=('GPL3' 'LGPL')
makedepends=('libtiff' 'libpng' 'sqlite3' 'ca-certificates' 'glib2' 'dbus'
    'fontconfig' 'libgl' 'libsm' 'libxrandr' 'libxv' 'libxi' 'alsa-lib'
    'xdg-utils' 'hicolor-icon-theme' 'desktop-file-utils' 'mesa'
    'unixodbc' 'gtk2')
options=('!libtool' 'staticlibs')
_pkgfqn="${pkgbase}-everywhere-opensource-src-${pkgver}"
source=("http://get.qt.nokia.com/qt/source/${_pkgfqn}.tar.gz"
        'assistant.desktop' 'designer.desktop' 'linguist.desktop'
        'qtconfig.desktop'
        'symbol_visibility.patch'
        'static_webkit.patch')
md5sums=('e8a5fdbeba2927c948d9f477a6abe904'
         'fc211414130ab2764132e7370f8e5caa'
         '85179f5e0437514f8639957e1d8baf62'
         'f11852b97583610f3dbb669ebc3e21bc'
         '6b771c8a81dd90b45e8a79afa0e5bbfd'
         '858a29fb9dbe9c80af3d975a6a2659b9'
         'bf44ae1e02b84b197f782247cc1ff958')

build() {
  cd "${srcdir}"/${_pkgfqn}

  export QT4DIR="${srcdir}"/${_pkgfqn}
  export LD_LIBRARY_PATH=${QT4DIR}/lib:${LD_LIBRARY_PATH}

  sed -i "s|-O2|${CXXFLAGS}|" mkspecs/common/g++-base.conf
  sed -i "/^QMAKE_LFLAGS_RPATH/s| -Wl,-rpath,||g" mkspecs/common/gcc-base-unix.conf
  sed -i "/^QMAKE_LFLAGS\s/s|+=|+= ${LDFLAGS}|g" mkspecs/common/gcc-base.conf

  #patch -p1 -i ../symbol_visibility.patch

  patch -p1 -i ../static_webkit.patch
  # patch to cxxflags
  sed -i 's|QMAKE_CXXFLAGS += -Werror|QMAKE_CXXFLAGS += -Wundef|g' src/3rdparty/webkit/Source/WebKit.pri
  sed -i 's|typedef struct _GMutex GMutex;|typedef union _GMutex GMutex;|g' src/3rdparty/webkit/Source/JavaScriptCore/wtf/gobject/GTypedefs.h
  sed -i 's|exists($$PWD/WebKit/qt/tests): SUBDIRS += WebKit/qt/tests| |g' src/3rdparty/webkit/Source/WebKit.pro

  sed -i '20 a QMAKE_LIBDIR += $$QT_BUILD_TREE/src/3rdparty/webkit/Source/JavaScriptCore/release' tools/assistant/tools/assistant/assistant.pro
  sed -i '21 a QMAKE_LIBDIR += $$QT_BUILD_TREE/src/3rdparty/webkit/Source/WebCore/release' tools/assistant/tools/assistant/assistant.pro

  ./configure -confirm-license -opensource -static \
    -prefix /usr/local \
    -docdir /usr/local/share/doc/qt \
    -plugindir /usr/local/lib/qt/plugins \
    -importdir /usr/local/lib/qt/imports \
    -datadir /usr/local/share/qt \
    -translationdir /usr/local/share/qt/translations \
    -sysconfdir /etc \
    -examplesdir /usr/local/share/doc/qt/examples \
    -demosdir /usr/local/share/doc/qt/demos \
    -plugin-sql-{sqlite,odbc} \
    -system-sqlite \
    -graphicssystem raster \
    -openssl-linked \
    -nomake demos \
    -nomake examples \
    -nomake docs \
    -silent \
    -no-rpath \
    -optimized-qmake \
    -reduce-relocations \
    -dbus-linked \
    -no-openvg -webkit

#    -no-phonon \
#    -no-phonon-backend \
#    -no-webkit \

  # enable dynamic load plugin
  sed -i 's|defined(QT_SHARED)|1|g' src/corelib/plugin/qpluginloader.cpp
  sed -i 's|def QT_SHARED| 1|g'     src/corelib/plugin/qfactoryloader.cpp

  #sed -i 's| -lQtWebKit | -lQtWebKit -lwebcore -lQtWebKit |g' tools/assistant/tools/assistant/Makefile
  sed -i 's|-lwebcore | |g' tools/assistant/tools/assistant/Makefile
  sed -i 's|-ljscore | |g' tools/assistant/tools/assistant/Makefile

  cd src
  make
  cd ..
  ../../pack_all_a.sh libQtWebKit.a
  rm ./lib/libQtWebKit.a
  mv ./libQtWebKit.a ./lib/
  sed -i 's|-lwebcore | |g' ./lib/libQtWebKit.prl
  sed -i 's|-ljscore | |g'  ./lib/libQtWebKit.prl
  sed -i 's|-lwebcore | |g' ./lib/pkgconfig/QtWebKit.pc
  sed -i 's|-ljscore | |g'  ./lib/pkgconfig/QtWebKit.pc
  sed -i 's|-lwebcore | |g' ./lib/libQtWebKit.la
  sed -i 's|-ljscore | |g'  ./lib/libQtWebKit.la

  make
}

package() {
    pkgdesc='A cross-platform application and UI framework'
    depends=('libtiff' 'libpng' 'sqlite3' 'ca-certificates' 'glib2' 'dbus'
      'fontconfig' 'libgl' 'libsm' 'libxrandr' 'libxv' 'libxi' 'alsa-lib'
      'xdg-utils' 'hicolor-icon-theme' 'desktop-file-utils')
    optdepends=('postgresql-libs: PostgreSQL driver'
                'libmysqlclient: MySQL driver'
                'unixodbc: ODBC driver'
                'libxinerama: Xinerama support'
                'libxcursor: Xcursor support'
                'libxfixes: Xfixes support')
    install='qt.install'

    cd "${srcdir}"/${_pkgfqn}
    make INSTALL_ROOT="${pkgdir}" install

    # install missing icons and desktop files
    for icon in tools/linguist/linguist/images/icons/linguist-*-32.png ; do
      size=$(echo $(basename ${icon}) | cut -d- -f2)
      install -p -D -m644 ${icon} \
        "${pkgdir}/usr/local/share/icons/hicolor/${size}x${size}/apps/linguist.png"
    done
    install -p -D -m644 src/gui/dialogs/images/qtlogo-64.png \
      "${pkgdir}/usr/local/share/icons/hicolor/64x64/apps/qtlogo.png"
    install -p -D -m644 tools/assistant/tools/assistant/images/assistant.png \
      "${pkgdir}/usr/local/share/icons/hicolor/32x32/apps/assistant.png"
    install -p -D -m644 tools/designer/src/designer/images/designer.png \
      "${pkgdir}/usr/local/share/icons/hicolor/128x128/apps/designer.png"
    install -d "${pkgdir}/usr/local/share/applications"
    install -m644 "${srcdir}"/{linguist,designer,assistant,qtconfig}.desktop \
      "${pkgdir}/usr/local/share/applications/"

    # install license addition
    install -D -m644 LGPL_EXCEPTION.txt \
      ${pkgdir}/usr/local/share/licenses/qt/LGPL_EXCEPTION.txt

    # Fix wrong path in pkgconfig files
    find "${pkgdir}/usr/local/lib/pkgconfig" -type f -name '*.pc' \
      -exec perl -pi -e "s, -L${srcdir}/?\S+,,g" {} \;

    # Fix wrong path in prl files
    find "${pkgdir}/usr/local/lib" -type f -name '*.prl' \
      -exec sed -i -e '/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/' {} \;

    #remove some execute file
    rm -f ${pkgdir}/usr/local/bin/{assistant,designer,linguist,xmlpatterns,xmlpatternsvalidator,pixeltool,qcollectiongenerator,qdbus,qdbuscpp2xml,qdbusviewer,qdbusxml2cpp,qdoc3,qhelpconverter,qhelpgenerator,qmlplugindump,qmlviewer,qt3to4,qtconfig,qttracereplay}
}
