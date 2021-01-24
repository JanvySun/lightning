#!/bin/bash

FILE="./电光词库.txt"
TARGET1="./bm.txt"
TEMP1=./temp1
TEMP2=./temp2

iconv -f utf16 -t utf8 $FILE -o $TEMP1

sed 's@ [^[:space:]]\{2,\}@@g' $TEMP1 | sed '/^[a-z]*[[:space:]]*$/d' > $TEMP2

iconv -f utf8 -t GB18030 $TEMP2 > $TARGET1

rm $TEMP1 $TEMP2
