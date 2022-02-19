from Guild import Guild
from Classes import DiscordAccount
import Channel
import base64
import requests


def getpfp(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')


def gettokens():
    f = open("accounts.txt")
    passtokens = []
    for x in f.readlines():
        split = x.split(":")
        passtokens.append({"token": split[0], "password": split[1].split("\n")[0]})
    return passtokens


def updateaccounts(accounts):
    passtokens = []
    for account in accounts:
        passtokens.append(f"{account.token}:{account.password}")
    passtokens = "\n".join(passtokens)
    w = open("accounts.txt", "w")
    w.write(passtokens)


if __name__ == '__main__':
    tokens = gettokens()

    bots = []
    for passtoken in tokens:
        bots.append(DiscordAccount(passtoken["token"], passtoken["password"]))


    # for bot in bots:
    #     bot.joinserver("ESpJnpnC")
    #
    # guild = Guild(937074826659651585, bots[0].token)
    #
    # for bot in bots:
    #     for channel in guild.textchannels:
    #         channel.sendmessage("xd", bot)

    print(bots[0].authheader)
    r = requests.get("https://discord.com/api/v9/guilds/895773448503197696/members", headers=bots[0].authheader)
    print(r.text)