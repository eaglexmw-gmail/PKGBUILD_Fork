# $Id$
# Maintainer: Jaroslav Lichtblau <dragonlord@aur.archlinux.org>
# Contributor: Jakub Schmidtke <sjakub-at-gmail.com>

pkgname=qsvn
pkgver=0.8.3
pkgrel=2
pkgdesc="Qt4 GUI for Subversion."
arch=('i686' 'x86_64')
url="http://www.anrichter.net/projects/qsvn/"
license=('GPL')
#depends=('qt' 'subversion' 'db>=4.7')
makedepends=('cmake')
#options=('!makeflags')
source=(http://www.anrichter.net/projects/qsvn/chrome/site/$pkgname-$pkgver-src.tar.gz
actionaddlocal.png
actionadd.png
actioncheckout.png
actioncommit.png
actiondeletelocal.png
actiondelete.png
actionupdate.png
actionrevert.png
)
md5sums=('cfdc9dab7c5f1cbf20b249901e10c04e'
'54aa66551bac3d0d4372d381062c78dc'
'2bcd8e841f9c43614210de2d827df268'
'665e5ff7473aad0d5904439a3454eb6d'
'50bc7e6d44038428ff2c29a78b10dd61'
'31b82699db52e2eccb4cfe0b45a10262'
'1aee46c37d175be6f40cdc74a12b3ba1'
'4da66fd7d8e81634bae1373bba43a56f'
'f0b6200fd9c7a80f4775616d77689ebc')
build() {
  cd ${srcdir}/$pkgname-$pkgver/src

  #patch -Np2 -i $srcdir/lib64-fix.patch || return 1
  cp ${srcdir}/*.png ./images/

  sed -i '192,193 d' ./CMakeLists.txt
  sed -i 's|.svg<|.png<|g' forms/qsvn.ui
  sed -i 's|.svg<|.png<|g' qsvn.qrc
#  sed -i 's|.svg<|.png<|g' qsvn.qrc.depends

  cmake -D CMAKE_INSTALL_PREFIX=/usr/local/qsvn -D CMAKE_BUILD_TYPE="Release" ../src || return 1

  sed -i 's|/usr/local/lib/lib| -l|g' svnqt/CMakeFiles/svnqt.dir/link.txt
  sed -i 's|-1.a |-1 |g'           svnqt/CMakeFiles/svnqt.dir/link.txt

  sed -i 's|-DNDEBUG|& -Wl,--no-undefined -Wl,-rpath -Wl,/usr/local/subversion/lib -L/usr/local/subversion/lib |g' svnqt/CMakeFiles/svnqt.dir/link.txt
  sed -i 's|libQtCore.a|& -lglib-2.0 -lz |g' svnqt/CMakeFiles/svnqt.dir/link.txt

  sed -i 's| -lapr-1 | |g' svnqt/CMakeFiles/svnqt.dir/link.txt
  sed -i 's| -laprutil-1 -lldap -llber | |g' svnqt/CMakeFiles/svnqt.dir/link.txt
  sed -i 's|-lnspr4 -lnss3 | |g' svnqt/CMakeFiles/svnqt.dir/link.txt
  sed -i 's| -lsvn_wc-1 |& -laprutil-1 |g' svnqt/CMakeFiles/svnqt.dir/link.txt
  #sed -i 's| -lsvn_diff-1  -lsvn_fs-1  -lsvn_ra-1  -lsvn_repos-1  -lsvn_subr-1  -lsvn_wc-1 | |g' svnqt/CMakeFiles/svnqt.dir/link.txt

  sed -i 's|/usr/local/lib/lib| -l|g' ./CMakeFiles/qsvn.dir/link.txt
  sed -i 's|-1.a |-1 |g'           ./CMakeFiles/qsvn.dir/link.txt
  sed -i 's|t.a |t |g'           ./CMakeFiles/qsvn.dir/link.txt

  sed -i 's|-DNDEBUG|& -Wl,--no-undefined -Wl,-rpath -Wl,/usr/local/subversion/lib -L/usr/local/subversion/lib |g' ./CMakeFiles/qsvn.dir/link.txt

  sed -i 's| -lapr-1 | |g' ./CMakeFiles/qsvn.dir/link.txt
  sed -i 's| -laprutil-1 -lldap -llber | |g' ./CMakeFiles/qsvn.dir/link.txt
  sed -i 's|-lnspr4 -lnss3 | |g' ./CMakeFiles/qsvn.dir/link.txt
  sed -i 's| -lsvn_client-1  -lsvn_diff-1  -lsvn_fs-1  -lsvn_ra-1  -lsvn_repos-1  -lsvn_subr-1  -lsvn_wc-1 | -lsvn_subr-1 |g' ./CMakeFiles/qsvn.dir/link.txt

  sed -i 's| -lpng | -lpng15 |g' ./CMakeFiles/qsvn.dir/link.txt

  make || return 1
}

package() {
  cd ${srcdir}/$pkgname-$pkgver/src

  make DESTDIR=${pkgdir} install

#desktop file
  install -D -m644 ${srcdir}/$pkgname-$pkgver/src/$pkgname.desktop \
    ${pkgdir}/usr/local/qsvn/share/applications/$pkgname.desktop || return 1

}

