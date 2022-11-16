import serial
ser = serial.Serial('/dev/ttyAMA1', 115200)
while (1) :
    speed = raw.input()
    angle = raw.input()
    command = "speed: " + speed + "angle: " + angle
    ser.write(bytes(command))
ser.close()