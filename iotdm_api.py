import sys
import ciotdm
from urlparse import urlparse
import json
from txThings.examples.client import Agent
from twisted.internet import reactor
from twisted.python import log
import txThings.txthings.coap as coap
import txThings.txthings.resource as resource


class Iotdm_api():

	def __init__(self):
	    self.agent = Agent() 

	def start(self):
	    # Start any infrastructure needed for the API
	    log.startLogging(sys.stdout)
	    endpoint = resource.Endpoint(None)
	    self.protocol = coap.Coap(endpoint)
	    self.agent.start(self.protocol)

	def stop(self):
	    # Stop any infrastructure 
	    self.agent.stop()

	def restConf(self, URI, Cse_name, username, password):
	    uri = urlparse(URI)
	    (code, string) = ciotdm.reconf(uri.netloc, Cse_name, (username, password))
	    # print str(response[0]) + '\n' + response[1]
            return (code, string)

	def cleanup(self, URI, username, password):
	    uri = urlparse(URI)
	    (code, string) = ciotdm.kill(uri.netloc, (username, password))
	    # print str(response[0]) + '\n' + response[1]
            return (code, string)

	def create(self, URI, resource_type, payload, origin=None, requestID=None):
	    uri = urlparse(URI)
	    if uri.scheme == "http":
		(code, string) = ciotdm.create(URI, resource_type, payload, origin, requestID)
		# print str(response[0]) + '\n' + response[1]
	    elif uri.scheme == "coap":
		(code, string) = self.agent.request(self.protocol, "post", URI, payload=payload, ty=resource_type, origin=origin, requestID=requestID)
	    else:
		print "Invalid protocol."
		sys.exit(2)
            return (code, string)

	def retrieve(self, URI, origin=None, requestID=None):
	    uri = urlparse(URI)
	    if uri.scheme == "http":
		(code, string) = ciotdm.retrieve(URI, origin, requestID)
		# print str(response[0]) + '\n' + response[1]
	    elif uri.scheme == "coap":
		(code, string) = self.agent.request(self.protocol, "get", URI, origin=origin, requestID=requestID)
	    else:
		print "Invalid protocol."
		sys.exit(2)
            return (code, string)


	def update(self, URI, payload, origin=None, requestID=None):
	    uri = urlparse(URI)
	    if uri.scheme == "http":
		(code, string) = ciotdm.update(URI, payload, origin, requestID)
		# print str(response[0]) + '\n' + response[1]
	    elif uri.scheme == "coap":
		(code, string) = self.agent.request(self.protocol, "put", URI, payload=payload, origin=origin, requestID=requestID)
	    else:
		print "Invalid protocol."
		sys.exit(2)
            return (code, string)

	def delete(self, URI, origin=None, requestID=None):
	    uri = urlparse(URI)
	    if uri.scheme == "http":
		(code, string) = ciotdm.delete(URI, origin, requestID)
		# print str(response[0]) + '\n' + response[1]
	    elif uri.scheme == "coap":
		(code, string) = self.agent.request(self.protocol, "delete", URI, origin=origin, requestID=requestID)
	    else:
		print "Invalid protocol."
		sys.exit(2)
            return (code, string)

