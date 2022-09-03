import re

url = 'https://www.bytebank.com.br/cambio'

padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ValueError("Sua URL esta invalida")
print("A URL é valida")