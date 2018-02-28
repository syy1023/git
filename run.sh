#!/bin/bash
result=`/home/jack/bullockchain-cli  -conf='/home/jack/bitcoin.conf' getbalance|cut -d":" -f1|sed 's/\,//g' |sed 's/\"//g' |tr -d "{}"|grep -v "^$"`
#将结果拼接到数组中循环转账

OLD_IFS="$IFS"
IFS=" "
arr=($result)

IFS="$OLD_IFS"

while true
do
for s in ${arr[@]}
do
    /home/jack/bullockchain-cli  -conf='/home/jack/bitcoin.conf' sendtoaddress 1AGoxBiXYTsRtyK6p9swXRaWqdiJ9uUd7o $s 1
   echo "currency $s"
    sleep 10
done
done


