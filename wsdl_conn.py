# -*- coding: utf-8 -*
from suds.transport.https import HttpAuthenticated
from suds.client import Client
#from IPy import IP
import urllib2
import logging
import logging

logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.transport.http').setLevel(logging.DEBUG)

auth = HttpAuthenticated(username='administrator', password='quative')
#client = Client('http://192.168.1.169:8180/ws-gateway/gateway/ws/qamservice?wsdl',transport=auth)
#client = Client('http://172.21.254.235/ws-gateway/gateway/ws/recommendationservice?wsdl',transport=auth) 
#client = Client('http://172.21.254.235/ws-gateway/gateway/ws/btvservice?wsdl',transport=auth)
#client = Client('http://172.21.254.235/ws-gateway/gateway/ws/accountservice?wsdl',transport=auth)
#client = Client('http://192.168.1.169:8180/ws-gateway/gateway/ws/qamservice?wsdl',transport=auth)
client = Client('http://192.168.1.169:8180/ws-gateway/gateway/ws/qamservice?wsdl',transport=auth)

print client
result = client.service.getServiceGroupsResourceByServiceGroupUID(226)
#result = client.service.getServiceGroupsResourceByServiceGroupFreqResponse(226,187000000)

print result
#print result[0].name
#print result[0].qamAddress
#print result[0].UID
    
    

    

    
