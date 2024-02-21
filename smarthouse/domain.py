from multiprocessing import Value
from pickle import TRUE
from typing import Optional


class measurement:
    """
    This class represents a measurement taken from a sensor.
    """

    def __init__(self, timestamp, value, unit):
        self.timestamp = timestamp
        self.value = value
        self.unit = unit




# TODO: Add your own classes here!d


class SmartHouse:
    """
    This class serves as the main entity and entry point for the SmartHouse system app.
    Do not delete this class nor its predefined methods since other parts of the
    application may depend on it (you are free to add as many new methods as you like, though).

    The SmartHouse class provides functionality to register rooms and floors (i.e. changing the 
    house's physical layout) as well as register and modify smart devices and their state.
    """
    #def __init__(self,floors:[],rooms:[]) -> None:
    # self.floors = floors
    #self.rooms = rooms
    def __init__(self):

        self.floors = []
        self.rooms = []
    #devices = {"Room":[],"Device":[]}
        self.devices = []
    #deviceTypes = {}


    def register_floor(self, level):#funker
        """
        This method registers a new floor at the given level in the house
        and returns the respective floor object.
        """
        self.floors.append(floor(level))
        return self.floors[-1] 

    def register_room(self, floor, room_size, room_name):#funker
        """
        This methods registers a new room with the given room areal size 
        at the given floor. Optionally the room may be assigned a mnemonic name.
        """
        devices = []
        r = room(room_name,room_size,floor, devices)
        self.rooms.append(r)
        return r


    def get_floors(self):#funker
        """
        This method returns the list of registered floors in the house.
        The list is ordered by the floor levels, e.g. if the house has 
        registered a basement (level=0), a ground floor (level=1) and a first floor 
        (leve=1), then the resulting list contains these three flors in the above order.
        """
        #tror sort sorterer listen og returnere none. dermed trenger den ikke å få en variabel
        #sorted_floors = SmartHouse.floors.sort()
        self.floors.sort()


        return self.floors

    def get_rooms(self):#funker
        """
        This methods returns the list of all registered rooms in the house.
        The resulting list has no particular order.
        """

        return self.rooms


    def get_area(self):#funker
        """
        This methods return the total area size of the house, i.e. the sum of the area sizes of each room in the house.
        """ 
        allRooms = SmartHouse.get_rooms(self)

        allArea = []
        
        for noe in allRooms:
            allArea.append(noe.area)


        totalArea = sum(allArea)
        return totalArea
    
    def register_device(self, room, device):
        """
        This methods registers a given device in a given room.
        """
        ##prøver å fjerne enheten om vi legger til en enhet som allerede finnes
     
        ##checking if the device exists
        #SmartHouse.devices.append(room, device)
        for old in self.devices:
            if old.id == device.id:
                self.devices.remove(old)

                return old
            

        
        #room.devices.remove(device)
        device.room = room
        

        self.devices.append(device)
        room.devices.append(device) ###fiiiiikskskssk

        #SmartHouse.devices["Room"].append(room)
        #SmartHouse.devices["Device"].append(device)

    
    #def register_deviceType(self, ID, supplier,model_name, devicetype, nickname):
        """
        This methods registers a given device in a given room.
        """
        #SmartHouse.deviceTypes.append(ID, supplier,model_name, devicetype, nickname)


    def get_devices(self):
        numDevice = (self.devices)
        return numDevice
    


    def get_device_by_id(self, device_id):
        # Gå gjennom hver enhet i listen 'Device'

        for room in self.rooms:
            for device in room.devices:
                if device.id == device_id:
                    return device 
                


#for device in self.devices[]:
#    if device.ID == device_id:  # Juster dette hvis strukturen er annerledes
        # Returner enheten hvis ID-en matcher
#        return device 

# Returner None hvis ingen enhet med gitt ID ble funnet
# return None


    
   # def get_device_by_id(self, device_id):
    #    """
     #   This method retrieves a device object via its id.
      #  """
       # for noe in SmartHouse.devices:
        #    if noe.device.device_id == device_id:
         #       return noe.device
          #  else:
           #     return print("ingen enheter med denne id")



class building:
    def __init__(self,floors:[],rooms:[]) -> None:
        self.floors = floors
        self.rooms = rooms
    
     
        

class floor:
    def __init__(self,floorNumber : int, ):
        self.floorNumber = floorNumber

    #def calculateArea(self, SmartHouse.rooms):
        
        

class room:
    def __init__(self, room_name : str, area:float, floor:int, devices):
        self.room_name = room_name
        self.area = area
        self.floor = floor
        self.devices = []
        #listname = "devices_in_"+ name
        #listname[]

       

class Device:
    def __init__(self, id:str, supplier:str, model_name:str, device_type:str, nickname:str, room):
        self.id = id
        self.supplier = supplier
        self.model_name = model_name
        self.device_type = device_type
        self.nickname = nickname
        self.room = room
        

class actuator(Device):
    def __init__(self, id: str, supplier: str, model_name: str, device_type: str, nickname: str, room,  state:bool):
        super().__init__(id, supplier, model_name, device_type, nickname, room)
        self.state = state
        

    def is_sensor(self):
        return False
    def is_actuator(self):
        return True
    def changeState(newState):
        #.......
        pass

    
    def turn_on(self,value=None):
        self.state = True
        self.value = value
        return self.state
    
    def is_active(self):
        if self.state:
            return True
        else:
            return False
        
    def turn_off(self):
        self.state = False
        


class sensor(Device):
    def __init__(self, id: str, supplier: str, model_name: str, device_type: str, nickname: str, room, unit):
        super().__init__(id, supplier, model_name, device_type, nickname, room)
        self.measurements = [] # Lager for å holde målinger
        self.unit = unit
        

    def last_measurement(self):
        return self.measurements[-1]

        
    def addMeasurement(self,value,unit):

        self.measurements.append(measurement("now",value, unit))

    def getHistory(self):
        return self.measurements
    def is_sensor(self):
        return TRUE
    def is_actuator(self):
        return False
        



        

    


