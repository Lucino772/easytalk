import time

from easytalk import Stream, Item


# Callback for incoming data
def on_data(msg_id: str,data: bytes,channel: int):
    # Do somthing with data
    return b'Hello World !' # Return a response

s = Stream.from_sys() # Create a stream instance
i = Item(s,autoclose=True) # Create an item instance
i.listen(on_data) # Start listening for data

time.sleep(1)