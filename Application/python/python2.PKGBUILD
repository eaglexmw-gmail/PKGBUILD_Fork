# $Id$
# Maintainer: Stéphane Gaudreault <stephane@archlinux.org>
# Contributer: Allan McRae <allan@archlinux.org>
# Contributer: Jason Chu <jason@archlinux.org>

pkgname=python2
pkgver=2.7.3
pkgrel=2
_pybasever=2.7
pkgdesc="A high-level scripting language"
arch=('i686' 'x86_64')
license=('PSF')
url="http://www.python.org/"
depends=('bzip2' 'gdbm' 'openssl' 'zlib' 'expat' 'sqlite' 'libffi')
#makedepends=('tk>=8.6.0' 'bluez')
optdepends=('tk: for IDLE')
conflicts=('python<3')
options=('!makeflags')
source=(http://www.python.org/ftp/python/${pkgver%rc?}/Python-${pkgver}.tar.xz)
#sha1sums=('08e78ebeb6d9c799644f6d787ca424291c0fe03e') # 2.7.4
sha1sums=('b2b0ada7ebed4a8204a855193afbdb3aa3308357')

build() {
  cd "${srcdir}/Python-${pkgver}"

  # Temporary workaround for FS#22322
  # See http://bugs.python.org/issue10835 for upstream report
  sed -i "/progname =/s/python/python${_pybasever}/" Python/pythonrun.c

  # Enable built-in SQLite module to load extensions (fix FS#22122)
  sed -i "/SQLITE_OMIT_LOAD_EXTENSION/d" setup.py

  # FS#23997
  sed -i -e "s|^#.* /usr/local/bin/python|#!/usr/local/python2/bin/python2|" Lib/cgi.py

  # Ensure that we are using the system copy of various libraries (expat, zlib and libffi),
  # rather than copies shipped in the tarball
  rm -r Modules/expat
  rm -r Modules/zlib
  rm -r Modules/_ctypes/{darwin,libffi}*

  export OPT="${CFLAGS}"
  ./configure --prefix=/usr/local/python2 --enable-shared --with-threads --enable-ipv6 \
              --enable-unicode=ucs4 --with-system-expat --with-system-ffi \
              --with-dbmliborder=gdbm:ndbm

  make
}

package() {
  cd "${srcdir}/Python-${pkgver}"
  make DESTDIR="${pkgdir}" altinstall maninstall

  ln -sf python${_pybasever}        "${pkgdir}/usr/local/python2/bin/python2"
  ln -sf python${_pybasever}-config "${pkgdir}/usr/local/python2/bin/python2-config"
  ln -sf python${_pybasever}.1      "${pkgdir}/usr/local/python2/share/man/man1/python2.1"

  ln -sf ../../libpython${_pybasever}.so \
    "${pkgdir}/usr/local/python2/lib/python${_pybasever}/config/libpython${_pybasever}.so"

  mv "${pkgdir}/usr/local/python2/bin/smtpd.py" "${pkgdir}/usr/local/python2/lib/python${_pybasever}/"

  # some useful "stuff"
  install -dm755 "${pkgdir}"/usr/local/python2/lib/python${_pybasever}/Tools/{i18n,scripts}
  install -m755 Tools/i18n/{msgfmt,pygettext}.py \
    "${pkgdir}/usr/local/python2/lib/python${_pybasever}/Tools/i18n/"
  install -m755 Tools/scripts/{README,*py} \
    "${pkgdir}/usr/local/python2/lib/python${_pybasever}/Tools/scripts/"

  # fix conflicts with python
  mv "${pkgdir}"/usr/local/python2/bin/idle{,2}
  mv "${pkgdir}"/usr/local/python2/bin/pydoc{,2}
  mv "${pkgdir}"/usr/local/python2/bin/2to3{,-2.7}

  # clean up #!s
  find "${pkgdir}/usr/local/python2/lib/python${_pybasever}/" -name '*.py' | \
    xargs sed -i "s|#[ ]*![ ]*/usr/bin/env python$|#!/usr/bin/env python2|"

  # clean-up reference to build directory
  sed -i "s#${srcdir}/Python-${pkgver}:##" \
    "${pkgdir}/usr/local/python2/lib/python${_pybasever}/config/Makefile"

  # license
  install -Dm644 LICENSE "${pkgdir}/usr/local/python2/share/licenses/${pkgname}/LICENSE"
}
