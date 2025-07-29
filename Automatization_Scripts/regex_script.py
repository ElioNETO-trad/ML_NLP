import re

names = ['Marquin Lagoa', 'Fernando Fernandes', 'Manoel Siqueira', 'Coronel Do Mato', "Imagin Dragons"]


regex = "^\w+\s+\w+$"

for name in names:
    result = re.search(regex, name)
    if result:
        print(result)

