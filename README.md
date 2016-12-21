# Iotdm-python-library

This is a fork of
https://github.com/peterchauyw/iotdm-pyclient.git

For further documentation on the original see
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


## Functionality

The distribution is a Python framework to support a oneM2M compatible IoT client. Though the code cotains support for HTTP
and CoAP protocols the current status seems to be that only the HTTP operation is working correctly.

HTTP support can be included by importing iotdm_api.py - see example usage in http_example.py.

The API is limited in this version. Results of operations are not returned to the calling application (even success/failure indications).
 API results are recorded only as print statements in iotdm_api.py.

To run the examples - install and start the IoTDM oneM2M server on localhost following the instructions at:
https://wiki.opendaylight.org/view/IoTDM:Main#Getting_started_for_users


Navigate to the route directory for the library. The HTTP examples may then be run using the command:
```python http_example.py```

Various other files are included from the original distribution which do not appear to work currently:
- examples.py
- tests.py
- TS_13_Tests.py
- SendInfo.py
- criotdm.py

Pull requets to address the current limitations and to better document the existing functioanlity are welcome.
