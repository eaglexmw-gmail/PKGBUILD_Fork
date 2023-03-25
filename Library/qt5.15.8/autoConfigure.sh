#! /bin/bash

QT_INSTALL_PATH="-prefix /usr/local/qt/qt5.15.8"     # Qt安装路径(自己对应修改)
QT_COMPLIER+="-platform linux-g++"  # 编译器

CONFIG_PARAM+="-static "               # 静态编译
CONFIG_PARAM+="-release "             # 编译release
CONFIG_PARAM+="-recheck-all "
CONFIG_PARAM+="-nomake examples "    # 不编译examples
CONFIG_PARAM+="-nomake tests "        # 不编译tests

#CONFIG_PARAM+="-qt-freetype -qt-harfbuzz " # 使用自带的harfbuzz/freetype，这个选项会与-fontconfig冲突，
#其实-fontconfig只与qt-freetype冲突，但freetype会自动包含harfbuzz所以都是不需要内嵌的
#而如果未配置-fontconfig，则需要自己去配置字体目录，中文字体时就是个大麻烦
CONFIG_PARAM+="-fontconfig -system-harfbuzz -system-freetype -no-glib -L/usr/lib -I /usr/include "
CONFIG_PARAM+="-skip qtwebengine -no-feature-testlib " # 禁止testlib特性，以规避qtdeclarative中Qt5QuickTest链接失败问题 -skip qtdeclarative"

#  -sql-mysql 
CONFIG_PARAM+=" -no-pch -c++std c++14 -xcb -xcb-xlib -xkbcommon -qt-zlib -qt-libpng -qt-libjpeg -qt-tiff -qt-webp -openssl -qpa xcb "

# 选择Qt版本(开源, 商业), 并自动确认许可认证
CONFIG_PARAM+="-opensource "         # 编译开源版本, -commercial商业版本
CONFIG_PARAM+="-confirm-license "      # 自动确认许可认证

echo "./configure $CONFIG_PARAM $QT_COMPLIER $QT_INSTALL_PATH"
./configure $CONFIG_PARAM $QT_COMPLIER $QT_INSTALL_PATH
