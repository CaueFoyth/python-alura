# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

pessoas = [{"nome":"Cauê", "idade":17, "cidade":"Joinville"} ,
          {"nome":"Gabriel", "idade":18, "cidade":"São Paulo"}]

# 2 - Utilizando o dicionário criado no item 1:
# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
for pessoa in pessoas:
    if "Gabriel" == pessoa["nome"]:
        pessoa["idade"] = 19
print(pessoas)

# Adicione um campo de profissão para essa pessoa;
pessoa['profissao'] = 'Engenheiro'

# Remova um item do dicionário.
del pessoa['cidade']