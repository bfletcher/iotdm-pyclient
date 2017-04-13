# class Iotdm_api()

See also https://wiki.opendaylight.org/view/IoTDM:PythonAPI
Modifications to that API are:

 - return values
 - start and stop calls for the CoAP processing thread

## Iotdm_api calls

```
	def startCoap(self)
```

Starts the reactor thread for the CoAP library

```
	def stopCoap(self)
```

Stops the reactor thread

```
	def restConf(self, URI, Cse_name, username, password):
            return (code, string)
```

Provisions the root of the tree. Needs to be called via http. ```code``` and ```string``` contain the response code 
and response string if the call succeeds, otherwise they contain ```None```.

```
	def cleanup(self, URI, username, password):
            return (code, string)
```

```
	def create(self, URI, resource_type, payload, origin=None, requestID=None):
            return (code, string)
```

POST request. URI is parsed to see if http or CoAP is required

```
	def retrieve(self, URI, origin=None, requestID=None):
            return (code, string)
```

GET request. URI is parsed to see if http or CoAP is required

```
	def update(self, URI, payload, origin=None, requestID=None):
            return (code, string)
```

PUT request. URI is parsed to see if http or CoAP is required
```
	def delete(self, URI, origin=None, requestID=None):
            return (code, string)
```

DELETE request. URI is parsed to see if http or CoAP is required
