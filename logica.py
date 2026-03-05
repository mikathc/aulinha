'''
construindo a logica de not
'''

var_1 = True
var_2 = False
print('var_1 {} quando negada fica {}'.format(var_1, not var_1))
print('var_2 {} quando negada fica {}'.format(var_2, not var_2))

'''
construindo a lógica do AND (E)
'''

var1_t = True
var1_f = False
var2_t = True
var2_f = False

print('Quando var_1_t é {} E var=2_t {} o resultado é {}'. format(var_1_t,var_2_t,var_1_t and var_2_t))
print('Quando var_1_f é {} E var=2_t {} o resultado é {}'. format(var_1_f,var_2_t,var_1_f and var_2_t))
print('Quando var_1_t é {} E var=2_f {} o resultado é {}'. format(var_1_t,var_2_f,var_1_t and var_2_f))
print('Quando var_1_f é {} E var=2_f {} o resultado é {}'. format(var_1_f,var_2_f,var_1_f and var_2_f))
print()

'''
construindo a logica do OR (OU)
'''

print('Quando var_1_t é {} OU var=2_t {} o resultado é {}'. format(var_1_t,var_2_t,var_1_t and var_2_t))
print('Quando var_1_f é {} OU var=2_t {} o resultado é {}'. format(var_1_f,var_2_t,var_1_f and var_2_t))
print('Quando var_1_t é {} OU var=2_f {} o resultado é {}'. format(var_1_t,var_2_f,var_1_t and var_2_f))
print('Quando var_1_f é {} OU var=2_f {} o resultado é {}'. format(var_1_f,var_2_f,var_1_f and var_2_f))
print()

'''
multiplas regras de lógica
'''
var_1_t = True
var_1_f = False
var_2_t = True
var_2_f = False

var_resultado = ((var_1_t and var_2_f) or ((var_1_f or var_2_t) and (not var_2_f)))
print('O resultado da lógica é ()'.format(var_resultado))
