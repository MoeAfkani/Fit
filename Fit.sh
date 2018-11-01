#!/bin/bash
cp $1 $(pwd)/DATA
data=$(pwd)/DATA
sed -i.backup -e '1d' $data
row= wc -l < $data 
>$(pwd)/PyDATA
for i in `LANG=en_US seq $row 1`;
do
echo -n |tail -$i $data |head -1| cut -d" " -f3 >> $(pwd)/PyDATA
done
