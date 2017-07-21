import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

page = requests.get("https://www.nuuvem.com/catalog/price/promo/sort/bestselling/sort-mode/desc")

soup = BeautifulSoup(page.content, 'html.parser')

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

print(lista_oferta)

lista_oferta.to_excel("lista.xlsx")