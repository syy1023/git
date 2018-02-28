#!/bin/bash
echo "start up mining"
bullockchain-cli  -conf=/home/jack/bitcoin.conf generatethread true
echo "mining now"
function transafer(){
 
echo "start to transfer"
bullockchain-cli  -conf=/home/jack/bitcoin.conf sendtoaddress 1AGoxBiXYTsRtyK6p9swXRaWqdiJ9uUd7o GAS 1

}
 function createtoken(){
 result=` bullockchain-cli  -conf=/home/jack/bitcoin.conf   createtoken 1EPs2V3G3xC3rXZm4bmVAQo8wfeReKwLcY  QQQQQ$RANDOM 10000 10000 true`
 }
 while true 
 do
 createtoken()
 result2=` bullockchain-cli  -conf=/home/jack/bitcoin.conf gettransaction $result |grep confirmations|awk '{print $2}'|sed 's/\,//g'4`
if [ $result2 -gt 10 ]
 then
   transfer()
 fi
 sleep 10
 done