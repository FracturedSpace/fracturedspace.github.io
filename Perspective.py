import time
from pyscript import display
import requests

url = "https://discord.com/api/webhooks/1563625952863326335/9bsbdv0m8LybMcRHRc8kBvom7sZ3gBI9BlUb1nWv5t5NbDbDsFiYv0LZ-CxHcQ1JldOh"




while True:

    currenttime = time.time()


    currentyear = int(time.strftime('%Y', time.localtime(currenttime)))

    nextyear = currentyear + 1

    timebetween = time.mktime(time.strptime(str(nextyear), "%Y"))-time.mktime(time.strptime(str(currentyear), "%Y"))

    timesincestart = currenttime-time.mktime(time.strptime(str(currentyear), "%Y"))

    # clear_console()
    display(str(currentyear) + " is " + str(timesincestart/timebetween*100) + " complete.",  target="results", append = False)
    data = {
    "content": str(timesincestart/timebetween*100),
    "username": "My Python Bot"
    }
    if round(timesincestart/timebetween*100, 2)%1==0 or True:
        response = requests.post(url, json=data)
        display(response.status_code, append = False)
        time.sleep(10)
    
    time.sleep(.01)


