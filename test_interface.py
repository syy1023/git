#coding=utf-8
# -*- coding: utf-8 -*-
import requests
import json
import unittest
import unittest,time,re,os
import HTMLTestRunner
import pprint

import sys
reload(sys)
sys.setdefaultencoding('utf-8')





#获取全局变量address
url1="http://192.168.0.68:9332"
header = {"Authorization": "Basic UlBDdXNlcjoxMjM0NTY="}
auth = ("RPCuser", "123456")        
verificationErrors=[]
accept_next_alert=True
data_address={"jsonrpc": "1.0", "id":"curltest", "method": "getnewaddress", "params": [] }
data_all=requests.post(url=url1,json=data_address, auth=auth)
#print data_address
#print data_all.text
address=json.loads(data_all.text, 'utf-8')



#获取全局变量第二个地址address2
#url2="http://192.168.0.68:9332"
header = {"Authorization": "Basic UlBDdXNlcjoxMjM0NTY="}
auth = ("RPCuser", "123456")        
verificationErrors=[]
accept_next_alert=True
data_address2={"jsonrpc": "1.0", "id":"curltest", "method": "getnewaddress", "params": [] }
data_all=requests.post(url=url1,json=data_address2, auth=auth)
#print data_address
#print data_all.text
address2=json.loads(data_all.text, 'utf-8')


#全局交易，有几个rpc命令会用到txid
url2="http://192.168.0.36:9332"
header = {"Authorization": "Basic UlBDdXNlcjoxMjM0NTY="}
auth = ("RPCuser", "123456")        
verificationErrors=[]
accept_next_alert=True
data={"jsonrpc": "1.0", "id":"curltest", "method": "sendtoaddress", "params": [address["result"], "DALI", 1] }
r=requests.post(url=url2,json=data, auth=auth)
print r.text
print r.status_code
txid=r.text[11:75]



class TestInterface(unittest.TestCase):
    def setUp(self):
        self.url="http://192.168.0.36:9332"
        self.header = {"Authorization": "Basic UlBDdXNlcjoxMjM0NTY="}
        self.auth = ("RPCuser", "123456")        
        self.verificationErrors=[]
        self.accept_next_alert=True
        
    def tearDown(self):
        self.assertEqual([],self.verificationErrors)

    

    
    

    def test_get_info_of_thenodes(self):
        u"**获取节点详细信息** getinfo"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"jsonrpc", "method": "getinfo", "params": []}
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        ret=json.loads(r.text)
        print ret
        print r.status_code
    def test_get_outputtransactionin(self):
        u"**获取输出交易的信息** gettxout 第一个参数含义1为手续费（可以是gas或dali），若是0代表代币，第二个参数表示该参数在内存池中未被确认"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "gettxout", "params": [txid, 1,1] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        ret=json.loads(r.text)
        pprint.pprint(ret.keys())
        print r.status_code

    def test_get_the_remained_amountofmoney_2(self):
        u"获取余额，params可以是地址或者账号，这里是账号"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"jsonrpc", "method": "getbalance", "params": ["one"]}
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_get_the_templates_of_blocks(self):
        u"**获取区块模板** getblocktemplate"
        url="http://192.168.0.36:9332"
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"jsonrpc", "method": "getblocktemplate", "params": []}
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        ret=json.loads(r.text)
        pprint.pprint(ret.keys())
        print r.status_code
    def test_get_information_inmempool(self):
        u"**获取内存池中的交易信息** getmempoolentry"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "getmempoolentry", "params": [txid] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        ret=json.loads(r.text)
        pprint.pprint(ret.keys())
        print r.status_code
    def test_get_unconfirmed_remianed_cash(self):
        u"**获取未确认的余额** getunconfirmedbalance"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"jsonrpc", "method": "getunconfirmedbalance", "params": []}
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        ret=json.loads(r.text)
        print ret.keys()
        print r.status_code
        
    def test_list_the_currency_inalladdresses(self):
        u"**列出所有地址货币** listaddressgroupings"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"jsonrpc", "method": "listaddressgroupings", "params": []}
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        ret=json.loads(r.text)
        pprint.pprint(ret.keys())
        print r.status_code
        
    def test_list_therecieved_money_inaddresses(self):
        u"**列出地址收到的货币** listreceivedbyaddress"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"jsonrpc", "method": "listreceivedbyaddress", "params": []}
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        ret=json.loads(r.text)
        pprint.pprint(ret.keys())
        print r.status_code
    def test_search_a_transaction(self):
        u"**查询某个交易** gettransaction"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "gettransaction", "params": [txid] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        ret=json.loads(r.text)
        pprint.pprint(ret.keys())
        print r.status_code
    def test_search_details_of_thewallet(self):
        u"**查询钱包详情** getwalletinfo"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"jsonrpc", "method": "getwalletinfo", "params": []}
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        ret=json.loads(r.text)
        pprint.pprint(ret.keys())
        print r.status_code
    def test_show_remianedmoney_onaccounts(self):
        u"**显示账号余额** listaccounts"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"jsonrpc", "method": "listaccounts", "params":[]}
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        ret=json.loads(r.text)
        print ret.keys()
        print r.status_code
    def test_thecurrencyrecievedbyaccounts(self):
        u"列出账号收到的货币** listreceivedbyaccount"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"jsonrpc","method":"listreceivedbyaccount","params":[]}
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        ret=json.loads(r.text)
        print ret.keys()
        print r.status_code        
    def test_transfer_money_from_one_account(self):
        u"**从某个账号转账** sendfrom"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendfrom", "params": ["anryan", address["result"],"DALI",0.01] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code

    def test_transfer_money_sendtoaddress(self):
        u"**向某个账号转账** sendtoaddress"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendtoaddress", "params": [address["result"], "DALI", 1] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code

    def test_gettransaction_and_decoderawtransaction(self):
        u"**查询某个交易信息与decode改交易** sendtoaddress"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendtoaddress", "params": [address["result"], "DALI", 1] }
        r=requests.post(url=url,json=data, auth=auth)
        txid=r.text[11:75]
        data2={"jsonrpc": "1.0", "id":"curltest", "method": "gettransaction", "params": [txid] }
        r2=requests.post(url=url,json=data2, auth=auth)
        r2Obj = json.loads(r2.text, 'utf-8')
        print "扣除手续费用："
        print r2Obj["result"]["fee"]
        r2_hexstring=r2Obj["result"]["hex"]
        #print r.text
        print r.status_code
        #使用decoderawtransaction获取fee
        data3={"jsonrpc": "1.0", "id":"curltest", "method": "decoderawtransaction", "params": [r2_hexstring] }
        r3=requests.post(url=url,json=data3, auth=auth)
        r3Obj = json.loads(r3.text, 'utf-8')
        print "扣除手续费用标志："
        print r3Obj["result"]["gascurrencysymbol"]
        print "交易大小："
        print r3Obj["result"]["size"] 
    
    
    def test_get_all_the_outputtransaction(self):
        
        u"**获取输出交易信息集合** gettxoutsetinfo"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "gettxoutsetinfo", "params": [] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        ret=json.loads(r.text)
        print ret.keys()
        print r.status_code
    def test_transferfromcertainaccounttoaddresses(self):
        u"**从指定账号向多个地址转账** sendmany"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendmany", "params": ["anryan","DALI",{address["result"]:"0.01",address2['result']:"0.02"}] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
           
    def test_transferfromcertainaccounttoaddresses_error1(self):
        u"**从指定账号向多个地址转账** 其中一个地址无效 sendmany"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendmany", "params": ["anryan","DALI",{address["result"]:"0.01",address2['result']:"0.02"}] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_transferfromcertainaccounttoaddresses_error2(self):
        u"**从指定账号向多个地址转账** 余额不足sendmany"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendmany", "params": ["anryan","DALI",{address["result"]:"10000000000000",address2['result']:"0.02"}] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_transferfromcertainaccounttoaddresses_error3(self):
        u"**从指定账号向多个地址转账** 转账数字无效 sendmany"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendmany", "params": ["anryan","DALI",{address["result"]:"-1",address2['result']:"0.02"}] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_transferfromcertainaccounttoaddresses_error4(self):	
        u"**从指定账号向多个地址转账** 转账数字超过最小精度** sendmany"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendmany", "params": ["anryan","DALI",{address["result"]:"0.000001",address2['result']:"0.02"}] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_transferfromcertainaccounttoaddresses_error5(self):
        u"**从指定账号向多个地址转账**,没有认证 sendmany"
        url=self.url
        header=self.header
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendmany", "params": ["anryan","DALI",{address["result"]:"0.01",address2['result']:"0.02"}] }
        r=requests.post(url=url,json=data)
        print r.text
        print r.status_code

    def test_transferfromcertainaccounttoaddresses_error6(self):
        u"**从指定账号向多个地址转账**,超出余额 sendmany"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendmany", "params": ["anryan","DALI",{address["result"]:"1000000000",address2['result']:"0.02"}] }
        r=requests.post(url=url,json=data,auth=auth)
        print r.text
        print r.status_code
    def test_transferfromcertainaccounttoaddresses_error7(self):
        u"**从指定账号向多个地址转账**,转向地址重复 sendmany"
        url=self.url
        header=self.header
        auth=self.auth
        data = "{\"jsonrpc\": \"1.0\", \"id\":\"curltest\", \"method\": \"sendmany\", \"params\": [\"anryan\",\"DALI\",{\"15qMa32bckkwEaiBh5iBNAQAR2EwgEhHqv\":\"0.00003\",\"15qMa32bckkwEaiBh5iBNAQAR2EwgEhHqv\":\"0.00002\",\"15qMa32bckkwEaiBh5iBNAQAR2EwgEhHqv\":\"0.00001\"}] }"
        r=requests.post(url=url,data=data,auth=auth)
        print r.text
        print r.status_code
    def test_transferfromcertainaccounttoaddresses_error8(self):
        u"**从指定账号向多个地址转账**,从本地账号向对应地址转账 sendmany"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendmany", "params": ["anryan","DALI",{address["result"]:"1",address2['result']:"1"}] }
        r=requests.post(url=url,json=data,auth=auth)
        print r.text
        print r.status_code
    def test_transferfromcertainaccounttoaddresses_error9(self):
        u"**从指定账号向多个地址转账**,从本地账号向本地其他地址转账 sendmany"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendmany", "params": ["anryan","DALI",{address["result"]:"1",address2['result']:"1"}] }
        r=requests.post(url=url,json=data,auth=auth)
        print r.text
        print r.status_code
    def test_transferfromcertainaccounttoaddresses_error10(self):
        u"**从指定账号向多个地址转账**,两个不同节点地址，地址均有效 sendmany"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendmany", "params": ["anryan","DALI",{address["result"]:"1",address2['result']:"1"}] }
        r=requests.post(url=url,json=data,auth=auth)
        print r.text
        print r.status_code
    def test_transferfromcertainaccounttoaddresses_error11(self):
         
        u"**从指定账号向多个地址转账**,两个不同节点地址，其中一个地址无效 sendmany"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendmany", "params": ["anryan","DALI",{address["result"]:"1",address2['result']:"1"}] }
        r=requests.post(url=url,json=data,auth=auth)
        print r.text
        print r.status_code
    def test_transferfromcertainaccounttoaddresses_error12(self):
        u"**从指定账号向多个地址转账**,两个不同节点地址，其中一个地址为空 sendmany"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendmany", "params": ["anryan","DALI",{"":"1",address2['result']:"1"}] }
        r=requests.post(url=url,json=data,auth=auth)
        print r.text
        print r.status_code
    def test_transferfromcertainaccounttoaddresses_error13(self):
        u"**从指定账号向多个地址转账**,两个不同节点地址，其中一个转账数目超出余额 sendmany"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendmany", "params": ["anryan","DALI",{address["result"]:"10000000000",address2['result']:"1"}] }
        r=requests.post(url=url,json=data,auth=auth)
        print r.text
        print r.status_code
    def test_transferfromcertainaccounttoaddresses_error14(self):
        u"**从指定账号向多个地址转账**,两个不同节点地址，其中一个转账数目为非法如-1  sendmany"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendmany", "params": ["anryan","DALI",{address["result"]:"-1",address2['result']:"1"}] }
        r=requests.post(url=url,json=data,auth=auth)
        print r.text
        print r.status_code
    def test_transferfromcertainaccounttoaddresses_error15(self):
        u"**从指定账号向多个地址转账**,两个不同节点地址，两个地址均无效  sendmany"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendmany", "params": ["anryan","DALI",{address2['result']:"-1",address['result']:"1"}] }
        r=requests.post(url=url,json=data,auth=auth)
        print r.text
        print r.status_code
    def test_transferfromcertainaccounttoaddresses_error16(self):
         
        u"**从指定账号向多个地址转账**,两个不同节点地址，币种无效如DCM  sendmany"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendmany", "params": ["anryan","DALI",{address2['result']:"-1",address['result']:"1"}] }
        r=requests.post(url=url,json=data,auth=auth)
        print r.text
        print r.status_code
    def test_transferfromcertainaccounttoaddresses_error17(self):
        u"**从指定账号向多个地址转账**,两个不同节点地址，币种为空  sendmany"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendmany", "params": ["anryan","",{address['result']:"-1",address2['result']:"1"}] }
        r=requests.post(url=url,json=data,auth=auth)
        print r.text
        print r.status_code
    def test_transferfromcertainaccounttoaddresses_error18(self):
        u"**从指定账号向多个地址转账**,三个不同节点地址，地址均有效 sendmany"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendmany", "params": ["anryan","DALI",{address['result']:"1",address2['result']:"1","16Wa5TYRBb1CXjgeDcEbDnzeTSfx695o66":"50"}] }
        r=requests.post(url=url,json=data,auth=auth)
        print r.text
        print r.status_code
    def test_transfer_money_from_one_account_error1(self):
        u"**从某个账号转账** 账号不存在   sendfrom"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendfrom", "params": ["anryan1", "13HigQdWns44dikjWisxxqiohuTojkKMYs00","DALI",0.01] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_transfer_money_from_one_account_error2(self):
        u"**从某个账号转账** 转账地址错误  sendfrom"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendfrom", "params": ["anryan1", "13HigQdWns44dikjWisxxqiohuTojkKMYs00","DALI",0.01] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_transfer_money_from_one_account_error3(self):
        u"**从某个账号转账** 转账数目超出余额  sendfrom"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendfrom", "params": ["anryan", "13HigQdWns44dikjWisxxqiohuTojkKMYs","DALI",10000000000] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_transfer_money_from_one_account_error4(self):
        u"**从某个账号转账** 转账数目非法  sendfrom"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendfrom", "params": ["anryan", address["result"],"DALI",-10] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_transfer_money_from_one_account_error5(self):
        u"**从某个账号转账** 转账数目超出最小精度  sendfrom"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendfrom", "params": ["anryan", address["result"],"DALI",0.000001] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_transfer_money_from_one_account_error6(self):
        u"**从某个账号转账** 币种错误"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendfrom", "params": ["anryan", address["result"],"DCM",0.01] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_transfer_money_from_one_account_error7(self):
        u"**从某个账号转账** 账号为空"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendfrom", "params": ["", address["result"],"DALI",0.01] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_transfer_money_from_one_account_error8(self):
        u"**从某个账号转账** 地址为空"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendfrom", "params": ["anryan", "","DALI",0.01] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_search_a_transaction_error1(self):
        u"**查询某个交易** 交易id错误 gettransaction"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "gettransaction", "params": [txid] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_search_a_transaction_error2(self):
        u"**查询某个交易** 交易id为空 gettransaction"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "gettransaction", "params": [""] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_get_information_inmempool_error1(self):       
         u"获取内存池中的交易信息，交易id错误 getmempoolentry"
         url=self.url
         header=self.header
         auth=self.auth
         data={"jsonrpc": "1.0", "id":"curltest", "method": "getmempoolentry", "params": [txid] }
         r=requests.post(url=url,json=data, auth=auth)
         print r.text
         print r.status_code
    def test_get_information_inmempool_error2(self):        
         u"获取内存池中的交易信息，交易id为空 getmempoolentry"
         url=self.url
         header=self.header
         auth=self.auth
         data={"jsonrpc": "1.0", "id":"curltest", "method": "getmempoolentry", "params": [""] }
         r=requests.post(url=url,json=data, auth=auth)
         print r.text
         print r.status_code
    def test_get_outputtransactionin_error1(self):
        u"**获取输出交易的信息**，交易id错误，params第二个参数可以取0-gas,1-token,第三个代表第几笔，从0开始  gettxout"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "gettxout", "params": [txid, 1,1] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_get_outputtransactionin_error2(self):
        u"**获取输出交易的信息**，交易id为空 gettxout"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "gettxout", "params": ["", 1,1] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_get_outputtransactionin_error3(self):
        u"**获取输出交易的信息**，交易id，第二个参数取0 gettxout"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "gettxout", "params": [txid, 0,0] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code        
    def test_decode_the_transaction_error1(self):
        u"解码交易,交易id错误 decoderawtransaction"
        url="http://192.168.0.68:9332"
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"jsonrpc", "method": "decoderawtransaction", "params": ["1"]}
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_get_unconfirmed_remianed_cash_error1(self):
        
        u"**获取未确认的余额** 币种错误 getunconfirmedbalance"
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"jsonrpc", "method": "getunconfirmedbalance", "params": [["DCM"]]}
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code


if __name__=="__main__":  
    testunit=unittest.TestSuite()
   
   
    testunit.addTest(TestInterface("test_get_info_of_thenodes"))
    testunit.addTest(TestInterface("test_get_outputtransactionin"))
    testunit.addTest(TestInterface("test_get_the_remained_amountofmoney_2"))
    testunit.addTest(TestInterface("test_get_the_templates_of_blocks"))
    testunit.addTest(TestInterface("test_get_information_inmempool"))
    testunit.addTest(TestInterface("test_get_unconfirmed_remianed_cash"))
    testunit.addTest(TestInterface("test_list_the_currency_inalladdresses"))
    testunit.addTest(TestInterface("test_list_therecieved_money_inaddresses"))
    testunit.addTest(TestInterface("test_search_a_transaction"))
    testunit.addTest(TestInterface("test_search_details_of_thewallet"))
    testunit.addTest(TestInterface("test_show_remianedmoney_onaccounts"))
    testunit.addTest(TestInterface("test_transfer_money_from_one_account"))
    testunit.addTest(TestInterface("test_transfer_money_sendtoaddress"))
    testunit.addTest(TestInterface("test_gettransaction_and_decoderawtransaction"))
    
    testunit.addTest(TestInterface("test_get_all_the_outputtransaction"))
    
    testunit.addTest(TestInterface("test_thecurrencyrecievedbyaccounts"))
    testunit.addTest(TestInterface("test_transferfromcertainaccounttoaddresses"))	
    testunit.addTest(TestInterface("test_transferfromcertainaccounttoaddresses_error1"))
    testunit.addTest(TestInterface("test_transferfromcertainaccounttoaddresses_error2"))
    testunit.addTest(TestInterface("test_transferfromcertainaccounttoaddresses_error3"))
    testunit.addTest(TestInterface("test_transferfromcertainaccounttoaddresses_error4"))
    testunit.addTest(TestInterface("test_transferfromcertainaccounttoaddresses_error5"))
    testunit.addTest(TestInterface("test_transferfromcertainaccounttoaddresses_error6"))
    testunit.addTest(TestInterface("test_transferfromcertainaccounttoaddresses_error7"))
    testunit.addTest(TestInterface("test_transferfromcertainaccounttoaddresses_error8"))
    testunit.addTest(TestInterface("test_transferfromcertainaccounttoaddresses_error9"))
    testunit.addTest(TestInterface("test_transferfromcertainaccounttoaddresses_error10"))
    testunit.addTest(TestInterface("test_transferfromcertainaccounttoaddresses_error11"))
    testunit.addTest(TestInterface("test_transferfromcertainaccounttoaddresses_error12"))
    testunit.addTest(TestInterface("test_transferfromcertainaccounttoaddresses_error13"))
    testunit.addTest(TestInterface("test_transferfromcertainaccounttoaddresses_error14"))
    testunit.addTest(TestInterface("test_transferfromcertainaccounttoaddresses_error15"))
    testunit.addTest(TestInterface("test_transferfromcertainaccounttoaddresses_error16"))
    testunit.addTest(TestInterface("test_transferfromcertainaccounttoaddresses_error17"))
    testunit.addTest(TestInterface("test_transferfromcertainaccounttoaddresses_error18"))
    testunit.addTest(TestInterface("test_transfer_money_from_one_account_error1"))
    testunit.addTest(TestInterface("test_transfer_money_from_one_account_error2"))
    testunit.addTest(TestInterface("test_transfer_money_from_one_account_error3"))
    testunit.addTest(TestInterface("test_transfer_money_from_one_account_error4"))
    testunit.addTest(TestInterface("test_transfer_money_from_one_account_error5"))
    testunit.addTest(TestInterface("test_transfer_money_from_one_account_error6"))
    testunit.addTest(TestInterface("test_transfer_money_from_one_account_error7"))
    testunit.addTest(TestInterface("test_transfer_money_from_one_account_error8"))
    testunit.addTest(TestInterface("test_search_a_transaction_error1"))
    testunit.addTest(TestInterface("test_search_a_transaction_error2"))
    testunit.addTest(TestInterface("test_get_information_inmempool_error1"))
    testunit.addTest(TestInterface("test_get_information_inmempool_error2"))    
    testunit.addTest(TestInterface("test_get_outputtransactionin_error1"))
    testunit.addTest(TestInterface("test_get_outputtransactionin_error2"))
    testunit.addTest(TestInterface("test_get_outputtransactionin_error3"))
    testunit.addTest(TestInterface("test_decode_the_transaction_error1"))
    testunit.addTest(TestInterface("test_get_unconfirmed_remianed_cash_error1"))
   

    
    filename="C:\\Users\\test\\Desktop\\all\\test_interface\\result.html"
    fp=open(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'rcf_interface测试结果报告',description='by anryan')
    runner.run(testunit)
    fp.close()

'''
 testunit.addTest(TestInterface("test_get_all_the_outputtransaction"))
   
'''
