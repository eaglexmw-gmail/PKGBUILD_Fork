# $Id$
# Maintainer: Andrea Scarpino <andrea@archlinux.org>
# Contributor: Pierre Schmitz <pierre@archlinux.de>

pkgname=qt
pkgver=4.7.1
pkgrel=3
pkgdesc='A cross-platform application and UI framework'
arch=('i686' 'x86_64')
url='http://qt.nokia.com/'
license=('GPL3' 'LGPL')
depends=('libtiff' 'libpng' 'sqlite3' 'ca-certificates' 'glib2' 'dbus'
    'fontconfig' 'libgl' 'libsm' 'libxrandr' 'libxv' 'libxi' 'alsa-lib'
    'xdg-utils' 'hicolor-icon-theme')
optdepends=('postgresql-libs: PostgreSQL driver'
	'libmysqlclient: MySQL driver'
	'unixodbc: ODBC driver'
	'libxinerama: Xinerama support'
	'libxcursor: Xcursor support'
	'libxfixes: Xfixes support')
makedepends=('mesa' 'gtk2')
install="${pkgname}.install"
options=('!libtool' 'staticlibs')
_pkgfqn="qt-everywhere-opensource-src-${pkgver}"
source=("ftp://ftp.qt.nokia.com/qt/source/${_pkgfqn}.tar.gz"
        'assistant.desktop' 'designer.desktop' 'linguist.desktop'
        'qtconfig.desktop'
        'fix-qtbug-15857.patch'
        'add-postgresql9.patch'
        'symbol_visibility.patch'
        'cups.patch')
md5sums=('6f88d96507c84e9fea5bf3a71ebeb6d7'
         'fc211414130ab2764132e7370f8e5caa'
         '85179f5e0437514f8639957e1d8baf62'
         'f11852b97583610f3dbb669ebc3e21bc'
         '6b771c8a81dd90b45e8a79afa0e5bbfd'
         'c359d7b8c3a7fdd99512feaab8c2e26b'
         'ae3bb58e7b63786d420905baf083fcd2'
         'baacfa7c591d290a79acc3bea86c47f2'
         '76cf5ce3d38bd69398e607a93d48ecc7')

build() {
	unset QMAKESPEC
	export QT4DIR=$srcdir/$_pkgfqn
	export PATH=${QT4DIR}/bin:${PATH}
	export LD_LIBRARY_PATH=${QT4DIR}/lib:${LD_LIBRARY_PATH}

	cd $srcdir/$_pkgfqn

    # Already fixed upstream
    patch -Np1 -i ${srcdir}/fix-qtbug-15857.patch
    patch -Np1 -i ${srcdir}/add-postgresql9.patch

    patch -Np1 -i ${srcdir}/symbol_visibility.patch
    patch -Np1 -i ${srcdir}/cups.patch

	sed -i "s|-O2|$CXXFLAGS|" mkspecs/common/g++.conf
	sed -i "/^QMAKE_RPATH/s| -Wl,-rpath,||g" mkspecs/common/g++.conf
	sed -i "/^QMAKE_LFLAGS\s/s|+=|+= $LDFLAGS|g" mkspecs/common/g++.conf

        sed -i '18 a QMAKE_LIBDIR += $$QT_BUILD_TREE/src/3rdparty/webkit/JavaScriptCore/release' tools/assistant/tools/assistant/assistant.pro

	./configure -confirm-license -opensource -static\
		-prefix /usr \
		-docdir /usr/share/doc/qt \
		-plugindir /usr/lib/qt/plugins \
		-importdir /usr/lib/qt/imports \
		-datadir /usr/share/qt \
		-translationdir /usr/share/qt/translations \
		-sysconfdir /etc \
		-examplesdir /usr/share/doc/qt/examples \
		-demosdir /usr/share/doc/qt/demos \
		-largefile \
		-system-sqlite \
		-xmlpatterns \
		-svg \
		-webkit \
		-script \
		-scripttools \
		-system-zlib \
		-system-libtiff \
		-system-libpng \
		-system-libjpeg \
		-nomake demos \
		-nomake examples \
		-nomake docs \
		-no-rpath \
		-openssl-linked \
		-silent \
		-optimized-qmake \
		-dbus \
		-reduce-relocations \
		-no-separate-debug-info \
		-gtkstyle \
		-opengl \
		-no-openvg \
		-glib

#		-no-phonon \
#		-no-phonon-backend \

        sed -i '18 a QMAKE_LIBDIR += $$QT_BUILD_TREE/src/3rdparty/webkit/JavaScriptCore/release' tools/assistant/tools/assistant/assistant.pro

        # enable dynamic load plugin
        sed -i 's|defined(QT_SHARED)|1|g' src/corelib/plugin/qpluginloader.cpp #:#if defined(QT_SHARED)
        sed -i 's|def QT_SHARED| 1|g' src/corelib/plugin/qfactoryloader.cpp    #:#ifdef QT_SHARED

	make
}

package() {
	cd $srcdir/$_pkgfqn
	make INSTALL_ROOT=$pkgdir install

	# install missing icons and desktop files
	for icon in tools/linguist/linguist/images/icons/linguist-*-32.png ; do
		size=$(echo $(basename ${icon}) | cut -d- -f2)
		install -p -D -m644 ${icon} ${pkgdir}/usr/share/icons/hicolor/${size}x${size}/apps/linguist.png
	done
	install -p -D -m644 src/gui/dialogs/images/qtlogo-64.png ${pkgdir}/usr/share/icons/hicolor/64x64/apps/qtlogo.png
	install -p -D -m644 tools/assistant/tools/assistant/images/assistant.png ${pkgdir}/usr/share/icons/hicolor/32x32/apps/assistant.png
	install -p -D -m644 tools/designer/src/designer/images/designer.png ${pkgdir}/usr/share/icons/hicolor/128x128/apps/designer.png
	install -d ${pkgdir}/usr/share/applications
	install -m644 ${srcdir}/{linguist,designer,assistant,qtconfig}.desktop ${pkgdir}/usr/share/applications/

	# install license addition
	install -D -m644 LGPL_EXCEPTION.txt ${pkgdir}/usr/share/licenses/qt/LGPL_EXCEPTION.txt

	# Fix wrong path in pkgconfig files
	find ${pkgdir}/usr/lib/pkgconfig -type f -name '*.pc' \
		-exec perl -pi -e "s, -L${srcdir}/?\S+,,g" {} \;
	# Fix wrong path in prl files
	find ${pkgdir}/usr/lib -type f -name '*.prl' \
		-exec sed -i -e '/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/' {} \;

        cp -f src/3rdparty/webkit/JavaScriptCore/release/* ${pkgdir}/usr/lib/

    #remove some execute file
    rm -f ${pkgdir}/usr/bin/{assistant,designer,linguist,xmlpatterns,xmlpatternsvalidator,pixeltool,qcollectiongenerator,qdbus,qdbuscpp2xml,qdbusviewer,qdbusxml2cpp,qdoc3,qhelpconverter,qhelpgenerator,qmlplugindump,qmlviewer,qt3to4,qtconfig,qttracereplay,uic3}

}
