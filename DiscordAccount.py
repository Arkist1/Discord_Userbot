import requests
from Guild import Guild

class DiscordAccount:
    def __init__(self, token, password=None):
        self.token = token
        self.authheader = {"Authorization": self.token}

        information = self.getinfo()
        self.id = information["id"]
        self.username = information["username"]
        self.discname = f"{information['username']}#{information['discriminator']}"
        self.email = information["email"]

        self.password = password
        print(f"{self.email} is online")

    def getinfo(self):
        info = requests.get("https://discord.com/api/v9/users/@me", headers=self.authheader)
        return info.json()

    def joinserver(self, invitecode):
        url = f"https://discord.com/api/v9/invites/{invitecode}"
        r = requests.post(url, headers=self.authheader)

    def leaveserver(self, server):
        url = f"https://discord.com/api/v9/users/@me/guilds/{server}"
        r = requests.delete(url, headers=self.authheader)

    def sendmessage(self, message, channel):
        url = f"https://discord.com/api/v9/channels/{channel}/messages"
        data = {"content": message}
        requests.post(url, data=data, headers=self.authheader)

    def setusername(self, username):
        url = "https://discord.com/api/v9/users/@me"
        headers = {"authorization": self.token, "Content-Type": "application/json"}
        data = {"username": username, "password": self.password}
        r = requests.patch(url, json=data, headers=headers)
        print(r.text)

    def setpfp(self, pfp):
        url = "https://discord.com/api/v9/users/@me"
        data = {"avatar": f"data:image/jpeg;base64, {getpfp(pfp)}"}
        headers = {"authorization": self.token, "Content-Type": "application/json"}
        r = requests.patch(url, json=data, headers=headers)
        print(r.text)

    def setbio(self, bio):
        url = "https://discord.com/api/v9/users/@me"
        data = {"bio": bio}
        headers = {"authorization": self.token, "Content-Type": "application/json"}
        requests.patch(url, json=data, headers=headers)

    def changepassword(self, new, password=None):
        url = "https://discord.com/api/v9/users/@me"
        data = {'password': self.password, "new_password": new}
        headers = {"authorization": self.token, "Content-Type": "application/json"}

        if password:
            data['password'] = password

        print(data)
        r = requests.patch(url, json=data, headers=headers).json()

        print(r)
        self.password = data["new_password"]
        self.token = r["token"]

    def setstatus(self, status):
        statusses = ["online", "idle", "dnd", "invisible"]
        if status not in statusses:
            print(f"{status} is not a status, use setcustomstatus() for a custom status")
            return

        url = "https://discord.com/api/v9/users/@me/settings"
        data = {'status': status}
        headers = {"authorization": self.token, "Content-Type": "application/json"}

        requests.patch(url, json=data, headers=headers)

    def setcustomstatus(self, status, emoji=None, state=None):
        url = "https://discord.com/api/v9/users/@me/settings"
        data = {"custom_status": {"text": status}}
        if emoji:
            data["custom_status"]["emoji_name"] = emoji
        if state:
            self.setstatus(state)
        headers = {"authorization": self.token, "Content-Type": "application/json"}

        requests.patch(url, json=data, headers=headers)

    def getdms(self):
        url = "https://discord.com/api/v9/users/@me/dms"
        r = requests.get(url, headers=self.authheader)
        print(r.text)

    def guilds(self):
        url = f"https://discord.com/api/v9/users/{self.id}/profile?with_mutual_guilds=true"
        r = requests.get(url, headers=self.authheader)
        r = r.json()
        guilds = []
        for x in r['mutual_guilds']:
            guilds.append(Guild(x['id']))
        return guilds

    # captcha is een bitch
    # def turnonline(self):
    #     url = "https://discord.com/api/v9/auth/login"
    #     headers = {"Content-Type": "application/json"}
    #     data = {"login": self.email, "password": self.password, "undelete": False, "captcha_key": None,
    #             "login_source": None, "gift_code_sku_id": None}
    #
    #     r = requests.session().post(url, headers=headers, json=data)
    #     print(r.text)
