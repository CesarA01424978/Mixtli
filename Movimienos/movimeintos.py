from djitellopy import Tello

dron = Tello()

dron.connect() #wifi
dron.takeoff() #despejar
dron.rotate_clockwise(90) #gira en sentido del reloj
dron.rotate_clockwise(-90) #gira en sentido del reloj
dron.get_battery()
dron.rotate_counter_clockwise(90)
#dron.move_left(30)
dron.land()

