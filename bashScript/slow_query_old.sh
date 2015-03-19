#!/bin/bash

#num=$(cat $1 |grep Query |awk -F : '{print $2}' |cut -c1-10 |sort -nr |head -1 )
#echo "$num"
#grep -A 2 -n $num <$1
#grep -A 2 -n $(cat $1 |grep -i Query |awk -F : '{print $2}' |cut -c1-10 |sort -nr |head -5) < $1


_slow_query_file=

num=$(cat $1 |grep -i Query |awk -F : '{print $2}' |cut -c1-10 |sort -nr |head -10) < $1


for i in $num 
	do 
		grep -A 6 -n $i < $1
		echo "----------------------------------------------------------------------------------------------------------------------------------------"
	done
