# def getcookies(session):
#     cookies = []
#     for cookie in session.get_cookies():
#         cookies.append([cookie['name'], cookie['value']])
#     return cookies
#
#
# def joinserver(invitecode):
#     url = f"https://discord.com/api/v9/invites/{invitecode}"
#     headers = {"Authorization": "NjUxNzk1NzUyNzk2MDI4OTMy.YfGt0Q.4HCQ97s50sUAuK75jeciB5nKU3U"}
#     # r = session.request('POST', url, headers=headers)
#     requests.post(url, headers=headers)
#
#
# def login(token):
#     session = Firefox()
#     session.get("https://discord.com/login")
#     session.execute_script(f'let token = "{token}";' +
#                           '' +
#                           'function login(token) {' +
#                           '    setInterval(() => {' +
#                           '      document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`' +
#                           '    }, 50);' +
#                           '    setTimeout(() => {' +
#                           '      location.reload();' +
#                           '    }, 2500);' +
#                           '  }' +
#                           '' +
#                           'login(token);')
#     return session