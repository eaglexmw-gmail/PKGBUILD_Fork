#include <stdio.h>
#include <unistd.h>
#include <string.h>
// #include <glib.h>

int is_absolute_path(const char* path)
{
    if ( (path == NULL) || (path[0] != '/') )
    {
        return 0;
    }
    return 1;
}

int __try_other_exe_path(char* strExePath, const char* argv0, int max_size)
{
    char* strBuf;
    const char* strhead;
    const char* strEnv;
    int len_argv0 = 0;
    int curr_len = 0;
    int skip_somthing = 0;
    // check argv0
    if (is_absolute_path(argv0))
    {
        strncpy(strExePath, argv0, max_size - 1);
        strExePath[max_size - 1] = '\0';
        return 0;
    }
    // check PATH environment
    strEnv = getenv("PATH");

    // better than nothing
    if (strEnv == NULL)
    {
        strncpy(strExePath, argv0, max_size - 1);
        strExePath[max_size - 1] = '\0';
        return 0;        
    }
    printf("PATH: %s\n", strEnv);
    
    len_argv0 = strlen(argv0);
    if (len_argv0 >= max_size)
    {
        strncpy(strExePath, argv0, max_size - 1);
        strExePath[max_size - 1] = '\0';
        return 0;
    }

    // find one valid path
    for(strhead = strEnv; strEnv[0] != '\0'; strEnv++)
    {
        if (strEnv[0] == ':')
        {
            curr_len = strEnv - strhead;
            /* nothing */
            if (strhead >= strEnv)
            {
                continue;
            }
            // we can't process this
            if (curr_len > (max_size - len_argv0))
            {
                skip_somthing = 1;
                continue;
            }
            strncpy(strExePath, strhead, curr_len);
            strExePath[curr_len] = '\0';
            // skip issue: strExePath may be a invalid absolute path, for example: aa/bb
            
            strBuf = g_build_path("/", strExePath, argv0, NULL);
            printf("start to check: %s\n", strBuf);
            // find first valid item, return it
            if (access(strBuf, R_OK) == 0)
            {
                strncpy(strExePath, strBuf, max_size - 1);
                strExePath[max_size - 1] = '\0';
                g_free(strBuf);
                return 0;
            }
            g_free(strBuf);
            
            //not found, next item
            strhead = strEnv + 1;
        }
    }
    
    // last item
    if (strhead >= strEnv)
    {
        if (skip_somthing)
        {
            return -2;
        }
        return -1;
    }
    
    if (strEnv - strhead > max_size - len_argv0)
        return -2;
    strncpy(strExePath, strhead, strEnv - strhead);
    
    strBuf = g_build_path("/", strExePath, argv0, NULL);
    printf("start to check: %s\n", strBuf);
    // find valid item, return it
    if (access(strBuf, R_OK) == 0)
    {
        strncpy(strExePath, strBuf, max_size - 1);
        strExePath[max_size - 1] = '\0';
        g_free(strBuf);
        return 0;
    }
    g_free(strBuf);

    // getcwd
    if (getcwd(strExePath, max_size - 1))
    {
        strBuf = g_build_path("/", strExePath, argv0, NULL);
        printf("start to check: %s\n", strBuf);
        if (access(strBuf, R_OK) == 0)
        {
            strncpy(strExePath, strBuf, max_size - 1);
            strExePath[max_size - 1] = '\0';
            g_free(strBuf);
            return 0;
        }
        g_free(strBuf);
    }

    return -1;
}

int __linux_get_exe_path(char* strExePath, const char* argv0, int max_size)
{
    int result;
    const char* strEnv;
    strExePath[0] = '\0';
    result = readlink("/proc/self/exe", strExePath, max_size - 1);
    if ( result != -1 )
    {
        strExePath[result] = '\0'; // readlink() doesn't NUL-terminate the buffer

        // if the /proc/self/exe symlink has been dropped by the kernel for
        // some reason, then readlink() could also return success but
        // "(deleted)" as link destination...
        if ( strcmp(strExePath, "(deleted)") == 0 )
            strExePath[0] = '\0';
    }

    if ( strExePath[0] == '\0' )
    {
        // UPX-specific hack: when using UPX on linux, the kernel will drop the
        // /proc/self/exe link; in this case we try to look for a special
        // environment variable called "   " which is created by UPX to save
        // /proc/self/exe contents. See
        //      http://sf.net/tracker/?func=detail&atid=309863&aid=1565357&group_id=9863
        // for more information about this issue.
        strEnv = getenv("   ");
        if ((strEnv != NULL) && (strEnv[0] != '\0'))
        {
            strncpy(strExePath, strEnv, max_size - 1);
            strExePath[max_size - 1] = '\0';
            return 0;
        }
    }

    if ( strExePath[0] != '\0' )
        return 0;

    return __try_other_exe_path(strExePath, argv0, max_size);
}

//
int main(int argc, char **argv)
{
    int ret;
    char strExePath[4096] = {0};
    
    if ((ret = __try_other_exe_path(strExePath, argv[0], 4096)) == 0)
    {
        printf("get valid execute path: %s\n", strExePath);
    }
    else
    {
        printf("not found : %d\n", ret);    
    }
    
    return 0;
}
