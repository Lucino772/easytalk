from typing import NamedTuple, Any
from easytalk.classes.stream import Stream

class Channel(NamedTuple):
    id: int
    name: str
    on_data: Any

class Channels:

    def __init__(self):
        self.__channels = []
    
    def add_channel(self,_id: int,name=None,on_data=None):
        if _id > 255 or _id < 0:
            return
        _name = (name or 'Channel_' + '{}'.format(_id).zfill(3))
        channel = Channel(id=_id,name=_name,on_data=on_data)
        self.__channels.append(channel)

    def get_channel(self,_id: int) -> Channel:
        r = list(filter(lambda x: x.id == _id,self.__channels))
        if len(r) > 0:
            return r[0]
        return None
    
    def exists(self,_id: int):
        return (not self.get_channel(_id) == None)
