from easytalk.classes.stream import Stream

reader, writer = Stream.from_sys()

# SEND DATA
writer.send(b'Hello World !')

# SEND DATA WITH CHANNEL ID
writer.send(b'Hello, using channel id',channel_id=68)
