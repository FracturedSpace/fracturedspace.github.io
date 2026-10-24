import time, os

def clear_console():
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        _ = os.system('cls')
    else:
        # Command for Linux, macOS, and other POSIX systems
        _ = os.system('clear')

# Call the function to clear the console


while True:

    currenttime = time.time()


    currentyear = int(time.strftime('%Y', time.localtime(currenttime)))

    nextyear = currentyear + 1

    timebetween = time.mktime(time.strptime(str(nextyear), "%Y"))-time.mktime(time.strptime(str(currentyear), "%Y"))

    timesincestart = currenttime-time.mktime(time.strptime(str(currentyear), "%Y"))

    # clear_console()
    print("\033c" + str(currentyear) + " is " + str(timesincestart/timebetween*100) + "% complete.")
    time.sleep(.01)


