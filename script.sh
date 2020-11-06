#!/bin/bash


tempFile="ext3.txt"
with_line_number() {

	grep -n $1 $2 | awk -F, '{print $1 }' > $3

	cut -d ':' -f1 $3 > $tempFile

	extract_line $2 $tempFile
	#for line in `cat $tempFile`
	#do
	#	sed -n ${line}p $2
	#done
}
extract_line() {
	for line in `cat $2`
	do
		sed -n ${line}p $1
	done	 
}
without_line_number() {


	grep -n $1 $2 | awk -F, '{print $1 }' > $3

	for line in `cut -d ':' -f1 $3`
	do 
		sed -n ${line}p $2
	done
}
#without_line_number $1 $2 $3
with_line_number $1 $2 $3






