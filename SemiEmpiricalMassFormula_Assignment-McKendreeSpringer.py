print('a.') #a
def semiEmpiricalMassFormula(A,Z): #Inputs A for mass number and Z for atomic number
    if A%2 == 0 and Z%2 == 0:
        a5 = 12.0
    elif A%2 == 0 and Z%2 != 0:
        a5 = -12.0
    elif A%2 != 0:
        a5 = 0
    B = (15.8*A)-(18.3*(A**(2/3)))-(0.714*((Z**2)/(A**(1/3))))-(23.3*(((A-(2*Z))**2)/A))+(a5/(A**(1/2)))
    print('Approx. Binding Energy: ',B) #Prints approximate binding energy

semiEmpiricalMassFormula(58,28)

print('\nb.') #b
def semiEmpiricalMassFormula(A,Z): #Inputs A for mass number and Z for atomic number
    if A%2 == 0 and Z%2 == 0:
        a5 = 12.0
    elif A%2 == 0 and Z%2 != 0:
        a5 = -12.0
    elif A%2 != 0:
        a5 = 0
    B = (15.8*A)-(18.3*(A**(2/3)))-(0.714*((Z**2)/(A**(1/3))))-(23.3*(((A-(2*Z))**2)/A))+(a5/(A**(1/2)))
    print('Approx. Binding Energy per Nucleon: ',B/A) #Prints approximate binding energy per nucleon

semiEmpiricalMassFormula(58,28)

print('\nc.') #c
def semiEmpiricalMassFormula(Z): #Inputs Z for atomic number and runs through Z-3Z as values for atomic number
    max = 0
    for i in range((2*Z)+1):
        A = Z + i
        if A%2 == 0 and Z%2 == 0:
            a5 = 12.0
        elif A%2 == 0 and Z%2 != 0:
            a5 = -12.0
        elif A%2 != 0:
            a5 = 0
        B = (15.8*A)-(18.3*(A**(2/3)))-(0.714*((Z**2)/(A**(1/3))))-(23.3*(((A-(2*Z))**2)/A))+(a5/(A**(1/2)))
        if B/A > max:
            max = B/A
            maxStableA = A
    print('Most Stable Mass Number: ',maxStableA, '\nApprox. Binding Energy per Nucleon: ', max)
    #prints most stable mass number and the corresponding approximate binding energy

semiEmpiricalMassFormula(28)

print('\nd.') #d
for i in range(100):
    semiEmpiricalMassFormula(i+1)
    print('\n')

print('e.') #e
import matplotlib.pyplot as plt
import numpy as np

def semiEmpiricalMassFormula(A,Z): #Inputs A for mass number and Z for atomic number
    if A%2 == 0 and Z%2 == 0:
        a5 = 12.0
    elif A%2 == 0 and Z%2 != 0:
        a5 = -12.0
    elif A%2 != 0:
        a5 = 0
    B = (15.8*A)-(18.3*(A**(2/3)))-(0.714*((Z**2)/(A**(1/3))))-(23.3*(((A-(2*Z))**2)/A))+(a5/(A**(1/2)))
    return(B/A) #Returns approximate binding energy per nucleon

massList = []
atomicNumList = []
bindEnrgyList = []
f = open('nuclear_data.txt')
for line in f:
    if line[0] != '#':
        lineList = line.split()
        massList.append(float(lineList[0]))
        atomicNumList.append(float(lineList[1]))
        bindEnrgyList.append(float(lineList[5]))
f.close()

calcBindEnrgyList = []
for i in range(len(massList)):
    calcBindEnrgyList.append(semiEmpiricalMassFormula(massList[i],atomicNumList[i]))

massArr = np.array(massList)
bindEnrgyArr = np.array(bindEnrgyList)
calcBindEnrgyArr = np.array(calcBindEnrgyList)

plt.scatter(massArr, bindEnrgyArr, color='red', s=1, alpha=0.5)
plt.scatter(massArr, calcBindEnrgyArr, color='blue', s=1, alpha = 0.5)
plt.ylim(bottom=-1)
plt.legend(['Experimental Values','Calculated Values'])
plt.xlabel('Mass Number')
plt.ylabel('Binding Energy Per Nucleus')
plt.title('Atomic Mass vs. Binding Energy Per Nucleus')
plt.show()
