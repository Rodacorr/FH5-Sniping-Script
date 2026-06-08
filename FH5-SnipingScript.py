# Imports for keyboard inputs, timed delays and a custom function
import keyboard
import time
import os

# Function to clear the terminal
def clear():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)


clear()

timer = 0.0      # Seconds
counter = 0      # Times sniped
start = 1        # Gouda cheese _xX(**[-.meme.-]**)Xx_
paused = False   # Pause state


# Toggle pause with S
def toggle_pause():
    global paused
    paused = not paused


keyboard.add_hotkey('s', toggle_pause, suppress=True)


def wait_if_paused():
    shown = False

    while paused:
        if not shown:
            clear()
            print(' ----------------------------------------------------------------------')
            print('|                              PAUSED                                  |')
            print('|                                                                      |')
            print('|                     Press S to resume the script                     |')
            print(' ----------------------------------------------------------------------')
            shown = True

        time.sleep(0.1)


def smart_sleep(seconds):
    remaining = seconds

    while remaining > 0:
        wait_if_paused()

        step = min(0.05, remaining)
        time.sleep(step)
        remaining -= step


def press_key(key):
    wait_if_paused()
    keyboard.press_and_release(key)


# This will initiate the script
if start == 1:
    while True:
        # Prints the explanation for using the script
        clear()
        print(' ----------------------------------------------------------------------')
        print('|                     Python FH5 Sniping Script                        |')
        print('|                                                                      |')
        print('|   1- First select the car you want and the potential max buyout      |')
        print('|   2- Make sure to focus the FH5 window when the countdown starts     |')
        print('|   3- Second monitor highly recommended because when you want to      |')
        print('|      close the script you have to just force close the window        |')
        print('|      (Put the game in windowed mode and put the script over it       |')
        print('|       if you don\'t have a second monitor)                            |')
        print('|   4- It will start counting down from 5 once you start the script.   |')
        print('|      \'y\' = yes | \'n\' = no                                            |')
        print('|                                                                      |')
        print('|      Press S to pause/resume while the script is running             |')
        print('|                                                                      |')
        print('|      GOOD LUCK SNIPING!                                              |')
        print(' ----------------------------------------------------------------------')

        # Asks if user wants to start sniping
        a = str(input('\nDo you want to start the script? y/n: ')).lower()

        # If user input equals 'n' it will close the program immediately
        if a == 'n':
            break

        # If user input equals 'y' it will start counting down from 5 and will start sniping
        elif a == 'y':
            clear()

            for i in range(5, -1, -1):
                print('!!FOCUS WINDOW!!\nSniping in: ')
                print(str(i) + ' seconds')
                time.sleep(1)
                clear()

            # The keyboard inputs and timings
            while True:
                wait_if_paused()

                counter = counter + 1
                timer = timer + 2.33
                minuteCounter = timer / 60

                clear()
                print('Sniped ' + str(counter) + ' Times')
                print('That\'s about ' + str(round(timer, 1)) + ' seconds (' + str(round(minuteCounter, 1)) + ' minutes)')
                print('Press S to pause/resume')

                press_key('Enter')

                # If you have lag, this one and all the ones with asterisks are probably
                # the ones you want to prolong. Recommended increments: +0.1
                smart_sleep(0.25)

                press_key('Enter')
                # *
                smart_sleep(0.78)

                press_key('y')
                smart_sleep(0.25)

                press_key('down')
                smart_sleep(0.1)

                press_key('Enter')

                # *
                smart_sleep(0.2)

                press_key('Enter')
                press_key('Escape')

                smart_sleep(0.75)

        # If input doesn't equal 'y' or 'n', ask the user to restart or exit
        else:
            while True:
                clear()

                restart = input('You didn\'t press \'y\' to start the script, do you want to restart? y/n : ').lower()

                if restart == 'y':
                    break

                elif restart == 'n':
                    exit()

                else:
                    continue

clear()