import sys
import ciotdm
from urlparse import urlparse
import json
from txThings.examples.client import Agent
from twisted.internet import reactor
from twisted.python import log
import iotdm_robot.txThings.txthings.coap as coap
import iotdm_robot.txThings.txthings.resource as resource
from iotdm_robot.onem2m_xml_protocols.ae import ae
from iotdm_robot.onem2m_xml_protocols.container import cnt
from iotdm_robot.onem2m_xml_protocols.contentinstance import cin
from iotdm_robot.onem2m_xml_protocols.subscription import sub


'''to-do: payload serialisation'''


def restConf(URI, Cse_name, username, password):
    uri = urlparse(URI)
    response = ciotdm.reconf(uri.netloc, Cse_name, (username, password))
    print str(response[0]) + '\n' + response[1]


def cleanup(URI, username, password):
    uri = urlparse(URI)
    response = ciotdm.kill(uri.netloc, (username, password))
    print str(response[0]) + '\n' + response[1]


def create(URI, resource_type, resource_name, payload):
    uri = urlparse(URI)
    if uri.scheme == "http":
        response = ciotdm.create(URI, resource_type, payload, resource_name)
        print str(response[0]) + '\n' + response[1]

    elif uri.scheme == "coap":
        log.startLogging(sys.stdout)
        endpoint = resource.Endpoint(None)
        protocol = coap.Coap(endpoint)
        Agent(protocol, "post", URI, payload, resource_type, resource_name)
        reactor.listenUDP(0, protocol)
        reactor.run()

    else:
        print "Invalid protocol."
        sys.exit(2)

def retrieve(URI):
    uri = urlparse(URI)
    if uri.scheme == "http":
        response = ciotdm.retrieve(URI)
        print str(response[0]) + '\n' + response[1]

    elif uri.scheme == "coap":
        log.startLogging(sys.stdout)
        endpoint = resource.Endpoint(None)
        protocol = coap.Coap(endpoint)
        Agent(protocol, "get", URI)
        reactor.listenUDP(0, protocol)
        reactor.run()

    else:
        print "Invalid protocol."
        sys.exit(2)


def update(URI, resource_type, attribute):
    uri = urlparse(URI)
    if uri.scheme == "http":
        response = ciotdm.update(URI, resource_type, attribute)
        print str(response[0]) + '\n' + response[1]

    elif uri.scheme == "coap":
        log.startLogging(sys.stdout)
        endpoint = resource.Endpoint(None)
        protocol = coap.Coap(endpoint)
        Agent(protocol, "put", URI)
        reactor.listenUDP(0, protocol)
        reactor.run()

    else:
        print "Invalid protocol."
        sys.exit(2)

def delete(URI):
    uri = urlparse(URI)
    if uri.scheme == "http":
        response = ciotdm.delete(URI)
        print str(response[0]) + '\n' + response[1]

    elif uri.scheme == "coap":
        log.startLogging(sys.stdout)
        endpoint = resource.Endpoint(None)
        protocol = coap.Coap(endpoint)
        Agent(protocol, "delete", URI)
        reactor.listenUDP(0, protocol)
        reactor.run()

    else:
        print "Invalid protocol."
        sys.exit(2)


#restConf('http://localhost', 'ODL-oneM2M-Cse', 'admin', 'admin')

#cleanup('http://localhost', 'admin', 'admin')



AE = ae()
AE.set_api("TestAppId")
AE.set_apn("testAppName")
AE.set_or("http://ontology/ref")
AE.set_rr(True)
payload = AE.to_JSON()
create("http://127.0.0.1:8282/ODL-oneM2M-Cse", 2, "AE10", payload)




# container = cnt()
# container.set_mbs(30)
# container.set_or("http://hey/you")
# container.set_lbl(["key1"])
# payload = container.to_JSON()
# create("coap://127.0.0.1:5683/ODL-oneM2M-Cse/AE", 3, "Container", payload)




# con_instance = cin()
# con_instance.set_con("37")
# payload = con_instance.to_JSON()
# create("coap://127.0.0.1:5683/ODL-oneM2M-Cse/AE/Container", 4, "Instance", payload)



# subscription = sub()
# subscription.set_nu(["10.195.131.12"])
# payload  = subscription.to_JSON()
# create("coap://127.0.0.1:5683/ODL-oneM2M-Cse/AE/Container", 23, "sub1", payload)



#retrieve("http://127.0.0.1:8282/ODL-oneM2M-Cse?fu=1")

#update("http://127.0.0.1:8282/ODL-oneM2M-Cse/AE3", 2, '"apn":"testAppName", "or":"http://ontology/ref","rr":true')

#delete("http://127.0.0.1:8282/ODL-oneM2M-Cse/AE4")