from smarthouse.domain import SmartHouse

DEMO_HOUSE = SmartHouse()


# Building house structure
ground_floor = DEMO_HOUSE.register_floor(1)
entrance = DEMO_HOUSE.register_room(ground_floor, 13.5, "Entrance")
garage = DEMO_HOUSE.register_room(ground_floor, 19.0, "Garage")
guestRoom1 = DEMO_HOUSE.register_room(ground_floor, 8.0, "Guest Room 1")
Bathroom1 = DEMO_HOUSE.register_room(ground_floor, 6.3, "Bathroom 1")
LivingRoomKitchen = DEMO_HOUSE.register_room(ground_floor, 39.75, "LivingRoom/Kitchen")

first_floor = DEMO_HOUSE.register_floor(2)
Hallway = DEMO_HOUSE.register_room(first_floor, 10.0, "Hallway")
guestRoom2 = DEMO_HOUSE.register_room(first_floor, 8.0, "Guest Room 2")
Bathroom2 = DEMO_HOUSE.register_room(first_floor, 9.25, "Bathroom 2")
Office = DEMO_HOUSE.register_room(first_floor, 11.75, "Office")
guestRoom3 = DEMO_HOUSE.register_room(first_floor, 10.0, "Guest Room 3")
DressingRoom = DEMO_HOUSE.register_room(first_floor, 4.0, "Dressing Room")
Masterbedroom = DEMO_HOUSE.register_room(first_floor, 17.0, "Master bedroom")

#devices


#test = DEMO_HOUSE.register_deviceType("cd5be4e8-0e6b-4cb5-a21f-819d06cf5fc5", "NebulaGuard Innovations", "MoveZ Detect 69", "Motion Sensor", "Motion sensor")

motion_sensor = ("cd5be4e8-0e6b-4cb5-a21f-819d06cf5fc5", "NebulaGuard Innovations", "MoveZ Detect 69", "Motion Sensor", "Motion sensor")
Motion_Sensor = DEMO_HOUSE.register_device(LivingRoomKitchen, motion_sensor)

smartlock = ("4d5f1ac6-906a-4fd1-b4bf-3a0671e4c4f1", "MythicalTech", "Guardian Lock 7000", "actuator", "Smart lock" )
SmartLock = DEMO_HOUSE.register_device(entrance, smartlock)

c02_sensor = ("8a43b2d7-e8d3-4f3d-b832-7dbf37bf629e", "ElysianTech", "Smoke Warden 1000","CO2 sensor","CO2 sensor" )
CO2_Sensor = DEMO_HOUSE.register_device(LivingRoomKitchen, c02_sensor)

electricity_meter= ("a2f8690f-2b3a-43cd-90b8-9deea98b42a7", "MysticEnergy Innovations", "Volt Watch Elite","Electricity Meter","Electricity Meter	" )
Electricity_Meter = DEMO_HOUSE.register_device(LivingRoomKitchen, c02_sensor)



#SmartLock = DEMO_HOUSE.register_device(entrance, smartlock )
# TODO: continue registering the remaining floor, rooms and devices

