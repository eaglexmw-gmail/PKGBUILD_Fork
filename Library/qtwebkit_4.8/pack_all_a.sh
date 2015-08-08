#!/bin/sh

pushd . > /dev/null

echo "start build static lib"

pushd . > /dev/null
mkdir -p ./WebKit1_obj
cd WebKit1_obj
ar x ./../WebKit/release/libWebKit1.a
for item in `ls *.o`; do mv $item WebKit1_$item; done
cd ../
popd > /dev/null

pushd . > /dev/null
mkdir -p ./WebCore_obj
cd ./WebCore_obj
ar x ../WebCore/release/libWebCore.a
for item in `ls *.o`; do mv $item WebCore_$item; done
cd ../
popd > /dev/null

pushd . > /dev/null
mkdir -p ./ANGLE_obj
cd ./ANGLE_obj
ar x ../ThirdParty/ANGLE/release/libANGLE.a
for item in `ls *.o`; do mv $item ANGLE_$item; done
cd ../
popd > /dev/null

pushd . > /dev/null
mkdir -p ./JavaScriptCore_obj
cd ./JavaScriptCore_obj
ar x ../JavaScriptCore/release/libJavaScriptCore.a
for item in `ls *.o`; do mv $item JavaScriptCore_$item; done
cd ../
popd > /dev/null

pushd . > /dev/null
mkdir -p ./WTF_obj
cd ./WTF_obj
ar x ../WTF/release/libWTF.a
for item in `ls *.o`; do mv $item WTF_$item; done
cd ../
popd > /dev/null

ar crus $1 ./WebKit1_obj/*.o ./WebCore_obj/*.o ./ANGLE_obj/*.o ./JavaScriptCore_obj/*.o ./WTF_obj/*.o
rm -rf ./WebKit1_obj/ ./WebCore_obj/ ./ANGLE_obj/ ./JavaScriptCore_obj/ ./WTF_obj/

popd > /dev/null

