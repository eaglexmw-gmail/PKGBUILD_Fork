# $Id$
# Maintainer: Jan de Groot <jgc@archlinux.org>
# Maintainer: Pierre Schmitz <pierre@archlinux.de>

pkgname=apr-util
pkgver=1.5.4
pkgrel=1
pkgdesc="The Apache Portable Runtime"
arch=('i686' 'x86_64')
url="http://apr.apache.org/"
#depends=('apr' 'expat')
depends=('expat')
options=('staticlibs')
makedepends=('gdbm' 'libldap' 'unixodbc' 'openssl' 'nss' 'sqlite' 'libmariadbclient' 'db' 'postgresql-libs')
optdepends=(
  'gdbm: enable gdbm support'
  'libldap: enable ldap support'
  'unixodbc: enable odbc support'
  'libmariadbclient: enable mysql/mariadb support'
  'postgresql-libs: enable postgres support'
  'db: enable berkley db support'
  'sqlite: enable sqlite support'
  'nss: enable nss crypto support'
  'openssl: enable openssl crypto support'
)
license=('APACHE')
source=(http://www.apache.org/dist/apr/apr-util-${pkgver}.tar.bz2)
md5sums=('2202b18f269ad606d70e1864857ed93c'
         )

#validpgpkeys=('5B5181C2C0AB13E59DA3F7A3EC582EB639FF092C') # Jeff Trawick


if [ "$CARCH" = "x86_64" ]; then
  dstdir=subversion64
elif [ "$CARCH" = "i686" ]; then
  dstdir=subversion
fi


build() {
  cd "${srcdir}/apr-util-${pkgver}"

  # export PKG_CONFIG_PATH=${PKG_CONFIG_PATH}:/usr/local/${dstdir}/lib/pkgconfig/

  export CFLAGS=-fPIC
  export CXXFLAGS=-fPIC
  export CPPFLAGS=-fPIC

  ./configure --prefix=/usr --with-apr=/usr/local --with-ldap --with-crypto \
    --with-gdbm=/usr --with-sqlite3=/usr --with-nss=/usr --with-odbc=/usr \
    --with-berkeley-db=/usr --with-pgsql=/usr --with-mysql=/usr --with-oracle=/usr \
    --with-openssl=/usr --disable-util-dso --enable-static

  make
}

check() {
  cd "${srcdir}/apr-util-${pkgver}"
  #make -j1 check
}

package() {
  cd "${srcdir}/apr-util-${pkgver}"

  export CFLAGS=-fPIC
  export CXXFLAGS=-fPIC
  export CPPFLAGS=-fPIC

  make DESTDIR="${pkgdir}" install
}
