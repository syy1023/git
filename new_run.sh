#!/bin/bash
echo "start up mining"
bullockchain-cli  -conf=/home/jack/bitcoin.conf generatethread true 
echo "mining now"
#var=QQQQQ$RANDOM
#function transafer(){
 
  #echo "start to transfer"
 # bullockchain-cli  -conf=/home/jack/bitcoin.conf sendtoaddress 1AGoxBiXYTsRtyK6p9swXRaWqdiJ9uUd7o GAS 1

#}
#function createtoken(){
 #result=` bullockchain-cli  -conf=/home/jack/bitcoin.conf   createtoken 1EPs2V3G3xC3rXZm4bmVAQo8wfeReKwLcY  $var 10000 10000 true`

#}
#result=` bullockchain-cli  -conf=/home/jack/bitcoin.conf   createtoken 1EPs2V3G3xC3rXZm4bmVAQo8wfeReKwLcY  $var 10000 10000 true`
while true 
do
#发布随机名称的币种英文字符加随机数，全局变量多出调用
var=QQQQQ$RANDOM
#发行
result=` bullockchain-cli  -conf=/home/jack/bitcoin.conf   createtoken 1EPs2V3G3xC3rXZm4bmVAQo8wfeReKwLcY  $var 10000 10000 true`
echo "this is the txid of createtoken $result"
#转账
result2=` bullockchain-cli  -conf=/home/jack/bitcoin.conf gettransaction $result |grep confirmations|awk '{print $2}'|sed 's/\,//g'`
echo "the confirmation of currency is $result2"
sleep 10
#if [[ $result2 -gt 10 ]]
#then
  result3=`bullockchain-cli  -conf=/home/jack/bitcoin.conf sendtoaddress 1AGoxBiXYTsRtyK6p9swXRaWqdiJ9uUd7o AAA 0.1`
 echo "this is the txid of the transaction $result3"
#fi
sleep 15
done




增加获取货币数量：
#获取货币数量
 16   #currency_amount=`bullockchain-cli  -conf=/home/jack/bitcoin.conf getbalance|grep $s|awk '{print $2}'|sed 's/\,//g'|awk '{print int($0)}'`
 17   #echo "currency symbol: $s" "amount: $currency_amount" 
 
 然后判断如果货币数量是0，则不进行转账 但是现在的问题是，数量都是通过rpc命令截取出来的，是文本字符而非数字
 
