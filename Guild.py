import requests
from Channel import Channel
import time


class Guild:
    def __init__(self, guildid, accestoken):
        self.token = accestoken
        self.authheader = {"Authorization": self.token}
        self.id = guildid
        self.textchannels = []
        self.voicechannels = []

        info = self.get_info()

    def get_info(self):
        url = f"https://discord.com/api/v9/guilds/{self.id}/channels"
        r = requests.get(url, headers=self.authheader).json()
        for x in r:
            if x['type'] == 0:
                self.textchannels.append(Channel(x['id']))


