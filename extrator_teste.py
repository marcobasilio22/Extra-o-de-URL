import re

endereco = "rua dos palmares, 157, lider, São Paulo, São Paulo, 02202-060"

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")

busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)
