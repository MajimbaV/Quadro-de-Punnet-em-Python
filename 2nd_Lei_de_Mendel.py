#Teste de código para 2º Lei de Mendel

gen1 = "AaBb"
gen2 = "AaBB"

#1º Passo: Identificar quantos gametas é possível formar

n_Heterozigoze_Gen1 = 0
n_Heterozigoze_Gen2 = 0

#Genótipo 1
if not gen1[0:2].isupper() and not gen1[0:2].islower():
    n_Heterozigoze_Gen1 += 1
    
if not gen1[2:4].isupper() and not gen1[2:4].islower():
    n_Heterozigoze_Gen1 += 1

#Genótipo 2
if not gen2[0:2].isupper() and not gen2[0:2].islower():
    n_Heterozigoze_Gen2 += 1
    
if not gen2[2:4].isupper() and not gen2[2:4].islower():
    n_Heterozigoze_Gen2 += 1
    
#2º Passo: Forma os gametas possíveis
#Genótipo 1

gametas_gen1 = []

for i in range(1, (2**n_Heterozigoze_Gen1) +1):
    if i <= (2**n_Heterozigoze_Gen1)/2:
        if not (gen1[0] + gen1[-2]) in gametas_gen1:
            gametas_gen1.append(gen1[0] + gen1[-2])
        else:
            gametas_gen1.append(gen1[0] + gen1[-1])
    else:
        if not (gen1[1] + gen1[-2]) in gametas_gen1:
            gametas_gen1.append(gen1[1] + gen1[-2])
        else:
            gametas_gen1.append(gen1[1] + gen1[-1])

print(gametas_gen1)

#Genótipo 2

gametas_gen2 = []

for i in range(1, (2**n_Heterozigoze_Gen2) +1):
    if i <= (2**n_Heterozigoze_Gen2)/2:
        if not (gen2[0] + gen2[-2]) in gametas_gen2:
            gametas_gen2.append(gen2[0] + gen2[-2])
        else:
            gametas_gen2.append(gen2[0] + gen2[-1])
    else:
        if not (gen2[1] + gen2[-2]) in gametas_gen2:
            gametas_gen2.append(gen2[1] + gen2[-2])
        else:
            gametas_gen2.append(gen2[1] + gen2[-1])

print(gametas_gen2)

#3º Passo, combinar os gametas

genotipos = []

for gametaP in gametas_gen1:
    linha = []
    for gametaM in gametas_gen2:
        genF1 = [gametaP[0], gametaM[0], gametaP[-1], gametaM[-1]]
        if genF1[0].islower() and genF1[1].isupper():
            genF1[0] = genF1[0].upper()
            genF1[1] = genF1[1].lower()
        if genF1[-2].islower() and genF1[-1].isupper():
            genF1[-2] = genF1[-2].upper()
            genF1[-1] = genF1[-1].lower()
        genF1 = ''.join(genF1)
        linha.append(genF1)
    genotipos.append(linha)



#4º  Formar o Quadro
quadro = ''

for linha in genotipos:
       quadro += '|'.join(linha)
       quadro += '\n'

print(quadro)