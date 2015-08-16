#!/bin/sh

pushd . > /dev/null

echo "start get all undefined symbol in ranlib&object file"

a_file="./build/Linux-i386/release/libctags.a
./build/Linux-i386/release/libfresh.a
./build/Linux-i386/release/libqCtagsSense.a"

obj_file="./build/Linux-i386/release/obj/*.o
./build/plugins/Linux-i386/release/obj/*.o"

pushd . > /dev/null
mkdir -p temp_obj/temp
cd temp_obj/temp
number=0
for item in ${a_file}
do
    let 'number+=1'
    ar -x ../../${item}
    for obj in `ls *.o`; do mv $obj obj_${number}_$obj; done
    mv ./*.o ../
done

for item in ${obj_file}
do
    let 'number+=1'
    cp ../../$item ./
    for obj in `ls *.o`; do mv $obj obj_${number}_$obj; done
    mv ./*.o ../
done

cd ..
rm -rf temp

# QtWebKit issue
rm -f *QtAssistant*.o

ar cru all_file.a *.o
rm -f *.o

nm -g all_file.a | grep " U " | awk '{print $2}' > undefine.txt
# bss
nm -g all_file.a | grep " B " | awk '{print $3}' > define.txt
# common
nm -g all_file.a | grep " C " | awk '{print $3}' >> define.txt
# defined data
nm -g all_file.a | grep " D " | awk '{print $3}' >> define.txt
# defined data
nm -g all_file.a | grep " G " | awk '{print $3}' >> define.txt
# referance
nm -g all_file.a | grep " R " | awk '{print $3}' >> define.txt
# defined function
nm -g all_file.a | grep " T " | awk '{print $3}' >> define.txt
# weak obj
nm -g all_file.a | grep " W " | awk '{print $3}' >> define.txt
# define vtable
nm -g all_file.a | grep " V " | awk '{print $3}' >> define.txt

python2 ../../../gen_import_code.py undefine.txt define.txt all_file.c all_file.sym all_file.map

rm -f ../all_file.c
rm -f ../all_file.sym
rm -f ../all_file.map
mv all_file.c ../
mv all_file.sym ../
mv all_file.map ../
cd ..
#rm -rf temp_obj

popd > /dev/null

#cp ../../Makefile.all_file
make -f ../../Makefile.all_file

rm -rf ../monkeystudio2-svn/bin

sed -i 's|LIBS          = |& -pthread -rdynamic -L../ -lmonkeystudio -L../ -lmonkeystudio -L/home/eaglexmw/x32/monkeystudio2-svn/src/monkeystudio2-svn-build/build/Linux-i386/release  -Wl,--whole-archive -lfresh -lctags -lqCtagsSense -Wl,--no-whole-archive # |g' monkey/Makefile

find ./plugins/ -iname Makefile -exec sed -i 's|LIBS          = |& -Wl,-rpath,-/usr/local/monkeystudio2/lib -L/home/eaglexmw/x32/monkeystudio2-svn/src/monkeystudio2-svn-build/ -lmonkeystudio # |g' {} \;

make

popd > /dev/null

