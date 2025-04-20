import rpc
import time
from time import mktime

print("RPC")
client_id = '1363456321655148735'  # Your application's client ID as a string. (This isn't a real client ID)
try:
    rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)  # Send the client ID to the rpc module
    print("RPC connection successful.")
except Exception as e:
    print(f"Failed to connect to Discord: {e}")

def discord_rpc(details, state, smallpic="none", smallpic_text="Doing something",version="NOT_PROVIDED"):
    time.sleep(1)
    start_time = mktime(time.localtime())
    while True:
        try:
            # Example
            activity = {
                "state": str(state),  # anything you like
                "details": str(details),  # anything you like
                "timestamps": {
                    "start": start_time
                },
                "assets": {
                    "small_text": str(smallpic_text),  # anything you like
                    "small_image": str(smallpic),  # must match the image key
                    "large_text": f"Pisun Editor, Version: {version}",  # anything you like
                    "large_image": "pisun_editor_icon"  # must match the image key
                }
            }
            rpc_obj.set_activity(activity)
        except Exception as e:
            print(f"Failed to update Discord activity: {e}")
        time.sleep(100)
