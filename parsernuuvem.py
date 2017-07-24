import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv


page_principal = requests.get("https://www.nuuvem.com/catalog/price/promo/sort/bestselling/sort-mode/desc")

soup_principal = BeautifulSoup(page_principal.content, 'html.parser')

paginas = soup_principal.findAll('section',{"data-pager":True} )
for data in paginas:
    conteudo = data['data-pager']

total_paginas = int(conteudo[32]) + 1
contador = 1

lo = pd.DataFrame()

for contador in range(1,total_paginas):
    page_unica = requests.get("https://www.nuuvem.com/catalog/price/promo/sort/bestselling/sort-mode/desc/page/%s" %contador)
    soup = BeautifulSoup(page_unica.content, 'html.parser')
    ofertas = soup.find(class_="products-dock--main nvm-mod mod-group-sell mod-group-sell-offer")
    nome_oferta = [no.get_text() for no in ofertas.select(".product-title")]
    valor_integer = [vi.get_text() for vi in ofertas.select(".integer")]
    valor_decimal = [vd.get_text() for vd in ofertas.select(".decimal")]

    columnsTitle = ['title','integer','decimal']

    lista_oferta = pd.DataFrame({
        'title': nome_oferta,
        'integer': valor_integer,
        'decimal': valor_decimal

    }, columns=columnsTitle)

    lo = lo.append(lista_oferta)

print(lo)
lo.to_excel("ofertas.xlsx")