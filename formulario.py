
nome = input('Entre com o seu nome?:')
sobrenome = input('Entre com o seu sobrenome?:')
dia_nascimento = input('Dia de nascimento?:')
mes_nascimento = input('Mês de nascimento?:')
ano_nascimento = input('Ano de nascimento?:')
universidade = input('Qual sua universidade?')

e_mail = nome.lower() + '.' + sobrenome_lower() + '@' + universidade.lower() + '.br'

senha = 'a' + str(e_mail.count('a')) + 'e' + str(e_mail.count('e')) + 'i' + str(e_mail.count('i')) + 'o' + str(e_mail.count('o')) + 'u' + str(e_mail.count('u'))
                                                                                                                        print('O seu e-mail é: {}' .format(e_mail))                                                                             print('A sua senha é : {}' .format(senha))
                                                                                                                        print('A sua senha e e-mail são: {}:{}'.format(senha,e_mail))
