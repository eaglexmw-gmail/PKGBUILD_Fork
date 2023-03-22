
使用静态编译的xkbcommon-x11库
export PKG_CONFIG_PATH="/usr/local/lib32/pkgconfig/:${PKG_CONFIG_PATH}"

需要系统中有python2，修改环境变量PATH，其中/usr/local/python2/bin需要有python
export PATH=/usr/local/python2/bin:$PATH

编译时，如果出现numeric_limits错误，找到对应头文件插入如下两行
#include <stdexcept>
#include <limits>

最好的办法，是在qtbase/src/corelib/global/qglobal.h头加上

#ifdef __cplusplus
#include <stdexcept>
#include <limits>
#endif

其中看到EGL on X11 ........................... no是失败的

在make install时会报
qt-everywhere-src-5.12.12/qtwayland/plugins/platforms/libqwayland-xcomposite-egl.a(qwaylandxcompositeeglwindow.o):qwaylandxcompositeeglwindow.cpp:function QtWaylandClient::QWaylandXCompositeEGLWindow::createEglSurface(): 错误: 对‘QXlibEglIntegration::getCompatibleVisualId(_XDisplay*, void*, void*)’未定义的引用

参考https://dev.t-firefly.com/thread-13087-1-1.html资料，实际上类型定义上的错误导致测试失败。
同时https://github.com/KhronosGroup/EGL-Registry/pull/130的说法，需要添加USE_X11宏定义

手动修改EGL/egl.h（位于/usr/include/目录下），在文件头部分就添加
#define USE_X11

错误：
qjp2handler.cpp:853:41: 错误：‘pow’在此作用域中尚未声明
在文件
./qtimageformats/src/plugins/imageformats/jp2/qjp2handler.cpp
下，添加
#include <math.h>

错误：
eglconvenience/qeglplatformcursor.cpp: 在成员函数‘bool QEGLPlatformCursor::setCurrentCursor(QCursor*)’中:
eglconvenience/qeglplatformcursor.cpp:234:15: 错误：expected unqualified-id before numeric constant
  234 |     const Qt::CursorShape newShape = cursor ? cursor->shape() : Qt::ArrowCursor;
      |               ^~~~~~~~~~~
eglconvenience/qeglplatformcursor.cpp:235:27: 错误：‘newShape’在此作用域中尚未声明
  235 |     if (m_cursor.shape == newShape && newShape != Qt::BitmapCursor)
      |                           ^~~~~~~~
eglconvenience/qeglplatformcursor.cpp:242:22: 错误：‘newShape’在此作用域中尚未声明
  242 |     m_cursor.shape = newShape;
      |                      ^~~~~~~~

在qtbase/include/QtCore/目录下添加一个qcursorshape_adp.h
内容如下：
#ifndef QCURSOR_SHAPE_ADAPT_H
#define QCURSOR_SHAPE_ADAPT_H

#include <X11/Xlib.h>
enum {
    XCursorShape = CursorShape
};
#undef CursorShape

#endif
在qeglplatformcursor.cpp文件QT_BEGIN_NAMESPACE之前添加一行
#include <QtCore/qcursorshape_adp.h>

类似有eglconvenience/qeglplatformintegration.cpp，需要在qtbase/src/platformsupport/eglconvenience/qeglplatformintegration_p.h中添加


错误：
        from eglconvenience/qeglplatformcontext.cpp:40:
../../include/QtCore/../../src/corelib/io/qtextstream.h:46:2: 错误：#error qtextstream.h must be included before any header file that defines Status
   46 | #error qtextstream.h must be included before any header file that defines Status
      |  ^~~~~

../../include/QtCore/../../src/corelib/io/qtextstream.h: 在全局域：
../../include/QtCore/../../src/corelib/io/qtextstream.h:72:10: 错误：expected identifier before ‘int’
   72 |     enum Status {
      |          ^~~~~~
../../include/QtCore/../../src/corelib/io/qtextstream.h:72:17: 错误：expected unqualified-id before ‘{’ token
   72 |     enum Status {
      |                 ^
修改qtbase/src/platformsupport/eglconvenience/qeglplatformcontext.cpp，将
#include <QDebug>
这一行移到文件头。











