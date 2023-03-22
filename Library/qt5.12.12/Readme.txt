使用静态编译的xkbcommon-x11库
export PKG_CONFIG_PATH="/usr/local/lib32/pkgconfig/:${PKG_CONFIG_PATH}"


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
qwebphandler.cpp:294:9: 错误：‘WebPMemoryWriterClear’ was not declared in this scope; did you mean ‘WebPMemoryWriterInit’?
  294 |         WebPMemoryWriterClear(&writer);