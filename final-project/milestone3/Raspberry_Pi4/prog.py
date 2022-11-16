# import serial
# ser = serial.Serial('/dev/ttyAMA1', 115200)
# while (1) :
#     speed = raw.input()
#     angle = raw.input()
#     command = "speed: " + speed + "angle: " + angle
#     ser.write(bytes(command))
# ser.close()

ser1 = serial.Serial('/dev/ttyAMA1')
ser1.baudrate = 115200

ser1.write(bytes("\n"))

with open("directions.txt", "r") as f:
    for line in f:
        array = line.split()
        info = array[0] + ' ' + array[1] + ' ' + array[2] + '\n'
        ser1.write(bytes(info))
        print(array)
        print(info)

        timeVal = int(array[2])
        time.sleep(timeVal)

ser1.close()