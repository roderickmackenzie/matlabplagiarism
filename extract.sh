base_dir=`pwd`

find . -depth -name '* *' \
| while read f ; do mv -i "$f" "$(dirname "$f")/$(basename "$f"|tr ' ' _)" ; done
a="0"
mkdir extracted

for i in `find |grep zip|grep orig` ; do
filename=`basename $i`
b="${filename%.*}"
mkdir ./extracted/$b
unzip $i -d ./extracted/$b/
let a=a+1
done


for i in `find |grep rar|grep orig` ; do
#rm $a -rf
filename=`basename $i`
b="${filename%.*}"
echo $i
echo $b
mkdir ./extracted/$b
cd ./extracted/$b
unrar e ../../orig/$b
cd $base_dir
let a=a+1
done
