class measurement:
    """
    This class represents a measurement taken from a sensor.
    """

    def __init__(self, timestamp, value, unit):
        self.timestamp = timestamp
        self.value = value
        self.unit = unit




# TODO: Add your own classes here!


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
    
    floors = []
    rooms = []
    devices = {"Room":[],"Device":[]}
    deviceTypes = {}


    def register_floor(self, level):#funker
        """
        This method registers a new floor at the given level in the house
        and returns the respective floor object.
        """
        SmartHouse.floors.append(floor(level))
        return SmartHouse.floors[-1] 

    def register_room(self, floor, room_size, room_name = None):#funker
        """
        This methods registers a new room with the given room areal size 
        at the given floor. Optionally the room may be assigned a mnemonic name.
        """
        SmartHouse.rooms.append(room(room_name,room_size,floor))
 


    def get_floors(self):#funker
        """
        This method returns the list of registered floors in the house.
        The list is ordered by the floor levels, e.g. if the house has 
        registered a basement (level=0), a ground floor (level=1) and a first floor 
        (leve=1), then the resulting list contains these three flors in the above order.
        """
        sorted_floors = SmartHouse.floors.sort()

        return sorted_floors


    def get_rooms(self):#funker
        """
        This methods returns the list of all registered rooms in the house.
        The resulting list has no particular order.
        """

        return SmartHouse.rooms


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
        #SmartHouse.devices.append(room, device)
        
        SmartHouse.devices["Room"].append(room)
        SmartHouse.devices["Device"].append(device)

    
    def register_deviceType(self, ID, Manufacturer,model, devicetype, nickname):
        """
        This methods registers a given device in a given room.
        """
        SmartHouse.deviceTypes.append(ID, Manufacturer,model, devicetype, nickname)


    def get_devices(self):
        numDevice = (SmartHouse.devices)
        return numDevice
    
    def get_device_by_id(self, device_id):
        """
        This method retrieves a device object via its id.
        """
        for noe in SmartHouse.devices:
            if noe.device.device_id == device_id:
                return noe.device
            else:
                return print("ingen enheter med denne id")



class building:
    def __init__(self,floors:[],rooms:[]) -> None:
        self.floors = floors
        self.rooms = rooms
    
     
        

class floor:
    def __init__(self,floorNumber : int, ) -> None:
        self.floorNumber = floorNumber

    #def calculateArea(self, SmartHouse.rooms):
        
        pass

class room:
    def __init__(self, name : str, area:float, floor:int) -> None:
        self.name = name
        self.area = area
        self.floor = floor
        pass

class device:
    def __init__(self, ID:str, manufacturer:str, model:str, deviceType:str, nickname:str) -> None:
        self.ID = ID
        self.manufacturer = manufacturer
        self.model = model
        self.deviceType = deviceType
        self.nickname = nickname
        

class actuator(device):
    def __init__(self, ID: int, manufacturer: str, model: str, deviceType: str, nickname: str, state) -> None:
        super().__init__(ID, manufacturer, model, deviceType, nickname)
        self.state = state
    def changeState(newState):
        #.......
        pass

class sensor(device):
    def __init__(self, ID: int, manufacturer: str, model: str, deviceType: str, nickname: str) -> None:
        super().__init__(ID, manufacturer, model, deviceType, nickname)
        self.measurements = []  # Lager for å holde målinger

    def getCurrentValue(self):
        
        if self.measurements:
            return self.measurements[-1].value
        else:
            return None
        
    def addMeasurement(self,measurement):
        self.measurements.append(measurement)

    def getHistory(self):
        return self.measurements
        



        

    


