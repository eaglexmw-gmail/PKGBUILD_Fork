#!/bin/sh

cd /usr/local/CorsixTH/share/CorsixTH


if [ ! -d ~/.config/CorsixTH/ ]; then
    mkdir  ~/.config/CorsixTH/
else
    echo not need mkdir config dir
fi

if [ ! -f ~/.config/CorsixTH/config.txt ]; then
    cp -f ./config.txt  ~/.config/CorsixTH/config.txt
else
    echo not need copy config file
fi

export TIMIDITY_CFG=/usr/local/CorsixTH/share/timidity/timidity.cfg

/usr/local/CorsixTH/bin/CorsixTH_opengl &
