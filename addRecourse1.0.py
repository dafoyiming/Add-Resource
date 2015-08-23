# -*- coding: utf-8 -*
###
###qamservice
###ver 1.0 
###author : grove.zhang


from suds.transport.https import HttpAuthenticated
from suds.client import Client
import urllib2
import logging
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.transport.http').setLevel(logging.DEBUG)

auth = HttpAuthenticated(username='administrator', password='quative')
client = Client('http://192.168.1.169:8180/ws-gateway/gateway/ws/qamservice?wsdl',transport=auth)
#print client

frequencyHertz = 203000000

frequencyNumber = 240

ipAddress = '172.21.252.7'

# cor_service_group:sgrp_uid   default = 1
serviceGroupUID = 21    

#optional
qamName = 'ns_test'

status = 'AVAILABLE'

#optional
streamingServerUID = 1

udpPorts = range(3325,3580) # 需要严格根据IPQAM PID 配置

serviceID = range(3069,len(udpPorts)+3069)

#programNumber = range(257,512)

udpInfos = zip(udpPorts,serviceID)

#print udpInfos

transportStreamID = 14011

for udpInfo in udpInfos:

    #创建一个实例
    servicegroupresource = client.factory.create('serviceGroupResource')
    #为实例赋值
    servicegroupresource.frequencyHertz = frequencyHertz
    servicegroupresource.frequencyNumber = frequencyNumber
    servicegroupresource.ipAddress = ipAddress
    servicegroupresource.programNumber = udpInfo[1] #programNumber MUST eq serviceID
    servicegroupresource.serviceGroupUID = serviceGroupUID
    servicegroupresource.serviceID = udpInfo[1]
    servicegroupresource.qamName = qamName
    servicegroupresource.status = status
    #servicegroupresource.streamingServerUID = streamingServerUID
    servicegroupresource.transportStreamID = transportStreamID
    servicegroupresource.udpPort = udpInfo[0]
    #print servicegroupresource
    result = client.service.createServiceGroupResource(servicegroupresource,checkConfig = False)
    print result
