import requests


class Channel:
    def __init__(self, channelid):
        self.id = channelid

    def sendmessage(self, message, bot):
        url = f"https://discord.com/api/v9/channels/{self.id}/messages"
        data = {"content": message}

        r = requests.post(url, data=data, headers=bot.authheader)