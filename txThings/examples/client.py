'''
Created on 08-09-2012

@author: Maciej Wasilak

Modified on 01-07-2016

@by: Peter Chau
'''

import sys
import threading
from urlparse import urlparse
import OneM2M
import socket
from twisted.internet import reactor
import txThings.txthings.coap as coap
# from twisted.internet.defer import Deferred
# from twisted.internet.protocol import DatagramProtocol
# from twisted.python import log
# import txThings.txthings.resource as resource

syncEvent = threading.Event()

class Agent():

    def start(self, protocol):
        print("Start reactor and UDP")
        reactor.listenUDP(0, protocol)
        threading.Thread(target=reactor.run, args=(False,)).start()

    def stop(self):
        print("Stop reactor")
        reactor.callFromThread(reactor.stop)

    def request(self, protocol, op, uri, payload=None, ty=None, origin=None, requestID=None):
        self.protocol = protocol
        self.ty = ty
        self.uri = urlparse(uri)
        tmp = self.uri.netloc.split(':')
        self.host = socket.gethostbyname(tmp[0])
        self.path = self.uri.path.strip("/")
        self.query = self.uri.query
        self.payload = payload
        self.origin = origin
        self.requestID = requestID
        syncEvent.clear()
        if op == "post":
            self.postResource()
        elif op == "get":
            self.getResource()
        elif op == "put":
            self.putResource()
        elif op == "delete":
            self.deleteResource()
        else:
            print "Invalid operation"
            sys.exit(2)
        syncEvent.wait()

    def postResource(self):

        request = coap.Message(code=coap.POST, payload=self.payload)
        request.opt.uri_host = (self.host,)
        request.opt.uri_port = int(self.uri.port)
        request.opt.uri_query = ("ty="+str(self.ty),)
        request.opt.uri_path = (self.path,)
        request.opt.content_format = coap.media_types_rev['application/json']
        if self.origin is not None:
            request.opt.oneM2M_FR = (self.origin,)
        else:
            request.opt.oneM2M_FR = ("//localhost:10000",)
        if self.requestID is not None:
            request.opt.oneM2M_RQI = (self.requestID,)
        else:
            request.opt.oneM2M_RQI = ("12345",)
        request.opt.oneM2M_TY = self.ty
        request.remote = (self.host, coap.COAP_PORT)
        d = self.protocol.request(request)
        d.addCallback(self.printResponse)
        d.addErrback(self.noResponse)
        d.addBoth(self.releaseBlocking)


    def getResource(self):

        request = coap.Message(code=coap.GET)
        request.opt.uri_path = (self.path,)
        request.opt.uri_query = (self.query,)
        if self.origin is not None:
            request.opt.oneM2M_FR = (self.origin,)
        else:
            request.opt.oneM2M_FR = ("//localhost:10000",)
        if self.requestID is not None:
            request.opt.oneM2M_RQI = (self.requestID,)
        else:
            request.opt.oneM2M_RQI = ("12345",)
        request.opt.observe = 0
        request.remote = (self.host, coap.COAP_PORT)
        d = self.protocol.request(request)
        d.addCallback(self.printResponse)
        d.addErrback(self.noResponse)
        d.addBoth(self.releaseBlocking)


    def putResource(self):

        request = coap.Message(code=coap.PUT, payload=self.payload)
        request.opt.uri_host = (self.host,)
        request.opt.uri_port = int(self.uri.port)
        request.opt.uri_path = (self.path,)
        request.opt.content_format = coap.media_types_rev['application/json']
        if self.origin is not None:
            request.opt.oneM2M_FR = (self.origin,)
        else:
            request.opt.oneM2M_FR = ("//localhost:10000",)
        if self.requestID is not None:
            request.opt.oneM2M_RQI = (self.requestID,)
        else:
            request.opt.oneM2M_RQI = ("12345",)
        request.remote = (self.host, coap.COAP_PORT)
        d = self.protocol.request(request)
        d.addCallback(self.printResponse)
        d.addErrback(self.noResponse)
        d.addBoth(self.releaseBlocking)

    def deleteResource(self):

        request = coap.Message(code=coap.DELETE)
        request.opt.uri_path = (self.path,)
        if self.origin is not None:
            request.opt.oneM2M_FR = (self.origin,)
        else:
            request.opt.oneM2M_FR = ("//localhost:10000",)
        if self.requestID is not None:
            request.opt.oneM2M_RQI = (self.requestID,)
        else:
            request.opt.oneM2M_RQI = ("12345",)
        request.opt.observe = 0
        request.remote = (self.host, coap.COAP_PORT)
        d = self.protocol.request(request)
        d.addCallback(self.printResponse)
        d.addErrback(self.noResponse)
        d.addBoth(self.releaseBlocking)

    def gotIP(ip):
        return ip

    def printResponse(self, response):
        print 'Response Code: ' + coap.responses[response.code]
        print 'Payload: ' + response.payload

    def noResponse(self, failure):
        print 'Failed to fetch resource:'
        print failure

    def releaseBlocking(self, _ ):
        print 'Sync Event'
        syncEvent.set()

