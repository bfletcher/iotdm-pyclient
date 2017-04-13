# Iotdm-python-library

This is a fork of:
https://github.com/peterchauyw/iotdm-pyclient.git

For further documentation on the original see:
https://wiki.opendaylight.org/view/IoTDM:PythonAPI


## Installation and dependencies

This library is for Python 2.7

The following Python dependencies exist:

1. Requests Library
  `sudo pip install requests`
2. psutil library
  `sudo pip install psutil`
3. Twisted Library
4. lxml Library


## Functionality and Limitations

The distribution is a Python framework to support a oneM2M compatible IoT client with HTTP and CoAP protocol support. 
API results are returned as (responseCode, responseString) for both http and CoAP requests.

When using the CoAP protocol functions they block until a response has been received. To achieve this, the twisted reactor runs in a separate thread.

Examples showing CoAP and HTTP may also be seen at:
https://wiki.opendaylight.org/view/IoTDM:PythonAPI

Note that the examples at Open Daylight do not show the return values from the API or the CoAP ```start()```, ```stop()``` calls.

HTTP and CoAP support can be included by importing iotdm_api.py - see example usage in http_example.py or TS_13_Tests.py.

To run the examples - install and start the IoTDM oneM2M server on localhost following the instructions at:
https://wiki.opendaylight.org/view/IoTDM:Main#Getting_started_for_users

Invoke the example commands below from the root directory for the library. 

## HTTP Examples 


The HTTP examples may be run using the command:
```
python http_example.py
```

## CoAP Examples 

CoAP examples may be seen by invoking tests from the module ```TS_13_Tests.py```.

```
python TS_13_Tests.py 
```

The CoAP test sequence in ```TS_13_Tests.py``` carries out various operations within a resource tree under a CSE base. The CoAP results have been confirmed vs using the TS_13 test collection via Postman and HTTP. The results are the same. TS_13 collection tests that fail on both Postman and this client have been removed. 

## Further Info

This project includes commits cherry-picked from https://github.com/sharpie7/iotdm-pyclient

## Todo

 - The project uses a fork of txthings for historic reasons. It would be sensible to move to use the upstream version.
 - The combination of twisted and threads used here is not fully thread-safe (yet). Consider before using as part of your starship's life-support systems.
