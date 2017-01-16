# Iotdm-python-library

This is a fork of:
https://github.com/peterchauyw/iotdm-pyclient.git

For further documentation on the original see:
https://wiki.opendaylight.org/view/IoTDM:PythonAPI


## Installation and dependencies

This library is  for Python 2.7

The following Python dependencies exist:

1. Requests Library
  `sudo pip install requests`
2. psutil library
  `sudo pip install psutil`
3. Twisted Library
4. lxml Library

The distribution directory ".idea" includes project files for the PyCharm IDE.


## Functionality and Limitations

The distribution is a Python framework to support a oneM2M compatible IoT client with HTTP and CoAP protocol support. The API is limited in this version. Results of operations are not returned to the calling application (even success/failure indications).
 API results are recorded only as print statements.

When using the CoAP protocol functions return before the protocol has been completely cleaned. There is no option for synchronous (blocking) use of the function or a mechanism in the API to determine if the protocol is ready to accept new commands. Therefore successive calls to CoAP functions must be well spaced in time if calls other than the initial call are to be successful.

Examples showing CoAP and HTTP may be seen at:
https://wiki.opendaylight.org/view/IoTDM:PythonAPI
but note this does not show all necessary Python imports therefore it may be better to refer to the example scripts below. 

## HTTP Examples in the Distribution

HTTP support can be included by importing iotdm_api.py - see example usage in http_example.py.

To run the examples - install and start the IoTDM oneM2M server on localhost following the instructions at:
https://wiki.opendaylight.org/view/IoTDM:Main#Getting_started_for_users

Navigate to the route directory for the library. The HTTP examples may then be run using the command:
```
python http_example.py
```

## CoAP Examples in the Distribution

CoAP examples may be seen by invoking individual tests from the module ```TS_13_Tests.py```.
For example:
```
python TS_13_Tests.py TS13.test_0_CSE_Provisioning
# This example actually uses HTTP but is necessary to initialize the server.
python TS_13_Tests.py TS13.test_TD_M2M_NH_01_Retrieve_CSEBase
# Get CSE Base using CoAP
```

The lack of synchronous support for calls to CoAP based procedues means that running the whole ```TS_13_Tests.py``` as a block will fail as the incomplete operation of earlier procedures will cause errors on subsequent procedures.

## Other Examples
Various other files are included from the original distribution which do not appear to work currently:
- examples.py
- tests.py
- SendInfo.py
- criotdm.py

Pull requets to address the current limitations and to better document the existing functioanlity are welcome.
