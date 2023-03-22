#! /bin/bash

QT_INSTALL_PATH="-prefix /usr/local/qt/qt4.8.7"     # Qt安装路径(自己对应修改)
QT_COMPLIER+="-platform linux-g++"  # 编译器

CONFIG_PARAM+="-static "               # 静态编译
CONFIG_PARAM+="-release "             # 编译release
#CONFIG_PARAM+="-recheck-all "
CONFIG_PARAM+="-nomake examples "    # 不编译examples
CONFIG_PARAM+="-nomake demos "        # 不编译demos
CONFIG_PARAM+="-nomake docs "        # 不编译docs
CONFIG_PARAM+="-xmlpatterns -qt3support -declarative -xshape -xsync -xfixes -xrandr -xrender -xcursor -xkb "

CONFIG_PARAM+="-no-glib "    # 不编译glib支持

#如果未配置-fontconfig，则需要自己去配置字体目录，中文字体时就是个大麻烦
CONFIG_PARAM+="-fontconfig "

#  -sql-mysql 
CONFIG_PARAM+=" -qt-zlib -qt-libpng -qt-libjpeg -qt-libtiff -qt-libmng -openssl-linked " # -qpa xcb 
CONFIG_PARAM+="-I/usr/include/openssl-1.1/ -L/usr/lib/openssl-1.1/ -L/usr/lib/ "

# 选择Qt版本(开源, 商业), 并自动确认许可认证
CONFIG_PARAM+="-opensource "         # 编译开源版本, -commercial商业版本
CONFIG_PARAM+="-confirm-license "      # 自动确认许可认证

echo "./configure $CONFIG_PARAM $QT_COMPLIER $QT_INSTALL_PATH"
./configure $CONFIG_PARAM $QT_COMPLIER $QT_INSTALL_PATH
