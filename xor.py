A = False
B = False
regra = ((not A) and B) or ((not B) and A)
print(A, B, regra)

A = False
B = True
regra = ((not A) and B) or ((not B) and A)
print(A, B, regra)

A = True
B = False
regra = ((not A) and B) or ((not B) and A)
print(A, B, regra)

A = True
B = True
regra = ((not A) and B) or ((not B) and A)
print(A, B, regra)

print('\n'*10)
A = True
B = True
C = True
D = True
regra_d_c = ((not D) and C)
regra_a_c = (A and (not C))
regra_b_d = B or D
regra = (regra_a_c or regra_b_d) and regra_d_c
print(A,B,C,D, regra)



regra = (not (A and(not C)) or (B or D)) and ((not D) and C)
print(A,B,C,D, regra)

valores = [True, False]
for A in valores:
    for B in valores:
        for C in valores:
            for D in valores:
                regra_d_c = ((not D) and C)
                regra_a_c = not (A and (not C))
                regra_b_d = B or D
                regra = (regra_a_c or regra_b_d) and regra_d_c
                print(A,B,C,D, regra)
