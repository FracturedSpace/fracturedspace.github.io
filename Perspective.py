import time
from pyscript import display
import requests

url = "https://discord.com/api/webhooks/1563625952863326335/9bsbdv0m8LybMcRHRc8kBvom7sZ3gBI9BlUb1nWv5t5NbDbDsFiYv0LZ-CxHcQ1JldOh"


print(response.status_code)
async def send_webhook(data):
    url = "https://discord.com/api/webhooks/1563625952863326335/9bsbdv0m8LybMcRHRc8kBvom7sZ3gBI9BlUb1nWv5t5NbDbDsFiYv0LZ-CxHcQ1JldOh"
    payload = {"type": 1,"event": {"type": "LOBBY_MESSAGE_CREATE", "timestamp": time.time(), "data": data}, "status": "success"}
    
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
    data = {
    "content": timesincestart/timebetween*100,
    "username": "My Python Bot"
    }
    if round(timesincestart/timebetween*100, 2)%1==0 or True:
        response = requests.post(url, json=data)
        time.sleep(10)
    
    time.sleep(.01)


