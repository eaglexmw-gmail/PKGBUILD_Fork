#!/usr/local/python2/bin/python2

static_plugin_def = [
        # core: coreelements --- [capsfilter fakesrc fakesink fdsrc fdsink filesrc funnel identity input-selector output-selector queue queue2 filesink tee typefind multiqueue valve]
        ["coreelements",     "coreelements", "-lgstcoreelements"],
        # core: coreindexers --- []
        ["coreindexers",     "coreindexers", "-lgstcoreindexers"],

        # base: adder
        ["adder",            "adder", "-lgstadder -lorc-0.4 -lm -lrt -lpthread"],
        # base: app ...
        ["app",              "app", "-lgstapp -lgstapp-0.10"],
        # base: audioconvert
        ["audioconvert",     "audioconvert", "-lgstaudioconvert -lorc-0.4 -lm -lrt -lpthread"],
        # base: audiorate ...
        ["audiorate",        "audiorate", "-lgstaudiorate"],
        # base: audiotestsrc ...
        ["audiotestsrc",     "audiotestsrc", "-lgstaudiotestsrc -lm"],
        # base: encoding ...
        ["encoding",         "encoding", "-lgstencodebin"],
        # base: ffmpegcolorspace ...
        ["ffmpegcolorspace", "ffmpegcolorspace", "-lgstffmpegcolorspace"],
        # base: gdp ...
        ["gdp",              "gdp", "-lgstgdp"],
        # base: decodebin ... in playback
        ["decodebin",        "decodebin", "-lgstdecodebin -lgstpbutils-0.10"],
        # base: playback ...
        ["playback",         "playback", "-lgstplaybin -lgstpbutils-0.10 -lgstinterfaces-0.10 -lgstvideo-0.10"],
        # base: uridecodebin ... in playback
        ["uridecodebin",     "uridecodebin", "-lgstdecodebin2 -lgstpbutils-0.10"],
        # base: audioresample
        ["audioresample",    "audioresample", "-lgstaudioresample -lorc-test-0.4 -lorc-0.4 -lm -lrt -lpthread"],
        # base: subparse ... libxml2
        ["subparse",         "subparse", "-lgstsubparse"],
        # base: tcp ...
        ["tcp",              "tcp", "-lgsttcp"],
        # base: typefindfunctions ...
        ["typefindfunctions", "typefindfunctions", "-lgsttypefindfunctions -lgstpbutils-0.10 -lgio-2.0 -lgobject-2.0 -lglib-2.0"],
        # base: videotestsrc ...
        ["videotestsrc",     "videotestsrc", "-lgstvideotestsrc"],
        # base: videorate ...
        ["videorate",        "videorate", "-lgstvideorate"],
        # base: videoscale ...
        ["videoscale",       "videoscale", "-lgstvideoscale"],
        # base: volume
        ["volume",           "volume", "-lgstvolume -lgstinterfaces-0.10 -lgstaudio-0.10 -lorc-0.4 -lm -lrt -lpthread"],

        # good: autodetect ...
        #["autodetect",       "autodetect", "-lgstautodetect"],
        # base plugin: alsa
        #["alsa",             "alsa", "-lgstalsa -lasound -lgstaudio-0.10"],
        
        # base sys: video4linux ...
        #"video4linux" :     ("video4linux", "-lgstvideo4linux -lgstinterfaces-0.10 -lxv"),
        # base sys: ximagesink ...
        ["ximagesink",       "ximagesink", "-lgstximagesink -lX11 -lXext"],
        # base sys: xvimagesink ...
        ["xvimagesink",      "xvimagesink", "-lgstxvimagesink -lgstvideo-0.10 -lX11 -lXext -lXv -lXext -lm"],

        # base plugin: alsa
        ["alsa",             "alsa", "-lgstalsa -lasound -lgstaudio-0.10"],
        # base plugin: cdparanoia ...
        ["cdparanoia",       "cdparanoia", "-lgstcdparanoia -lcdda_paranoia -lcdda_interface"],
        # base plugin: gio ...
        ["gio",              "gio", "-lgstgio -lgio-2.0 -lgobject-2.0 -lglib-2.0"],
        # base plugin: gnomevfs ...
        #"gnomevfs":         ("gnomevfs", "-lgstgnomevfs"),
        # base plugin: libvisual ...
        ["libvisual",        "libvisual", "-lgstlibvisual -lpthread -lm -ldl -lvisual-0.4"],
        # base plugin: ogg ...
        ["ogg",              "ogg", "-lgstogg -lgstriff-0.10 -lgsttag-0.10 -logg"],
        # base plugin: pango ...
        ["pango",            "pango", "-lgstpango -lpangocairo-1.0 -lpango-1.0 -lgobject-2.0 -lglib-2.0 -lcairo"],
        # base plugin: theora ...
        ["theora",           "theora", "-lgsttheora -lgsttag-0.10 -lgstvideo-0.10 -ltheoraenc -ltheoradec -logg"],
        # base plugin: vorbis ..., use GST_PLUGIN_DEFINE2 and define gst_plugin_desc
        ["vorbis",           "vorbis", "-lgstvorbis -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lvorbis -lvorbisenc"],
        # base plugin: ivorbisdec ...
        #"ivorbisdec":       ("ivorbisdec", "-lgstivorbisdec"),

        # good: alpha ...
        ["alpha",            "alpha", "-lgstalpha -lgstvideo-0.10"],
        # good: alphacolor ...
        ["alphacolor",       "alphacolor", "-lgstalphacolor -lgstvideo-0.10"],
        # good: apetag ...
        ["apetag",           "apetag", "-lgstapetag -lgsttag-0.10 -lgstpbutils-0.10"],
        # good: audiofx ...
        ["audiofx",          "audiofx", "-lgstaudiofx -lgstaudio-0.10 -lgstfft-0.10 -lm"],
        # good: audioparsers ...
        ["audioparsers",     "audioparsers", "-lgstaudioparsers -lgsttag-0.10 -lgstaudio-0.10"],
        # good: auparse ...
        ["auparse",          "auparse", "-lgstauparse"],
        # good: autodetect ...
        ["autodetect",       "autodetect", "-lgstautodetect"],
        # good: avi ...
        ["avi",              "avi", "-lgstavi -lgstriff-0.10 -lgstaudio-0.10 -lgsttag-0.10"],
        # good: cutter ...
        ["cutter",           "cutter", "-lgstcutter -lgstaudio-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # good: efence ... in debugutils
        ["efence",           "efence", "-lgstefence -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # good: debug ...  in debugutils
        ["debug",            "debug", "-lgstdebug -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # good: navigationtest ... in debugutils
        ["navigationtest",   "navigationtest", "-lgstnavigationtest -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lgstvideo-0.10 -lm"],
        # good: deinterlace ...
        ["deinterlace",      "deinterlace", "-lgstdeinterlace -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lgstvideo-0.10 -lm"],
        # good: effectv ...
        ["effectv",          "effectv", "-lgsteffectv -lgstvideo-0.10 -lgstcontroller-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # good: equalizer ...
        ["equalizer",        "equalizer", "-lgstequalizer -lgstaudio-0.10 -lgstbase-0.10 -lgstcontroller-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # good: flv ...
        ["flv",              "flv", "-lgstflv -lgstpbutils-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # good: flxdec ...
        ["flxdec",           "flxdec", "-lgstflxdec -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # good: goom ...
        ["goom",             "goom", "-lgstgoom -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lorc-0.4 -lm -lrt -lpthread"],
        # good: goom2k1 ...
        ["goom2k1",          "goom2k1", "-lgstgoom2k1 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # good: icydemux ...
        ["icydemux",         "icydemux", "-lgsticydemux -lgsttag-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lz"],
        # good: id3demux ...
        ["id3demux",         "id3demux", "-lgstid3demux -lgsttag-0.10 -lgstpbutils-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # good: imagefreeze ...
        ["imagefreeze",      "imagefreeze", "-lgstimagefreeze -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # good: interleave ...
        ["interleave",       "interleave", "-lgstinterleave -lgstaudio-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # good: isomp4 ...
        ["isomp4",           "isomp4", "-lgstisomp4 -lgstriff-0.10 -lgstaudio-0.10 -lgstrtp-0.10 -lgsttag-0.10 -lgstpbutils-0.10 -lz"],
        # good: alaw ...
        ["alaw",             "alaw", "-lgstalaw -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # good: mulaw ...
        ["mulaw",            "mulaw", "-lgstmulaw -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # good: level ...
        ["level",            "level", "-lgstlevel -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # good: matroska ...
        ["matroska",         "matroska", "-lgstmatroska -lgstriff-0.10 -lgstaudio-0.10 -lgsttag-0.10 -lgstpbutils-0.10 -lz -lbz2 -lm"],
        # good: monoscope ...
        ["monoscope",        "monoscope", "-lgstmonoscope -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # good: multifile ...
        ["multifile",        "multifile", "-lgstmultifile -lgstvideo-0.10 -lgio-2.0 -lgobject-2.0 -lglib-2.0"],
        # good: multipart ...
        ["multipart",        "multipart", "-lgstmultipart -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # good: replaygain ...
        ["replaygain",       "replaygain", "-lgstreplaygain -lgstpbutils-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # good: rtp ...
        ["rtp",              "rtp", "-lgstrtp  -lgstaudio-0.10 -lgsttag-0.10 -lgstrtp-0.10 -lgstpbutils-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # good: gstrtpmanager ...
        ["gstrtpmanager",    "gstrtpmanager", "-lgstrtpmanager -lgstnetbuffer-0.10 -lgstrtp-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # good: rtsp ...
        ["rtsp",             "rtsp", "-lgstrtsp -lgstbase-0.10 -lgstinterfaces-0.10 -lgstrtp-0.10 -lgstrtsp-0.10 -lgstsdp-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # good: shapewipe ...
        ["shapewipe",        "shapewipe", "-lgstshapewipe -lgstcontroller-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lgstvideo-0.10"],
        # good: smpte ...
        ["smpte",            "smpte", "-lgstsmpte -lgstbase-0.10 -lgstvideo-0.10 -lgstcontroller-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # good: spectrum ...
        ["spectrum",         "spectrum", "-lgstspectrum -lgstfft-0.10 -lgstaudio-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # good: udp ...
        ["udp",              "udp", "-lgstudp -lgstnetbuffer-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # good: videobox ...
        ["videobox",         "videobox", "-lgstvideobox -lgstcontroller-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lorc-0.4 -lm -lrt -lpthread -lgstvideo-0.10"],
        # good: videocrop ...
        ["videocrop",        "videocrop", "-lgstvideocrop -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # good: videotemplate ... in videofilter
        #"videotemplate":    ("videotemplate", "-lgstvideotemplate"),
        # good: videofilter ...
        ["videofilter",      "videofilter", "-lgstvideofilter -lgstvideo-0.10 -lgstinterfaces-0.10 -lgstcontroller-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # good: videomixer ...
        ["videomixer",       "videomixer", "-lgstvideomixer -lgstvideo-0.10 -lgstbase-0.10 -lgstcontroller-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lorc-0.4 -lm -lrt -lpthread"],
        # good: wavenc ...
        ["wavenc",           "wavenc", "-lgstwavenc -lgstriff-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # good: wavparse ...
        ["wavparse",         "wavparse", "-lgstwavparse  -lgstriff-0.10 -lgstaudio-0.10 -lgsttag-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # good: y4menc ...
        ["y4menc",           "y4menc", "-lgsty4menc -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],

        # good sys: directsound ...
        #"directsound":      ("directsound", "-lgstdirectsound"),
        # good sys: ossaudio ...
        ["ossaudio",         "ossaudio", "-lgstossaudio -lgstinterfaces-0.10 -lgstaudio-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # good sys: oss4 ...
        #"oss4":             ("oss4", "-lgstoss4"),
        # good sys: osxaudio ...
        #"osxaudio":         ("osxaudio", "-lgstosxaudio"),
        # good sys: osxvideo ...
        #"osxvideo":         ("osxvideo", "-lgstosxvideo"),
        # good sys: sunaudio ...
        #"sunaudio":         ("sunaudio", "-lgstsunaudio"),
        # good sys: video4linux2 ...
        #"video4linux2":     ("video4linux2", "-lgstvideo4linux2 -lgstbase-0.10 -lgstcontroller-0.10 -lgstvideo-0.10 -lgstinterfaces-0.10 -lgstreamer-0.10 -ldl -lm -lgmodule-2.0 -lgthread-2.0 -lxml2 -lX11 -lXv -lXext -lv4l2 -lgudev-1.0 -lgobject-2.0 -lglib-2.0"),
        # good sys: waveform ...
        #"waveform":         ("waveform", "-lgstwaveform"),
        # good sys: ximagesrc ...
        ["ximagesrc",        "ximagesrc", "-lgstximagesrc -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lX11 -lXext -lXdamage -lXfixes"],

        # good plugin: aasink ...
        #"aasink":           ("aasink", "-lgstaasink"),
        # good plugin: annodex ...
        ["annodex",          "annodex", "-lgstannodex -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # good plugin: cairo ...
        ["cairo",            "cairo", "-lgstcairo -lgstvideo-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgmodule-2.0 -lgthread-2.0 -lxml2 -lcairo-gobject -lcairo -lgobject-2.0 -lglib-2.0 -lm"],
        # good plugin: dv ...
        ["dv",               "dv", "-lgstdv -lgstaudio-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -ldv -lm"],
        # good plugin: esdsink ...
        #"esdsink":          ("esdsink", "-lgstesdsink"),
        # good plugin: flac ...
        ["flac",             "flac", "-lgstflac -lgsttag-0.10 -lgstaudio-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lFLAC"],
        # good plugin: gconfelements ...
        ["gconfelements",    "gconfelements", "-lgstgconfelements -lgstreamer-0.10 -ldl -lm -lgmodule-2.0 -lxml2 -lgconf-2 -lORBit-2 -lgthread-2.0 -lgobject-2.0 -lglib-2.0"],
        # good plugin: gdkpixbuf ...
        ["gdkpixbuf",        "gdkpixbuf", "-lgstgdkpixbuf -lgstvideo-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgmodule-2.0 -lgthread-2.0 -lxml2 -lgdk_pixbuf-2.0 -lgobject-2.0 -lglib-2.0"],
        # good plugin: halelements ...
        #"halelements":      ("halelements", "-lgsthalelements"),
        # good plugin: jack ...
        ["jack",             "jack", "-lgstjack -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lgstaudio-0.10 -ljack -lpthread -lm -lrt"],
        # good plugin: jpeg ...
        ["jpeg",             "jpeg", "-lgstjpeg -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lgstvideo-0.10 -ljpeg -lm"],
        # good plugin: cacasink ...
        ["cacasink",         "cacasink", "-lgstcacasink -lncursesw -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lcaca -lz"],
        # good plugin: png ...
        ["png",              "png", "-lgstpng -lgstvideo-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lpng16"],
        # good plugin: pulseaudio ...
        #"pulseaudio":       ("pulseaudio", "-lgstpulseaudio"),
        # good plugin: 1394 ...
        ["1394",             "1394", "-lgst1394 -lgstinterfaces-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lavc1394 -lrom1394 -lm -liec61883 -lraw1394"],
        # good plugin: shout2send ...
        ["shout2send",       "shout2send", "-lgstshout2 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lshout -lvorbis -ltheora -logg -lspeex -lm"],
        # good plugin: soup ...
        ["soup",             "soup", "-lgstsouphttpsrc -lgsttag-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgmodule-2.0 -lgthread-2.0 -lxml2 -lsoup-gnome-2.4 -lsoup-2.4 -lgio-2.0 -lgobject-2.0 -lglib-2.0"],
        # good plugin: speex ...
        ["speex",            "speex", "-lgstspeex -lgsttag-0.10 -lgstaudio-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lspeex -lm"],
        # good plugin: taglib ...
        ["taglib",           "taglib", "-lgsttaglib -lgsttag-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -ltag -lstdc++"],
        # good plugin: wavpack ...
        ["wavpack",          "wavpack", "-lgstwavpack -lgstaudio-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lwavpack"],

        # ugly: asf ...
        ["asf",              "asf", "-lgstasf -lgstriff-0.10 -lgstrtsp-0.10 -lgstsdp-0.10 -lgstrtp-0.10 -lgstaudio-0.10 -lgsttag-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # ugly: dvdlpcmdec ...
        ["dvdlpcmdec",       "dvdlpcmdec", "-lgstdvdlpcmdec -lgstaudio-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # ugly: dvdsub ...
        ["dvdsub",           "dvdsub", "-lgstdvdsub -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # ugly: iec958 ...
        ["iec958",           "iec958", "-lgstiec958 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # ugly: mpegaudioparse ...
        ["mpegaudioparse",   "mpegaudioparse", "-lgstmpegaudioparse -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # ugly: mpegstream ...
        ["mpegstream",       "mpegstream", "-lgstmpegstream -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lgstaudio-0.10"],
        # ugly: realmedia ...
        ["realmedia",        "realmedia", "-lgstrmdemux -lgstrtsp-0.10 -lgstsdp-0.10 -lgstpbutils-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # ugly: synaesthesia ... memory overwrite:
        #Dump of assembler code for function synaesthesia_init:
        #   0xb1fd5580 <+0>:     mov    0xb2d63780,%eax
        #   0xb1fd5585 <+5>:     test   %eax,%eax
        #   0xb1fd5587 <+7>:     jne    0xb1fd5765 <synaesthesia_init+485>
        #   0xb1fd558d <+13>:    push   %ebp
        #   0xb1fd558e <+14>:    push   %edi
        #   0xb1fd558f <+15>:    push   %esi
        #   0xb1fd5590 <+16>:    push   %ebx
        #   0xb1fd5591 <+17>:    xor    %ebx,%ebx
        #   0xb1fd5593 <+19>:    sub    $0x2c,%esp
        #   0xb1fd5596 <+22>:    lea    0x0(%esi),%esi
        #   0xb1fd5599 <+25>:    lea    0x0(%edi,%eiz,1),%edi
        #   0xb1fd55a0 <+32>:    sub    $0x10,%esp
        #   0xb1fd55a3 <+35>:    add    $0x1,%ebx
        #   0xb1fd55a6 <+38>:    mov    %ebx,0x18(%esp)
        #   0xb1fd55aa <+42>:    fildl  0x18(%esp)
        #   0xb1fd55ae <+46>:    fstpl  (%esp)
        #   0xb1fd55b1 <+49>:    call   0xb7c2b510 <log>
        #   0xb1fd55b6 <+54>:    fdivl  0xb268cf68
        #   0xb1fd55bc <+60>:    add    $0x10,%esp
        #   0xb1fd55bf <+63>:    cmp    $0x202,%ebx
        #   0xb1fd55c5 <+69>:    fmull  0xb2773650
        #   0xb1fd55cb <+75>:    fmuls  0xb25d5d24
        #   0xb1fd55d1 <+81>:    fstpl  -0x4d297048(,%ebx,8)
        #=> 0xb1fd55d8 <+88>:    jne    0xb1fd55a0 <synaesthesia_init+32>
        #["synaesthesia",     "synaesthesia", "-lgstsynaesthesia -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],

        # ugly plugin: a52dec ...
        ["a52dec",           "a52dec", "-lgsta52dec -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lgstaudio-0.10 -lorc-0.4 -lrt -lpthread -la52 -lm"],
        # ugly plugin: amrnb ...
        ["amrnb",            "amrnb", "-lgstamrnb -lgstaudio-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lopencore-amrnb"],
        # ugly plugin: amrwbdec ...
        ["amrwbdec",         "amrwbdec", "-lgstamrwbdec -lgstaudio-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lopencore-amrwb"],
        # ugly plugin: cdio ...
        ["cdio",             "cdio", "-lgstcdio -lgstcdda-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lcdio -lm"],
        # ugly plugin: dvdread ...
        ["dvdread",          "dvdread", "-lgstdvdread -lgstbase-0.10 -lgstreamer-0.10 -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -ldvdread -ldl"],
        # ugly plugin: lame ...
        ["lame",             "lame", "-lgstlame -lgstaudio-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lmp3lame -lm"],
        # ugly plugin: mad ...
        ["mad",              "mad", "-lgstmad -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lgsttag-0.10 -lgstaudio-0.10 -lmad"],
        # ugly plugin: mpeg2dec ...
        ["mpeg2dec",         "mpeg2dec", "-lgstmpeg2dec -lgstvideo-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lmpeg2"],
        # ugly plugin: siddec ...
        ["sid",              "siddec", "-lgstsid -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lsidplay"],
        # ugly plugin: twolame ...
        ["twolame",          "twolame", "-lgsttwolame -lgstaudio-0.10 -lgstpbutils-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -ltwolame"],
        # ugly plugin: x264 ...
        ["x264",             "x264", "-lgstx264 -lgstvideo-0.10 -lgstpbutils-0.10 -lgstreamer-0.10 -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -L/usr/local/local/lib -lx264 -lpthread -lm -ldl"],

        # bad: adpcmdec ...
        ["adpcmdec",         "adpcmdec", "-lgstadpcmdec -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: adpcmenc ...
        ["adpcmenc",         "adpcmenc", "-lgstadpcmenc -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: aiff ...
        ["aiff",             "aiff", "-lgstaiff -lgsttag-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # bad: asfmux ...
        ["asfmux",           "asfmux", "-lgstasfmux -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lgstrtp-0.10"],
        # bad: audiovisualizers ...
        ["audiovisualizers", "audiovisualizers", "-lgstaudiovisualizers -lgstaudio-0.10 -lgstvideo-0.10 -lgstfft-0.10 -lgstbase-0.10 -lgstcontroller-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # bad: autoconvert ...
        ["autoconvert",      "autoconvert", "-lgstautoconvert -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: bayer ...
        ["bayer",            "bayer", "-lgstbayer -lgstvideo-0.10 -lorc-0.4 -lrt -lpthread -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: camerabin ... , multiple definition of `orc_splat_u32'
        #"camerabin":        ("camerabin", "-lgstcamerabin -lgstphotography-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lgstinterfaces-0.10 -lgsttag-0.10"),
        # bad: camerabin2 ...
        ["camerabin2",       "camerabin2", "-lgstcamerabin2 -lgstphotography-0.10 -lgstbasecamerabinsrc-0.10 -lgstinterfaces-0.10 -lgsttag-0.10 -lgstapp-0.10 -lgstpbutils-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: cdxaparse ...
        ["cdxaparse",        "cdxaparse", "-lgstcdxaparse -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lgstriff-0.10"],
        # bad: coloreffects ...
        ["coloreffects",     "coloreffects", "-lgstcoloreffects -lgstvideo-0.10 -lgstcontroller-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: colorspace ...
        ["colorspace",       "colorspace", "-lgstcolorspace -lgstvideo-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lorc-0.4 -lm -lrt -lpthread"],
        # bad: dataurisrc ...
        ["dataurisrc",       "dataurisrc", "-lgstdataurisrc -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: dccp ...
        ["dccp",             "dccp", "-lgstdccp -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lpthread"],
        # bad: debugutilsbad ...
        ["debugutilsbad",    "debugutilsbad", "-lgstdebugutilsbad -lgstbase-0.10 -lgstvideo-0.10 -lgstinterfaces-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: dtmf ...
        ["dtmf",             "dtmf", "-lgstdtmf -lgstrtp-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # bad: dvbsuboverlay ...
        ["dvbsuboverlay",    "dvbsuboverlay", "-lgstdvbsuboverlay -lgstvideo-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: dvdspu ...
        ["dvdspu",           "dvdspu", "-lgstdvdspu -lgstvideo-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: faceoverlay ...
        ["faceoverlay",      "faceoverlay", "-lgstfaceoverlay -lgstvideo-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: festival ...
        ["festival",         "festival", "-lgstfestival -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lgstaudio-0.10"],
        # bad: fieldanalysis ...
        ["fieldanalysis",    "fieldanalysis", "-lgstfieldanalysis -lgstvideo-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lorc-0.4 -lm -lrt -lpthread"],
        # bad: freeverb ...
        ["freeverb",         "freeverb", "-lgstfreeverb -lgstbase-0.10 -lgstcontroller-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: freeze ...
        ["freeze",           "freeze", "-lgstfreeze -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: frei0r ...
        ["frei0r",           "frei0r", "-lgstfrei0r -lgstcontroller-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lgstvideo-0.10"],
        # bad: gaudieffects ...
        ["gaudieffects",     "gaudieffects", "-lgstgaudieffects -lgstvideo-0.10 -lgstcontroller-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # bad: geometrictransform ...
        ["geometrictransform", "geometrictransform", "-lgstgeometrictransform -lgstvideo-0.10 -lgstinterfaces-0.10 -lgstcontroller-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # bad: h264parse ...
        ["h264parse",        "h264parse", "-lgsth264parse -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: hdvparse ...
        ["hdvparse",         "hdvparse", "-lgsthdvparse -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # bad: fragmented ...
        ["fragmented",       "fragmented", "-lgstfragmented -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: id3tag ...
        ["id3tag",           "id3tag", "-lgstid3tag -lgsttag-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: inter ...
        ["inter",            "inter", "-lgstinter -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lgstvideo-0.10 -lgstaudio-0.10 -lm"],
        # bad: interlace ...
        ["interlace",        "interlace", "-lgstinterlace -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lgstvideo-0.10 -lm"],
        # bad: ivfparse ...
        ["ivfparse",         "ivfparse", "-lgstivfparse -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: jp2kdecimator ...
        ["jp2kdecimator",    "jp2kdecimator", "-lgstjp2kdecimator -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: jpegformat ...
        ["jpegformat",       "jpegformat", "-lgstjpegformat -lgstinterfaces-0.10 -lgsttag-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: legacyresample ...
        ["legacyresample",   "legacyresample", "-lgstlegacyresample -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # bad: rfbsrc ...
        ["rfbsrc",           "rfbsrc", "-lgstrfbsrc -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lxml2 -lX11 -lgobject-2.0 -lgthread-2.0 -lgmodule-2.0 -lglib-2.0"],
        # bad: liveadder ...
        ["liveadder",        "liveadder", "-lgstliveadder -lgstaudio-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: mpegdemux2 ...
        ["mpegdemux2",       "mpegdemux2", "-lgstmpegdemux -lgsttag-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: mpegpsmux ...
        ["mpegpsmux",        "mpegpsmux", "-lgstmpegpsmux -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: mpegtsdemux ...
        ["mpegtsdemux",      "mpegtsdemux", "-lgstmpegtsdemux -lgsttag-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: mpegtsmux ...
        ["mpegtsmux",        "mpegtsmux", "-lgstmpegtsmux -lgstvideo-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: mpegvideoparse ... , multiple definition of `mpeg_util_parse_picture_hdr'
        #"mpegvideoparse":   ("mpegvideoparse", "-lgstmpegvideoparse -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"),
        # bad: mve ...
        ["mve",              "mve", "-lgstmve -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # bad: mxf ...
        ["mxf",              "mxf", "-lgstmxf -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lgstvideo-0.10"],
        # bad: nsf ...
        ["nsf",              "nsf", "-lgstnsf -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # bad: nuvdemux ...
        ["nuvdemux",         "nuvdemux", "-lgstnuvdemux -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: patchdetect ...
        ["patchdetect",      "patchdetect", "-lgstpatchdetect -lgstvideo-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # bad: pcapparse ...
        ["pcapparse",        "pcapparse", "-lgstpcapparse -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: pnm ...
        ["pnm",              "pnm", "-lgstpnm -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lgstvideo-0.10"],
        # bad: rawparse ...
        ["rawparse",         "rawparse", "-lgstrawparse -lgstvideo-0.10 -lgstaudio-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: real ...
        ["real",             "real", "-lgstreal -lgstaudio-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: removesilence ...
        ["removesilence",    "removesilence", "-lgstremovesilence -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: rtpmux ...
        ["rtpmux",           "rtpmux", "-lgstrtpmux -lgstrtp-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: rtpvp8 ...
        ["rtpvp8",           "rtpvp8", "-lgstrtpvp8 -lgstrtp-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: scaletempo ...
        ["scaletempo",       "scaletempo", "-lgstscaletempoplugin -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: sdi ...
        ["sdi",              "sdi", "-lgstsdi -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: sdp ...
        ["sdp",              "sdp", "-lgstsdpelem -lgstbase-0.10 -lgstinterfaces-0.10 -lgstrtp-0.10 -lgstsdp-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: segmentclip ...
        ["segmentclip",      "segmentclip", "-lgstsegmentclip -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lgstaudio-0.10"],
        # bad: gstsiren ...
        ["gstsiren",         "gstsiren", "-lgstsiren -lgstrtp-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # bad: smooth ...
        ["smooth",           "smooth", "-lgstsmooth -lgstvideo-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: speed ...
        ["speed",            "speed", "-lgstspeed -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # bad: stereo ...
        ["stereo",           "stereo", "-lgststereo -lgstbase-0.10 -lgstcontroller-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lgstaudio-0.10"],
        # bad: subenc ...
        ["subenc",           "subenc", "-lgstsubenc -lgstbase-0.10 -lgstcontroller-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: tta ...
        ["tta",              "tta", "-lgsttta -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # bad: videofiltersbad ...
        ["videofiltersbad",  "videofiltersbad", "-lgstvideofiltersbad -lgstvideo-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lorc-0.4 -lrt -lpthread -lm"],
        # bad: videomaxrate ...
        ["videomaxrate",     "videomaxrate", "-lgstvideomaxrate -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: videomeasure ...
        ["videomeasure",     "videomeasure", "-lgstvideomeasure -lgstvideo-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # bad: videoparsersbad ... , multiple definition gst_h264_parse_get_type etc
        #"videoparsersbad":  ("videoparsersbad", "-lgstvideoparsersbad -lgstpbutils-0.10 -lgstvideo-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"),
        # bad: videosignal ...
        ["videosignal",      "videosignal", "-lgstvideosignal -lgstvideo-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: vmnc ...
        ["vmnc",             "vmnc", "-lgstvmnc -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad: y4mdec ...
        ["y4mdec",           "y4mdec", "-lgsty4mdec -lgstvideo-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],

        # bad sys: acmenc ...
        #"acmenc":           ("acmenc", "-lgstacmenc"),
        # bad sys: acmmp3dec ...
        #"acmmp3dec":        ("acmmp3dec", "-lgstacmmp3dec"),
        # bad sys: applemedia ...
        #"applemedia":       ("applemedia", "-lgstapplemedia"),
        # bad sys: avcsrc ...
        #"avcsrc":           ("avcsrc", "-lgstavcsrc"),
        # bad sys: d3dsinkwrapper ...
        #"d3dsinkwrapper":   ("d3dsinkwrapper", "-lgstd3dsinkwrapper"),
        # bad sys: decklink ...
        ["decklink",         "decklink", "-lgstdecklink -lgstbase-0.10 -lgstreamer-0.10 -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lpthread -ldl"],
        # bad sys: directdraw ...
        #"directdraw":       ("directdraw", "-lgsdirectdraw"),
        # bad sys: directsoundsrc ...
        #"directsoundsrc":   ("directsoundsrc", "-lgstdirectsoundsrc"),
        # bad sys: dshowdecwrapper ...
        #"dshowdecwrapper":  ("dshowdecwrapper", "-lgstdshowdecwrapper"),
        # bad sys: dshowsrcwrapper ...
        #"dshowsrcwrapper":  ("dshowsrcwrapper", "-lgstdshowsrcwrapper"),
        # bad sys: dshowsinkwrapper ...
        #"dshowsinkwrapper": ("dshowsinkwrapper", "-lgstdshowsinkwrapper"),
        # bad sys: dvb ...
        ["dvb",              "dvb", "-lgstdvb -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad sys: fbdevsink ...
        ["fbdevsink",        "fbdevsink", "-lgstfbdevsink -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad sys: linsys ...
        ["linsys",           "linsys", "-lgstlinsys -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad sys: osxvideosrc ...
        #"osxvideosrc":      ("osxvideosrc", "-lgstosxvideosrc"),
        # bad sys: pvr ...
        #"pvr":              ("pvr", "-lgstpvr"),
        # bad sys: qtwrapper ...
        #"qtwrapper":        ("qtwrapper", "-lgstqtwrapper"),
        # bad sys: shm ...
        ["shm",              "shm", "-lgstshm -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lrt"],
        # bad sys: vcdsrc ...
        ["vcdsrc",           "vcdsrc", "-lgstvcdsrc -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad sys: vdpau ...
        ["vdpau",            "vdpau", "-lgstvdpau -lgstvdp-0.10 -lX11 -lvdpau -lgstvideo-0.10 -lgstinterfaces-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lm"],
        # bad sys: wasapi ...
        #"wasapi":           ("wasapi", "-lgstwasapi"),
        # bad sys: wininet ...
        #"wininet":          ("wininet", "-lgstwininet"),
        # bad sys: winks ...
        #"winks":            ("winks", "-lgstwinks"),
        # bad sys: winscreencap ...
        #"winscreencap":     ("winscreencap", "-lgstwinscreencap"),

        # bad plugin: apexsink ...
        ["apexsink",         "apexsink", "-lgstapexsink -lgstaudio-0.10 -lgstinterfaces-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lssl -lcrypto"],
        # bad plugin: assrender ..., harfbuzz link issue
        #"assrender":        ("assrender", "-lgstassrender -lass -lharfbuzz -lfontconfig -lenca -lfribidi -lfreetype -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lgstvideo-0.10"),
        # bad plugin: bz2 ...
        ["bz2",              "bz2", "-lgstbz2 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lbz2"],
        # bad plugin: cdaudio ...
        ["cdaudio",          "cdaudio", "-lgstcdaudio -lcdaudio -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad plugin: celt ...
        ["celt",             "celt", "-lgstcelt -lgstaudio-0.10 -lgsttag-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lcelt0"],
        # bad plugin: cog ..., multiple definition of `cogorc_memcpy_2d'
        #"cog":              ("cog", "-lgstcog -lgstvideo-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lorc-0.4 -lm -lrt -lpthread -lpng16"),
        # bad plugin: curl ...
        ["curl",             "curl", "-lgstcurl -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lcurl"],
        # bad plugin: dc1394 ...
        ["dc1394",           "dc1394", "-lgstdc1394 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -ldc1394 -lusb-1.0 -ludev -pthread"],
        # bad plugin: dirac ...
        #"dirac":            ("dirac", "-lgstdirac"),
        # bad plugin: dfbvideosink ...
        #"dfbvideosink":     ("dfbvideosink", "-lgstdfbvideosink"),
        # bad plugin: divxdec ...
        #"divxdec":          ("divxdec", "-lgstdivxdec"),
        # bad plugin: divxenc ...
        #"divxenc":          ("divxenc", "-lgstdivxenc"),
        # bad plugin: dtsdec ...
        #"dtsdec":           ("dtsdec", "-lgstdtsdec"),
        # bad plugin: eglglessink ...
        ["eglglessink",      "eglglessink", "-lgsteglglessink -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lEGL -lGLESv2 -lgstvideo-0.10 -lgstinterfaces-0.10"],
        # bad plugin: faac ...
        ["faac",             "faac", "-lgstfaac -lgstaudio-0.10 -lgstpbutils-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lfaac -lm"],
        # bad plugin: faad ...
        ["faad",             "faad", "-lgstfaad -lgstaudio-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lfaad -lm"],
        # bad plugin: flite ...
        #"flite":            ("flite", "-lgstflite"),
        # bad plugin: gmedec ...
        #"gmedec":           ("gmedec", "-lgstgmedec"),
        # bad plugin: gsettings ...
        #"gsettings":        ("gsettings", "-lgstgsettingselements -lgstreamer-0.10 -ldl -lm -lgmodule-2.0 -lgthread-2.0 -lxml2 -lgio-2.0 -lgobject-2.0 -lglib-2.0"),
        # bad plugin: gsm ...
        ["gsm",              "gsm", "-lgstgsm  -lgsm -lgstaudio-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2"],
        # bad plugin: jp2k ...
        ["jp2k",             "jp2k", "-lgstjp2k -lgstvideo-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -ljasper"],
        # bad plugin: kate ...
        #"kate":             ("kate", "-lgstkate"),
        # bad plugin: ladspa ...
        #"ladspa":           ("ladspa", "-lgstladspa"),
        # bad plugin: mms ...
        #"mms":              ("mms", "-lgstmms"),
        # bad plugin: lv2 ...
        #"lv2":              ("lv2", "-lgstlv2"),
        # bad plugin: mimic ...
        #"mimic":            ("mimic", "-lgstmimic"),
        # bad plugin: modplug ...
        ["modplug",          "modplug", "-lgstmodplug -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lmodplug"],
        # bad plugin: wavpack ...
        #"mpeg2enc":         ("mpeg2enc", "-lgstmpeg2enc"),
        # bad plugin: mplex ...
        #"mplex":            ("mplex", "-lgstmplex"),
        # bad plugin: musepack ...
        #"musepack":         ("musepack", "-lgstwmusepack"),
        # bad plugin: musicbrainz ...
        #"musicbrainz":      ("musicbrainz", "-lgstmusicbrainz"),
        # bad plugin: mythtv ...
        #"mythtv":           ("mythtv", "-lgstmythtv"),
        # bad plugin: nas ...
        #"nas":              ("nas", "-lgstnas"),
        # bad plugin: neon ...
        #"neon":             ("neon", "-lgstneon"),
        # bad plugin: ofa ...
        #"ofa":              ("ofa", "-lgstofa"),
        # bad plugin: openal ...
        ["openal",           "openal", "-lgstopenal -lgstaudio-0.10 -lgstbase-0.10 -lgstreamer-0.10 -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lopenal -lrt -lpthread -ldl -lm"],
        # bad plugin: opencv ...
        #"opencv":           ("opencv", "-lgstopencv"),
        # bad plugin: opus ..., multiple definition of `celt_encoder_get_size'
        #"opus":             ("opus", "-lgstopus  -lgstaudio-0.10 -lgsttag-0.10 -lgstrtp-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lopus -lm"),
        # bad plugin: resindvd ...
        ["resindvd",         "resindvd", "-lresindvd -lgstinterfaces-0.10 -lgstvideo-0.10 -lgstpbutils-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -ldvdnav -lpthread -ldvdread"],
        # bad plugin: rsvg ...
        ["rsvg",             "rsvg", "-lgstrsvg -lgstvideo-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgmodule-2.0 -lgthread-2.0 -lxml2 -lrsvg-2 -lm -lgio-2.0 -lgdk_pixbuf-2.0 -lgobject-2.0 -lglib-2.0 -lcairo"],
        # bad plugin: rtmp ...
        ["rtmp",             "rtmp", "-lgstrtmp -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lrtmp -lz -lssl -lcrypto"],
        # bad plugin: schro ..., multiple definition of `orc_unpack_yuyv_y'
        #["schro",            "schro", "-lgstschro -lgstvideo-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lschroedinger-1.0 -lorc-0.4 -lm -lrt -lpthread"],
        # bad plugin: sdl ..., multiple definition of `XShmQueryExtension'
        #"sdl":              ("sdl", "-lgstsdl -lgstreamer-0.10 -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lgstvideo-0.10 -lgstaudio-0.10 -lgstinterfaces-0.10 -L/usr/local/lib64 -lSDL -lm -ldl -lpthread"),
        # bad plugin: sndfile ...
        ["sndfile",          "sndfile", "-lgstsndfile -lgstbase-0.10 -lgstreamer-0.10 -ldl -lm -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lsndfile"],
        # bad plugin: soundtouch ...
        #"soundtouch":       ("soundtouch", "-lgstsoundtouch"),
        # bad plugin: spandsp ...
        #"spandsp":          ("spandsp", "-lgstspandsp"),
        # bad plugin: spcdec ...
        #"spcdec":           ("spcdec", "-lgstspcdec"),
        # bad plugin: swfdec ...
        #"swfdec":           ("swfdec", "-lgstswfdeck"),
        # bad plugin: teletext ...
        #"teletext":         ("teletext", "-lgstteletext"),
        # bad plugin: timidity ...
        #"timidity":         ("timidity", "-lgsttimidity"),
        # bad plugin: wildmidi ...
        #"wildmidi":         ("wildmidi", "-lgstwildmidi"),
        # bad plugin: voaacenc ...
        #"voaacenc":         ("voaacenc", "-lgstvoaacenc"),
        # bad plugin: voamrwbenc ...
        #"voamrwbenc":       ("voamrwbenc", "-lgstvoamrwbenc"),
        # bad plugin: vp8 ..., multiple definition of `basevideodecoder_debug'
        #"vp8":              ("vp8", "-lgstvp8 -lgstbasevideo-0.10 -lgsttag-0.10 -lgstvideo-0.10 -lgstbase-0.10 -lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2 -lvpx -lm"),
        # bad plugin: xvid ...
        ["xvid",             "xvid", "-lgstxvid -lxvidcore -lm"],
        # bad plugin: zbar ...
        #"zbar":             ("zbar", "-lgstzbar"),
        ]
'''

-lgstreamer-0.10 -ldl -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lxml2

'''

'''
ac3iec.c (gst-plugins-ugly-0.10.19\gst\iec958):450
  if (!gst_element_register (plugin, "ac3iec958", GST_RANK_NONE,
          GST_TYPE_AC3IEC)) {
    return FALSE;
acmenc.c (gst-plugins-bad-0.10.23\sys\acmenc):570
  if (!gst_element_register (plugin, type_name, GST_RANK_NONE, type)) {
    g_warning ("Failed to register %s", type_name);;
    g_type_set_qdata (type, ACMENC_PARAMS_QDATA, NULL);
acmmp3dec.c (gst-plugins-bad-0.10.23\sys\acmmp3dec):424
  if (!gst_element_register (plugin, "acmmp3dec", GST_RANK_PRIMARY,
          GST_TYPE_ACM_MP3_DEC)) {
    return FALSE;
adpcmdec.c (gst-plugins-bad-0.10.23\gst\adpcmdec):579
  if (!gst_element_register (plugin, "adpcmdec", GST_RANK_PRIMARY,
          GST_TYPE_ADPCM_DEC)) {
    return FALSE;
adpcmenc.c (gst-plugins-bad-0.10.23\gst\adpcmenc):561
  if (!gst_element_register (plugin, "adpcmenc", GST_RANK_PRIMARY,
          GST_TYPE_ADPCM_ENC)) {
    return FALSE;
aiff.c (gst-plugins-bad-0.10.23\gst\aiff):54
  ret = gst_element_register (plugin, "aiffparse", GST_RANK_PRIMARY,
      GST_TYPE_AIFF_PARSE);
  ret &= gst_element_register (plugin, "aiffmux", GST_RANK_PRIMARY,
      GST_TYPE_AIFF_MUX);

alaw.c (gst-plugins-good-0.10.31\gst\law):63
  if (!gst_element_register (plugin, "alawenc",
          GST_RANK_PRIMARY, GST_TYPE_ALAW_ENC) ||
      !gst_element_register (plugin, "alawdec",
          GST_RANK_PRIMARY, GST_TYPE_ALAW_DEC))
    return FALSE;
amrnb.c (gst-plugins-ugly-0.10.19\ext\amrnb):30
  return gst_element_register (plugin, "amrnbdec",
      GST_RANK_PRIMARY, GST_TYPE_AMRNBDEC) &&
      gst_element_register (plugin, "amrnbenc",
      GST_RANK_SECONDARY, GST_TYPE_AMRNBENC);
}
amrwb.c (gst-plugins-ugly-0.10.19\ext\amrwbdec):29
  return gst_element_register (plugin, "amrwbdec",
      GST_RANK_PRIMARY, GST_TYPE_AMRWBDEC);
}
audiodecoders.c (gst-plugins-bad-0.10.23\sys\qtwrapper):1077
      if (!gst_element_register (plugin, type_name, GST_RANK_MARGINAL, type)) {
        g_warning ("Failed to register %s", type_name);;
        g_type_set_qdata (type, QTWRAPPER_ADEC_PARAMS_QDATA, NULL);
audiofx.c (gst-plugins-good-0.10.31\gst\audiofx):52
  return (gst_element_register (plugin, "audiopanorama", GST_RANK_NONE,
          GST_TYPE_AUDIO_PANORAMA) &&
      gst_element_register (plugin, "audioinvert", GST_RANK_NONE,
          GST_TYPE_AUDIO_INVERT) &&
      gst_element_register (plugin, "audiokaraoke", GST_RANK_NONE,
          GST_TYPE_AUDIO_KARAOKE) &&
      gst_element_register (plugin, "audioamplify", GST_RANK_NONE,
          GST_TYPE_AUDIO_AMPLIFY) &&
      gst_element_register (plugin, "audiodynamic", GST_RANK_NONE,
          GST_TYPE_AUDIO_DYNAMIC) &&
      gst_element_register (plugin, "audiocheblimit", GST_RANK_NONE,
          GST_TYPE_AUDIO_CHEB_LIMIT) &&
      gst_element_register (plugin, "audiochebband", GST_RANK_NONE,
          GST_TYPE_AUDIO_CHEB_BAND) &&
      gst_element_register (plugin, "audioiirfilter", GST_RANK_NONE,
          GST_TYPE_AUDIO_IIR_FILTER) &&
      gst_element_register (plugin, "audiowsinclimit", GST_RANK_NONE,
          GST_TYPE_AUDIO_WSINC_LIMIT) &&
      gst_element_register (plugin, "audiowsincband", GST_RANK_NONE,
          GST_TYPE_AUDIO_WSINC_BAND) &&
      gst_element_register (plugin, "audiofirfilter", GST_RANK_NONE,
          GST_TYPE_AUDIO_FIR_FILTER) &&
      gst_element_register (plugin, "audioecho", GST_RANK_NONE,
          GST_TYPE_AUDIO_ECHO));
}
baseaudiovisualizer.c (gst-plugins-bad-0.10.23\...\elements):165
  gst_element_register (NULL, "testscope", GST_RANK_NONE, GST_TYPE_TEST_SCOPE);
}

d3dvideosink.c (gst-plugins-bad-0.10.23\sys\d3dvideosink):2617
  if (!gst_element_register (plugin, "d3dvideosink",
          GST_RANK_PRIMARY, GST_TYPE_D3DVIDEOSINK))
    return FALSE;
debugutilsbad.c (gst-plugins-bad-0.10.23\gst\debugutils):35
  gst_element_register (plugin, "checksumsink", GST_RANK_NONE,
      gst_checksum_sink_get_type ());
  gst_element_register (plugin, "fpsdisplaysink", GST_RANK_NONE,
      fps_display_sink_get_type ());
  gst_element_register (plugin, "chopmydata", GST_RANK_NONE,
      gst_chop_my_data_get_type ());
  gst_element_register (plugin, "compare", GST_RANK_NONE,
      gst_compare_get_type ());
  gst_element_register (plugin, "debugspy", GST_RANK_NONE,
      gst_debug_spy_get_type ());

decodebin.c (gst-plugins-base-0.10.36\...\elements):300
  return gst_element_register (plugin, "testmpegaudioparse", GST_RANK_NONE,
      test_mpeg_audio_parse_get_type ());
}
decodebin2.c (gst-plugins-base-0.10.36\...\elements):305
  return gst_element_register (plugin, "testmpegaudioparse", GST_RANK_NONE,
      test_mpeg_audio_parse_get_type ());
}
decodebin2.c (gst-plugins-base-0.10.36\...\elements):579
  gst_element_register (NULL, "fakeh264parse", GST_RANK_PRIMARY + 101,
      gst_fake_h264_parser_get_type ());
  gst_element_register (NULL, "fakeh264dec", GST_RANK_PRIMARY + 100,
      gst_fake_h264_decoder_get_type ());

dfbvideosink.c (gst-plugins-bad-0.10.23\ext\directfb):2406
  if (!gst_element_register (plugin, "dfbvideosink", GST_RANK_MARGINAL,
          GST_TYPE_DFBVIDEOSINK))
    return FALSE;
dvbbasebin.c (gst-plugins-bad-0.10.23\sys\dvb):1031
  return gst_element_register (plugin, "dvbbasebin",
      GST_RANK_NONE, GST_TYPE_DVB_BASE_BIN);
}
dvdreadsrc.c (gst-plugins-ugly-0.10.19\ext\dvdread):1789
  if (!gst_element_register (plugin, "dvdreadsrc", GST_RANK_SECONDARY,
          GST_TYPE_DVD_READ_SRC)) {
    return FALSE;
efence.c (gst-plugins-good-0.10.31\gst\debugutils):356
  if (!gst_element_register (plugin, "efence", GST_RANK_NONE, GST_TYPE_EFENCE))
    return FALSE;

gst.c (gstreamer-0.10.36\gst):636
  if (!gst_element_register (plugin, "bin", GST_RANK_PRIMARY,
          GST_TYPE_BIN) ||
      !gst_element_register (plugin, "pipeline", GST_RANK_PRIMARY,
          GST_TYPE_PIPELINE)
      )
gst1394.c (gst-plugins-good-0.10.31\ext\raw1394):35
  if (!gst_element_register (plugin, "dv1394src", GST_RANK_NONE,
          GST_TYPE_DV1394SRC))
    return FALSE;
gst1394.c (gst-plugins-good-0.10.31\ext\raw1394):39
  if (!gst_element_register (plugin, "hdv1394src", GST_RANK_NONE,
          GST_TYPE_HDV1394SRC))
    return FALSE;
gsta52dec.c (gst-plugins-ugly-0.10.19\ext\a52dec):1000
  if (!gst_element_register (plugin, "a52dec", GST_RANK_SECONDARY,
          GST_TYPE_A52DEC))
    return FALSE;
gstaasink.c (gst-plugins-good-0.10.31\ext\aalib):577
  if (!gst_element_register (plugin, "aasink", GST_RANK_NONE, GST_TYPE_AASINK))
    return FALSE;

gstadder.c (gst-plugins-base-0.10.36\gst\adder):1322
  if (!gst_element_register (plugin, "adder", GST_RANK_NONE, GST_TYPE_ADDER)) {
    return FALSE;
  }
gstalpha.c (gst-plugins-good-0.10.31\gst\alpha):2647
  return gst_element_register (plugin, "alpha", GST_RANK_NONE, GST_TYPE_ALPHA);
}

gstalphacolor.c (gst-plugins-good-0.10.31\gst\alpha):664
  return gst_element_register (plugin, "alphacolor", GST_RANK_NONE,
      GST_TYPE_ALPHA_COLOR);
}
gstalsaplugin.c (gst-plugins-base-0.10.36\ext\alsa):61
  if (!gst_element_register (plugin, "alsamixer", GST_RANK_NONE,
          GST_TYPE_ALSA_MIXER_ELEMENT))
    return FALSE;
  if (!gst_element_register (plugin, "alsasrc", GST_RANK_PRIMARY,
          GST_TYPE_ALSA_SRC))
    return FALSE;
  if (!gst_element_register (plugin, "alsasink", GST_RANK_PRIMARY,
          GST_TYPE_ALSA_SINK))
    return FALSE;
gstapedemux.c (gst-plugins-good-0.10.31\gst\apetag):428
  return gst_element_register (plugin, "apedemux",
      GST_RANK_PRIMARY, GST_TYPE_APE_DEMUX);
}
gstapexplugin.c (gst-plugins-bad-0.10.23\ext\apexsink):34
  return gst_element_register (plugin, GST_APEX_SINK_NAME, GST_RANK_NONE,
      GST_TYPE_APEX_SINK);
}
gstapp.c (gst-plugins-base-0.10.36\gst\app):58
  gst_element_register (plugin, "appsrc", GST_RANK_NONE, GST_TYPE_APP_SRC);
  gst_element_register (plugin, "appsink", GST_RANK_NONE, GST_TYPE_APP_SINK);

  return TRUE;
gstasf.c (gst-plugins-ugly-0.10.19\gst\asfdemux):48
  if (!gst_element_register (plugin, "asfdemux", GST_RANK_SECONDARY,
          GST_TYPE_ASF_DEMUX)) {
    return FALSE;
gstasf.c (gst-plugins-ugly-0.10.19\gst\asfdemux):52
  if (!gst_element_register (plugin, "rtspwms", GST_RANK_SECONDARY,
          GST_TYPE_RTSP_WMS)) {
    return FALSE;
gstasf.c (gst-plugins-ugly-0.10.19\gst\asfdemux):56
  if (!gst_element_register (plugin, "rtpasfdepay", GST_RANK_MARGINAL,
          GST_TYPE_RTP_ASF_DEPAY)) {
    return FALSE;
gstasfmux.c (gst-plugins-bad-0.10.23\gst\asfmux):2427
  return gst_element_register (plugin, "asfmux",
      GST_RANK_PRIMARY, GST_TYPE_ASF_MUX);
}
gstasfparse.c (gst-plugins-bad-0.10.23\gst\asfmux):575
  return gst_element_register (plugin, "asfparse",
      GST_RANK_NONE, GST_TYPE_ASF_PARSE);
}
gstassrender.c (gst-plugins-bad-0.10.23\ext\assrender):1420
  return gst_element_register (plugin, "assrender",
      GST_RANK_PRIMARY, GST_TYPE_ASS_RENDER);
}
gstasteriskh263.c (gst-plugins-good-0.10.31\gst\rtp):233
  return gst_element_register (plugin, "asteriskh263",
      GST_RANK_SECONDARY, GST_TYPE_ASTERISK_H263);
}
gstaudiorate.c (gst-plugins-base-0.10.36\gst\audiorate):869
  return gst_element_register (plugin, "audiorate", GST_RANK_NONE,
      GST_TYPE_AUDIO_RATE);
}
gstaudioresample.c (gst-plugins-base-0.10.36\gst\audioresample):1589
  if (!gst_element_register (plugin, "audioresample", GST_RANK_PRIMARY,
          GST_TYPE_AUDIO_RESAMPLE)) {
    return FALSE;
gstaudiotestsrc.c (gst-plugins-base-0.10.36\gst\audiotestsrc):1348
  return gst_element_register (plugin, "audiotestsrc",
      GST_RANK_NONE, GST_TYPE_AUDIO_TEST_SRC);
}
gstauparse.c (gst-plugins-good-0.10.31\gst\auparse):810
  if (!gst_element_register (plugin, "auparse", GST_RANK_SECONDARY,
          GST_TYPE_AU_PARSE)) {
    return FALSE;
gstautodetect.c (gst-plugins-good-0.10.31\gst\autodetect):40
  return gst_element_register (plugin, "autovideosink",
      GST_RANK_NONE, GST_TYPE_AUTO_VIDEO_SINK) &&
      gst_element_register (plugin, "autovideosrc",
      GST_RANK_NONE, GST_TYPE_AUTO_VIDEO_SRC) &&
      gst_element_register (plugin, "autoaudiosink",
      GST_RANK_NONE, GST_TYPE_AUTO_AUDIO_SINK) &&
      gst_element_register (plugin, "autoaudiosrc",
      GST_RANK_NONE, GST_TYPE_AUTO_AUDIO_SRC);
}
gstavi.c (gst-plugins-good-0.10.31\gst\avi):43
  if (!gst_element_register (plugin, "avidemux", GST_RANK_PRIMARY,
          GST_TYPE_AVI_DEMUX) ||
      !gst_element_register (plugin, "avimux", GST_RANK_PRIMARY,
          GST_TYPE_AVI_MUX) ||
      !gst_element_register (plugin, "avisubtitle", GST_RANK_PRIMARY,
          GST_TYPE_AVI_SUBTITLE)) {
    return FALSE;
gstbayer.c (gst-plugins-bad-0.10.23\gst\bayer):33
  gst_element_register (plugin, "bayer2rgb", GST_RANK_NONE,
      gst_bayer2rgb_get_type ());
  gst_element_register (plugin, "rgb2bayer", GST_RANK_NONE,
      gst_rgb2bayer_get_type ());

gstbulge.c (gst-plugins-bad-0.10.23\gst\geometrictransform):220
  return gst_element_register (plugin, "bulge", GST_RANK_NONE, GST_TYPE_BULGE);
}
gstburn.c (gst-plugins-bad-0.10.23\gst\gaudieffects):285
  return gst_element_register (burn, "burn", GST_RANK_NONE, GST_TYPE_BURN);
}

gstbz2.c (gst-plugins-bad-0.10.23\ext\bz2):33
  if (!gst_element_register (p, "bz2enc", GST_RANK_NONE, GST_TYPE_BZ2ENC))
    return FALSE;
  if (!gst_element_register (p, "bz2dec", GST_RANK_NONE, GST_TYPE_BZ2DEC))
    return FALSE;
  return TRUE;
gstcacasink.c (gst-plugins-good-0.10.31\ext\libcaca):415
  if (!gst_element_register (plugin, "cacasink", GST_RANK_NONE,
          GST_TYPE_CACASINK))
    return FALSE;
gstcairo.c (gst-plugins-good-0.10.31\ext\cairo):41
  gst_element_register (plugin, "cairotextoverlay", GST_RANK_NONE,
      GST_TYPE_CAIRO_TEXT_OVERLAY);
  gst_element_register (plugin, "cairotimeoverlay", GST_RANK_NONE,
      GST_TYPE_CAIRO_TIME_OVERLAY);
#ifdef HAVE_CAIRO_GOBJECT
  gst_element_register (plugin, "cairooverlay", GST_RANK_NONE,
      GST_TYPE_CAIRO_OVERLAY);
#endif
  gst_element_register (plugin, "cairorender", GST_RANK_SECONDARY,
      GST_TYPE_CAIRO_RENDER);

gstcamerabin.c (gst-plugins-bad-0.10.23\gst\camerabin):4335
  return gst_element_register (plugin, "camerabin",
      GST_RANK_NONE, GST_TYPE_CAMERABIN);
}
gstcamerabin2.c (gst-plugins-bad-0.10.23\gst\camerabin2):2428
  return gst_element_register (plugin, "camerabin2", GST_RANK_NONE,
      gst_camera_bin2_get_type ());
}
gstcdaudio.c (gst-plugins-bad-0.10.23\ext\cdaudio):574
  if (!gst_element_register (plugin, "cdaudio", GST_RANK_NONE,
          GST_TYPE_CDAUDIO))
    return FALSE;
gstcdio.c (gst-plugins-ugly-0.10.19\ext\cdio):108
  if (!gst_element_register (plugin, "cdiocddasrc", GST_RANK_SECONDARY - 1,
          GST_TYPE_CDIO_CDDA_SRC))
    return FALSE;
gstcdparanoiasrc.c (gst-plugins-base-0.10.36\ext\cdparanoia):521
  if (!gst_element_register (plugin, "cdparanoiasrc", GST_RANK_SECONDARY,
          GST_TYPE_CD_PARANOIA_SRC))
    return FALSE;
gstcdxaparse.c (gst-plugins-bad-0.10.23\gst\cdxaparse):564
  if (!gst_element_register (plugin, "cdxaparse", GST_RANK_PRIMARY,
          GST_TYPE_CDXA_PARSE))
    return FALSE;
  if (!gst_element_register (plugin, "vcdparse", GST_RANK_PRIMARY,
          GST_TYPE_VCD_PARSE))
    return FALSE;
gstcelt.c (gst-plugins-bad-0.10.23\ext\celt):33
  if (!gst_element_register (plugin, "celtenc", GST_RANK_NONE,
          GST_TYPE_CELT_ENC))
    return FALSE;
gstcelt.c (gst-plugins-bad-0.10.23\ext\celt):37
  if (!gst_element_register (plugin, "celtdec", GST_RANK_PRIMARY,
          GST_TYPE_CELT_DEC))
    return FALSE;
gstchromium.c (gst-plugins-bad-0.10.23\gst\gaudieffects):317
  return gst_element_register (chromium, "chromium", GST_RANK_NONE,
      GST_TYPE_CHROMIUM);
}
gstcircle.c (gst-plugins-bad-0.10.23\gst\geometrictransform):242
  return gst_element_register (plugin, "circle", GST_RANK_NONE,
      GST_TYPE_CIRCLE);
}
gstcmmldec.c (gst-plugins-good-0.10.31\ext\annodex):700
  if (!gst_element_register (plugin, "cmmldec", GST_RANK_PRIMARY,
          GST_TYPE_CMML_DEC))
    return FALSE;
gstcmmlenc.c (gst-plugins-good-0.10.31\ext\annodex):623
  if (!gst_element_register (plugin, "cmmlenc", GST_RANK_NONE,
          GST_TYPE_CMML_ENC))
    return FALSE;
gstcog.c (gst-plugins-bad-0.10.23\ext\cog):49
  gst_element_register (plugin, "cogdownsample", GST_RANK_NONE,
      gst_cogdownsample_get_type ());
  gst_element_register (plugin, "cogcolorspace", GST_RANK_NONE,
      gst_cogcolorspace_get_type ());
  gst_element_register (plugin, "cogscale", GST_RANK_NONE,
      gst_cog_scale_get_type ());
  gst_element_register (plugin, "cogcolorconvert", GST_RANK_NONE,
      gst_colorconvert_get_type ());
  gst_element_register (plugin, "coglogoinsert", GST_RANK_NONE,
      gst_logoinsert_get_type ());
  gst_element_register (plugin, "cogmse", GST_RANK_NONE, gst_mse_get_type ());

  return TRUE;
gstcolorspace.c (gst-plugins-bad-0.10.23\gst\colorspace):591
  return gst_element_register (plugin, "colorspace",
      GST_RANK_NONE, GST_TYPE_CSP);
}
gstcurl.c (gst-plugins-bad-0.10.23\ext\curl):29
  if (!gst_element_register (plugin, "curlsink", GST_RANK_NONE,
          GST_TYPE_CURL_SINK))
    return FALSE;
gstcutter.c (gst-plugins-good-0.10.31\gst\cutter):455
  if (!gst_element_register (plugin, "cutter", GST_RANK_NONE, GST_TYPE_CUTTER))
    return FALSE;

gstcvdilate.c (gst-plugins-bad-0.10.23\ext\opencv):128
  return gst_element_register (plugin, "cvdilate", GST_RANK_NONE,
      GST_TYPE_CV_DILATE);
}
gstcvequalizehist.c (gst-plugins-bad-0.10.23\ext\opencv):121
  return gst_element_register (plugin, "cvequalizehist", GST_RANK_NONE,
      GST_TYPE_CV_EQUALIZE_HIST);
}
gstcverode.c (gst-plugins-bad-0.10.23\ext\opencv):128
  return gst_element_register (plugin, "cverode", GST_RANK_NONE,
      GST_TYPE_CV_ERODE);
}
gstcvlaplace.c (gst-plugins-bad-0.10.23\ext\opencv):297
  return gst_element_register (plugin, "cvlaplace", GST_RANK_NONE,
      GST_TYPE_CV_LAPLACE);
}
gstcvsmooth.c (gst-plugins-bad-0.10.23\ext\opencv):343
  return gst_element_register (plugin, "cvsmooth", GST_RANK_NONE,
      GST_TYPE_CV_SMOOTH);
}
gstcvsobel.c (gst-plugins-bad-0.10.23\ext\opencv):274
  return gst_element_register (plugin, "cvsobel", GST_RANK_NONE,
      GST_TYPE_CV_SOBEL);
}
gstdataurisrc.c (gst-plugins-bad-0.10.23\gst\dataurisrc):474
  return gst_element_register (plugin, "dataurisrc",
      GST_RANK_PRIMARY, GST_TYPE_DATA_URI_SRC);
}
gstdc1394.c (gst-plugins-bad-0.10.23\ext\dc1394):1327
  return gst_element_register (plugin, "dc1394src", GST_RANK_NONE,
      GST_TYPE_DC1394);

gstdccpplugin.c (gst-plugins-bad-0.10.23\gst\dccp):34
  if (!gst_element_register (plugin, "dccpclientsrc", GST_RANK_NONE,
          GST_TYPE_DCCP_CLIENT_SRC))
    return FALSE;
gstdccpplugin.c (gst-plugins-bad-0.10.23\gst\dccp):38
  if (!gst_element_register (plugin, "dccpserversink", GST_RANK_NONE,
          GST_TYPE_DCCP_SERVER_SINK))
    return FALSE;
gstdccpplugin.c (gst-plugins-bad-0.10.23\gst\dccp):42
  if (!gst_element_register (plugin, "dccpclientsink", GST_RANK_NONE,
          GST_TYPE_DCCP_CLIENT_SINK))
    return FALSE;
gstdccpplugin.c (gst-plugins-bad-0.10.23\gst\dccp):46
  if (!gst_element_register (plugin, "dccpserversrc", GST_RANK_NONE,
          GST_TYPE_DCCP_SERVER_SRC))
    return FALSE;
gstdebug.c (gst-plugins-good-0.10.31\gst\debugutils):43
  if (!gst_element_register (plugin, "breakmydata", GST_RANK_NONE,
          gst_break_my_data_get_type ())
      || !gst_element_register (plugin, "capssetter", GST_RANK_NONE,
          gst_caps_setter_get_type ())
      || !gst_element_register (plugin, "rndbuffersize", GST_RANK_NONE,
          gst_rnd_buffer_size_get_type ())
      || !gst_element_register (plugin, "navseek", GST_RANK_NONE,
          gst_navseek_get_type ())
      || !gst_element_register (plugin, "pushfilesrc", GST_RANK_NONE,
          gst_push_file_src_get_type ()) ||
/*    !gst_element_register (plugin, "negotiation", GST_RANK_NONE, gst_gst_negotiation_get_type ()) || */
      !gst_element_register (plugin, "progressreport", GST_RANK_NONE,
          gst_progress_report_get_type ())
      || !gst_element_register (plugin, "taginject", GST_RANK_NONE,
          gst_tag_inject_get_type ())
      || !gst_element_register (plugin, "testsink", GST_RANK_NONE,
          gst_test_get_type ())
      || !gst_element_register (plugin, "capsdebug", GST_RANK_NONE,
          gst_caps_debug_get_type ())
      || !gst_element_register (plugin, "cpureport", GST_RANK_NONE,
          gst_cpu_report_get_type ()))

gstdecodebin.c (gst-plugins-base-0.10.36\gst\playback):2071
  return gst_element_register (plugin, "decodebin", GST_RANK_NONE,
      GST_TYPE_DECODE_BIN);
}
gstdecodebin2.c (gst-plugins-base-0.10.36\gst\playback):4104
  return gst_element_register (plugin, "decodebin2", GST_RANK_NONE,
      GST_TYPE_DECODE_BIN);
}
gstdeinterlace.c (gst-plugins-good-0.10.31\gst\deinterlace):2683
  if (!gst_element_register (plugin, "deinterlace", GST_RANK_NONE,
          GST_TYPE_DEINTERLACE)) {
    return FALSE;
gstdiffuse.c (gst-plugins-bad-0.10.23\gst\geometrictransform):227
  return gst_element_register (plugin, "diffuse", GST_RANK_NONE,
      GST_TYPE_DIFFUSE);
}
gstdilate.c (gst-plugins-bad-0.10.23\gst\gaudieffects):286
  return gst_element_register (dilate, "dilate", GST_RANK_NONE,
      GST_TYPE_DILATE);
}
gstdirectdrawplugin.c (gst-plugins-bad-0.10.23\sys\directdraw):36
  if (!gst_element_register (plugin, "directdrawsink", GST_RANK_SECONDARY,
          GST_TYPE_DIRECTDRAW_SINK))
    return FALSE;
gstdirectsoundplugin.c (gst-plugins-bad-0.10.23\sys\directsound):38
  if (!gst_element_register (plugin, "directsoundsrc", GST_RANK_PRIMARY,
          GST_TYPE_DIRECTSOUND_SRC))
    return FALSE;
gstdirectsoundplugin.c (gst-plugins-good-0.10.31\sys\directsound):38
  if (!gst_element_register (plugin, "directsoundsink", GST_RANK_PRIMARY,
          GST_TYPE_DIRECTSOUND_SINK))
    return FALSE;
gstdivxdec.c (gst-plugins-bad-0.10.23\ext\divx):566
  return gst_element_register (plugin, "divxdec",
      GST_RANK_SECONDARY, GST_TYPE_DIVXDEC);
}
gstdivxenc.c (gst-plugins-bad-0.10.23\ext\divx):533
  return gst_element_register (plugin, "divxenc",
      GST_RANK_NONE, GST_TYPE_DIVXENC);
}
gstdodge.c (gst-plugins-bad-0.10.23\gst\gaudieffects):253
  return gst_element_register (dodge, "dodge", GST_RANK_NONE, GST_TYPE_DODGE);
}

gstdtmfdetect.c (gst-plugins-bad-0.10.23\gst\dtmf):279
  return gst_element_register (plugin, "dtmfdetect",
      GST_RANK_MARGINAL, GST_TYPE_DTMF_DETECT);
}
gstdtmfsrc.c (gst-plugins-bad-0.10.23\gst\dtmf):956
  return gst_element_register (plugin, "dtmfsrc",
      GST_RANK_NONE, GST_TYPE_DTMF_SRC);
}
gstdtsdec.c (gst-plugins-bad-0.10.23\ext\dts):803
  if (!gst_element_register (plugin, "dtsdec", GST_RANK_PRIMARY,
          GST_TYPE_DTSDEC))
    return FALSE;
gstdv.c (gst-plugins-good-0.10.31\ext\dv):33
  if (!gst_element_register (plugin, "dvdemux", GST_RANK_PRIMARY,
          gst_dvdemux_get_type ()))
    return FALSE;
gstdv.c (gst-plugins-good-0.10.31\ext\dv):37
  if (!gst_element_register (plugin, "dvdec", GST_RANK_MARGINAL,
          gst_dvdec_get_type ()))
    return FALSE;
gstdvbsrc.c (gst-plugins-bad-0.10.23\sys\dvb):899
  return gst_element_register (plugin, "dvbsrc", GST_RANK_NONE,
      GST_TYPE_DVBSRC);
}
gstdvbsuboverlay.c (gst-plugins-bad-0.10.23\gst\dvbsuboverlay):1077
  return gst_element_register (plugin, "dvbsuboverlay",
      GST_RANK_PRIMARY, GST_TYPE_DVBSUB_OVERLAY);
}
gstdvddemux.c (gst-plugins-ugly-0.10.19\gst\mpegstream):1282
  return gst_element_register (plugin, "dvddemux",
      GST_RANK_SECONDARY + 1, GST_TYPE_DVD_DEMUX);
}
gstdvdlpcmdec.c (gst-plugins-ugly-0.10.19\gst\dvdlpcmdec):819
  if (!gst_element_register (plugin, "dvdlpcmdec", GST_RANK_PRIMARY,
          GST_TYPE_DVDLPCMDEC)) {
    return FALSE;
gstdvdspu.c (gst-plugins-bad-0.10.23\gst\dvdspu):1175
  return gst_element_register (plugin, "dvdspu",
      GST_RANK_PRIMARY, GST_TYPE_DVD_SPU);
}
gstdvdsubdec.c (gst-plugins-ugly-0.10.19\gst\dvdsub):1137
  if (!gst_element_register (plugin, "dvdsubdec", GST_RANK_NONE,
          GST_TYPE_DVD_SUB_DEC) ||
      !gst_element_register (plugin, "dvdsubparse", GST_RANK_NONE,
          GST_TYPE_DVD_SUB_PARSE)) {
    return FALSE;
gstedgedetect.c (gst-plugins-bad-0.10.23\ext\opencv):328
  return gst_element_register (plugin, "edgedetect", GST_RANK_NONE,
      GST_TYPE_EDGE_DETECT);
}
gsteffectv.c (gst-plugins-good-0.10.31\gst\effectv):70
    if (!gst_element_register (plugin, _elements[i].name,
            GST_RANK_NONE, (_elements[i].type) ()))
      return FALSE;
gstelementfactory.c (gstreamer-0.10.36\gst):209
gst_element_register (GstPlugin * plugin, const gchar * name, guint rank,
    GType type)
{
gstelementfactory.h (gstreamer-0.10.36\gst):171
gboolean                gst_element_register                    (GstPlugin *plugin, const gchar *name,
                                                                 guint rank, GType type);

gstelements.c (gstreamer-0.10.36\...\elements):85
    if (!gst_element_register (plugin, (*my_elements).name, (*my_elements).rank,
            ((*my_elements).type) ()))
      return FALSE;
gstencodebin.c (gst-plugins-base-0.10.36\gst\encoding):2015
  res = gst_element_register (plugin, "encodebin", GST_RANK_NONE,
      GST_TYPE_ENCODE_BIN);

gstesd.c (gst-plugins-good-0.10.31\ext\esd):36
  if (!gst_element_register (plugin, "esdsink", GST_RANK_MARGINAL,
          GST_TYPE_ESDSINK))
    return FALSE;
gstesd.c (gst-plugins-good-0.10.31\ext\esd):41
  if (!gst_element_register (plugin, "esdmon", GST_RANK_NONE, GST_TYPE_ESDMON))
    return FALSE;
#endif
gstexclusion.c (gst-plugins-bad-0.10.23\gst\gaudieffects):285
  return gst_element_register (exclusion, "exclusion", GST_RANK_NONE,
      GST_TYPE_EXCLUSION);
}
gstfaac.c (gst-plugins-bad-0.10.23\ext\faac):759
  return gst_element_register (plugin, "faac", GST_RANK_SECONDARY,
      GST_TYPE_FAAC);
}
gstfaad.c (gst-plugins-bad-0.10.23\ext\faad):870
  return gst_element_register (plugin, "faad", GST_RANK_PRIMARY, GST_TYPE_FAAD);
}

gstfaceblur.c (gst-plugins-bad-0.10.23\ext\opencv):316
  return gst_element_register (plugin, "faceblur", GST_RANK_NONE,
      GST_TYPE_FACE_BLUR);
}
gstfacedetect.c (gst-plugins-bad-0.10.23\ext\opencv):718
  return gst_element_register (plugin, "facedetect", GST_RANK_NONE,
      GST_TYPE_FACE_DETECT);
}
gstfaceoverlay.c (gst-plugins-bad-0.10.23\gst\faceoverlay):480
  return gst_element_register (faceoverlay, "faceoverlay", GST_RANK_NONE,
      GST_TYPE_FACEOVERLAY);
}
gstfbdevsink.c (gst-plugins-bad-0.10.23\sys\fbdev):370
  if (!gst_element_register (plugin, "fbdevsink", GST_RANK_NONE,
          GST_TYPE_FBDEVSINK))
    return FALSE;
gstfestival.c (gst-plugins-bad-0.10.23\gst\festival):539
  if (!gst_element_register (plugin, "festival", GST_RANK_NONE,
          GST_TYPE_FESTIVAL))
    return FALSE;
gstffmpegcolorspace.c (gst-plugins-base-0.10.36\gst\ffmpegcolorspace):509
  return gst_element_register (plugin, "ffmpegcolorspace",
      GST_RANK_NONE, GST_TYPE_FFMPEGCSP);
}
gstfieldanalysis.c (gst-plugins-bad-0.10.23\gst\fieldanalysis):1804
  return gst_element_register (fieldanalysis, "fieldanalysis", GST_RANK_NONE,
      GST_TYPE_FIELDANALYSIS);
}
gstfisheye.c (gst-plugins-bad-0.10.23\gst\geometrictransform):148
  return gst_element_register (plugin, "fisheye", GST_RANK_NONE,
      GST_TYPE_FISHEYE);
}
gstflac.c (gst-plugins-good-0.10.31\ext\flac):41
  if (!gst_element_register (plugin, "flacenc", GST_RANK_PRIMARY,
          GST_TYPE_FLAC_ENC))
    return FALSE;
  if (!gst_element_register (plugin, "flacdec", GST_RANK_PRIMARY,
          GST_TYPE_FLAC_DEC))
    return FALSE;
  if (!gst_element_register (plugin, "flactag", GST_RANK_PRIMARY,
          gst_flac_tag_get_type ()))
    return FALSE;
gstflite.c (gst-plugins-bad-0.10.23\ext\flite):38
  gst_element_register (plugin, "flitetestsrc", GST_RANK_NONE,
      gst_flite_test_src_get_type ());

gstflvdemux.c (gst-plugins-good-0.10.31\gst\flv):3298
  if (!gst_element_register (plugin, "flvdemux", GST_RANK_PRIMARY,
          gst_flv_demux_get_type ()) ||
      !gst_element_register (plugin, "flvmux", GST_RANK_PRIMARY,
          gst_flv_mux_get_type ()))
    return FALSE;
gstflxdec.c (gst-plugins-good-0.10.31\gst\flx):682
  return gst_element_register (plugin, "flxdec",
      GST_RANK_PRIMARY, GST_TYPE_FLXDEC);
}
gstfragmentedplugin.c (gst-plugins-bad-0.10.23\gst\hls):17
  if (!gst_element_register (plugin, "hlsdemux", GST_RANK_PRIMARY,
          GST_TYPE_HLS_DEMUX) || FALSE)
    return FALSE;
gstfreeverb.c (gst-plugins-bad-0.10.23\gst\freeverb):964
  return gst_element_register (plugin, "freeverb",
      GST_RANK_NONE, GST_TYPE_FREEVERB);
}
gstfreeze.c (gst-plugins-bad-0.10.23\gst\freeze):376
  return gst_element_register (plugin, "freeze", GST_RANK_NONE,
      GST_TYPE_FREEZE);
}
gstfrei0rfilter.c (gst-plugins-bad-0.10.23\gst\frei0r):271
  if (gst_element_register (plugin, type_name, GST_RANK_NONE, type))
    ret = GST_FREI0R_PLUGIN_REGISTER_RETURN_OK;

gstfrei0rmixer.c (gst-plugins-bad-0.10.23\gst\frei0r):816
  if (gst_element_register (plugin, type_name, GST_RANK_NONE, type))
    ret = GST_FREI0R_PLUGIN_REGISTER_RETURN_OK;

gstfrei0rsrc.c (gst-plugins-bad-0.10.23\gst\frei0r):434
  if (gst_element_register (plugin, type_name, GST_RANK_NONE, type))
    ret = GST_FREI0R_PLUGIN_REGISTER_RETURN_OK;

gstgaussblur.c (gst-plugins-bad-0.10.23\gst\gaudieffects):407
  return gst_element_register (plugin, "gaussianblur", GST_RANK_NONE,
      GST_TYPE_GAUSS_BLUR);
}
gstgconfelements.c (gst-plugins-good-0.10.31\ext\gconf):41
  if (!gst_element_register (plugin, "gconfvideosink",
          GST_RANK_NONE, GST_TYPE_GCONF_VIDEO_SINK) ||
      !gst_element_register (plugin, "gconfvideosrc",
          GST_RANK_NONE, GST_TYPE_GCONF_VIDEO_SRC) ||
      !gst_element_register (plugin, "gconfaudiosink",
          GST_RANK_NONE, GST_TYPE_GCONF_AUDIO_SINK) ||
      !gst_element_register (plugin, "gconfaudiosrc",
          GST_RANK_NONE, GST_TYPE_GCONF_AUDIO_SRC)) {
    return FALSE;
gstgdkpixbuf.c (gst-plugins-good-0.10.31\ext\gdk_pixbuf):531
  if (!gst_element_register (plugin, "gdkpixbufdec", GST_RANK_SECONDARY,
          GST_TYPE_GDK_PIXBUF))
    return FALSE;
gstgdkpixbuf.c (gst-plugins-good-0.10.31\ext\gdk_pixbuf):540
  if (!gst_element_register (plugin, "gdkpixbufsink", GST_RANK_NONE,
          GST_TYPE_GDK_PIXBUF_SINK))
    return FALSE;
gstgdpdepay.c (gst-plugins-base-0.10.36\gst\gdp):473
  if (!gst_element_register (plugin, "gdpdepay", GST_RANK_NONE,
          GST_TYPE_GDP_DEPAY))
    return FALSE;
gstgdppay.c (gst-plugins-base-0.10.36\gst\gdp):894
  if (!gst_element_register (plugin, "gdppay", GST_RANK_NONE, GST_TYPE_GDP_PAY))
    return FALSE;

gstgio.c (gst-plugins-base-0.10.36\ext\gio):242
  ret &= gst_element_register (plugin, "giosink", GST_RANK_SECONDARY,
      GST_TYPE_GIO_SINK);

  ret &= gst_element_register (plugin, "giosrc", GST_RANK_SECONDARY,
      GST_TYPE_GIO_SRC);

  ret &= gst_element_register (plugin, "giostreamsink", GST_RANK_NONE,
      GST_TYPE_GIO_STREAM_SINK);

  ret &= gst_element_register (plugin, "giostreamsrc", GST_RANK_NONE,
      GST_TYPE_GIO_STREAM_SRC);

gstgme.c (gst-plugins-bad-0.10.23\ext\gme):548
  return gst_element_register (plugin, "gmedec", GST_RANK_PRIMARY,
      GST_TYPE_GME_DEC);
}
gstgnomevfs.c (gst-plugins-base-0.10.36\ext\gnomevfs):120
  if (!gst_element_register (plugin, "gnomevfssrc", GST_RANK_MARGINAL,
          gst_gnome_vfs_src_get_type ()))
    return FALSE;
gstgnomevfs.c (gst-plugins-base-0.10.36\ext\gnomevfs):124
  if (!gst_element_register (plugin, "gnomevfssink", GST_RANK_MARGINAL,
          gst_gnome_vfs_sink_get_type ()))
    return FALSE;
gstgoom.c (gst-plugins-good-0.10.31\gst\goom):669
  return gst_element_register (plugin, "goom", GST_RANK_NONE, GST_TYPE_GOOM);
}

gstgoom.c (gst-plugins-good-0.10.31\gst\goom2k1):654
  return gst_element_register (plugin, "goom2k1", GST_RANK_NONE, GST_TYPE_GOOM);
}

gstgsm.c (gst-plugins-bad-0.10.23\ext\gsm):32
  if (!gst_element_register (plugin, "gsmenc", GST_RANK_PRIMARY,
          GST_TYPE_GSMENC))
    return FALSE;
  if (!gst_element_register (plugin, "gsmdec", GST_RANK_PRIMARY,
          GST_TYPE_GSMDEC))
    return FALSE;
gsth264parse.c (gst-plugins-bad-0.10.23\gst\h264parse):2735
  return gst_element_register (plugin, "legacyh264parse",
      GST_RANK_NONE, GST_TYPE_H264PARSE);
}
gsthalelements.c (gst-plugins-good-0.10.31\ext\hal):40
  if (!gst_element_register (plugin, "halaudiosink",
          GST_RANK_NONE, GST_TYPE_HAL_AUDIO_SINK) ||
      !gst_element_register (plugin, "halaudiosrc",
          GST_RANK_NONE, GST_TYPE_HAL_AUDIO_SRC)) {
    return FALSE;
gsthdvparse.c (gst-plugins-bad-0.10.23\gst\hdvparse):877
  return gst_element_register (HDVParse, "hdvparse", GST_RANK_NONE,
      GST_TYPE_HDVPARSE);
}
gsticydemux.c (gst-plugins-good-0.10.31\gst\icydemux):643
  return gst_element_register (plugin, "icydemux",
      GST_RANK_PRIMARY, GST_TYPE_ICYDEMUX);
}
gstid3demux.c (gst-plugins-good-0.10.31\gst\id3demux):279
  return gst_element_register (plugin, "id3demux",
      GST_RANK_PRIMARY, GST_TYPE_ID3DEMUX);
}
gstid3mux.c (gst-plugins-bad-0.10.23\gst\id3tag):224
  if (!gst_element_register (plugin, "id3mux", GST_RANK_PRIMARY,
          GST_TYPE_ID3_MUX))
    return FALSE;
gstiirequalizer.c (gst-plugins-good-0.10.31\gst\equalizer):923
  if (!(gst_element_register (plugin, "equalizer-nbands", GST_RANK_NONE,
              GST_TYPE_IIR_EQUALIZER_NBANDS)))
    return FALSE;
gstiirequalizer.c (gst-plugins-good-0.10.31\gst\equalizer):927
  if (!(gst_element_register (plugin, "equalizer-3bands", GST_RANK_NONE,
              GST_TYPE_IIR_EQUALIZER_3BANDS)))
    return FALSE;
gstiirequalizer.c (gst-plugins-good-0.10.31\gst\equalizer):931
  if (!(gst_element_register (plugin, "equalizer-10bands", GST_RANK_NONE,
              GST_TYPE_IIR_EQUALIZER_10BANDS)))
    return FALSE;
gstimagefreeze.c (gst-plugins-good-0.10.31\gst\imagefreeze):916
  if (!gst_element_register (plugin, "imagefreeze", GST_RANK_NONE,
          GST_TYPE_IMAGE_FREEZE))
    return FALSE;
gstinter.c (gst-plugins-bad-0.10.23\gst\inter):33
  gst_element_register (plugin, "interaudiosrc", GST_RANK_NONE,
      GST_TYPE_INTER_AUDIO_SRC);
  gst_element_register (plugin, "interaudiosink", GST_RANK_NONE,
      GST_TYPE_INTER_AUDIO_SINK);
  gst_element_register (plugin, "intervideosrc", GST_RANK_NONE,
      GST_TYPE_INTER_VIDEO_SRC);
  gst_element_register (plugin, "intervideosink", GST_RANK_NONE,
      GST_TYPE_INTER_VIDEO_SINK);

gstinterlace.c (gst-plugins-bad-0.10.23\gst\interlace):868
  return gst_element_register (plugin, "interlace", GST_RANK_NONE,
      GST_TYPE_INTERLACE);
}
gstivfparse.c (gst-plugins-bad-0.10.23\gst\ivfparse):286
  if (!gst_element_register (ivfparse, "ivfparse", GST_RANK_PRIMARY,
          GST_TYPE_IVF_PARSE))
    return FALSE;
gstivorbisdec.c (gst-plugins-base-0.10.36\ext\vorbis):33
  if (!gst_element_register (plugin, "ivorbisdec", GST_RANK_SECONDARY,
          gst_vorbis_dec_get_type ()))
    return FALSE;
gstjack.c (gst-plugins-good-0.10.31\ext\jack):83
  if (!gst_element_register (plugin, "jackaudiosrc", GST_RANK_PRIMARY,
          GST_TYPE_JACK_AUDIO_SRC))
    return FALSE;
  if (!gst_element_register (plugin, "jackaudiosink", GST_RANK_PRIMARY,
          GST_TYPE_JACK_AUDIO_SINK))
    return FALSE;
gstjp2k.c (gst-plugins-bad-0.10.23\ext\jp2k):35
  if (!gst_element_register (plugin, "jp2kdec", GST_RANK_MARGINAL,
          GST_TYPE_JASPER_DEC))
    return FALSE;
gstjp2k.c (gst-plugins-bad-0.10.23\ext\jp2k):39
  if (!gst_element_register (plugin, "jp2kenc", GST_RANK_MARGINAL,
          GST_TYPE_JASPER_ENC))
    return FALSE;
gstjp2kdecimator.c (gst-plugins-bad-0.10.23\gst\jp2kdecimator):377
  gst_element_register (plugin, "jp2kdecimator", GST_RANK_NONE,
      gst_jp2k_decimator_get_type ());

gstjpeg.c (gst-plugins-good-0.10.31\ext\jpeg):54
  if (!gst_element_register (plugin, "jpegenc", GST_RANK_PRIMARY,
          GST_TYPE_JPEGENC))
    return FALSE;
gstjpeg.c (gst-plugins-good-0.10.31\ext\jpeg):58
  if (!gst_element_register (plugin, "jpegdec", GST_RANK_PRIMARY,
          GST_TYPE_JPEG_DEC))
    return FALSE;
gstjpeg.c (gst-plugins-good-0.10.31\ext\jpeg):62
  if (!gst_element_register (plugin, "smokeenc", GST_RANK_PRIMARY,
          GST_TYPE_SMOKEENC))
    return FALSE;
gstjpeg.c (gst-plugins-good-0.10.31\ext\jpeg):66
  if (!gst_element_register (plugin, "smokedec", GST_RANK_PRIMARY,
          GST_TYPE_SMOKEDEC))
    return FALSE;
gstjpegformat.c (gst-plugins-bad-0.10.23\gst\jpegformat):33
  if (!gst_element_register (plugin, "jpegparse", GST_RANK_NONE,
          GST_TYPE_JPEG_PARSE))
    return FALSE;
  if (!gst_element_register (plugin, "jifmux", GST_RANK_SECONDARY,
          GST_TYPE_JIF_MUX))
    return FALSE;
gstkaleidoscope.c (gst-plugins-bad-0.10.23\gst\geometrictransform):252
  return gst_element_register (plugin, "kaleidoscope", GST_RANK_NONE,
      GST_TYPE_KALEIDOSCOPE);
}
gstkate.c (gst-plugins-bad-0.10.23\ext\kate):86
  if (!gst_element_register (plugin, "katedec", GST_RANK_PRIMARY,
          GST_TYPE_KATE_DEC))
    return FALSE;
gstkate.c (gst-plugins-bad-0.10.23\ext\kate):90
  if (!gst_element_register (plugin, "kateenc", GST_RANK_NONE,
          GST_TYPE_KATE_ENC))
    return FALSE;
gstkate.c (gst-plugins-bad-0.10.23\ext\kate):94
  if (!gst_element_register (plugin, "kateparse", GST_RANK_NONE,
          GST_TYPE_KATE_PARSE))
    return FALSE;
gstkate.c (gst-plugins-bad-0.10.23\ext\kate):98
  if (!gst_element_register (plugin, "katetag", GST_RANK_NONE,
          GST_TYPE_KATE_TAG))
    return FALSE;
gstkate.c (gst-plugins-bad-0.10.23\ext\kate):103
  if (!gst_element_register (plugin, "tiger", GST_RANK_PRIMARY,
          GST_TYPE_KATE_TIGER))
    return FALSE;
gstksvideosrc.c (gst-plugins-bad-0.10.23\sys\winks):1140
  return gst_element_register (plugin, "ksvideosrc",
      GST_RANK_NONE, GST_TYPE_KS_VIDEO_SRC);
}
gstladspa.c (gst-plugins-bad-0.10.23\ext\ladspa):711
    if (!gst_element_register (ladspa_plugin, type_name, GST_RANK_NONE, type))
      goto next;

gstlame.c (gst-plugins-ugly-0.10.19\ext\lame):1454
  if (!gst_element_register (plugin, "lame", GST_RANK_MARGINAL, GST_TYPE_LAME))
    return FALSE;

gstlamemp3enc.c (gst-plugins-ugly-0.10.19\ext\lame):914
  if (!gst_element_register (plugin, "lamemp3enc", GST_RANK_PRIMARY,
          GST_TYPE_LAMEMP3ENC))
    return FALSE;
gstlegacyresample.c (gst-plugins-bad-0.10.23\gst\legacyresample):866
  if (!gst_element_register (plugin, "legacyresample", GST_RANK_MARGINAL,
          GST_TYPE_LEGACYRESAMPLE)) {
    return FALSE;
gstlevel.c (gst-plugins-good-0.10.31\gst\level):720
  return gst_element_register (plugin, "level", GST_RANK_NONE, GST_TYPE_LEVEL);
}

gstlinsys.c (gst-plugins-bad-0.10.23\sys\linsys):35
  gst_element_register (plugin, "linsyssdisrc", GST_RANK_NONE,
      gst_linsys_sdi_src_get_type ());
  gst_element_register (plugin, "linsyssdisink", GST_RANK_NONE,
      gst_linsys_sdi_sink_get_type ());

gstlv2.c (gst-plugins-bad-0.10.23\ext\lv2):852
    if (!gst_element_register (gst_lv2_plugin, type_name, GST_RANK_NONE, type))
      goto next;

gstmad.c (gst-plugins-ugly-0.10.19\ext\mad):1878
  return gst_element_register (plugin, "mad", GST_RANK_SECONDARY,
      gst_mad_get_type ());
}
gstmarble.c (gst-plugins-bad-0.10.23\gst\geometrictransform):285
  return gst_element_register (plugin, "marble", GST_RANK_NONE,
      GST_TYPE_MARBLE);
}
gstmimic.c (gst-plugins-bad-0.10.23\ext\mimic):33
  if (!gst_element_register (plugin, "mimenc", GST_RANK_NONE,
          GST_TYPE_MIM_ENC) ||
      !gst_element_register (plugin, "mimdec", GST_RANK_NONE, GST_TYPE_MIM_DEC)
      )
    return FALSE;
gstmirror.c (gst-plugins-bad-0.10.23\gst\geometrictransform):223
  return gst_element_register (plugin, "mirror", GST_RANK_NONE,
      GST_TYPE_MIRROR);
}
gstmms.c (gst-plugins-bad-0.10.23\ext\libmms):542
  return gst_element_register (plugin, "mmssrc", GST_RANK_NONE, GST_TYPE_MMS);
}

gstmonoscope.c (gst-plugins-good-0.10.31\gst\monoscope):545
  return gst_element_register (plugin, "monoscope",
      GST_RANK_NONE, GST_TYPE_MONOSCOPE);
}
gstmotioncells.c (gst-plugins-bad-0.10.23\ext\opencv):1094
  return gst_element_register (plugin, "motioncells", GST_RANK_NONE,
      GST_TYPE_MOTIONCELLS);
}
gstmpeg2dec.c (gst-plugins-ugly-0.10.19\ext\mpeg2dec):1816
  if (!gst_element_register (plugin, "mpeg2dec", GST_RANK_PRIMARY,
          GST_TYPE_MPEG2DEC))
    return FALSE;
gstmpegdemux.c (gst-plugins-bad-0.10.23\gst\mpegdemux):3010
  if (!gst_element_register (plugin, "mpegpsdemux",
          GST_RANK_PRIMARY, GST_TYPE_FLUPS_DEMUX))
    return FALSE;
gstmpegdemux.c (gst-plugins-ugly-0.10.19\gst\mpegstream):1456
  return gst_element_register (plugin, "mpegdemux",
      GST_RANK_SECONDARY, GST_TYPE_MPEG_DEMUX);
}
gstmpegparse.c (gst-plugins-ugly-0.10.19\gst\mpegstream):1359
  return gst_element_register (plugin, "mpegparse",
      GST_RANK_NONE, GST_TYPE_MPEG_PARSE);
}
gstmpegtsdemux.c (gst-plugins-bad-0.10.23\gst\mpegdemux):3549
  if (!gst_element_register (plugin, "mpegtsdemux",
          GST_RANK_PRIMARY, GST_TYPE_MPEGTS_DEMUX))
    return FALSE;
gstmultifile.c (gst-plugins-good-0.10.31\gst\multifile):38
  gst_element_register (plugin, "multifilesrc", GST_RANK_NONE,
      gst_multi_file_src_get_type ());
  gst_element_register (plugin, "multifilesink", GST_RANK_NONE,
      gst_multi_file_sink_get_type ());
  gst_element_register (plugin, "splitfilesrc", GST_RANK_NONE,
      gst_split_file_src_get_type ());

gstmusepackdec.c (gst-plugins-bad-0.10.23\ext\musepack):658
  return gst_element_register (plugin, "musepackdec",
      GST_RANK_PRIMARY, GST_TYPE_MUSEPACK_DEC);
}
gstmve.c (gst-plugins-bad-0.10.23\gst\mve):35
  return gst_element_register (plugin, "mvedemux", GST_RANK_PRIMARY,
      GST_TYPE_MVE_DEMUX)
      && gst_element_register (plugin, "mvemux", GST_RANK_PRIMARY,
      GST_TYPE_MVE_MUX);
}
gstmythtvsrc.c (gst-plugins-bad-0.10.23\ext\mythtv):955
  return gst_element_register (plugin, "mythtvsrc", GST_RANK_NONE,
      GST_TYPE_MYTHTV_SRC);
}
gstnavigationtest.c (gst-plugins-good-0.10.31\gst\debugutils):344
  return gst_element_register (plugin, "navigationtest", GST_RANK_NONE,
      GST_TYPE_NAVIGATIONTEST);
}
gstneonhttpsrc.c (gst-plugins-bad-0.10.23\ext\neon):1180
  return gst_element_register (plugin, "neonhttpsrc", GST_RANK_NONE,
      GST_TYPE_NEONHTTP_SRC);
}
gstnsf.c (gst-plugins-bad-0.10.23\gst\nsf):635
  return gst_element_register (plugin, "nsfdec", GST_RANK_PRIMARY,
      GST_TYPE_NSFDEC);
}
gstnuvdemux.c (gst-plugins-bad-0.10.23\gst\nuvdemux):933
  if (!gst_element_register (plugin, "nuvdemux", GST_RANK_SECONDARY,
          GST_TYPE_NUV_DEMUX)) {
    return FALSE;
gstofa.c (gst-plugins-bad-0.10.23\ext\ofa):265
  ret = gst_element_register (plugin, "ofa", GST_RANK_NONE, GST_TYPE_OFA);

  if (ret) {
gstoggaviparse.c (gst-plugins-base-0.10.36\ext\ogg):474
  return gst_element_register (plugin, "oggaviparse", GST_RANK_PRIMARY,
      GST_TYPE_OGG_AVI_PARSE);
}
gstoggdemux.c (gst-plugins-base-0.10.36\ext\ogg):4649
  return gst_element_register (plugin, "oggdemux", GST_RANK_PRIMARY,
      GST_TYPE_OGG_DEMUX);
}
gstoggmux.c (gst-plugins-base-0.10.36\ext\ogg):2095
  return gst_element_register (plugin, "oggmux", GST_RANK_PRIMARY,
      GST_TYPE_OGG_MUX);
}
gstoggparse.c (gst-plugins-base-0.10.36\ext\ogg):756
  return gst_element_register (plugin, "oggparse", GST_RANK_NONE,
      GST_TYPE_OGG_PARSE);
}
gstogmparse.c (gst-plugins-base-0.10.36\ext\ogg):959
  return gst_element_register (plugin, "ogmaudioparse", GST_RANK_PRIMARY,
      GST_TYPE_OGM_AUDIO_PARSE) &&
      gst_element_register (plugin, "ogmvideoparse", GST_RANK_PRIMARY,
      GST_TYPE_OGM_VIDEO_PARSE) &&
      gst_element_register (plugin, "ogmtextparse", GST_RANK_PRIMARY,
      GST_TYPE_OGM_TEXT_PARSE);
}
gstopenal.c (gst-plugins-bad-0.10.23\ext\openal):36
  if (!gst_element_register (plugin, "openalsink", GST_RANK_SECONDARY,
          GST_TYPE_OPENAL_SINK) ||
      !gst_element_register (plugin, "openalsrc", GST_RANK_SECONDARY,
          GST_TYPE_OPENAL_SRC))
    return FALSE;
gstopus.c (gst-plugins-bad-0.10.23\ext\opus):37
  if (!gst_element_register (plugin, "opusenc", GST_RANK_NONE,
          GST_TYPE_OPUS_ENC))
    return FALSE;
gstopus.c (gst-plugins-bad-0.10.23\ext\opus):41
  if (!gst_element_register (plugin, "opusdec", GST_RANK_PRIMARY,
          GST_TYPE_OPUS_DEC))
    return FALSE;
gstopus.c (gst-plugins-bad-0.10.23\ext\opus):45
  if (!gst_element_register (plugin, "opusparse", GST_RANK_NONE,
          GST_TYPE_OPUS_PARSE))
    return FALSE;
gstopus.c (gst-plugins-bad-0.10.23\ext\opus):49
  if (!gst_element_register (plugin, "rtpopusdepay", GST_RANK_NONE,
          GST_TYPE_RTP_OPUS_DEPAY))
    return FALSE;
gstopus.c (gst-plugins-bad-0.10.23\ext\opus):53
  if (!gst_element_register (plugin, "rtpopuspay", GST_RANK_NONE,
          GST_TYPE_RTP_OPUS_PAY))
    return FALSE;
gstossaudio.c (gst-plugins-good-0.10.31\sys\oss):36
  if (!gst_element_register (plugin, "ossmixer", GST_RANK_NONE,
          GST_TYPE_OSS_MIXER_ELEMENT) ||
      !gst_element_register (plugin, "osssrc", GST_RANK_SECONDARY,
          GST_TYPE_OSS_SRC) ||
      !gst_element_register (plugin, "osssink", GST_RANK_SECONDARY,
          GST_TYPE_OSSSINK)) {
    return FALSE;
gstosxaudio.c (gst-plugins-good-0.10.31\sys\osxaudio):37
  if (!gst_element_register (plugin, "osxaudiosink", GST_RANK_PRIMARY,
          GST_TYPE_OSX_AUDIO_SINK)) {
    return FALSE;
gstosxaudio.c (gst-plugins-good-0.10.31\sys\osxaudio):41
  if (!gst_element_register (plugin, "osxaudiosrc", GST_RANK_PRIMARY,
          GST_TYPE_OSX_AUDIO_SRC)) {
    return FALSE;
gstpatchdetect.c (gst-plugins-bad-0.10.23\gst\patchdetect):1225
  gst_element_register (plugin, "patchdetect", GST_RANK_NONE,
      gst_patchdetect_get_type ());

gstpinch.c (gst-plugins-bad-0.10.23\gst\geometrictransform):220
  return gst_element_register (plugin, "pinch", GST_RANK_NONE, GST_TYPE_PINCH);
}
gstplaybin.c (gst-plugins-base-0.10.36\gst\playback):1988
  return gst_element_register (plugin, "playbin", GST_RANK_NONE,
      GST_TYPE_PLAY_BIN);
}
gstplaybin2.c (gst-plugins-base-0.10.36\gst\playback):4025
  return gst_element_register (plugin, "playbin2", GST_RANK_NONE,
      GST_TYPE_PLAY_BIN);
}
gstplaysink.c (gst-plugins-base-0.10.36\gst\playback):3753
  return gst_element_register (plugin, "playsink", GST_RANK_NONE,
      GST_TYPE_PLAY_SINK);
}
gstplugin.c (gst-plugins-bad-0.10.23\gst\coloreffects):47
    if (!gst_element_register (plugin, _elements[i].name,
            GST_RANK_NONE, (_elements[i].type) ()))
      return FALSE;
gstpng.c (gst-plugins-good-0.10.31\ext\libpng):32
  if (!gst_element_register (plugin, "pngdec", GST_RANK_PRIMARY,
          GST_TYPE_PNGDEC))
    return FALSE;
gstpng.c (gst-plugins-good-0.10.31\ext\libpng):36
  if (!gst_element_register (plugin, "pngenc", GST_RANK_PRIMARY,
          GST_TYPE_PNGENC))
    return FALSE;
gstpnm.c (gst-plugins-bad-0.10.23\gst\pnm):33
  if (!gst_element_register (plugin, "pnmdec", GST_RANK_PRIMARY,
          GST_TYPE_PNMDEC))
    return FALSE;
  if (!gst_element_register (plugin, "pnmenc", GST_RANK_PRIMARY,
          GST_TYPE_PNMENC))
    return FALSE;
gstpreset.c (gstreamer-0.10.36\...\gst):146
  gst_element_register (plugin, GST_PRESET_TEST_NAME, GST_RANK_NONE,
      GST_TYPE_PRESET_TEST);
  return TRUE;
gstpvr.c (gst-plugins-bad-0.10.23\sys\pvr2d):35
  return gst_element_register (plugin, "pvrvideosink", GST_RANK_PRIMARY,
      GST_TYPE_PVRVIDEOSINK);
}
gstpyramidsegment.c (gst-plugins-bad-0.10.23\ext\opencv):330
  return gst_element_register (plugin, "pyramidsegment", GST_RANK_NONE,
      GST_TYPE_PYRAMID_SEGMENT);
}
gstqtmoovrecover.c (gst-plugins-good-0.10.31\gst\isomp4):393
  return gst_element_register (plugin, "qtmoovrecover", GST_RANK_NONE,
      GST_TYPE_QT_MOOV_RECOVER);
}
gstqtmux.c (gst-plugins-good-0.10.31\gst\isomp4):3607
    if (!gst_element_register (plugin, prop->name, prop->rank, type))
      return FALSE;

gstreal.c (gst-plugins-bad-0.10.23\gst\real):32
  if (!gst_element_register (p, "realvideodec", GST_RANK_MARGINAL,
          GST_TYPE_REAL_VIDEO_DEC))
    return FALSE;
  if (!gst_element_register (p, "realaudiodec", GST_RANK_MARGINAL,
          GST_TYPE_REAL_AUDIO_DEC))
    return FALSE;
gstremovesilence.c (gst-plugins-bad-0.10.23\gst\removesilence):253
  return gst_element_register (plugin, "removesilence", GST_RANK_NONE,
      gst_remove_silence_get_type ());
}
gstrfbsrc.c (gst-plugins-bad-0.10.23\gst\librfb):543
  return gst_element_register (plugin, "rfbsrc", GST_RANK_NONE,
      GST_TYPE_RFB_SRC);
}
gstrotate.c (gst-plugins-bad-0.10.23\gst\geometrictransform):224
  return gst_element_register (plugin, "rotate", GST_RANK_NONE,
      GST_TYPE_ROTATE);
}
gstrsvg.c (gst-plugins-bad-0.10.23\ext\rsvg):34
  return (gst_element_register (plugin, "rsvgoverlay",
          GST_RANK_NONE, GST_TYPE_RSVG_OVERLAY)
      &&
      gst_element_register (plugin, "rsvgdec", GST_RANK_PRIMARY,
          GST_TYPE_RSVG_DEC));
}
gstrtmp.c (gst-plugins-bad-0.10.23\ext\rtmp):42
  ret = gst_element_register (plugin, "rtmpsrc", GST_RANK_PRIMARY,
      GST_TYPE_RTMP_SRC);
  ret &= gst_element_register (plugin, "rtmpsink", GST_RANK_PRIMARY,
      GST_TYPE_RTMP_SINK);

gstrtpac3depay.c (gst-plugins-good-0.10.31\gst\rtp):217
  return gst_element_register (plugin, "rtpac3depay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_AC3_DEPAY);
}
gstrtpac3pay.c (gst-plugins-good-0.10.31\gst\rtp):450
  return gst_element_register (plugin, "rtpac3pay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_AC3_PAY);
}
gstrtpamrdepay.c (gst-plugins-good-0.10.31\gst\rtp):456
  return gst_element_register (plugin, "rtpamrdepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_AMR_DEPAY);
}
gstrtpamrpay.c (gst-plugins-good-0.10.31\gst\rtp):437
  return gst_element_register (plugin, "rtpamrpay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_AMR_PAY);
}
gstrtpasfpay.c (gst-plugins-bad-0.10.23\gst\asfmux):468
  return gst_element_register (plugin, "rtpasfpay",
      GST_RANK_NONE, GST_TYPE_RTP_ASF_PAY);
}
gstrtpbvdepay.c (gst-plugins-good-0.10.31\gst\rtp):179
  return gst_element_register (plugin, "rtpbvdepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_BV_DEPAY);
}
gstrtpbvpay.c (gst-plugins-good-0.10.31\gst\rtp):219
  return gst_element_register (plugin, "rtpbvpay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_BV_PAY);
}
gstrtpceltdepay.c (gst-plugins-good-0.10.31\gst\rtp):273
  return gst_element_register (plugin, "rtpceltdepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_CELT_DEPAY);
}
gstrtpceltpay.c (gst-plugins-good-0.10.31\gst\rtp):475
  return gst_element_register (plugin, "rtpceltpay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_CELT_PAY);
}
gstrtpdepay.c (gst-plugins-good-0.10.31\gst\rtp):160
  return gst_element_register (plugin, "rtpdepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_DEPAY);
}
gstrtpdtmfdepay.c (gst-plugins-bad-0.10.23\gst\dtmf):537
  return gst_element_register (plugin, "rtpdtmfdepay",
      GST_RANK_MARGINAL, GST_TYPE_RTP_DTMF_DEPAY);
}
gstrtpdtmfmux.c (gst-plugins-bad-0.10.23\gst\rtpmux):231
  return gst_element_register (plugin, "rtpdtmfmux", GST_RANK_NONE,
      GST_TYPE_RTP_DTMF_MUX);
}
gstrtpdtmfsrc.c (gst-plugins-bad-0.10.23\gst\dtmf):1150
  return gst_element_register (plugin, "rtpdtmfsrc",
      GST_RANK_NONE, GST_TYPE_RTP_DTMF_SRC);
}
gstrtpdvdepay.c (gst-plugins-good-0.10.31\gst\rtp):411
  return gst_element_register (plugin, "rtpdvdepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_DV_DEPAY);
}
gstrtpdvpay.c (gst-plugins-good-0.10.31\gst\rtp):373
  return gst_element_register (plugin, "rtpdvpay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_DV_PAY);
}
gstrtpg722depay.c (gst-plugins-good-0.10.31\gst\rtp):258
  return gst_element_register (plugin, "rtpg722depay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_G722_DEPAY);
}
gstrtpg722pay.c (gst-plugins-good-0.10.31\gst\rtp):206
  return gst_element_register (plugin, "rtpg722pay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_G722_PAY);
}
gstrtpg723depay.c (gst-plugins-good-0.10.31\gst\rtp):226
  return gst_element_register (plugin, "rtpg723depay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_G723_DEPAY);
}
gstrtpg723pay.c (gst-plugins-good-0.10.31\gst\rtp):314
  return gst_element_register (plugin, "rtpg723pay", GST_RANK_SECONDARY,
      gst_rtp_g723_pay_get_type ());
}
gstrtpg726depay.c (gst-plugins-good-0.10.31\gst\rtp):388
  return gst_element_register (plugin, "rtpg726depay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_G726_DEPAY);
}
gstrtpg726pay.c (gst-plugins-good-0.10.31\gst\rtp):417
  return gst_element_register (plugin, "rtpg726pay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_G726_PAY);
}
gstrtpg729depay.c (gst-plugins-good-0.10.31\gst\rtp):225
  return gst_element_register (plugin, "rtpg729depay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_G729_DEPAY);
}
gstrtpg729pay.c (gst-plugins-good-0.10.31\gst\rtp):401
  return gst_element_register (plugin, "rtpg729pay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_G729_PAY);
}
gstrtpgsmdepay.c (gst-plugins-good-0.10.31\gst\rtp):150
  return gst_element_register (plugin, "rtpgsmdepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_GSM_DEPAY);
}
gstrtpgsmpay.c (gst-plugins-good-0.10.31\gst\rtp):181
  return gst_element_register (plugin, "rtpgsmpay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_GSM_PAY);
}
gstrtpgstdepay.c (gst-plugins-good-0.10.31\gst\rtp):357
  return gst_element_register (plugin, "rtpgstdepay",
      GST_RANK_MARGINAL, GST_TYPE_RTP_GST_DEPAY);
}
gstrtpgstpay.c (gst-plugins-good-0.10.31\gst\rtp):222
  return gst_element_register (plugin, "rtpgstpay",
      GST_RANK_NONE, GST_TYPE_RTP_GST_PAY);
}
gstrtph263depay.c (gst-plugins-good-0.10.31\gst\rtp):379
  return gst_element_register (plugin, "rtph263depay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_H263_DEPAY);
}
gstrtph263pay.c (gst-plugins-good-0.10.31\gst\rtp):1798
  return gst_element_register (plugin, "rtph263pay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_H263_PAY);
}
gstrtph263pdepay.c (gst-plugins-good-0.10.31\gst\rtp):397
  return gst_element_register (plugin, "rtph263pdepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_H263P_DEPAY);
}
gstrtph263ppay.c (gst-plugins-good-0.10.31\gst\rtp):751
  return gst_element_register (plugin, "rtph263ppay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_H263P_PAY);
}
gstrtph264depay.c (gst-plugins-good-0.10.31\gst\rtp):965
  return gst_element_register (plugin, "rtph264depay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_H264_DEPAY);
}
gstrtph264pay.c (gst-plugins-good-0.10.31\gst\rtp):1396
  return gst_element_register (plugin, "rtph264pay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_H264_PAY);
}
gstrtpilbcdepay.c (gst-plugins-good-0.10.31\gst\rtp):234
  return gst_element_register (plugin, "rtpilbcdepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_ILBC_DEPAY);
}
gstrtpilbcpay.c (gst-plugins-good-0.10.31\gst\rtp):214
  return gst_element_register (plugin, "rtpilbcpay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_ILBC_PAY);
}
gstrtpj2kdepay.c (gst-plugins-good-0.10.31\gst\rtp):672
  return gst_element_register (plugin, "rtpj2kdepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_J2K_DEPAY);
}
gstrtpj2kpay.c (gst-plugins-good-0.10.31\gst\rtp):581
  return gst_element_register (plugin, "rtpj2kpay", GST_RANK_SECONDARY,
      GST_TYPE_RTP_J2K_PAY);
}
gstrtpjpegdepay.c (gst-plugins-good-0.10.31\gst\rtp):757
  return gst_element_register (plugin, "rtpjpegdepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_JPEG_DEPAY);
}
gstrtpjpegpay.c (gst-plugins-good-0.10.31\gst\rtp):932
  return gst_element_register (plugin, "rtpjpegpay", GST_RANK_SECONDARY,
      GST_TYPE_RTP_JPEG_PAY);
}
gstrtpL16depay.c (gst-plugins-good-0.10.31\gst\rtp):263
  return gst_element_register (plugin, "rtpL16depay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_L16_DEPAY);
}
gstrtpL16pay.c (gst-plugins-good-0.10.31\gst\rtp):236
  return gst_element_register (plugin, "rtpL16pay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_L16_PAY);
}
gstrtpmanager.c (gst-plugins-good-0.10.31\gst\rtpmanager):33
  if (!gst_element_register (plugin, "gstrtpbin", GST_RANK_NONE,
          GST_TYPE_RTP_BIN))
    return FALSE;
gstrtpmanager.c (gst-plugins-good-0.10.31\gst\rtpmanager):37
  if (!gst_element_register (plugin, "gstrtpjitterbuffer", GST_RANK_NONE,
          GST_TYPE_RTP_JITTER_BUFFER))
    return FALSE;
gstrtpmanager.c (gst-plugins-good-0.10.31\gst\rtpmanager):41
  if (!gst_element_register (plugin, "gstrtpptdemux", GST_RANK_NONE,
          GST_TYPE_RTP_PT_DEMUX))
    return FALSE;
gstrtpmanager.c (gst-plugins-good-0.10.31\gst\rtpmanager):45
  if (!gst_element_register (plugin, "gstrtpsession", GST_RANK_NONE,
          GST_TYPE_RTP_SESSION))
    return FALSE;
gstrtpmanager.c (gst-plugins-good-0.10.31\gst\rtpmanager):49
  if (!gst_element_register (plugin, "gstrtpssrcdemux", GST_RANK_NONE,
          GST_TYPE_RTP_SSRC_DEMUX))
    return FALSE;
gstrtpmp1sdepay.c (gst-plugins-good-0.10.31\gst\rtp):144
  return gst_element_register (plugin, "rtpmp1sdepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_MP1S_DEPAY);
}
gstrtpmp2tdepay.c (gst-plugins-good-0.10.31\gst\rtp):226
  return gst_element_register (plugin, "rtpmp2tdepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_MP2T_DEPAY);
}
gstrtpmp2tpay.c (gst-plugins-good-0.10.31\gst\rtp):206
  return gst_element_register (plugin, "rtpmp2tpay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_MP2T_PAY);
}
gstrtpmp4adepay.c (gst-plugins-good-0.10.31\gst\rtp):432
  return gst_element_register (plugin, "rtpmp4adepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_MP4A_DEPAY);
}
gstrtpmp4apay.c (gst-plugins-good-0.10.31\gst\rtp):435
  return gst_element_register (plugin, "rtpmp4apay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_MP4A_PAY);
}
gstrtpmp4gdepay.c (gst-plugins-good-0.10.31\gst\rtp):773
  return gst_element_register (plugin, "rtpmp4gdepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_MP4G_DEPAY);
}
gstrtpmp4gpay.c (gst-plugins-good-0.10.31\gst\rtp):629
  return gst_element_register (plugin, "rtpmp4gpay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_MP4G_PAY);
}
gstrtpmp4vdepay.c (gst-plugins-good-0.10.31\gst\rtp):229
  return gst_element_register (plugin, "rtpmp4vdepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_MP4V_DEPAY);
}
gstrtpmp4vpay.c (gst-plugins-good-0.10.31\gst\rtp):674
  return gst_element_register (plugin, "rtpmp4vpay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_MP4V_PAY);
}
gstrtpmpadepay.c (gst-plugins-good-0.10.31\gst\rtp):178
  return gst_element_register (plugin, "rtpmpadepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_MPA_DEPAY);
}
gstrtpmpapay.c (gst-plugins-good-0.10.31\gst\rtp):325
  return gst_element_register (plugin, "rtpmpapay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_MPA_PAY);
}
gstrtpmparobustdepay.c (gst-plugins-good-0.10.31\gst\rtp):790
  return gst_element_register (plugin, "rtpmparobustdepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_MPA_ROBUST_DEPAY);
}
gstrtpmpvdepay.c (gst-plugins-good-0.10.31\gst\rtp):202
  return gst_element_register (plugin, "rtpmpvdepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_MPV_DEPAY);
}
gstrtpmpvpay.c (gst-plugins-good-0.10.31\gst\rtp):308
  return gst_element_register (plugin, "rtpmpvpay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_MPV_PAY);
}
gstrtpmux.c (gst-plugins-bad-0.10.23\gst\rtpmux):880
  return gst_element_register (plugin, "rtpmux", GST_RANK_NONE,
      GST_TYPE_RTP_MUX);
}
gstrtppcmadepay.c (gst-plugins-good-0.10.31\gst\rtp):162
  return gst_element_register (plugin, "rtppcmadepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_PCMA_DEPAY);
}
gstrtppcmapay.c (gst-plugins-good-0.10.31\gst\rtp):116
  return gst_element_register (plugin, "rtppcmapay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_PCMA_PAY);
}
gstrtppcmudepay.c (gst-plugins-good-0.10.31\gst\rtp):163
  return gst_element_register (plugin, "rtppcmudepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_PCMU_DEPAY);
}
gstrtppcmupay.c (gst-plugins-good-0.10.31\gst\rtp):116
  return gst_element_register (plugin, "rtppcmupay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_PCMU_PAY);
}
gstrtpqcelpdepay.c (gst-plugins-good-0.10.31\gst\rtp):430
  return gst_element_register (plugin, "rtpqcelpdepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_QCELP_DEPAY);
}
gstrtpqdmdepay.c (gst-plugins-good-0.10.31\gst\rtp):417
  return gst_element_register (plugin, "rtpqdm2depay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_QDM2_DEPAY);
}
gstrtpsirendepay.c (gst-plugins-good-0.10.31\gst\rtp):122
  return gst_element_register (plugin, "rtpsirendepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_SIREN_DEPAY);
}
gstrtpsirenpay.c (gst-plugins-good-0.10.31\gst\rtp):150
  return gst_element_register (plugin, "rtpsirenpay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_SIREN_PAY);
}
gstrtpspeexdepay.c (gst-plugins-good-0.10.31\gst\rtp):224
  return gst_element_register (plugin, "rtpspeexdepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_SPEEX_DEPAY);
}
gstrtpspeexpay.c (gst-plugins-good-0.10.31\gst\rtp):339
  return gst_element_register (plugin, "rtpspeexpay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_SPEEX_PAY);
}
gstrtpsv3vdepay.c (gst-plugins-good-0.10.31\gst\rtp):322
  return gst_element_register (plugin, "rtpsv3vdepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_SV3V_DEPAY);
}
gstrtptheoradepay.c (gst-plugins-good-0.10.31\gst\rtp):645
  return gst_element_register (plugin, "rtptheoradepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_THEORA_DEPAY);
}
gstrtptheorapay.c (gst-plugins-good-0.10.31\gst\rtp):855
  return gst_element_register (plugin, "rtptheorapay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_THEORA_PAY);
}
gstrtpvorbisdepay.c (gst-plugins-good-0.10.31\gst\rtp):698
  return gst_element_register (plugin, "rtpvorbisdepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_VORBIS_DEPAY);
}
gstrtpvorbispay.c (gst-plugins-good-0.10.31\gst\rtp):692
  return gst_element_register (plugin, "rtpvorbispay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_VORBIS_PAY);
}
gstrtpvp8depay.c (gst-plugins-bad-0.10.23\gst\rtpvp8):204
  return gst_element_register (plugin, "rtpvp8depay",
      GST_RANK_MARGINAL, GST_TYPE_RTP_VP8_DEPAY);
}
gstrtpvp8pay.c (gst-plugins-bad-0.10.23\gst\rtpvp8):435
  return gst_element_register (plugin, "rtpvp8pay",
      GST_RANK_MARGINAL, GST_TYPE_RTP_VP8_PAY);
}
gstrtpvrawdepay.c (gst-plugins-good-0.10.31\gst\rtp):625
  return gst_element_register (plugin, "rtpvrawdepay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_VRAW_DEPAY);
}
gstrtpvrawpay.c (gst-plugins-good-0.10.31\gst\rtp):637
  return gst_element_register (plugin, "rtpvrawpay",
      GST_RANK_SECONDARY, GST_TYPE_RTP_VRAW_PAY);
}
gstrtsp.c (gst-plugins-good-0.10.31\gst\rtsp):62
  if (!gst_element_register (plugin, "rtspsrc", GST_RANK_NONE,
          GST_TYPE_RTSPSRC))
    return FALSE;
  if (!gst_element_register (plugin, "rtpdec", GST_RANK_NONE, GST_TYPE_RTP_DEC))
    return FALSE;

gstscaletempoplugin.c (gst-plugins-bad-0.10.23\gst\scaletempo):62
  return gst_element_register (plugin, "scaletempo", GST_RANK_NONE,
      GST_TYPE_SCALETEMPO);
}
gstschro.c (gst-plugins-bad-0.10.23\ext\schroedinger):39
  gst_element_register (plugin, "schrodec", GST_RANK_PRIMARY,
      gst_schro_dec_get_type ());
  gst_element_register (plugin, "schroenc", GST_RANK_PRIMARY,
      gst_schro_enc_get_type ());

gstsdi.c (gst-plugins-bad-0.10.23\gst\sdi):32
  gst_element_register (plugin, "sdidemux", GST_RANK_NONE,
      gst_sdi_demux_get_type ());
  gst_element_register (plugin, "sdimux", GST_RANK_NONE,
      gst_sdi_mux_get_type ());

gstsdl.c (gst-plugins-bad-0.10.23\ext\sdl):29
  if (!gst_element_register (plugin, "sdlvideosink", GST_RANK_NONE,
          GST_TYPE_SDLVIDEOSINK) ||
      !gst_element_register (plugin, "sdlaudiosink", GST_RANK_NONE,
          GST_TYPE_SDLAUDIOSINK)) {
    return FALSE;
gstsdpelem.c (gst-plugins-bad-0.10.23\gst\sdp):29
  if (!gst_element_register (plugin, "sdpdemux", GST_RANK_SECONDARY,
          GST_TYPE_SDP_DEMUX))
    return FALSE;
gstsf.c (gst-plugins-bad-0.10.23\ext\sndfile):115
  if (!gst_element_register (plugin, "sfsink", GST_RANK_NONE,
          gst_sf_sink_get_type ()))
    return FALSE;
gstsf.c (gst-plugins-bad-0.10.23\ext\sndfile):119
  if (!gst_element_register (plugin, "sfsrc", GST_RANK_NONE,
          gst_sf_src_get_type ()))
    return FALSE;
gstshapewipe.c (gst-plugins-good-0.10.31\gst\shapewipe):1151
  if (!gst_element_register (plugin, "shapewipe", GST_RANK_NONE,
          GST_TYPE_SHAPE_WIPE))
    return FALSE;
gstshm.c (gst-plugins-bad-0.10.23\sys\shm):32
  return gst_element_register (plugin, "shmsrc",
      GST_RANK_NONE, GST_TYPE_SHM_SRC) &&
      gst_element_register (plugin, "shmsink",
      GST_RANK_NONE, GST_TYPE_SHM_SINK);
}
gstshout2.c (gst-plugins-good-0.10.31\ext\shout2):843
  return gst_element_register (plugin, "shout2send", GST_RANK_NONE,
      GST_TYPE_SHOUT2SEND);
}
gstsirendec.c (gst-plugins-bad-0.10.23\gst\siren):352
  return gst_element_register (plugin, "sirendec",
      GST_RANK_MARGINAL, GST_TYPE_SIREN_DEC);
}
gstsirenenc.c (gst-plugins-bad-0.10.23\gst\siren):355
  return gst_element_register (plugin, "sirenenc",
      GST_RANK_MARGINAL, GST_TYPE_SIREN_ENC);
}
gstsmooth.c (gst-plugins-bad-0.10.23\gst\smooth):285
  return gst_element_register (plugin, "smooth",
      GST_RANK_NONE, GST_TYPE_SMOOTH);
}
gstsmpte.c (gst-plugins-good-0.10.31\gst\smpte):654
  return gst_element_register (plugin, "smpte", GST_RANK_NONE, GST_TYPE_SMPTE);
}
gstsmptealpha.c (gst-plugins-good-0.10.31\gst\smpte):751
  return gst_element_register (plugin, "smptealpha", GST_RANK_NONE,
      GST_TYPE_SMPTE_ALPHA);
}
gstsolarize.c (gst-plugins-bad-0.10.23\gst\gaudieffects):316
  return gst_element_register (solarize, "solarize", GST_RANK_NONE,
      GST_TYPE_SOLARIZE);
}
gstsoup.c (gst-plugins-good-0.10.31\ext\soup):35
  gst_element_register (plugin, "souphttpsrc", GST_RANK_PRIMARY,
      GST_TYPE_SOUP_HTTP_SRC);
  gst_element_register (plugin, "souphttpclientsink", GST_RANK_NONE,
      GST_TYPE_SOUP_HTTP_CLIENT_SINK);

gstspacescope.c (gst-plugins-bad-0.10.23\gst\audiovisualizers):444
  return gst_element_register (plugin, "spacescope", GST_RANK_NONE,
      GST_TYPE_SPACE_SCOPE);
}
gstspandsp.c (gst-plugins-bad-0.10.23\ext\spandsp):32
  return gst_element_register (plugin, "spanplc",
      GST_RANK_PRIMARY, GST_TYPE_SPAN_PLC);
}
gstspc.c (gst-plugins-bad-0.10.23\ext\spc):585
  return gst_element_register (plugin, "spcdec", GST_RANK_SECONDARY,
      GST_TYPE_SPC_DEC);
}
gstspectrascope.c (gst-plugins-bad-0.10.23\gst\audiovisualizers):222
  return gst_element_register (plugin, "spectrascope", GST_RANK_NONE,
      GST_TYPE_SPECTRA_SCOPE);
}
gstspectrum.c (gst-plugins-good-0.10.31\gst\spectrum):1156
  return gst_element_register (plugin, "spectrum", GST_RANK_NONE,
      GST_TYPE_SPECTRUM);
}
gstspeed.c (gst-plugins-bad-0.10.23\gst\speed):765
  return gst_element_register (plugin, "speed", GST_RANK_NONE, GST_TYPE_SPEED);
}

gstspeex.c (gst-plugins-good-0.10.31\ext\speex):32
  if (!gst_element_register (plugin, "speexenc", GST_RANK_PRIMARY,
          GST_TYPE_SPEEX_ENC))
    return FALSE;
gstspeex.c (gst-plugins-good-0.10.31\ext\speex):36
  if (!gst_element_register (plugin, "speexdec", GST_RANK_PRIMARY,
          GST_TYPE_SPEEX_DEC))
    return FALSE;
gstsphere.c (gst-plugins-bad-0.10.23\gst\geometrictransform):231
  return gst_element_register (plugin, "sphere", GST_RANK_NONE,
      GST_TYPE_SPHERE);
}
gstsquare.c (gst-plugins-bad-0.10.23\gst\geometrictransform):237
  return gst_element_register (plugin, "square", GST_RANK_NONE,
      GST_TYPE_SQUARE);
}
gststereo.c (gst-plugins-bad-0.10.23\gst\stereo):222
  return gst_element_register (plugin, "stereo", GST_RANK_NONE,
      GST_TYPE_STEREO);
}
gststretch.c (gst-plugins-bad-0.10.23\gst\geometrictransform):222
  return gst_element_register (plugin, "stretch", GST_RANK_NONE,
      GST_TYPE_STRETCH);
}
gstsubenc.c (gst-plugins-bad-0.10.23\gst\subenc):30
  gst_element_register (plugin, "srtenc", GST_RANK_NONE, GST_TYPE_SRT_ENC);
  gst_element_register (plugin, "webvttenc", GST_RANK_NONE,
      GST_TYPE_WEBVTT_ENC);

gstsubparse.c (gst-plugins-base-0.10.36\gst\subparse):1866
  if (!gst_element_register (plugin, "subparse",
          GST_RANK_PRIMARY, GST_TYPE_SUBPARSE) ||
      !gst_element_register (plugin, "ssaparse",
          GST_RANK_PRIMARY, GST_TYPE_SSA_PARSE)) {
    return FALSE;
gstsubtitleoverlay.c (gst-plugins-base-0.10.36\gst\playback):2296
  return gst_element_register (plugin, "subtitleoverlay", GST_RANK_NONE,
      GST_TYPE_SUBTITLE_OVERLAY);
}
gstsunaudio.c (gst-plugins-good-0.10.31\sys\sunaudio):39
  if (!gst_element_register (plugin, "sunaudiomixer", GST_RANK_NONE,
          GST_TYPE_SUNAUDIO_MIXER) ||
      !gst_element_register (plugin, "sunaudiosink", GST_RANK_SECONDARY,
          GST_TYPE_SUNAUDIO_SINK) ||
      !gst_element_register (plugin, "sunaudiosrc", GST_RANK_SECONDARY,
          GST_TYPE_SUNAUDIO_SRC)) {
    return FALSE;
gstswfdec.c (gst-plugins-bad-0.10.23\ext\swfdec):900
  return gst_element_register (plugin, "swfdec", GST_RANK_PRIMARY,
      GST_TYPE_SWFDEC);
}
gstsynaescope.c (gst-plugins-bad-0.10.23\gst\audiovisualizers):305
  return gst_element_register (plugin, "synaescope", GST_RANK_NONE,
      GST_TYPE_SYNAE_SCOPE);
}
gstsynaesthesia.c (gst-plugins-ugly-0.10.19\gst\synaesthesia):435
  return gst_element_register (plugin, "synaesthesia", GST_RANK_NONE,
      GST_TYPE_SYNAESTHESIA);
}
gsttcpplugin.c (gst-plugins-base-0.10.36\gst\tcp):38
  if (!gst_element_register (plugin, "tcpclientsink", GST_RANK_NONE,
          GST_TYPE_TCP_CLIENT_SINK))
    return FALSE;
  if (!gst_element_register (plugin, "tcpclientsrc", GST_RANK_NONE,
          GST_TYPE_TCP_CLIENT_SRC))
    return FALSE;
  if (!gst_element_register (plugin, "tcpserversink", GST_RANK_NONE,
          GST_TYPE_TCP_SERVER_SINK))
    return FALSE;
  if (!gst_element_register (plugin, "tcpserversrc", GST_RANK_NONE,
          GST_TYPE_TCP_SERVER_SRC))
    return FALSE;
  if (!gst_element_register (plugin, "multifdsink", GST_RANK_NONE,
          GST_TYPE_MULTI_FD_SINK))
    return FALSE;
gsttemplatematch.c (gst-plugins-bad-0.10.23\ext\opencv):426
  return gst_element_register (templatematch, "templatematch", GST_RANK_NONE,
      GST_TYPE_TEMPLATE_MATCH);
}
gsttextoverlay.c (gst-plugins-bad-0.10.23\ext\opencv):409
  return gst_element_register (plugin, "opencvtextoverlay", GST_RANK_NONE,
      GST_TYPE_OPENCV_TEXT_OVERLAY);
}
gsttextoverlay.c (gst-plugins-base-0.10.36\ext\pango):2382
  if (!gst_element_register (plugin, "textoverlay", GST_RANK_NONE,
          GST_TYPE_TEXT_OVERLAY) ||
      !gst_element_register (plugin, "timeoverlay", GST_RANK_NONE,
          GST_TYPE_TIME_OVERLAY) ||
      !gst_element_register (plugin, "clockoverlay", GST_RANK_NONE,
          GST_TYPE_CLOCK_OVERLAY) ||
      !gst_element_register (plugin, "textrender", GST_RANK_NONE,
          GST_TYPE_TEXT_RENDER)) {
    return FALSE;
gsttheora.c (gst-plugins-base-0.10.36\ext\theora):33
  if (!gst_element_register (plugin, "theoradec", GST_RANK_PRIMARY,
          gst_theora_dec_get_type ()))
    return FALSE;
gsttheora.c (gst-plugins-base-0.10.36\ext\theora):37
  if (!gst_element_register (plugin, "theoraenc", GST_RANK_PRIMARY,
          gst_theora_enc_get_type ()))
    return FALSE;
gsttheora.c (gst-plugins-base-0.10.36\ext\theora):41
  if (!gst_element_register (plugin, "theoraparse", GST_RANK_NONE,
          gst_theora_parse_get_type ()))
    return FALSE;
gsttimidity.c (gst-plugins-bad-0.10.23\ext\timidity):797
  return gst_element_register (plugin, "timidity",
      GST_RANK_PRIMARY, GST_TYPE_TIMIDITY);
}
gsttrm.c (gst-plugins-bad-0.10.23\ext\musicbrainz):379
  if (!gst_element_register (plugin, "trm", GST_RANK_NONE, GST_TYPE_TRM))
    return FALSE;

gstttadec.c (gst-plugins-bad-0.10.23\gst\tta):442
  return gst_element_register (plugin, "ttadec",
      GST_RANK_NONE, GST_TYPE_TTA_DEC);
}
gstttaparse.c (gst-plugins-bad-0.10.23\gst\tta):495
  if (!gst_element_register (plugin, "ttaparse",
          GST_RANK_NONE, GST_TYPE_TTA_PARSE)) {
    return FALSE;
gsttunnel.c (gst-plugins-bad-0.10.23\gst\geometrictransform):148
  return gst_element_register (plugin, "tunnel", GST_RANK_NONE,
      GST_TYPE_TUNNEL);
}
gsttwirl.c (gst-plugins-bad-0.10.23\gst\geometrictransform):210
  return gst_element_register (plugin, "twirl", GST_RANK_NONE, GST_TYPE_TWIRL);
}
gsttwolame.c (gst-plugins-ugly-0.10.19\ext\twolame):890
  if (!gst_element_register (plugin, "twolame", GST_RANK_PRIMARY,
          GST_TYPE_TWO_LAME))
    return FALSE;
gstudp.c (gst-plugins-good-0.10.31\gst\udp):43
  if (!gst_element_register (plugin, "udpsink", GST_RANK_NONE,
          GST_TYPE_UDPSINK))
    return FALSE;
gstudp.c (gst-plugins-good-0.10.31\gst\udp):47
  if (!gst_element_register (plugin, "multiudpsink", GST_RANK_NONE,
          GST_TYPE_MULTIUDPSINK))
    return FALSE;
gstudp.c (gst-plugins-good-0.10.31\gst\udp):51
  if (!gst_element_register (plugin, "dynudpsink", GST_RANK_NONE,
          GST_TYPE_DYNUDPSINK))
    return FALSE;
gstudp.c (gst-plugins-good-0.10.31\gst\udp):55
  if (!gst_element_register (plugin, "udpsrc", GST_RANK_NONE, GST_TYPE_UDPSRC))
    return FALSE;

gsturidecodebin.c (gst-plugins-base-0.10.36\gst\playback):2551
  return gst_element_register (plugin, "uridecodebin", GST_RANK_NONE,
      GST_TYPE_URI_DECODE_BIN);
}
gstv4l.c (gst-plugins-base-0.10.36\sys\v4l):44
  if (!gst_element_register (plugin, "v4lsrc", GST_RANK_MARGINAL,
          GST_TYPE_V4LSRC))
/*       !gst_element_register (plugin, "v4ljpegsrc", */
gstv4l2.c (gst-plugins-good-0.10.31\sys\v4l2):56
  if (!gst_element_register (plugin, "v4l2src", GST_RANK_PRIMARY,
          GST_TYPE_V4L2SRC) ||
#ifdef HAVE_EXPERIMENTAL
      !gst_element_register (plugin, "v4l2sink", GST_RANK_NONE,
          GST_TYPE_V4L2SINK) ||
#endif
      !gst_element_register (plugin, "v4l2radio", GST_RANK_NONE,
          GST_TYPE_V4L2RADIO) ||
      /*       !gst_element_register (plugin, "v4l2jpegsrc", */
gstvdpau.c (gst-plugins-bad-0.10.23\sys\vdpau):23
  gst_element_register (vdpau_plugin, "vdpaumpegdec",
      GST_RANK_NONE, GST_TYPE_VDP_MPEG_DEC);
  gst_element_register (vdpau_plugin, "vdpauh264dec",
      GST_RANK_NONE, GST_TYPE_VDP_H264_DEC);
  gst_element_register (vdpau_plugin, "vdpaumpeg4dec",
      GST_RANK_NONE, GST_TYPE_VDP_MPEG4_DEC);
  gst_element_register (vdpau_plugin, "vdpauvideopostprocess",
      GST_RANK_NONE, GST_TYPE_VDP_VIDEO_POST_PROCESS);
  gst_element_register (vdpau_plugin, "vdpausink",
      GST_RANK_NONE, GST_TYPE_VDP_SINK);

gstvideobox.c (gst-plugins-good-0.10.31\gst\videobox):3399
  return gst_element_register (plugin, "videobox", GST_RANK_NONE,
      GST_TYPE_VIDEO_BOX);
}
gstvideocrop.c (gst-plugins-good-0.10.31\gst\videocrop):747
  if (gst_element_register (plugin, "videocrop", GST_RANK_NONE,
          GST_TYPE_VIDEO_CROP)
      && gst_element_register (plugin, "aspectratiocrop", GST_RANK_NONE,
          GST_TYPE_ASPECT_RATIO_CROP))
    return TRUE;
gstvideofiltersbad.c (gst-plugins-bad-0.10.23\gst\videofilters):34
  gst_element_register (plugin, "scenechange", GST_RANK_NONE,
      gst_scene_change_get_type ());
  gst_element_register (plugin, "zebrastripe", GST_RANK_NONE,
      gst_zebra_stripe_get_type ());

gstvideomeasure.c (gst-plugins-bad-0.10.23\gst\videomeasure):59
  res = gst_element_register (plugin, "ssim", GST_RANK_NONE, GST_TYPE_SSIM);

  res &= gst_element_register (plugin, "measurecollector", GST_RANK_NONE,
      GST_TYPE_MEASURE_COLLECTOR);

gstvideorate.c (gst-plugins-base-0.10.36\gst\videorate):1287
  return gst_element_register (plugin, "videorate", GST_RANK_NONE,
      GST_TYPE_VIDEO_RATE);
}
gstvideoscale.c (gst-plugins-base-0.10.36\gst\videoscale):1437
  if (!gst_element_register (plugin, "videoscale", GST_RANK_NONE,
          GST_TYPE_VIDEO_SCALE))
    return FALSE;
gstvideosignal.c (gst-plugins-bad-0.10.23\gst\videosignal):33
  res = gst_element_register (plugin, "videoanalyse", GST_RANK_NONE,
      GST_TYPE_VIDEO_ANALYSE);

  res &= gst_element_register (plugin, "videodetect", GST_RANK_NONE,
      GST_TYPE_VIDEO_DETECT);

  res &= gst_element_register (plugin, "videomark", GST_RANK_NONE,
      GST_TYPE_VIDEO_MARK);

gstvideotemplate.c (gst-plugins-good-0.10.31\gst\videofilter):218
  return gst_element_register (plugin, "videotemplate", GST_RANK_NONE,
      GST_TYPE_VIDEOTEMPLATE);
}
gstvideotestsrc.c (gst-plugins-base-0.10.36\gst\videotestsrc):950
  return gst_element_register (plugin, "videotestsrc", GST_RANK_NONE,
      GST_TYPE_VIDEO_TEST_SRC);
}
gstviewfinderbin.c (gst-plugins-bad-0.10.23\gst\camerabin2):375
  return gst_element_register (plugin, "viewfinderbin", GST_RANK_NONE,
      gst_viewfinder_bin_get_type ());
}
gstvoaac.c (gst-plugins-bad-0.10.23\ext\voaacenc):29
  return gst_element_register (plugin, "voaacenc",
      GST_RANK_SECONDARY, GST_TYPE_VOAACENC);
}
gstvoamrwb.c (gst-plugins-bad-0.10.23\ext\voamrwbenc):29
  return gst_element_register (plugin, "voamrwbenc",
      GST_RANK_SECONDARY, GST_TYPE_VOAMRWBENC);
}
gstvolume.c (gst-plugins-base-0.10.36\gst\volume):1042
  return gst_element_register (plugin, "volume", GST_RANK_NONE,
      GST_TYPE_VOLUME);
}
gstvorbis.c (gst-plugins-base-0.10.36\ext\vorbis):39
  if (!gst_element_register (plugin, "vorbisenc", GST_RANK_PRIMARY,
          GST_TYPE_VORBISENC))
    return FALSE;
gstvorbis.c (gst-plugins-base-0.10.36\ext\vorbis):43
  if (!gst_element_register (plugin, "vorbisdec", GST_RANK_PRIMARY,
          gst_vorbis_dec_get_type ()))
    return FALSE;
gstvorbis.c (gst-plugins-base-0.10.36\ext\vorbis):47
  if (!gst_element_register (plugin, "vorbisparse", GST_RANK_NONE,
          gst_vorbis_parse_get_type ()))
    return FALSE;
gstvorbis.c (gst-plugins-base-0.10.36\ext\vorbis):51
  if (!gst_element_register (plugin, "vorbistag", GST_RANK_NONE,
          gst_vorbis_tag_get_type ()))
    return FALSE;
gstwasapi.c (gst-plugins-bad-0.10.23\sys\wasapi):32
  ret = gst_element_register (plugin, "wasapisrc",
      GST_RANK_NONE, GST_TYPE_WASAPI_SRC);
  if (!ret)
gstwasapi.c (gst-plugins-bad-0.10.23\sys\wasapi):37
  return gst_element_register (plugin, "wasapisink",
      GST_RANK_NONE, GST_TYPE_WASAPI_SINK);
}
gstwaterripple.c (gst-plugins-bad-0.10.23\gst\geometrictransform):250
  return gst_element_register (plugin, "waterripple", GST_RANK_NONE,
      GST_TYPE_WATER_RIPPLE);
}
gstwaveformplugin.c (gst-plugins-good-0.10.31\sys\waveform):31
  if (!gst_element_register (plugin, "waveformsink", GST_RANK_PRIMARY,
          GST_TYPE_WAVEFORM_SINK))
    return FALSE;
gstwavenc.c (gst-plugins-good-0.10.31\gst\wavenc):739
  return gst_element_register (plugin, "wavenc", GST_RANK_PRIMARY,
      GST_TYPE_WAVENC);
}
gstwavescope.c (gst-plugins-bad-0.10.23\gst\audiovisualizers):420
  return gst_element_register (plugin, "wavescope", GST_RANK_NONE,
      GST_TYPE_WAVE_SCOPE);
}
gstwavpackdec.c (gst-plugins-good-0.10.31\ext\wavpack):506
  if (!gst_element_register (plugin, "wavpackdec",
          GST_RANK_PRIMARY, GST_TYPE_WAVPACK_DEC))
    return FALSE;
gstwavpackenc.c (gst-plugins-good-0.10.31\ext\wavpack):1041
  if (!gst_element_register (plugin, "wavpackenc",
          GST_RANK_NONE, GST_TYPE_WAVPACK_ENC))
    return FALSE;
gstwavpackparse.c (gst-plugins-good-0.10.31\ext\wavpack):1335
  if (!gst_element_register (plugin, "wavpackparse",
          GST_RANK_PRIMARY, GST_TYPE_WAVPACK_PARSE)) {
    return FALSE;
gstwavparse.c (gst-plugins-good-0.10.31\gst\wavparse):2665
  return gst_element_register (plugin, "wavparse", GST_RANK_PRIMARY,
      GST_TYPE_WAVPARSE);
}
gstwildmidi.c (gst-plugins-bad-0.10.23\ext\timidity):993
  return gst_element_register (plugin, "wildmidi",
      GST_RANK_SECONDARY, GST_TYPE_WILDMIDI);
}
gstwininetsrc.c (gst-plugins-bad-0.10.23\sys\wininet):442
  return gst_element_register (plugin, "wininetsrc",
      GST_RANK_NONE, GST_TYPE_WIN_INET_SRC);
}
gstwinscreencap.c (gst-plugins-bad-0.10.23\sys\winscreencap):60
  if (!gst_element_register (plugin, "gdiscreencapsrc",
          GST_RANK_NONE, GST_TYPE_GDISCREENCAPSRC)) {
    return FALSE;
gstwinscreencap.c (gst-plugins-bad-0.10.23\sys\winscreencap):65
  if (!gst_element_register (plugin, "dx9screencapsrc",
          GST_RANK_NONE, GST_TYPE_DX9SCREENCAPSRC)) {
    return FALSE;
gstwrappercamerabinsrc.c (gst-plugins-bad-0.10.23\gst\camerabin2):1162
  return gst_element_register (plugin, "wrappercamerabinsrc", GST_RANK_NONE,
      gst_wrapper_camera_bin_src_get_type ());
}
gstx264enc.c (gst-plugins-ugly-0.10.19\ext\ x264):2441
  return gst_element_register (plugin, "x264enc",
      GST_RANK_PRIMARY, GST_TYPE_X264_ENC);
}
gstximagesrc.c (gst-plugins-good-0.10.31\sys\ ximage):1307
  ret = gst_element_register (plugin, "ximagesrc", GST_RANK_NONE,
      GST_TYPE_XIMAGE_SRC);

gstxvid.c (gst-plugins-bad-0.10.23\ext\ xvid):361
  return (gst_element_register (plugin, "xvidenc",
          GST_RANK_SECONDARY, GST_TYPE_XVIDENC) &&
      gst_element_register (plugin, "xviddec",
          GST_RANK_NONE, GST_TYPE_XVIDDEC));
}
gsty4mdec.c (gst-plugins-bad-0.10.23\gst\y4m):727
  gst_element_register (plugin, "y4mdec", GST_RANK_SECONDARY,
      gst_y4m_dec_get_type ());

gsty4mencode.c (gst-plugins-good-0.10.31\gst\y4m):369
  return gst_element_register (plugin, "y4menc", GST_RANK_PRIMARY,
      GST_TYPE_Y4M_ENCODE);
}
gstzbar.c (gst-plugins-bad-0.10.23\ext\zbar):373
  return gst_element_register (plugin, "zbar", GST_RANK_NONE, GST_TYPE_ZBAR);
}

isomp4-plugin.c (gst-plugins-good-0.10.31\gst\isomp4):54
  if (!gst_element_register (plugin, "qtdemux",
          GST_RANK_PRIMARY, GST_TYPE_QTDEMUX))
    return FALSE;
isomp4-plugin.c (gst-plugins-good-0.10.31\gst\isomp4):58
  if (!gst_element_register (plugin, "rtpxqtdepay",
          GST_RANK_MARGINAL, GST_TYPE_RTP_XQT_DEPAY))
    return FALSE;
liveadder.c (gst-plugins-bad-0.10.23\gst\liveadder):1527
  if (!gst_element_register (plugin, "liveadder", GST_RANK_NONE,
          GST_TYPE_LIVE_ADDER)) {
    return FALSE;
matroska-demux.c (gst-plugins-good-0.10.31\gst\matroska):5580
  if (!gst_element_register (plugin, "matroskademux",
          GST_RANK_PRIMARY, GST_TYPE_MATROSKA_DEMUX))
    return FALSE;
matroska-parse.c (gst-plugins-good-0.10.31\gst\matroska):3237
  if (!gst_element_register (plugin, "matroskaparse",
          GST_RANK_NONE, GST_TYPE_MATROSKA_PARSE))
    return FALSE;
matroska.c (gst-plugins-good-0.10.31\gst\matroska):49
  ret &= gst_element_register (plugin, "matroskamux", GST_RANK_PRIMARY,
      GST_TYPE_MATROSKA_MUX);
  ret &= gst_element_register (plugin, "webmmux", GST_RANK_PRIMARY,
      GST_TYPE_WEBM_MUX);

mpegpsmux.c (gst-plugins-bad-0.10.23\gst\mpegpsmux):792
  if (!gst_element_register (plugin, "mpegpsmux", GST_RANK_PRIMARY,
          mpegpsmux_get_type ()))
    return FALSE;
mpegtsmux.c (gst-plugins-bad-0.10.23\gst\mpegtsmux):1340
  if (!gst_element_register (plugin, "mpegtsmux", GST_RANK_PRIMARY,
          mpegtsmux_get_type ()))
    return FALSE;
mpegtsparse.c (gst-plugins-bad-0.10.23\gst\mpegdemux):1469
  return gst_element_register (plugin, "mpegtsparse",
      GST_RANK_NONE, GST_TYPE_MPEGTS_PARSE);
}
mpegtsparse.c (gst-plugins-bad-0.10.23\gst\mpegtsdemux):715
  return gst_element_register (plugin, "tsparse",
      GST_RANK_NONE, GST_TYPE_MPEGTS_PARSE);
}
mpegvideoparse.c (gst-plugins-bad-0.10.23\gst\mpegvideoparse):1032
  return gst_element_register (plugin, "legacympegvideoparse",
      GST_RANK_NONE, GST_TYPE_MPEGVIDEOPARSE);
}
mulaw.c (gst-plugins-good-0.10.31\gst\law):62
  if (!gst_element_register (plugin, "mulawenc",
          GST_RANK_PRIMARY, GST_TYPE_MULAWENC) ||
      !gst_element_register (plugin, "mulawdec",
          GST_RANK_PRIMARY, GST_TYPE_MULAWDEC))
    return FALSE;
multipartdemux.c (gst-plugins-good-0.10.31\gst\multipart):730
  return gst_element_register (plugin, "multipartdemux", GST_RANK_PRIMARY,
      GST_TYPE_MULTIPART_DEMUX);
}
multipartmux.c (gst-plugins-good-0.10.31\gst\multipart):679
  return gst_element_register (plugin, "multipartmux", GST_RANK_NONE,
      GST_TYPE_MULTIPART_MUX);
}
mxf.c (gst-plugins-bad-0.10.23\gst\mxf):72
  if (!gst_element_register (plugin, "mxfdemux", GST_RANK_PRIMARY,
          GST_TYPE_MXF_DEMUX) ||
      !gst_element_register (plugin, "mxfmux", GST_RANK_PRIMARY,
          GST_TYPE_MXF_MUX))
    return FALSE;
nassink.c (gst-plugins-bad-0.10.23\ext\nas):624
  if (!gst_element_register (plugin, "nassink", GST_RANK_NONE,
          GST_TYPE_NAS_SINK)) {
    return FALSE;
oss4-audio.c (gst-plugins-good-0.10.31\sys\oss4):701
  if (!gst_element_register (plugin, "oss4sink", rank, GST_TYPE_OSS4_SINK) ||
      !gst_element_register (plugin, "oss4src", rank, GST_TYPE_OSS4_SOURCE) ||
      !gst_element_register (plugin, "oss4mixer", rank, GST_TYPE_OSS4_MIXER)) {
    return FALSE;
  }
osxvideoplugin.c (gst-plugins-bad-0.10.23\sys\osxvideo):36
  if (!gst_element_register (plugin, "osxvideosrc",
          GST_RANK_PRIMARY, GST_TYPE_OSX_VIDEO_SRC))
    return FALSE;
parse-launch.c (gstreamer-0.10.36\...\pipelines):122
  fail_unless (gst_element_register (NULL, "1dentity", GST_RANK_NONE, type));

  for (s = test_lines; *s != NULL; s++) {
parse-launch.c (gstreamer-0.10.36\...\pipelines):452
  fail_unless (gst_element_register (NULL, "parsetestelement",
          GST_RANK_NONE, GST_TYPE_PARSE_TEST_ELEMENT));

pixbufscale.c (gst-plugins-good-0.10.31\ext\gdk_pixbuf):475
  if (!gst_element_register (plugin, "gdkpixbufscale", GST_RANK_NONE,
          GST_TYPE_PIXBUFSCALE))
    return FALSE;
playbin.c (gst-plugins-base-0.10.36\...\elements):54
  fail_unless (gst_element_register (NULL, "redvideosrc", GST_RANK_PRIMARY,
          gst_red_video_src_get_type ()));

playbin.c (gst-plugins-base-0.10.36\...\elements):107
  fail_unless (gst_element_register (NULL, "redvideosrc", GST_RANK_PRIMARY,
          gst_red_video_src_get_type ()));

playbin.c (gst-plugins-base-0.10.36\...\elements):142
  fail_unless (gst_element_register (NULL, "redvideosrc", GST_RANK_PRIMARY,
          gst_red_video_src_get_type ()));

playbin.c (gst-plugins-base-0.10.36\...\elements):176
  fail_unless (gst_element_register (NULL, "redvideosrc", GST_RANK_PRIMARY,
          gst_red_video_src_get_type ()));

playbin.c (gst-plugins-base-0.10.36\...\elements):347
  fail_unless (gst_element_register (NULL, "codecsrc", GST_RANK_PRIMARY,
          gst_codec_src_get_type ()));

playbin2-compressed.c (gst-plugins-base-0.10.36\...\elements):681
  fail_unless (gst_element_register (NULL, "capssrc", GST_RANK_PRIMARY,
          gst_caps_src_get_type ()));
  fail_unless (gst_element_register (NULL, "audiocodecsink",
          GST_RANK_PRIMARY + 100, gst_audio_codec_sink_get_type ()));
  fail_unless (gst_element_register (NULL, "videocodecsink",
          GST_RANK_PRIMARY + 100, gst_video_codec_sink_get_type ()));

playbin2-compressed.c (gst-plugins-base-0.10.36\...\elements):767
  fail_unless (gst_element_register (NULL, "capssrc", GST_RANK_PRIMARY,
          gst_caps_src_get_type ()));
  fail_unless (gst_element_register (NULL, "audiocodecsink",
          GST_RANK_PRIMARY + 100, gst_audio_codec_sink_get_type ()));
  fail_unless (gst_element_register (NULL, "videocodecsink",
          GST_RANK_PRIMARY + 100, gst_video_codec_sink_get_type ()));

playbin2-compressed.c (gst-plugins-base-0.10.36\...\elements):847
  fail_unless (gst_element_register (NULL, "capssrc", GST_RANK_PRIMARY,
          gst_caps_src_get_type ()));
  fail_unless (gst_element_register (NULL, "codecdemuxer",
          GST_RANK_PRIMARY + 100, gst_codec_demuxer_get_type ()));
  fail_unless (gst_element_register (NULL, "audiocodecsink",
          GST_RANK_PRIMARY + 100, gst_audio_codec_sink_get_type ()));
  fail_unless (gst_element_register (NULL, "videocodecsink",
          GST_RANK_PRIMARY + 100, gst_video_codec_sink_get_type ()));

playbin2-compressed.c (gst-plugins-base-0.10.36\...\elements):930
  fail_unless (gst_element_register (NULL, "capssrc", GST_RANK_PRIMARY,
          gst_caps_src_get_type ()));
  fail_unless (gst_element_register (NULL, "codecdemuxer",
          GST_RANK_PRIMARY + 100, gst_codec_demuxer_get_type ()));
  fail_unless (gst_element_register (NULL, "audiocodecsink",
          GST_RANK_PRIMARY + 100, gst_audio_codec_sink_get_type ()));
  fail_unless (gst_element_register (NULL, "videocodecsink",
          GST_RANK_PRIMARY + 100, gst_video_codec_sink_get_type ()));

playbin2-compressed.c (gst-plugins-base-0.10.36\...\elements):1013
  fail_unless (gst_element_register (NULL, "capssrc", GST_RANK_PRIMARY,
          gst_caps_src_get_type ()));
  fail_unless (gst_element_register (NULL, "audiocodecsink",
          GST_RANK_PRIMARY + 100, gst_audio_codec_sink_get_type ()));
  fail_unless (gst_element_register (NULL, "videocodecsink",
          GST_RANK_PRIMARY + 100, gst_video_codec_sink_get_type ()));

playbin2-compressed.c (gst-plugins-base-0.10.36\...\elements):1099
  fail_unless (gst_element_register (NULL, "capssrc", GST_RANK_PRIMARY,
          gst_caps_src_get_type ()));
  fail_unless (gst_element_register (NULL, "audiocodecsink",
          GST_RANK_PRIMARY + 100, gst_audio_codec_sink_get_type ()));
  fail_unless (gst_element_register (NULL, "videocodecsink",
          GST_RANK_PRIMARY + 100, gst_video_codec_sink_get_type ()));

playbin2-compressed.c (gst-plugins-base-0.10.36\...\elements):1179
  fail_unless (gst_element_register (NULL, "capssrc", GST_RANK_PRIMARY,
          gst_caps_src_get_type ()));
  fail_unless (gst_element_register (NULL, "codecdemuxer",
          GST_RANK_PRIMARY + 100, gst_codec_demuxer_get_type ()));
  fail_unless (gst_element_register (NULL, "audiocodecsink",
          GST_RANK_PRIMARY + 100, gst_audio_codec_sink_get_type ()));
  fail_unless (gst_element_register (NULL, "videocodecsink",
          GST_RANK_PRIMARY + 100, gst_video_codec_sink_get_type ()));

playbin2-compressed.c (gst-plugins-base-0.10.36\...\elements):1262
  fail_unless (gst_element_register (NULL, "capssrc", GST_RANK_PRIMARY,
          gst_caps_src_get_type ()));
  fail_unless (gst_element_register (NULL, "codecdemuxer",
          GST_RANK_PRIMARY + 100, gst_codec_demuxer_get_type ()));
  fail_unless (gst_element_register (NULL, "audiocodecsink",
          GST_RANK_PRIMARY + 100, gst_audio_codec_sink_get_type ()));
  fail_unless (gst_element_register (NULL, "videocodecsink",
          GST_RANK_PRIMARY + 100, gst_video_codec_sink_get_type ()));

playbin2-compressed.c (gst-plugins-base-0.10.36\...\elements):1345
  fail_unless (gst_element_register (NULL, "capssrc", GST_RANK_PRIMARY,
          gst_caps_src_get_type ()));
  fail_unless (gst_element_register (NULL, "codecdemuxer",
          GST_RANK_PRIMARY + 100, gst_codec_demuxer_get_type ()));
  fail_unless (gst_element_register (NULL, "audiocodecsink",
          GST_RANK_PRIMARY + 100, gst_audio_codec_sink_get_type ()));
  fail_unless (gst_element_register (NULL, "videocodecsink",
          GST_RANK_PRIMARY + 100, gst_video_codec_sink_get_type ()));

playbin2-compressed.c (gst-plugins-base-0.10.36\...\elements):1428
  fail_unless (gst_element_register (NULL, "capssrc", GST_RANK_PRIMARY,
          gst_caps_src_get_type ()));
  fail_unless (gst_element_register (NULL, "codecdemuxer",
          GST_RANK_PRIMARY + 100, gst_codec_demuxer_get_type ()));
  fail_unless (gst_element_register (NULL, "audiocodecsink",
          GST_RANK_PRIMARY + 100, gst_audio_codec_sink_get_type ()));
  fail_unless (gst_element_register (NULL, "videocodecsink",
          GST_RANK_PRIMARY + 100, gst_video_codec_sink_get_type ()));

playbin2-compressed.c (gst-plugins-base-0.10.36\...\elements):1512
  fail_unless (gst_element_register (NULL, "capssrc", GST_RANK_PRIMARY,
          gst_caps_src_get_type ()));
  fail_unless (gst_element_register (NULL, "codecdemuxer",
          GST_RANK_PRIMARY + 100, gst_codec_demuxer_get_type ()));
  fail_unless (gst_element_register (NULL, "audiocodecsink",
          GST_RANK_PRIMARY + 100, gst_audio_codec_sink_get_type ()));
  fail_unless (gst_element_register (NULL, "videocodecsink",
          GST_RANK_PRIMARY + 100, gst_video_codec_sink_get_type ()));

playbin2-compressed.c (gst-plugins-base-0.10.36\...\elements):1592
  fail_unless (gst_element_register (NULL, "capssrc", GST_RANK_PRIMARY,
          gst_caps_src_get_type ()));
  fail_unless (gst_element_register (NULL, "codecdemuxer",
          GST_RANK_PRIMARY + 100, gst_codec_demuxer_get_type ()));
  fail_unless (gst_element_register (NULL, "audiocodecsink",
          GST_RANK_PRIMARY + 100, gst_audio_codec_sink_get_type ()));
  fail_unless (gst_element_register (NULL, "videocodecsink",
          GST_RANK_PRIMARY + 100, gst_video_codec_sink_get_type ()));

playbin2-compressed.c (gst-plugins-base-0.10.36\...\elements):1699
  fail_unless (gst_element_register (NULL, "capssrc", GST_RANK_PRIMARY,
          gst_caps_src_get_type ()));
  fail_unless (gst_element_register (NULL, "codecdemuxer",
          GST_RANK_PRIMARY + 100, gst_codec_demuxer_get_type ()));
  fail_unless (gst_element_register (NULL, "audiocodecsink",
          GST_RANK_PRIMARY + 100, gst_audio_codec_sink_get_type ()));
  fail_unless (gst_element_register (NULL, "videocodecsink",
          GST_RANK_PRIMARY + 100, gst_video_codec_sink_get_type ()));

playbin2-compressed.c (gst-plugins-base-0.10.36\...\elements):1794
  fail_unless (gst_element_register (NULL, "capssrc", GST_RANK_PRIMARY,
          gst_caps_src_get_type ()));
  fail_unless (gst_element_register (NULL, "codecdemuxer",
          GST_RANK_PRIMARY + 100, gst_codec_demuxer_get_type ()));
  fail_unless (gst_element_register (NULL, "audiocodecsink",
          GST_RANK_PRIMARY + 100, gst_audio_codec_sink_get_type ()));
  fail_unless (gst_element_register (NULL, "videocodecsink",
          GST_RANK_PRIMARY + 100, gst_video_codec_sink_get_type ()));

playbin2-compressed.c (gst-plugins-base-0.10.36\...\elements):1889
  fail_unless (gst_element_register (NULL, "capssrc", GST_RANK_PRIMARY,
          gst_caps_src_get_type ()));
  fail_unless (gst_element_register (NULL, "codecdemuxer",
          GST_RANK_PRIMARY + 100, gst_codec_demuxer_get_type ()));
  fail_unless (gst_element_register (NULL, "audiocodecsink",
          GST_RANK_PRIMARY + 100, gst_audio_codec_sink_get_type ()));
  fail_unless (gst_element_register (NULL, "videocodecsink",
          GST_RANK_PRIMARY + 100, gst_video_codec_sink_get_type ()));

playbin2-compressed.c (gst-plugins-base-0.10.36\...\elements):1984
  fail_unless (gst_element_register (NULL, "capssrc", GST_RANK_PRIMARY,
          gst_caps_src_get_type ()));
  fail_unless (gst_element_register (NULL, "codecdemuxer",
          GST_RANK_PRIMARY + 100, gst_codec_demuxer_get_type ()));
  fail_unless (gst_element_register (NULL, "audiocodecsink",
          GST_RANK_PRIMARY + 100, gst_audio_codec_sink_get_type ()));
  fail_unless (gst_element_register (NULL, "videocodecsink",
          GST_RANK_PRIMARY + 100, gst_video_codec_sink_get_type ()));

playbin2-compressed.c (gst-plugins-base-0.10.36\...\elements):2098
  fail_unless (gst_element_register (NULL, "capssrc", GST_RANK_PRIMARY,
          gst_caps_src_get_type ()));
  fail_unless (gst_element_register (NULL, "codecdemuxer",
          GST_RANK_PRIMARY + 100, gst_codec_demuxer_get_type ()));
  fail_unless (gst_element_register (NULL, "audiocodecsink",
          GST_RANK_PRIMARY + 100, gst_audio_codec_sink_get_type ()));
  fail_unless (gst_element_register (NULL, "videocodecsink",
          GST_RANK_PRIMARY + 100, gst_video_codec_sink_get_type ()));

playbin2-compressed.c (gst-plugins-base-0.10.36\...\elements):2193
  fail_unless (gst_element_register (NULL, "capssrc", GST_RANK_PRIMARY,
          gst_caps_src_get_type ()));
  fail_unless (gst_element_register (NULL, "codecdemuxer",
          GST_RANK_PRIMARY + 100, gst_codec_demuxer_get_type ()));
  fail_unless (gst_element_register (NULL, "audiocodecsink",
          GST_RANK_PRIMARY + 100, gst_audio_codec_sink_get_type ()));
  fail_unless (gst_element_register (NULL, "videocodecsink",
          GST_RANK_PRIMARY + 100, gst_video_codec_sink_get_type ()));

playbin2-compressed.c (gst-plugins-base-0.10.36\...\elements):2288
  fail_unless (gst_element_register (NULL, "capssrc", GST_RANK_PRIMARY,
          gst_caps_src_get_type ()));
  fail_unless (gst_element_register (NULL, "codecdemuxer",
          GST_RANK_PRIMARY + 100, gst_codec_demuxer_get_type ()));
  fail_unless (gst_element_register (NULL, "audiocodecsink",
          GST_RANK_PRIMARY + 100, gst_audio_codec_sink_get_type ()));
  fail_unless (gst_element_register (NULL, "videocodecsink",
          GST_RANK_PRIMARY + 100, gst_video_codec_sink_get_type ()));

playbin2-compressed.c (gst-plugins-base-0.10.36\...\elements):2383
  fail_unless (gst_element_register (NULL, "capssrc", GST_RANK_PRIMARY,
          gst_caps_src_get_type ()));
  fail_unless (gst_element_register (NULL, "codecdemuxer",
          GST_RANK_PRIMARY + 100, gst_codec_demuxer_get_type ()));
  fail_unless (gst_element_register (NULL, "audiocodecsink",
          GST_RANK_PRIMARY + 100, gst_audio_codec_sink_get_type ()));
  fail_unless (gst_element_register (NULL, "videocodecsink",
          GST_RANK_PRIMARY + 100, gst_video_codec_sink_get_type ()));

playbin2.c (gst-plugins-base-0.10.36\...\elements):43
  fail_unless (gst_element_register (NULL, "redvideosrc", GST_RANK_PRIMARY,
          gst_red_video_src_get_type ()));

playbin2.c (gst-plugins-base-0.10.36\...\elements):103
  fail_unless (gst_element_register (NULL, "redvideosrc", GST_RANK_PRIMARY,
          gst_red_video_src_get_type ()));

playbin2.c (gst-plugins-base-0.10.36\...\elements):137
  fail_unless (gst_element_register (NULL, "redvideosrc", GST_RANK_PRIMARY,
          gst_red_video_src_get_type ()));

playbin2.c (gst-plugins-base-0.10.36\...\elements):170
  fail_unless (gst_element_register (NULL, "redvideosrc", GST_RANK_PRIMARY,
          gst_red_video_src_get_type ()));

playbin2.c (gst-plugins-base-0.10.36\...\elements):352
  fail_unless (gst_element_register (NULL, "codecsrc", GST_RANK_PRIMARY,
          gst_codec_src_get_type ()));

playbin2.c (gst-plugins-base-0.10.36\...\elements):414
  fail_unless (gst_element_register (NULL, "redvideosrc", GST_RANK_PRIMARY,
          gst_red_video_src_get_type ()));

playbin2.c (gst-plugins-base-0.10.36\...\elements):481
    fail_unless (gst_element_register (NULL, "redvideosrc", GST_RANK_PRIMARY,
            gst_red_video_src_get_type ()));
  }
plugin.c (gst-plugins-bad-0.10.23\ext\gsettings):33
  if (!gst_element_register (plugin, "gsettingsaudiosink", GST_RANK_NONE,
          GST_TYPE_GSETTINGS_AUDIO_SINK) ||
      !gst_element_register (plugin, "gsettingsaudiosrc", GST_RANK_NONE,
          GST_TYPE_GSETTINGS_AUDIO_SRC) ||
      !gst_element_register (plugin, "gsettingsvideosink", GST_RANK_NONE,
          GST_TYPE_GSETTINGS_VIDEO_SINK) ||
      !gst_element_register (plugin, "gsettingsvideosrc", GST_RANK_NONE,
          GST_TYPE_GSETTINGS_VIDEO_SRC))
    return FALSE;
plugin.c (gst-plugins-bad-0.10.23\ext\resindvd):48
  result &= gst_element_register (plugin, "rsndvdbin",
      GST_RANK_PRIMARY, RESIN_TYPE_DVDBIN);

plugin.c (gst-plugins-bad-0.10.23\ext\soundtouch):34
  return gst_element_register (plugin, "pitch", GST_RANK_NONE, GST_TYPE_PITCH)
      && gst_element_register (plugin, "bpmdetect", GST_RANK_NONE,
      GST_TYPE_BPM_DETECT);
}
plugin.c (gst-plugins-bad-0.10.23\ext\vp8):35
  gst_element_register (plugin, "vp8dec", GST_RANK_PRIMARY,
      gst_vp8_dec_get_type ());
#endif
plugin.c (gst-plugins-bad-0.10.23\ext\vp8):40
  gst_element_register (plugin, "vp8enc", GST_RANK_PRIMARY,
      gst_vp8_enc_get_type ());
#endif
plugin.c (gst-plugins-bad-0.10.23\gst\autoconvert):33
  ret = gst_element_register (plugin, "autoconvert",
      GST_RANK_NONE, GST_TYPE_AUTO_CONVERT);

  ret &= gst_element_register (plugin, "autovideoconvert",
      GST_RANK_NONE, GST_TYPE_AUTO_VIDEO_CONVERT);

plugin.c (gst-plugins-bad-0.10.23\gst\pcapparse):32
  ret = gst_element_register (plugin, "pcapparse",
      GST_RANK_NONE, GST_TYPE_PCAP_PARSE);
  ret &= gst_element_register (plugin, "irtspparse",
      GST_RANK_NONE, GST_TYPE_IRTSP_PARSE);

plugin.c (gst-plugins-bad-0.10.23\gst\rawparse):14
  ret = gst_element_register (plugin, "videoparse", GST_RANK_NONE,
      gst_video_parse_get_type ());
  ret &= gst_element_register (plugin, "audioparse", GST_RANK_NONE,
      gst_audio_parse_get_type ());

plugin.c (gst-plugins-bad-0.10.23\gst\segmentclip):30
  if (!gst_element_register (plugin, "audiosegmentclip", GST_RANK_NONE,
          GST_TYPE_AUDIO_SEGMENT_CLIP) ||
      !gst_element_register (plugin, "videosegmentclip", GST_RANK_NONE,
          GST_TYPE_VIDEO_SEGMENT_CLIP))
    return FALSE;
plugin.c (gst-plugins-bad-0.10.23\gst\videoparsers):36
  ret |= gst_element_register (plugin, "h263parse",
      GST_RANK_PRIMARY + 1, GST_TYPE_H263_PARSE);
  ret |= gst_element_register (plugin, "h264parse",
      GST_RANK_PRIMARY + 1, GST_TYPE_H264_PARSE);
  ret |= gst_element_register (plugin, "diracparse",
      GST_RANK_NONE, GST_TYPE_DIRAC_PARSE);
  ret |= gst_element_register (plugin, "mpegvideoparse",
      GST_RANK_PRIMARY + 1, GST_TYPE_MPEGVIDEO_PARSE);
  ret |= gst_element_register (plugin, "mpeg4videoparse",
      GST_RANK_PRIMARY + 1, GST_TYPE_MPEG4VIDEO_PARSE);

plugin.c (gst-plugins-base-0.10.36\gst\audioconvert):40
  if (!gst_element_register (plugin, "audioconvert",
          GST_RANK_PRIMARY, gst_audio_convert_get_type ()))
    return FALSE;
plugin.c (gst-plugins-good-0.10.31\ext\pulse):44
  if (!gst_element_register (plugin, "pulsesink", GST_RANK_PRIMARY + 10,
          GST_TYPE_PULSESINK))
    return FALSE;
plugin.c (gst-plugins-good-0.10.31\ext\pulse):48
  if (!gst_element_register (plugin, "pulsesrc", GST_RANK_PRIMARY + 10,
          GST_TYPE_PULSESRC))
    return FALSE;
plugin.c (gst-plugins-good-0.10.31\ext\pulse):53
  if (!gst_element_register (plugin, "pulseaudiosink", GST_RANK_MARGINAL - 1,
          GST_TYPE_PULSE_AUDIO_SINK))
    return FALSE;
plugin.c (gst-plugins-good-0.10.31\ext\pulse):58
  if (!gst_element_register (plugin, "pulsemixer", GST_RANK_NONE,
          GST_TYPE_PULSEMIXER))
    return FALSE;
plugin.c (gst-plugins-good-0.10.31\gst\audioparsers):36
  ret = gst_element_register (plugin, "aacparse",
      GST_RANK_PRIMARY + 1, GST_TYPE_AAC_PARSE);
  ret &= gst_element_register (plugin, "amrparse",
      GST_RANK_PRIMARY + 1, GST_TYPE_AMR_PARSE);
  ret &= gst_element_register (plugin, "ac3parse",
      GST_RANK_PRIMARY + 1, GST_TYPE_AC3_PARSE);
  ret &= gst_element_register (plugin, "dcaparse",
      GST_RANK_PRIMARY + 1, GST_TYPE_DCA_PARSE);
  ret &= gst_element_register (plugin, "flacparse",
      GST_RANK_PRIMARY + 1, GST_TYPE_FLAC_PARSE);
  ret &= gst_element_register (plugin, "mpegaudioparse",
      GST_RANK_PRIMARY + 2, GST_TYPE_MPEG_AUDIO_PARSE);

plugin.c (gst-plugins-good-0.10.31\gst\interleave):31
  if (!gst_element_register (plugin, "interleave",
          GST_RANK_NONE, gst_interleave_get_type ()) ||
      !gst_element_register (plugin, "deinterleave",
          GST_RANK_NONE, gst_deinterleave_get_type ()))
    return FALSE;
plugin.c (gst-plugins-good-0.10.31\gst\videofilter):36
  return (gst_element_register (plugin, "gamma", GST_RANK_NONE, GST_TYPE_GAMMA)
      && gst_element_register (plugin, "videobalance", GST_RANK_NONE,
          GST_TYPE_VIDEO_BALANCE)
      && gst_element_register (plugin, "videoflip", GST_RANK_NONE,
          GST_TYPE_VIDEO_FLIP));
}
plugin.c (gst-plugins-ugly-0.10.19\gst\mpegaudioparse):31
  if (!gst_element_register (plugin, "xingmux", GST_RANK_NONE,
          GST_TYPE_XING_MUX))
    return FALSE;
  if (!gst_element_register (plugin, "mp3parse", GST_RANK_PRIMARY + 1,
          GST_TYPE_MP3PARSE))
    return FALSE;
pnmsrc.c (gst-plugins-ugly-0.10.19\gst\realmedia):133
  return gst_element_register (plugin, "pnmsrc",
      GST_RANK_MARGINAL, GST_TYPE_PNM_SRC);
}
qtmux.c (gst-plugins-good-0.10.31\...\elements):647
  return gst_element_register (plugin, "testmp3enc", GST_RANK_NONE,
      test_mp3_enc_get_type ());
}
rademux.c (gst-plugins-ugly-0.10.19\gst\realmedia):960
  return gst_element_register (plugin, "rademux",
      GST_RANK_SECONDARY, GST_TYPE_REAL_AUDIO_DEMUX);
}
rdtdepay.c (gst-plugins-ugly-0.10.19\gst\realmedia):500
  return gst_element_register (plugin, "rdtdepay",
      GST_RANK_MARGINAL, GST_TYPE_RDT_DEPAY);
}
rdtmanager.c (gst-plugins-ugly-0.10.19\gst\realmedia):1325
  return gst_element_register (plugin, "rdtmanager",
      GST_RANK_NONE, GST_TYPE_RDT_MANAGER);
}
replaygain.c (gst-plugins-good-0.10.31\gst\replaygain):36
  if (!gst_element_register (plugin, "rganalysis", GST_RANK_NONE,
          GST_TYPE_RG_ANALYSIS))
    return FALSE;
replaygain.c (gst-plugins-good-0.10.31\gst\replaygain):40
  if (!gst_element_register (plugin, "rglimiter", GST_RANK_NONE,
          GST_TYPE_RG_LIMITER))
    return FALSE;
replaygain.c (gst-plugins-good-0.10.31\gst\replaygain):44
  if (!gst_element_register (plugin, "rgvolume", GST_RANK_NONE,
          GST_TYPE_RG_VOLUME))
    return FALSE;
rmdemux.c (gst-plugins-ugly-0.10.19\gst\realmedia):2669
  return gst_element_register (plugin, "rmdemux",
      GST_RANK_PRIMARY, GST_TYPE_RMDEMUX);
}
rtspreal.c (gst-plugins-ugly-0.10.19\gst\realmedia):751
  return gst_element_register (plugin, "rtspreal",
      GST_RANK_MARGINAL, GST_TYPE_RTSP_REAL);
}
teletext.c (gst-plugins-bad-0.10.23\ext\teletextdec):35
  return gst_element_register (teletext, "teletextdec", GST_RANK_NONE,
      GST_TYPE_TELETEXTDEC);
}
tsdemux.c (gst-plugins-bad-0.10.23\gst\mpegtsdemux):2397
  return gst_element_register (plugin, "tsdemux",
      GST_RANK_SECONDARY, GST_TYPE_TS_DEMUX);
}
vcdsrc.c (gst-plugins-bad-0.10.23\sys\vcd):580
  return gst_element_register (plugin, "vcdsrc", GST_RANK_SECONDARY,
      GST_TYPE_VCDSRC);
}
videodecoders.c (gst-plugins-bad-0.10.23\sys\qtwrapper):847
      if (!gst_element_register (plugin, type_name, GST_RANK_MARGINAL, type)) {
        g_warning ("Failed to register %s", type_name);;
        g_type_set_qdata (type, QTWRAPPER_VDEC_PARAMS_QDATA, NULL);
videomaxrate.c (gst-plugins-bad-0.10.23\gst\videomaxrate):322
  return gst_element_register (plugin, "videomaxrate", GST_RANK_NONE,
      GST_TYPE_VIDEO_MAX_RATE);
}
videomixer.c (gst-plugins-good-0.10.31\gst\videomixer):1900
  return gst_element_register (plugin, "videomixer", GST_RANK_PRIMARY,
      GST_TYPE_VIDEO_MIXER) && gst_videomixer2_register (plugin);
}
videomixer2.c (gst-plugins-good-0.10.31\gst\videomixer):2017
  return gst_element_register (plugin, "videomixer2", GST_RANK_SECONDARY,
      GST_TYPE_VIDEO_MIXER2);
}
visual.c (gst-plugins-base-0.10.36\ext\libvisual):1010
      if (!gst_element_register (plugin, name, GST_RANK_NONE, type)) {
        g_free (name);
        return FALSE;
vmncdec.c (gst-plugins-bad-0.10.23\gst\vmnc):1134
  if (!gst_element_register (plugin, "vmncdec", GST_RANK_PRIMARY,
          gst_vmnc_dec_get_type ()))
    return FALSE;
vtdec.c (gst-plugins-bad-0.10.23\sys\applemedia):504
  result = gst_element_register (plugin, type_name, GST_RANK_NONE, type);
  if (!result) {
    GST_ERROR_OBJECT (plugin, "failed to register element %s", type_name);
vtenc.c (gst-plugins-bad-0.10.23\sys\applemedia):886
  result = gst_element_register (plugin, type_name, GST_RANK_NONE, type);
  if (!result) {
    GST_ERROR_OBJECT (plugin, "failed to register element %s", type_name);
ximage.c (gst-plugins-base-0.10.36\sys\ ximage):33
  if (!gst_element_register (plugin, "ximagesink",
          GST_RANK_SECONDARY, GST_TYPE_XIMAGESINK))
    return FALSE;
xvimagesink.c (gst-plugins-base-0.10.36\sys\ xvimage):3767
  if (!gst_element_register (plugin, "xvimagesink",
          GST_RANK_PRIMARY, GST_TYPE_XVIMAGESINK))
    return FALSE;

'''
