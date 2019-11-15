# EasyTalk

**EasyTalk**  makes communication **easier** between subprocess or even sockets.

It's very easy to use and simple to understand.

# Installation
The package will be soon available on PyPi but for now you must install it from the github repo for that you will need git.

You will also need python 3.6+.

```
pip install git+https://github.com/Lucino772/easytalk.git
```
OR
```
git clone https://github.com/Lucino772/easytalk.git
cd easytalk/
python setup.py install
```

# Documentation
## Stream Object
**Initialize a Stream object**
 ```
# From custom stream
input_stream = ...
output_stream = ...
stream_obj = Stream(input_stream,output_stream)

# From standard output/input
stream_obj = Stream.from_sys()

# From socket
stream_obj = Stream.from_sock(socket_obj)

# From subprocess
stream_obj = Stream.from_subprocess(popen_obj)
```
**Send data**
```
input_stream = ...
output_stream = ...

stream_obj = Stream(input_stream,output_stream)

stream_obj.send(b'Hello World !')
```
**Receive data**
```
input_stream = ...
output_stream = ...

stream_obj = Stream(input_stream,output_stream)

data = stream_obj.recv(b'Hello World !')
print(data)
```
## Item Object
**Initialize an Item Object**
```
input_stream = ...
output_stream = ...

stream_obj = Stream(input_stream,output_stream)

item_obj = Item(stream_obj)
```
The Item object gives you 2 more advanced functionnalities:
- Listen for data
```
def on_data(msg_id,msg):
	# Do something
	return b'Hello this is my response !' # Will send a response back

item_obj.listen(on_data=on_data)
```
- Send and directly receive the response
```
! You must be listening for data if you want this to work !

# When you send data set the response parameter to true
response = item_obj.send(b'Hello, this is my request !',response=True)
print(response)
```

# Examples
[Go check the examples](https://github.com/Lucino772/easytalk/tree/master/examples)

# Reporting bugs
If you find any bug in EasyTalk please report it on the [Github issue tracker](https://github.com/Lucino772/easytalk/issues)
