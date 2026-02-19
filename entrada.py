user = input('insert your username:')
password = input('insert your password:')
domain = input('insert your domain:')

print("Usuário:", user)
print("Senha:", password)
print("Domínio:", domain)

email = user + '@' + domain
print('Seu e-mail é:', email)

palavra = 'site'
print('Colocando o texto em maiusculo:', palavra.upper())

PALAVRA = 'SITE'
print('Colocando o texto em minusculo:', PALAVRA.lower())

palavra_contar = 'banana'
print('Contar a letra b', palavra_contar.count('b'))
print('Contar a letra a', palavra_contar.count('a'))
print('Contar a letra n', palavra_contar.count('n'))
print('Contar a letra a', palavra_contar.count('a'))
print('Contar a letra n', palavra_contar.count('n'))
print('Contar a letra a', palavra_contar.count('a'))

email2 = email
letraA= email2.count ('a')
letraE= email2.count ('e')
letraI= email2.count ('i')
letraO= email2.count ('o')
letraU= email2.count ('o')

senha = 'a'+str(letraA) + 'e'+str(letraE) + 'i'+str(letraI) + 'o'+str(letraO) + 'u'+str(letraU)
print('sua senha é:', senha)
