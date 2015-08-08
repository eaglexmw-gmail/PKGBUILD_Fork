#!/bin/sh

export PATH=$PATH:/usr/local/python-qt/python2_qt3/bin:/usr/local/qt/qt3/bin
export PYTHONPATH=$PYTHONPATH:/usr/local/python-qt/python2_qt3/lib/python2.7/site-packages
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/qt/qt3/lib

/usr/local/python2/bin/python2_spec "$@"

