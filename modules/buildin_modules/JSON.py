# use dictionary formats
# JSON is always a string
import json
x='{"name":"saliha","age":21}'
print(type(x))
#parsing JSON to python
y=json.loads(x)
print(type(y))

#parsing python to json
y=json.dumps(x)
print(type(y))
