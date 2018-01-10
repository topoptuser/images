#!/bin/sh

FOLDER='new'
LIST='image-names.txt'
PROG=$1

ls | grep bmp > $LIST

while read name
do
  python $PROG $name
done < $LIST

mkdir new
mv *-0.bmp new
mv *-1.bmp new
mv *-2.bmp new
mv *-3.bmp new

rm *.bmp
