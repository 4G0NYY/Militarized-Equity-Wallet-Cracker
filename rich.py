import threading
import PyPresence as Presence

# TO BE IMPLICATED - NOT IN USE

def rich():
    client_id = "1198291732807286845"
    RPC = Presence(client_id)
    RPC.connect()
    RPC.update(state="Mining Crypto with MEWC!" ,
        large_text="Militarized Equity Wallet Cracker",
        large_image="mewc" ,
        buttons=[{"label": "GitHub", "url": "https://github.com/4G0NYY/equity_cracker/"}, {"label": "Discord", "url": "https://discord.gg/ZhtcnQsbZz"}])

rich_thread = threading.Thread(Target=rich(), name="DRPC")