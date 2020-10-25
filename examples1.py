import winsound
import time
import sys

print('Welcome to alarmie, the simple CLI alarm application. Press Ctrl + C to stop beeping.')

frequency = 2500
duration = 1000

clock_active = False

try:
    usr_input = float(input('Enter in how many minutes until the beep: '))
    print(f'Alright, you will be reminded in {int(usr_input)} minutes!')
except ValueError:
    print('Not a number')    

usr_input = usr_input * 60
time.sleep(usr_input)

clock_active = True

if clock_active is True:
    while True:
        try:
            winsound.Beep(frequency, duration)
        except KeyboardInterrupt:
            print('Stopping')
            sys.exit()