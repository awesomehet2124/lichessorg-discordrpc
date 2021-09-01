from pypresence import Presence
import requests, time, config

client_id = int(config.client_id)
RPC = Presence(client_id)
RPC.connect()

while True:
    response = requests.get(f"https://lichess.org/api/user/{config.lichess_username}")
    try:
        stat = response.json()
    except:
        pass

    if str(response) == "<Response [200]>":
        if stat["online"]:
            RPC.update(
                large_image="lichess-icon",
                buttons =
                [
                    {
                        "label": "Playing on Lichess.org",
                        "url": f"https://lichess.org/@/{config.lichess_username}/tv"
                    }
                ]
            )
        if not stat["online"]:
            RPC.update(
                large_image="lichess-icon",
                buttons = [
                    {
                        "label": "Idling on Lichess.org",
                        "url": f"https://lichess.org/@/{config.lichess_username}"
                    }
                ]
            )

    time.sleep(5)