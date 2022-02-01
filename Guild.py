import requests

class Guild:
    def __init__(self, guildid, accestoken):
        self.token = accestoken
        self.authheader = {"Authorization": self.token}
        self.id = guildid

        info = self.get_info()

    def get_info(self):
        url = f"https://discord.com/api/v9/guilds/{self.id}"
        r = requests.get(url, headers=self.authheader)
        print(r.text)
