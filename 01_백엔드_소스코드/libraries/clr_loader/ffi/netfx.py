# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: netfx.pyc (Python 3.11)

cdef = [
    '\ntypedef void* pyclr_domain;\ntypedef int (*entry_point)(void* buffer, int size);\n\nvoid pyclr_initialize();\nvoid* pyclr_create_appdomain(const char* name, const char* config_file);\nentry_point pyclr_get_function(pyclr_domain domain, const char* assembly_path, const char* class_name, const char* function);\nvoid pyclr_close_appdomain(pyclr_domain domain);\nvoid pyclr_finalize();\n    ']
