import time
from pyscript import display
from pyodide.http import pyfetch
import json
import asyncio

async def send_webhook():
    url = "https://discord.com/api/webhooks/1563625952863326335/9bsbdv0m8LybMcRHRc8kBvom7sZ3gBI9BlUb1nWv5t5NbDbDsFiYv0LZ-CxHcQ1JldOh"
    payload = {"event": "$results", "status": "success"}
    
    response = await pyfetch(
        url,
        method="POST",
        headers={"Content-Type": "application/json"},
        body=json.dumps(payload)
    )
    
    if response.ok:
        data = await response.json()
        print("Webhook sent successfully:", data)
    else:
        print(f"Failed to send webhook: {response.status}")

# Run the async function


while True:

    currenttime = time.time()


    currentyear = int(time.strftime('%Y', time.localtime(currenttime)))

    nextyear = currentyear + 1

    timebetween = time.mktime(time.strptime(str(nextyear), "%Y"))-time.mktime(time.strptime(str(currentyear), "%Y"))

    timesincestart = currenttime-time.mktime(time.strptime(str(currentyear), "%Y"))

    # clear_console()
    display(str(currentyear) + " is " + str(timesincestart/timebetween*100) + " complete.",  target="results", append = False)
    
    if round(timesincestart/timebetween*100, 2)%1==0 or True:
        asyncio.ensure_future(send_webhook())
        time.sleep(10)
    
    time.sleep(.01)


