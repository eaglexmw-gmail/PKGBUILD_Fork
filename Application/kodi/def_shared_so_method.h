#ifndef __DEF_SHARED_SO_METHOD_H__
#define __DEF_SHARED_SO_METHOD_H__

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
  classname () : DllDynamic( dllname ) {}

#define RESOLVE_METHOD(method) \
  if (!m_dll->ResolveExport( #method , & m_##method##_ptr )) \
    return false;

#define RESOLVE_METHOD_FP(method) \
  if (!m_dll->ResolveExport( #method , & method##_ptr )) \
    return false;

#define RESOLVE_METHOD_OPTIONAL(method) \
   m_dll->ResolveExport( #method , & m_##method##_ptr );

#define RESOLVE_METHOD_OPTIONAL_FP(method) \
   method##_ptr = NULL; \
   m_dll->ResolveExport( #method , & method##_ptr );

#define RESOLVE_METHOD_RENAME(dllmethod, method) \
  if (!m_dll->ResolveExport( #dllmethod , & m_##method##_ptr )) \
    return false;

#define RESOLVE_METHOD_RENAME_FP(dllmethod, method) \
  if (!m_dll->ResolveExport( #dllmethod , & method##_ptr )) \
    return false;

#undef __DEF_STATIC_LIB_METHOD_H__

#endif
