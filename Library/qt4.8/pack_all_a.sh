#!/bin/sh

pushd . > /dev/null

echo "start build static lib"

pushd . > /dev/null
mkdir -p ./QtWebKit_obj
cd QtWebKit_obj
ar x ./../lib/libQtWebKit.a
for item in `ls *.o`; do mv $item QtWebKit_$item; done
cd ../
popd > /dev/null

pushd . > /dev/null
mkdir -p ./JavaScriptCore_obj
cd ./JavaScriptCore_obj
ar x ./../src/3rdparty/webkit/Source/JavaScriptCore/release/libjscore.a
for item in `ls *.o`; do mv $item JavaScriptCore_$item; done
cd ../
popd > /dev/null

pushd . > /dev/null
mkdir -p ./WebCore_obj
cd ./WebCore_obj
ar x ./../src/3rdparty/webkit/Source/WebCore/release/libwebcore.a
for item in `ls *.o`; do mv $item WebCore_$item; done
cd ../
popd > /dev/null

ar crus $1 ./QtWebKit_obj/*.o ./JavaScriptCore_obj/*.o ./WebCore_obj/*.o
rm -rf ./QtWebKit_obj/ ./JavaScriptCore_obj/ ./WebCore_obj/

popd > /dev/null

