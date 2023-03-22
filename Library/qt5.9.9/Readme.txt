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
no declaration matches ‘Display* QEglFSKmsEglDevice::nativeDisplay() const’
https://code.qt.io/cgit/qt/qtbase.git/commit/?h=dev&id=9a640e7bc67b0a1ff5c61c63703b669e6f24521e

diff --git a/src/plugins/platforms/eglfs/deviceintegration/eglfs_kms_egldevice/qeglfskmsegldevice.cpp b/src/plugins/platforms/eglfs/deviceintegration/eglfs_kms_egldevice/qeglfskmsegldevice.cpp
index 0a66a897a1..cca413ff2d 100644
--- a/src/plugins/platforms/eglfs/deviceintegration/eglfs_kms_egldevice/qeglfskmsegldevice.cpp
+++ b/src/plugins/platforms/eglfs/deviceintegration/eglfs_kms_egldevice/qeglfskmsegldevice.cpp
@@ -77,9 +77,9 @@ void QEglFSKmsEglDevice::close()
     setFd(-1);
 }
 
-EGLNativeDisplayType QEglFSKmsEglDevice::nativeDisplay() const
+void *QEglFSKmsEglDevice::nativeDisplay() const
 {
-    return reinterpret_cast<EGLNativeDisplayType>(m_devInt->eglDevice());
+    return m_devInt->eglDevice();
 }
 
 QPlatformScreen *QEglFSKmsEglDevice::createScreen(const QKmsOutput &output)

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

编译qtwebengine报错
File "/usr/local/00.x32/00.pkg/Library/qt5.9.9/qt-everywhere-opensource-src-5.9.9/qtwebengine/src/3rdparty/chromium/tools/gn/bootstrap/bootstrap.py", line 72
    print 'Building gn manually in a temporary directory for bootstrapping...'
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

需要系统中有python2，修改环境变量PATH，其中/usr/local/python2/bin需要有python
export PATH=/usr/local/python2/bin:$PATH

错误：
qt-everywhere-opensource-src-5.9.9/qtwebengine/src/3rdparty/chromium/base/sys_info_posix.cc:90:10: 
错误：narrowing conversion of ‘2508478710’ from ‘unsigned int’ to ‘int’
需要将sys_info_posix.cc的88行，修改为
  switch ((unsigned int)stats.f_type) {

