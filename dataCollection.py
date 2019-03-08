
#dataCollection
#Bo Eaves and Grace Anderson
#This is the code that our microbit uses to collect data and compress it into a file


import microbit, math, os, random

while True:
    if microbit.button_a.is_pressed(): #Data collection starts when A is pushed
        filename = "pendulumData " + str(random.randint(1,999))+ ".txt" #New file with a random number is created
        with open(filename, 'w') as my_file:
            start_time = (microbit.running_time()/1000)

            while not microbit.button_b.is_pressed(): #Gathers data from the accelerometer on the microbit
                microbit.sleep(40)                      #Data collection stops when B is pushed
                microbit.display.show(microbit.Image.HAPPY)
                acc_x = microbit.accelerometer.get_x()
                acc_y = microbit.accelerometer.get_y()
                acc_z = microbit.accelerometer.get_z()
                time = microbit.running_time()/1000 - start_time
                data = str(acc_x) + ',' + str(acc_y) + ',' + str(acc_z) + ',' + str(time) + "\n"
                my_file.write(data)

        microbit.display.show(microbit.Image.SAD)
        my_file.close()