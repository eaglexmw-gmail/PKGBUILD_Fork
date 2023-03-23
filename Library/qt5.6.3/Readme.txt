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
qxcbconnection_xi2.cpp:701:87: 错误：operator '<' has no left operand
  701 | #elif (LIBXI_MAJOR == 1) && ((LIBXI_MINOR < 7) || ((LIBXI_MINOR == 7) && (LIBXI_PATCH < 4)))

第701行前插入：
#elif (LIBXI_MAJOR == 1) && ((LIBXI_MINOR >= 8))
            XIAllowTouchEvents(static_cast<Display *>(m_xlib_display), xiDeviceEvent->deviceid,
                               xiDeviceEvent->detail, xiDeviceEvent->event, XIAcceptTouch);

错误：
qjp2handler.cpp:853:41: 错误：‘pow’在此作用域中尚未声明
在文件
./qtimageformats/src/plugins/imageformats/jp2/qjp2handler.cpp
下，添加
#include <math.h>


错误：
socketcanbackend.cpp:667:41: 错误：‘SIOCGSTAMP’ was not declared in this scope; did you mean ‘SIOCGRARP’?
在文件
./qtserialbus/src/plugins/canbus/socketcan/socketcanbackend.cpp
下，添加
#include <linux/sockios.h>

