如果没有编译进xcb的后端，需要安装xcb-util-renderutil xcb-util-image
原因在于Qt5.15后，删除了自带的qtxcb
https://codereview.qt-project.org/c/qt/qtbase/+/272993
https://codereview.qt-project.org/c/qt/qtdoc/+/300877/3/doc/src/platforms/linux.qdoc
使用静态编译的xkbcommon-x11库
export PKG_CONFIG_PATH="/usr/local/lib32/pkgconfig/:${PKG_CONFIG_PATH}"

补丁来自于BLFS
patch -Np1 -i ../qt-everywhere-opensource-src-5.15.8-kf5-1.patch
打完补丁后，拷贝qtsan_impl.h至qtbase/include/QtCore/目录下
如果有老版本的harfbuzz头文件，需要先改名。
同时编译动态库版本时，需要有python


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
qwebphandler.cpp: 在成员函数‘virtual bool QWebpHandler::write(const QImage&)’中:
qwebphandler.cpp:294:9: 错误：‘WebPMemoryWriterClear’ was not declared in this scope; did you mean ‘WebPMemoryWriterInit’?
  294 |         WebPMemoryWriterClear(&writer);
      |         ^~~~~~~~~~~~~~~~~~~~~
      |         WebPMemoryWriterInit
qwebphandler.cpp:343:5: 错误：‘WebPMemoryWriterClear’ was not declared in this scope; did you mean ‘WebPMemoryWriterInit’?
  343 |     WebPMemoryWriterClear(&writer);
      |     ^~~~~~~~~~~~~~~~~~~~~
      |     WebPMemoryWriterInit
在qwebphandler.cpp文件头插入一行：

extern "C" void WebPMemoryWriterClear(WebPMemoryWriter* writer);

编译qtdeclarative时报错。

