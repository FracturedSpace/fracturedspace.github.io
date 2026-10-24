import time
from pyscript import display

# Call the function to clear the console


while True:

    currenttime = time.time()


    currentyear = int(time.strftime('%Y', time.localtime(currenttime)))

    nextyear = currentyear + 1

    timebetween = time.mktime(time.strptime(str(nextyear), "%Y"))-time.mktime(time.strptime(str(currentyear), "%Y"))

    timesincestart = currenttime-time.mktime(time.strptime(str(currentyear), "%Y"))

    # clear_console()
    display(str(currentyear) + " is " + str(timesincestart/timebetween*100) + " complete.", append = False)
    time.sleep(.01)


