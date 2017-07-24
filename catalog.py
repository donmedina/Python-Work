import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import time

ti = time.time()

paginas_catalogo = requests.get("https://www.nuuvem.com/catalog/sort/title/sort-mode/asc")
soup_paginas = BeautifulSoup(paginas_catalogo.content, 'html.parser')

data_pagina = soup_paginas.findAll('section',{"data-pager":True})

for data in data_pagina:
    conteudo = data['data-pager']

np = int(conteudo[32:35])
contador = 0

lc = pd.DataFrame()

for contador in range(1, np):
    page_u = requests.get("https://www.nuuvem.com/catalog/sort/title/sort-mode/asc/page/%s" %contador)
    soup = BeautifulSoup(page_u.content,'html.parser')
    catalogo = soup.find(class_="products-dock--main nvm-mod mod-group-sell mod-group-sell-offer")
    titulo = [t.get_text() for t in catalogo.select(".product-title")]
    valor_inteiro = [vi.get_text() for vi in catalogo.select(".integer")]
    valor_decimal = [vd.get_text() for vd in catalogo.select(".decimal")]
    
    l1 = pd.Series(titulo, name='titulo')
    l2 = pd.Series(sem_desconto, name='sem_desconto')
    l3 = pd.Series(valor_inteiro, name='inteiro')
    l4 = pd.Series(valor_decimal, name='decimal')
    
    lista = pd.concat ([l1,l2,l3,l4], axis=1)
    print (lista)
    lc = lc.append(lista)

lc.to_excel("catalogo.xlsx")
tf = time.time()

print (tf-ti)
