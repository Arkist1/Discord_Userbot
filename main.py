import Guild
import Channel
import DiscordAccount
import base64

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

    for bot in bots:
        bot.joinserver("bwsFZkRM")


    Guild("895773448503197696", "NTI5MDA4NzQyMDYzMjc2MDYy.YfceJA.qAM8TWe-k4JwmpYRI8RnCgNFOpo")
    Guild("713444727558504500", "NTI5MDA4NzQyMDYzMjc2MDYy.YfceJA.qAM8TWe-k4JwmpYRI8RnCgNFOpo")

