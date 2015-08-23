# -*- coding: utf-8 -*-

"""
Module implementing addresource.
"""
import PyQt4,PyQt4.QtGui,sys
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature
from suds.transport.https import HttpAuthenticated
from suds.client import Client
from suds.bindings.binding import WebFault
import urllib2
import logging
import traceback
import StringIO

from Ui_addresourceforHamonic import Ui_addresourceforHamonic

class addresourceforHamonic(QDialog, Ui_addresourceforHamonic):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)   

    @pyqtSignature("")
    def on_TEST_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        global SDP_IP, SDP_PORT
        SDP_IP = self.SDP_IP.text()
        SDP_PORT = self.PORT.text()
        global QAM_NAME_LIST,QAM_ADDRESS_LIST,QAM_UID_LIST
        QAM_NAME_LIST = list()
        QAM_ADDRESS_LIST = list()
        QAM_UID_LIST = list()
        def testConnection(IP, PORT, SERVICE_NAME):
            url_origin = u'http://'+IP+u':'+PORT+u'/ws-gateway/gateway/ws/'+SERVICE_NAME+'?wsdl'
            url = str(url_origin)
            auth = HttpAuthenticated(username='administrator', password='quative')
            try:
                client = Client(url,transport=auth)
#                self.Result.append(SERVICE_NAME+u'Connect[test] Successfully')
                return url
            except:
                fp = StringIO.StringIO()
                traceback.print_exc(file = fp)
                message = fp.getvalue()
                self.Result.append(message)

                
        def getQAMs(IP, PORT):
            url=testConnection(IP, PORT, 'deviceservice')
            auth = HttpAuthenticated(username='administrator', password='quative')
            client = Client(url,transport=auth)
            qaminfo = client.service.getQams()
            return qaminfo
                
        def setQAM_NAME(qaminfo):
            for i in range(len(qaminfo)):
                QAM_NAME_LIST.append(qaminfo[i].name)
                QAM_ADDRESS_LIST.append(qaminfos[i].qamAddress)
                QAM_UID_LIST.append(qaminfos[i].UID)
                self.QAM_NAME.addItem(QAM_NAME_LIST[i])
                
        def setQAM_IP(qam_name):
            qam_Address=QAM_ADDRESS_LIST[QAM_NAME_LIST.index(qam_name)]
            self.QAM_IP.setText(qam_Address)
            
        def getQAM_UID(qam_name):
            qam_uid=QAM_UID_LIST[QAM_NAME_LIST.index(qam_name)]
            return qam_uid
            
        def getServiceGroups(IP,PORT,qam_uid):
            url=testConnection(IP, PORT, 'qamservice')
            auth = HttpAuthenticated(username='administrator', password='quative')
            client = Client(url,transport=auth)
            ServiceGroupinfo = client.service.getServiceGroupsByQamUID(qam_uid)
            return ServiceGroupinfo
                
        def setServiceGroups_NAME(ServiceGroupinfo):
            ServiceGroup_NAME_list = list()
            self.ServiceGroup.clear()
            for i in range(len(ServiceGroupinfo)):
                ServiceGroup_NAME_list.append(ServiceGroupinfo[i].name)
                self.ServiceGroup.addItem(ServiceGroup_NAME_list[i])
            
        testConnection(SDP_IP, SDP_PORT, 'qamservice')
        qaminfos = getQAMs(SDP_IP, SDP_PORT)
        setQAM_NAME(qaminfos)
        qam_name = self.QAM_NAME.currentText()
        setQAM_IP(qam_name)
        qam_uid=getQAM_UID(qam_name)
        ServiceGroupinfos = getServiceGroups(SDP_IP, SDP_PORT, qam_uid)
        setServiceGroups_NAME(ServiceGroupinfos)

    @pyqtSignature("QString")
    def on_QAM_NAME_activated(self, p0):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        def testConnection(IP, PORT, SERVICE_NAME):
            url_origin = u'http://'+IP+u':'+PORT+u'/ws-gateway/gateway/ws/'+SERVICE_NAME+'?wsdl'
            url = str(url_origin)
            auth = HttpAuthenticated(username='administrator', password='quative')
            try:
                client = Client(url,transport=auth)
#                self.Result.append(SERVICE_NAME+u'Connect[active] Successfully')
                return url
            except:
                fp = StringIO.StringIO()
                traceback.print_exc(file = fp)
                message = fp.getvalue()
                self.Result.append(message)

                
        def setQAM_IP(qam_name):
            qam_Address=QAM_ADDRESS_LIST[QAM_NAME_LIST.index(qam_name)]
            self.QAM_IP.setText(qam_Address)
        
        def getQAM_UID(qam_name):
            qam_uid=QAM_UID_LIST[QAM_NAME_LIST.index(qam_name)]
            return qam_uid
            
        def getServiceGroups(IP,PORT,qam_uid):
            url=testConnection(IP, PORT, 'qamservice')
            auth = HttpAuthenticated(username='administrator', password='quative')
            client = Client(url,transport=auth)
            ServiceGroupinfo = client.service.getServiceGroupsByQamUID(qam_uid)
            return ServiceGroupinfo
                
        def setServiceGroups_NAME(ServiceGroupinfo):
            ServiceGroup_NAME_list = list()
            self.ServiceGroup.clear()
            for i in range(len(ServiceGroupinfo)):
                ServiceGroup_NAME_list.append(ServiceGroupinfo[i].name)
                self.ServiceGroup.addItem(ServiceGroup_NAME_list[i])
            
        qam_name = self.QAM_NAME.currentText()
        setQAM_IP(qam_name)
        qam_uid=getQAM_UID(qam_name)
        ServiceGroupinfos = getServiceGroups(SDP_IP, SDP_PORT, qam_uid)
        setServiceGroups_NAME(ServiceGroupinfos)
    
    @pyqtSignature("QString")
    def on_ServiceGroup_activated(self, p0):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet

        
    @pyqtSignature("")  
    def on_Add_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        def testConnection(IP, PORT, SERVICE_NAME):
            url_origin = u'http://'+IP+u':'+PORT+u'/ws-gateway/gateway/ws/'+SERVICE_NAME+'?wsdl'
            url = str(url_origin)
            auth = HttpAuthenticated(username='administrator', password='quative')
            try:
                client = Client(url,transport=auth)
                self.Result.append(SERVICE_NAME+u'Connect[add] Successfully')
                return url
            except:
                fp = StringIO.StringIO()
                traceback.print_exc(file = fp)
                message = fp.getvalue()
                self.Result.append(message)
        
        def getqamName():
            qamName = self.QAM_NAME.currentText()
            return qamName
            
        def getipAddress():
            ipAddress = self.QAM_IP.text()
            return ipAddress    
        
        def getServiceGroups_NAME():
            ServiceGroups_NAME = self.ServiceGroup.currentText()
            return ServiceGroups_NAME
            
        def getServiceGroup_UID(IP, PORT, ServiceGroup_NAME):
            url=testConnection(IP, PORT, 'qamservice')
            auth = HttpAuthenticated(username='administrator', password='quative')
            client = Client(url,transport=auth)
            ServiceGroup_info = client.service.getServiceGroupByName(ServiceGroup_NAME)
            ServiceGroup_UID = int(ServiceGroup_info.UID)
            return ServiceGroup_UID
        
        def getstatusCode():
            status = self.Status.currentText()
            return status    
            
        def getFreqNumber():
            FreqNumber = int(self.FreqNumber.text())
            return FreqNumber
            
        def getfrequencyHertz():
            frequencyHertz = int(self.Frequency.text())
            return frequencyHertz
            
        def getudpPorts():
            udpPort_start = int(self.UdpPortsfrom.text())
            udpPort_end = int(self.UdpPortsto.text())
            udpPort_interval = int(self.Interval.text())
            udpPorts = range(udpPort_start,udpPort_end+1,udpPort_interval)
            return udpPorts
            
        def getserviceIDs(udpPorts):
            ServiceID_end = udpPorts[len(udpPorts)-1] - udpPorts[0]
            serviceId_interval = int(self.Interval.text())
            serviceIDs = range(1, 1+ServiceID_end+1, serviceId_interval)
            return serviceIDs
        
        def getudpinfos(udpPorts,serviceIDs):
            udpInfos = zip(udpPorts,serviceIDs)
            return udpInfos
            
        def gettransportStreamID():
            transportStreamID = int(self.TSID.text())
            return transportStreamID
        
#        logging.basicConfig(level=logging.INFO)
#        logging.getLogger('suds.transport.http').setLevel(logging.DEBUG)    
        url=testConnection(SDP_IP, SDP_PORT, 'qamservice')
        auth = HttpAuthenticated(username='administrator', password='quative')
        client = Client(url,transport=auth)
        qamName=getqamName()
        ipAddress=getipAddress()
        ServiceGroups_NAME=getServiceGroups_NAME()
        serviceGroupUID=getServiceGroup_UID(SDP_IP, SDP_PORT,ServiceGroups_NAME)
        statusCode=getstatusCode()
        frequencyNumber=getFreqNumber()
        frequencyHertz=getfrequencyHertz()
        udpPorts=getudpPorts()
        serviceIDs=getserviceIDs(udpPorts)
        udpInfos=getudpinfos(udpPorts,serviceIDs)
        transportStreamID=gettransportStreamID()
        
        for udpInfo in udpInfos:
            servicegroupresource = client.factory.create('serviceGroupResource')
            servicegroupresource.frequencyHertz = frequencyHertz
            servicegroupresource.frequencyNumber = frequencyNumber
            servicegroupresource.ipAddress = ipAddress
            servicegroupresource.programNumber = udpInfo[1] 
            servicegroupresource.serviceGroupUID = serviceGroupUID
            servicegroupresource.serviceID = udpInfo[1]
            servicegroupresource.qamName = transportStreamID
            servicegroupresource.statusCode = statusCode
            servicegroupresource.transportStreamID = transportStreamID
            servicegroupresource.udpPort = udpInfo[0]
            try:
                result = client.service.createServiceGroupResource(servicegroupresource,checkConfig = False)
            except:
                fp = StringIO.StringIO()
                traceback.print_exc(file = fp)
                message = fp.getvalue()
                self.Result.append(message)
                break
            self.Result.append(u'Append: '+str(len(serviceIDs)))              
                
    @pyqtSignature("")
    def on_Clear_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.Result.clear()

    @pyqtSignature("")
    def on_Append_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        def testConnection(IP, PORT, SERVICE_NAME):
                url_origin = u'http://'+IP+u':'+PORT+u'/ws-gateway/gateway/ws/'+SERVICE_NAME+'?wsdl'
                url = str(url_origin)
                auth = HttpAuthenticated(username='administrator', password='quative')
                try:
                    client = Client(url,transport=auth)
#                    self.Result.append(SERVICE_NAME+u'Connect[append] Successfully')
                    return url
                except:
                    fp = StringIO.StringIO()
                    traceback.print_exc(file = fp)
                    message = fp.getvalue()
                    self.Result.append(message)
            
        def getqamName():
                qamName = self.QAM_NAME.currentText()
                return qamName
                
        def getipAddress():
                ipAddress = self.QAM_IP.text()
                return ipAddress    
            
        def getServiceGroups_NAME():
                ServiceGroups_NAME = self.ServiceGroup.currentText()
                return ServiceGroups_NAME
                
        def getServiceGroup_UID(IP, PORT, ServiceGroup_NAME):
                url=testConnection(IP, PORT, 'qamservice')
                auth = HttpAuthenticated(username='administrator', password='quative')
                client = Client(url,transport=auth)
                ServiceGroup_info = client.service.getServiceGroupByName(ServiceGroup_NAME)
                ServiceGroup_UID = int(ServiceGroup_info.UID)
                return ServiceGroup_UID
            
        def getstatusCode():
                status = self.Status.currentText()
                return status    
                
        def getFreqNumber():
                FreqNumber = int(self.FreqNumber.text())
                return FreqNumber
                
        def getfrequencyHertz():
                frequencyHertz = int(self.Frequency.text())
                return frequencyHertz
                
        def getudpPorts():
                udpPort_start = int(self.UdpPortsfrom.text())
                udpPort_end = int(self.UdpPortsto.text())
                udpPort_interval = int(self.Interval.text())
                udpPorts = range(udpPort_start,udpPort_end+1,udpPort_interval)
                return udpPorts
                
        def getserviceIDs(udpPorts):
                ServiceID_start = int(self.ServiceID_start.text())
                ServiceID_end = udpPorts[len(udpPorts)-1] - udpPorts[0]
                serviceId_interval = int(self.Interval.text())
                serviceIDs = range(ServiceID_start,ServiceID_start+ServiceID_end+1, serviceId_interval)
                return serviceIDs
            
        def getudpinfos(udpPorts,serviceIDs):
                udpInfos = zip(udpPorts,serviceIDs)
                return udpInfos
                
        def gettransportStreamID():
                transportStreamID = int(self.TSID.text())
                return transportStreamID
            
    #    logging.basicConfig(level=logging.INFO)
    #    logging.getLogger('suds.transport.http').setLevel(logging.DEBUG)    
        url=testConnection(SDP_IP, SDP_PORT, 'qamservice')
        auth = HttpAuthenticated(username='administrator', password='quative')
        client = Client(url,transport=auth)
        qamName=getqamName()
        ipAddress=getipAddress()
        ServiceGroups_NAME=getServiceGroups_NAME()
        serviceGroupUID=getServiceGroup_UID(SDP_IP, SDP_PORT,ServiceGroups_NAME)
        statusCode=getstatusCode()
        frequencyNumber=getFreqNumber()
        frequencyHertz=getfrequencyHertz()
        udpPorts=getudpPorts()
        serviceIDs=getserviceIDs(udpPorts)
        udpInfos=getudpinfos(udpPorts,serviceIDs)
        transportStreamID=gettransportStreamID()
            
        for udpInfo in udpInfos:
            servicegroupresource = client.factory.create('serviceGroupResource')
            servicegroupresource.frequencyHertz = frequencyHertz
            servicegroupresource.frequencyNumber = frequencyNumber
            servicegroupresource.ipAddress = ipAddress
            servicegroupresource.programNumber = udpInfo[1] 
            servicegroupresource.serviceGroupUID = serviceGroupUID
            servicegroupresource.serviceID = udpInfo[1]
            servicegroupresource.qamName = transportStreamID
            servicegroupresource.statusCode = statusCode
            servicegroupresource.transportStreamID = transportStreamID
            servicegroupresource.udpPort = udpInfo[0]
            try:
                result = client.service.createServiceGroupResource(servicegroupresource,checkConfig = False)
            except:
                fp = StringIO.StringIO()
                traceback.print_exc(file = fp)
                message = fp.getvalue()
                self.Result.append(message)
                break    
        self.Result.append(u'Append: '+str(len(serviceIDs))+u' resources into ' + str(transportStreamID))  
        
    @pyqtSignature("bool")
    def on_isDelete_toggled(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        def testConnection(IP, PORT, SERVICE_NAME):
                url_origin = u'http://'+IP+u':'+PORT+u'/ws-gateway/gateway/ws/'+SERVICE_NAME+'?wsdl'
                url = str(url_origin)
                auth = HttpAuthenticated(username='administrator', password='quative')
                try:
                    client = Client(url,transport=auth)
#                    self.Result.append(SERVICE_NAME+u'Connect[delete] Successfully')
                    return url
                except:
                    fp = StringIO.StringIO()
                    traceback.print_exc(file = fp)
                    message = fp.getvalue()
                    self.Result.append(message)
                    
        def getServiceGroups_NAME():
                ServiceGroups_NAME = self.ServiceGroup.currentText()
                return ServiceGroups_NAME
                
        def getServiceGroup_UID(IP, PORT, ServiceGroup_NAME):
                url=testConnection(IP, PORT, 'qamservice')
                auth = HttpAuthenticated(username='administrator', password='quative')
                client = Client(url,transport=auth)
                ServiceGroup_info = client.service.getServiceGroupByName(ServiceGroup_NAME)
                ServiceGroup_UID = int(ServiceGroup_info.UID)
                return ServiceGroup_UID
                
        def getresourceUIDs(IP, PORT, ServiceGroupUID):
                url = testConnection(IP, PORT, 'qamservice')
                auth = HttpAuthenticated(username='administrator', password='quative')
                client = Client(url,transport=auth)
                ServiceGroupsResources = client.service.getServiceGroupsResourceByServiceGroupUID(ServiceGroupUID)
                resourceUID_list=list()
                for i in range(0, len(ServiceGroupsResources)):
                    resourceUID_list.append(ServiceGroupsResources[i].UID)
                return resourceUID_list
        
        url=testConnection(SDP_IP, SDP_PORT, 'qamservice')
        auth = HttpAuthenticated(username='administrator', password='quative')
        client = Client(url,transport=auth)
        ServiceGroups_NAME=getServiceGroups_NAME()
        serviceGroupUID=getServiceGroup_UID(SDP_IP, SDP_PORT,ServiceGroups_NAME)
        resourceUIDs = getresourceUIDs(SDP_IP, SDP_PORT,serviceGroupUID)
        self.Result.append(u'Warning: there are '+ str(len(resourceUIDs))+' resources will be deleted cascade '+ str(ServiceGroups_NAME))
            
    @pyqtSignature("")
    def on_Delete_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        def testConnection(IP, PORT, SERVICE_NAME):
                url_origin = u'http://'+IP+u':'+PORT+u'/ws-gateway/gateway/ws/'+SERVICE_NAME+'?wsdl'
                url = str(url_origin)
                auth = HttpAuthenticated(username='administrator', password='quative')
                try:
                    client = Client(url,transport=auth)
#                    self.Result.append(SERVICE_NAME+u'Connect[delete] Successfully')
                    return url
                except:
                    fp = StringIO.StringIO()
                    traceback.print_exc(file = fp)
                    message = fp.getvalue()
                    self.Result.append(message)
                    
        def getServiceGroups_NAME():
                ServiceGroups_NAME = self.ServiceGroup.currentText()
                return ServiceGroups_NAME
                
        def getServiceGroup_UID(IP, PORT, ServiceGroup_NAME):
                url=testConnection(IP, PORT, 'qamservice')
                auth = HttpAuthenticated(username='administrator', password='quative')
                client = Client(url,transport=auth)
                ServiceGroup_info = client.service.getServiceGroupByName(ServiceGroup_NAME)
                ServiceGroup_UID = int(ServiceGroup_info.UID)
                return ServiceGroup_UID
                
        def getresourceUIDs(IP, PORT, ServiceGroupUID):
                url = testConnection(IP, PORT, 'qamservice')
                auth = HttpAuthenticated(username='administrator', password='quative')
                client = Client(url,transport=auth)
                ServiceGroupsResources = client.service.getServiceGroupsResourceByServiceGroupUID(ServiceGroupUID)
                resourceUID_list=list()
                for i in range(0, len(ServiceGroupsResources)):
                    resourceUID_list.append(int(ServiceGroupsResources[i].UID))
                return resourceUID_list          
                
        url=testConnection(SDP_IP, SDP_PORT, 'qamservice')
        auth = HttpAuthenticated(username='administrator', password='quative')
        client = Client(url,transport=auth)
        ServiceGroups_NAME=getServiceGroups_NAME()
        serviceGroupUID=getServiceGroup_UID(SDP_IP, SDP_PORT,ServiceGroups_NAME)
        resourceUIDs = getresourceUIDs(SDP_IP, SDP_PORT,serviceGroupUID)
        
        for resourceUID in resourceUIDs:
            try:
                result = client.service.deleteServiceGroupResource(resourceUID)
            except:
                fp = StringIO.StringIO()
                traceback.print_exc(file = fp)
                message = fp.getvalue()
                self.Result.append(message)
                break
        self.Result.append(u'Deleted '+str(len(resourceUIDs))+u' resources cascade '+str(ServiceGroups_NAME))
        
    @pyqtSignature("")
    def on_Reset_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.Frequency.clear()
        self.FreqNumber.clear()
        self.Interval.clear()
        self.UdpPortsfrom.clear()
        self.UdpPortsto.clear()
        self.TSID.clear()
        self.Add.setEnabled(True)
        self.Append.setDisabled(True)
        self.ServiceID_start.setDisabled(True)
        self.Delete.setDisabled(True)
#        self.ServiceID_start.setDisabled(True)
#        self.isAppend.clicked(False)
        
if __name__ == "__main__":  
  
    app = PyQt4.QtGui.QApplication(sys.argv)  
  
    myapp = addresourceforHamonic()  
  
    myapp.show()  
  
sys.exit(app.exec_())
    

