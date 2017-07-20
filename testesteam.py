import steamapi
import json
import csv

steamapi.core.APIConnection(api_key="326D9F920A4E18B729EA508CA8DF8F38", validate_key=True)
amigos = steamapi.user.SteamUser(userurl="donmedinarj").friends

jogos = steamapi.user.SteamUser(userurl="donmedinarj").games
#jogo = steamapi.app.SteamApp(appid='', name="Dishonored 2")

print (amigos)
print (jogos)

with open('arqOut.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile,delimiter=';', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(jogos)