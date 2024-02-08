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

SmartLock = DEMO_HOUSE.register_device(entrance, )
# TODO: continue registering the remaining floor, rooms and devices

