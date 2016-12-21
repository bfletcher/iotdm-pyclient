# File to demonstate operation of Python API using HTTP protocol to talk to host
# To operate run IoTDM server on localhost as described at:
# https://wiki.opendaylight.org/view/IoTDM:Main#Getting_started_for_users
# Contents of this file is based on:
# https://wiki.opendaylight.org/view/IoTDM:PythonAPI

# December 2016
# Author: Iain Sharp


import iotdm_api
from onem2m_xml_protocols.ae import *
from onem2m_xml_protocols.container import *
from onem2m_xml_protocols.contentinstance import *

# Build the root CSE base of a tree by Restconf:
iotdm_api.restConf('http://localhost', 'InCSE1', 'admin', 'admin')

# Creation of an AE named "myAE" under the CSE base "InCSE1".
AE = ae()
AE.set_api("Nk836-t071-fc022")
AE.set_rr(True)
AE.set_rn("myAE")
payload = AE.to_JSON()
iotdm_api.create("http://localhost:8282/InCSE1", 2, payload, origin="AE-ID", requestID="12345")

# Creation of a Container named "myContainer" with a maximum number of bytes of 32, under "myAE".
container = cnt()
container.set_rn("myContainer")
container.set_mbs(32)
payload = container.to_JSON()
iotdm_api.create("http://localhost:8282/InCSE1/myAE", 3, payload, origin="AE-ID", requestID="12345")

# Creation of a Container named "mySubContainer" with a maximum number of instances of 5, under "myContainer".
container = cnt()
container.set_rn("mySubContainer")
container.set_mni(5)
payload = container.to_JSON()
iotdm_api.create("http://localhost:8282/InCSE1/myAE/myContainer", 3, payload, origin="AE-ID", requestID="12345")

# Creation of a Content Instance named "myContentInstance" under "myContainer", with "hello" as its content.
con_instance = cin()
con_instance.set_con("hello")
con_instance.set_rn("myContentInstance")
payload = con_instance.to_JSON()
iotdm_api.create("http://localhost:8282/InCSE1/myAE/myContainer", 4, payload, origin="AE-ID", requestID="12345")

# Creation of a Content Instance named "myOtherContentInstance" under "mySubContainer", with "world" as its content.
con_instance = cin()
con_instance.set_con("world")
con_instance.set_rn("myOtherContentInstance")
payload = con_instance.to_JSON()
iotdm_api.create("http://localhost:8282/InCSE1/myAE/myContainer/mySubContainer", 4, payload, origin="AE-ID", requestID="12345")

# Update of the Container "myContainer", with its attribute "Ontology Reference" being set to "http://info"
container = cnt()
container.set_or("http://info")
payload = container.to_JSON()
iotdm_api.update("http://localhost:8282/InCSE1/myAE/myContainer", payload, origin="AE-ID", requestID="12345")

# Update of the Container "mySubContainer", with its attribute "label" being set to "submarine"
container = cnt()
container.set_lbl(["submarine"])
payload = container.to_JSON()
iotdm_api.update("http://localhost:8282/InCSE1/myAE/myContainer/mySubContainer", payload, origin="AE-ID", requestID="12345")

# Deletion of the ContentInstance "myContentInstance"
iotdm_api.delete("http://localhost:8282/InCSE1/myAE/myContainer/myContentInstance", origin="AE-ID", requestID="12345")