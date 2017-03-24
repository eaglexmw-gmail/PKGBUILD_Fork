#ifndef __DEF_STATIC_LIB_METHOD_H__
#define __DEF_STATIC_LIB_METHOD_H__

#undef DECLARE_DLL_WRAPPER
#undef XDECLARE_DLL_WRAPPER
#undef RESOLVE_METHOD
#undef RESOLVE_METHOD_FP
#undef RESOLVE_METHOD_OPTIONAL
#undef RESOLVE_METHOD_OPTIONAL_FP
#undef RESOLVE_METHOD_RENAME
#undef RESOLVE_METHOD_RENAME_FP

#define DECLARE_DLL_WRAPPER(classname, dllname) \
XDECLARE_DLL_WRAPPER(classname,dllname)

#define XDECLARE_DLL_WRAPPER(classname, dllname) \
public: \
  classname () : DllDynamic( dllname ) {} \
  virtual bool Load() { if (m_dll) return true; m_dll = (LibraryLoader*)1; return ResolveExports(); }    \
  virtual void Unload()  { m_dll = 0; }

#define RESOLVE_METHOD(method) \
  m_##method##_ptr = (void*) & :: method; 

#define RESOLVE_METHOD_FP(method) \
  method##_ptr = (void*) & :: method ;

#define RESOLVE_METHOD_OPTIONAL(method) \
  m_##method##_ptr = (void*) & :: method;

#define RESOLVE_METHOD_OPTIONAL_FP(method) \
  method##_ptr = (void*) & :: method ;

#define RESOLVE_METHOD_RENAME(dllmethod, method) \
  m_##method##_ptr = (void*) & :: dllmethod ;

#define RESOLVE_METHOD_RENAME_FP(dllmethod, method) \
  method##_ptr = (void*) & :: dllmethod ;

#undef __DEF_SHARED_SO_METHOD_H__

#endif
