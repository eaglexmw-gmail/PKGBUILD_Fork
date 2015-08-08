/*
Copyright (C) 2009 COR Entertainment, LLC.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
*/

/*
 * qal_unix.c
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <stddef.h>
#include <stdio.h>
#if defined HAVE_DLFCN_H
#include <dlfcn.h>
#endif

#if defined HAVE_AL_H
#include <al.h>
#include <alc.h>
#elif defined HAVE_AL_AL_H
#include <AL/al.h>
#include <AL/alc.h>
#elif defined HAVE_OPENAL_AL_H
#include <OpenAL/al.h>
#include <OpenAL/alc.h>
#else
#error OpenAL header includes not defined.
#endif

#include "client/client.h"
#include "client/qal.h"

/*
 * OpenAL Library
 *  OpenAL 1.1 required.
 */
#if defined OPENAL_DRIVER
const char libopenal_name[] = OPENAL_DRIVER;
#else
const char libopenal_name[] = "libopenal.so.1";
#endif
void *dynlib;
qboolean dlsym_error;

/*
 ==
 get_dlsym()

 get symbol from shared library
 ==
 */
/*
static void get_dlsym( const char* symbol_name, void** symbol_addr )
{
	char *dlerror_message;

	dlerror_message = dlerror(); // clear any error
	*symbol_addr = dlsym( dynlib, symbol_name );
	dlerror_message = dlerror();
	if( dlerror_message != NULL )
	{
		printf( "%s\n", dlerror_message );
		dlsym_error = true;
	}
}
*/

#define GET_DLSYM(sym_name, sym_addr) \
    *(sym_addr) = & (sym_name)

/*
 ==
 QAL_Init()
 QAL_Shutdown()

 Dynamically link/unlink OpenAL shared library
 ==
 */
qboolean QAL_Init( void )
{
        /*
        dynlib = dlopen( libopenal_name, RTLD_LAZY | RTLD_GLOBAL );
	if( dynlib == NULL )
	{
		Com_Printf("dlopen() on %s failed\n", libopenal_name );
		return false;
	}
        */

	dlsym_error = false;
	GET_DLSYM( alEnable, (void**) &pqalEnable );
	GET_DLSYM( alDisable, (void**) &pqalDisable );
	GET_DLSYM( alIsEnabled, (void**) &pqalIsEnabled );
	GET_DLSYM( alGetBooleanv, (void**) &pqalGetBooleanv );
	GET_DLSYM( alGetIntegerv, (void**) &pqalGetIntegerv );
	GET_DLSYM( alGetString, (void**) &pqalGetString );
	GET_DLSYM( alGetFloatv, (void**) &pqalGetFloatv );
	GET_DLSYM( alGetDoublev, (void**) &pqalGetDoublev );
	GET_DLSYM( alGetBoolean, (void**) &pqalGetBoolean );
	GET_DLSYM( alGetInteger, (void**) &pqalGetInteger );
	GET_DLSYM( alGetFloat, (void**) &pqalGetFloat );
	GET_DLSYM( alGetDouble, (void**) &pqalGetDouble );
	GET_DLSYM( alGetError, (void**) &pqalGetError );
	GET_DLSYM( alIsExtensionPresent, (void**) &pqalIsExtensionPresent );
	GET_DLSYM( alGetProcAddress, (void**) &pqalGetProcAddress );
	GET_DLSYM( alGetEnumValue, (void**) &pqalGetEnumValue );
	GET_DLSYM( alListenerf, (void**) &pqalListenerf );
	GET_DLSYM( alListener3f, (void**) &pqalListener3f );
	GET_DLSYM( alListenerfv, (void**) &pqalListenerfv );
	GET_DLSYM( alListeneri, (void**) &pqalListeneri );
	GET_DLSYM( alListener3i, (void**) &pqalListener3i );
	GET_DLSYM( alListeneriv, (void**) &pqalListeneriv );
	GET_DLSYM( alGetListenerf, (void**) &pqalGetListenerf );
	GET_DLSYM( alGetListener3f, (void**) &pqalGetListener3f );
	GET_DLSYM( alGetListenerfv, (void**) &pqalGetListenerfv );
	GET_DLSYM( alGetListeneri, (void**) &pqalGetListeneri );
	GET_DLSYM( alGetListener3i, (void**) &pqalGetListener3i );
	GET_DLSYM( alGetListeneriv, (void**) &pqalGetListeneriv );
	GET_DLSYM( alGenSources, (void**) &pqalGenSources );
	GET_DLSYM( alDeleteSources, (void**) &pqalDeleteSources );
	GET_DLSYM( alIsSource, (void**) &pqalIsSource );
	GET_DLSYM( alSourcef, (void**) &pqalSourcef );
	GET_DLSYM( alSource3f, (void**) &pqalSource3f );
	GET_DLSYM( alSourcefv, (void**) &pqalSourcefv );
	GET_DLSYM( alSourcei, (void**) &pqalSourcei );
	GET_DLSYM( alSource3i, (void**) &pqalSource3i );
	GET_DLSYM( alSourceiv, (void**) &pqalSourceiv );
	GET_DLSYM( alGetSourcef, (void**) &pqalGetSourcef );
	GET_DLSYM( alGetSource3f, (void**) &pqalGetSource3f );
	GET_DLSYM( alGetSourcefv, (void**) &pqalGetSourcefv );
	GET_DLSYM( alGetSourcei, (void**) &pqalGetSourcei );
	GET_DLSYM( alGetSource3i, (void**) &pqalGetSource3i );
	GET_DLSYM( alGetSourceiv, (void**) &pqalGetSourceiv );
	GET_DLSYM( alSourcePlayv, (void**) &pqalSourcePlayv );
	GET_DLSYM( alSourceStopv, (void**) &pqalSourceStopv );
	GET_DLSYM( alSourceRewindv, (void**) &pqalSourceRewindv );
	GET_DLSYM( alSourcePausev, (void**) &pqalSourcePausev );
	GET_DLSYM( alSourcePlay, (void**) &pqalSourcePlay );
	GET_DLSYM( alSourceStop, (void**) &pqalSourceStop );
	GET_DLSYM( alSourceRewind, (void**) &pqalSourceRewind );
	GET_DLSYM( alSourcePause, (void**) &pqalSourcePause );
	GET_DLSYM( alSourceQueueBuffers, (void**) &pqalSourceQueueBuffers );
	GET_DLSYM( alSourceUnqueueBuffers, (void**) &pqalSourceUnqueueBuffers );
	GET_DLSYM( alGenBuffers, (void**) &pqalGenBuffers );
	GET_DLSYM( alDeleteBuffers, (void**) &pqalDeleteBuffers );
	GET_DLSYM( alIsBuffer, (void**) &pqalIsBuffer );
	GET_DLSYM( alBufferData, (void**) &pqalBufferData );
	GET_DLSYM( alBufferf, (void**) &pqalBufferf );
	GET_DLSYM( alBuffer3f, (void**) &pqalBuffer3f );
	GET_DLSYM( alBufferfv, (void**) &pqalBufferfv );
	GET_DLSYM( alBufferi, (void**) &pqalBufferi );
	GET_DLSYM( alBuffer3i, (void**) &pqalBuffer3i );
	GET_DLSYM( alBufferiv, (void**) &pqalBufferiv );
	GET_DLSYM( alGetBufferf, (void**) &pqalGetBufferf );
	GET_DLSYM( alGetBuffer3f, (void**) &pqalGetBuffer3f );
	GET_DLSYM( alGetBufferfv, (void**) &pqalGetBufferfv );
	GET_DLSYM( alGetBufferi, (void**) &pqalGetBufferi );
	GET_DLSYM( alGetBuffer3i, (void**) &pqalGetBuffer3i );
	GET_DLSYM( alGetBufferiv, (void**) &pqalGetBufferiv );
	GET_DLSYM( alDopplerFactor, (void**) &pqalDopplerFactor );
	GET_DLSYM( alDopplerVelocity, (void**) &pqalDopplerVelocity );
	GET_DLSYM( alSpeedOfSound, (void**) &pqalSpeedOfSound );
	GET_DLSYM( alDistanceModel, (void**) &pqalDistanceModel );
	GET_DLSYM( alcCreateContext, (void**) &pqalcCreateContext );
	GET_DLSYM( alcMakeContextCurrent, (void**) &pqalcMakeContextCurrent );
	GET_DLSYM( alcProcessContext, (void**) &pqalcProcessContext );
	GET_DLSYM( alcSuspendContext, (void**) &pqalcSuspendContext );
	GET_DLSYM( alcDestroyContext, (void**) &pqalcDestroyContext );
	GET_DLSYM( alcGetCurrentContext, (void**) &pqalcGetCurrentContext );
	GET_DLSYM( alcGetContextsDevice, (void**) &pqalcGetContextsDevice );
	GET_DLSYM( alcOpenDevice, (void**) &pqalcOpenDevice );
	GET_DLSYM( alcCloseDevice, (void**) &pqalcCloseDevice );
	GET_DLSYM( alcGetError, (void**) &pqalcGetError );
	GET_DLSYM( alcIsExtensionPresent, (void**) &pqalcIsExtensionPresent );
	GET_DLSYM( alcGetProcAddress, (void**) &pqalcGetProcAddress );
	GET_DLSYM( alcGetEnumValue, (void**) &pqalcGetEnumValue );
	GET_DLSYM( alcGetString, (void**) &pqalcGetString );
	GET_DLSYM( alcGetIntegerv, (void**) &pqalcGetIntegerv );
	GET_DLSYM( alcCaptureOpenDevice, (void**) &pqalcCaptureOpenDevice );
	GET_DLSYM( alcCaptureCloseDevice, (void**) &pqalcCaptureCloseDevice );
	GET_DLSYM( alcCaptureStart, (void**) &pqalcCaptureStart );
	GET_DLSYM( alcCaptureStop, (void**) &pqalcCaptureStop );
	GET_DLSYM( alcCaptureSamples, (void**) &pqalcCaptureSamples );

	return !dlsym_error;
}

void QAL_Shutdown( void )
{
	int result;
        /*
	if( dynlib )
	{
		result = dlclose( dynlib );
		if( result )
		{
			Com_Printf( "dlclose() error\n" );
		}
		dynlib = NULL;
	}
        */

	pqalEnable = NULL;
	pqalDisable = NULL;
	pqalIsEnabled = NULL;
	pqalGetBooleanv = NULL;
	pqalGetIntegerv = NULL;
	pqalGetString = NULL;
	pqalGetFloatv = NULL;
	pqalGetDoublev = NULL;
	pqalGetBoolean = NULL;
	pqalGetInteger = NULL;
	pqalGetFloat = NULL;
	pqalGetDouble = NULL;
	pqalGetError = NULL;
	pqalIsExtensionPresent = NULL;
	pqalGetProcAddress = NULL;
	pqalGetEnumValue = NULL;
	pqalListenerf = NULL;
	pqalListener3f = NULL;
	pqalListenerfv = NULL;
	pqalListeneri = NULL;
	pqalListener3i = NULL;
	pqalListeneriv = NULL;
	pqalGetListenerf = NULL;
	pqalGetListener3f = NULL;
	pqalGetListenerfv = NULL;
	pqalGetListeneri = NULL;
	pqalGetListener3i = NULL;
	pqalGetListeneriv = NULL;
	pqalGenSources = NULL;
	pqalDeleteSources = NULL;
	pqalIsSource = NULL;
	pqalSourcef = NULL;
	pqalSource3f = NULL;
	pqalSourcefv = NULL;
	pqalSourcei = NULL;
	pqalSource3i = NULL;
	pqalSourceiv = NULL;
	pqalGetSourcef = NULL;
	pqalGetSource3f = NULL;
	pqalGetSourcefv = NULL;
	pqalGetSourcei = NULL;
	pqalGetSource3i = NULL;
	pqalGetSourceiv = NULL;
	pqalSourcePlayv = NULL;
	pqalSourceStopv = NULL;
	pqalSourceRewindv = NULL;
	pqalSourcePausev = NULL;
	pqalSourcePlay = NULL;
	pqalSourceStop = NULL;
	pqalSourceRewind = NULL;
	pqalSourcePause = NULL;
	pqalSourceQueueBuffers = NULL;
	pqalSourceUnqueueBuffers = NULL;
	pqalGenBuffers = NULL;
	pqalDeleteBuffers = NULL;
	pqalIsBuffer = NULL;
	pqalBufferData = NULL;
	pqalBufferf = NULL;
	pqalBuffer3f = NULL;
	pqalBufferfv = NULL;
	pqalBufferi = NULL;
	pqalBuffer3i = NULL;
	pqalBufferiv = NULL;
	pqalGetBufferf = NULL;
	pqalGetBuffer3f = NULL;
	pqalGetBufferfv = NULL;
	pqalGetBufferi = NULL;
	pqalGetBuffer3i = NULL;
	pqalGetBufferiv = NULL;
	pqalDopplerFactor = NULL;
	pqalDopplerVelocity = NULL;
	pqalSpeedOfSound = NULL;
	pqalDistanceModel = NULL;
	pqalcCreateContext = NULL;
	pqalcMakeContextCurrent = NULL;
	pqalcProcessContext = NULL;
	pqalcSuspendContext = NULL;
	pqalcDestroyContext = NULL;
	pqalcGetCurrentContext = NULL;
	pqalcGetContextsDevice = NULL;
	pqalcOpenDevice = NULL;
	pqalcCloseDevice = NULL;
	pqalcGetError = NULL;
	pqalcIsExtensionPresent = NULL;
	pqalcGetProcAddress = NULL;
	pqalcGetEnumValue = NULL;
	pqalcGetString = NULL;
	pqalcGetIntegerv = NULL;
	pqalcCaptureOpenDevice = NULL;
	pqalcCaptureCloseDevice = NULL;
	pqalcCaptureStart = NULL;
	pqalcCaptureStop = NULL;
	pqalcCaptureSamples = NULL;

}

/*
 ==
 QAL_Loaded()

 check for OpenAL shared library
 ==
*/
qboolean QAL_Loaded( void )
{
	//return ( dynlib != NULL && !dlsym_error);
        return true;
}
