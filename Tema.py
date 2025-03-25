import math
import random
import bisect

def citire():
    f = open("date.in")
    nrCromozomi = int(f.readline())
    a, b = [float(x) for x in f.readline().split()]
    a1, a2, a3 = [float(x) for x in f.readline().split()]
    precizie = int(f.readline())
    probRecombinare = float(f.readline())
    probMutatie = float(f.readline())
    nrEtape = int(f.readline())
    f.close()
    return (nrCromozomi, (a, b), (a1, a2, a3), precizie, probRecombinare, probMutatie, nrEtape)

def afisareArgs(args):
    output.write(f'Dimensiunea populatiei: {args[0]} \n\
Domeniul de definitie: {args[1]} \n\
Coeficienti polinom: {args[2]} \n\
Precizie: {args[3]} \n\
Probabilitate crossover: {args[4]} \n\
Probabilitate mutatie: {args[5]} \n\
Numar etape: {args[6]}')

def binary(number, length):
    result = [0] * length
    for i in range(length):
        result[i] = number % 2
        number //= 2
    result = [str(x) for x in result]
    return ''.join(result[::-1])

def TO(nr, a, l, d):
    stanga = a
    k = 0
    while stanga + d <= nr:
        stanga += d
        k += 1
    return binary(k, l)

def FROM(sir, a, d):
    numar = 0
    power = 1
    for i in sir[::-1]:
        numar += int(i) * power
        power *= 2
    return a + numar * d

def generareInitiala(nrCromozomi, a, b, l, d):
    cromozomi = []
    for i in range(nrCromozomi):
        x = random.uniform(a, b)
        cromozomi.append(TO(x, a, l, d))
    return cromozomi

def functie(x, a, b, c):
    return a * x * x + b * x + c

def calcProbSelectie(cromozomi, a, d, a1, a2, a3):
    f = [functie(FROM(cromozom, a, d), a1, a2, a3) for cromozom in cromozomi]
    F = sum(f)
    p = [f[i]/F for i in range(len(cromozomi))]
    for i in range(len(p)):
        p[i] = f[i] / F
    return p

def calcIntervaleSelectie(p):
    result = [0]
    for i in range(len(p)):
        result.append(result[i] + p[i])
    return result

def selectieCromozomi(intervale):
    u = [random.random() for _ in range(len(intervale)-1)]
    selectati = [bisect.bisect_left(intervale, val) for val in u]
    return u, selectati

def recombinare(cromozomi, u, probRecombinare):
    indiceCromozom = [(i+1, cromozomi[i]) for i in range(len(u)) if u[i] <= probRecombinare]
    recombinari = []
    while len(indiceCromozom) >= 2:
        indCrom1 = random.randrange(len(indiceCromozom))
        indice1, crom1 = indiceCromozom[indCrom1]
        indiceCromozom.pop(indCrom1)
        indCrom2 = random.randrange(len(indiceCromozom))
        indice2, crom2 = indiceCromozom[indCrom2]
        indiceCromozom.pop(indCrom2)
        punctDeRupere = random.randrange(len(crom1))
        crom1_nou = crom1[:punctDeRupere] + crom2[punctDeRupere:]
        crom2_nou = crom2[:punctDeRupere] + crom1[punctDeRupere:]
        CROM1 = (indice1, crom1, crom1_nou)
        CROM2 = (indice2, crom2, crom2_nou)
        recombinari.append((CROM1, CROM2, punctDeRupere))
    return recombinari

def mutatie(cromozomi, probMutatie):
    schimbati = []
    for i in range(len(cromozomi)):
        newCrom = ''.join([str((int(ch) + 1) % 2) if random.random() <= probMutatie else ch for ch in cromozomi[i]])
        if newCrom != cromozomi[i]:
            schimbati.append(i+1)
            cromozomi[i] = newCrom
    return schimbati, cromozomi

def maxFitness(cromozomi):
    return max([functie(FROM(cromozom, a, d), a1, a2, a3) for cromozom in cromozomi])

def meanFitness(cromozomi):
    return sum([functie(FROM(cromozom, a, d), a1, a2, a3) for cromozom in cromozomi]) / len(cromozomi)

def afisarePopulatie(output, cromozomi, a, d):
    for i in range(len(cromozomi)):
        x = FROM(cromozomi[i], a, d)
        output.write(f'{i+1:2}: {cromozomi[i]} x= {x:9.6f} f= {functie(FROM(cromozomi[i], a, d), a1, a2, a3):8.6f}\n')
    output.write('\n')

def afisareProbSelectie(output, p):
    output.write('Probabilitati selectie\n')
    for i in range(len(p)):
        output.write(f'cromozom {i+1:2} probabilitate {p[i]}\n')
    output.write('\n')

def afisareIntervaleSelectie(output, intervale):
    output.write('Intervale probabilitati selectie\n')
    output.write(' '.join([str(x) for x in intervale]))
    output.write('\n\n')

def afisareSelectie(output, u, indiciCromozomiSelectati):
    for i in range(len(u)):
        output.write(f'u={u[i]} selectam cromozomul {indiciCromozomiSelectati[i]}\n')
    output.write('\n')

def afisareProbIncrucisare(output, cromozomi, u, probRecombinare):
    output.write(f'Probabilitatea de incrucisare {probRecombinare}\n')
    for i in range(len(u)):
        output.write(f'{i+1:2}: {cromozomi[i]} u= {u[i]} {f"< {probRecombinare} participa" if u[i] <= probRecombinare else ""}\n')
    output.write('\n')

def afisareRecombinari(output, recombinari):
    for (CROM1, CROM2, punctDeRupere) in recombinari:
        output.write(f'Recombinare dintre cromozomul {CROM1[0]} cu cromozomul {CROM2[0]}:\n')
        output.write(f'{CROM1[1]} {CROM2[1]} punct {punctDeRupere}\n')
        output.write(f'Rezultat\t{CROM1[2]} {CROM2[2]}\n')
    output.write('\n')

def afisareSchimbati(output, schimbati):
    output.write('Au fost modificati cromozomii\n')
    output.write(' '.join([str(x) for x in schimbati]))
    output.write('\n\n')


#Data
output = open('solutie.txt', 'w')
nrCromozomi, (a, b), (a1, a2, a3), precizie, probRecombinare, probMutatie, nrEtape = citire()
l = math.ceil(math.log2((b - a) * (10 ** precizie)))
d = (b - a) / (2 ** l)

args = nrCromozomi, a, b, l, d
cromozomi = generareInitiala(*args)

for i in range(nrEtape):
    # Selectie
    args = cromozomi, a, d, a1, a2, a3
    probSelectie = calcProbSelectie(*args)
    intervaleSelectie = calcIntervaleSelectie(probSelectie)
    u, indiciCromozomiSelectati = selectieCromozomi(intervaleSelectie)
    if i == 0:
        output.write('Populatia initiala\n')
        afisarePopulatie(output, cromozomi, a, d)
        afisareProbSelectie(output, probSelectie)
        afisareIntervaleSelectie(output, intervaleSelectie)
        afisareSelectie(output, u, indiciCromozomiSelectati)

    # Incrucisare
    cromozomi = [cromozomi[i-1] for i in indiciCromozomiSelectati]
    uParticipa = [random.random() for _ in cromozomi]
    recombinari = recombinare(cromozomi, uParticipa, probRecombinare)
    
    if i == 0:
        output.write('Dupa selectie:\n')
        afisarePopulatie(output, cromozomi, a, d)
        afisareProbIncrucisare(output, cromozomi, uParticipa, probRecombinare)
        afisareRecombinari(output, recombinari)
        
    # Mutatii
    for (CROM1, CROM2, _) in recombinari:
        cromozomi[CROM1[0] - 1] = CROM1[2]
        cromozomi[CROM2[0] - 1] = CROM2[2]
    schimbati, cromozomiMutati = mutatie(cromozomi, probMutatie)
    if i == 0:
        output.write('Dupa recombinare:\n')
        afisarePopulatie(output, cromozomi, a, d)
        output.write(f'Probabilitate de mutatie pentru fiecare gena {probMutatie}\n')
        afisareSchimbati(output, schimbati)
        output.write('Dupa mutatie:\n')
        afisarePopulatie(output, cromozomiMutati, a, d)
        output.write('Evolutia maximului si a mediei\n')
    
    cromozomi = cromozomiMutati
    output.write(f'max = {maxFitness(cromozomi)} mean = {meanFitness(cromozomi)}\n')

output.close()