import pandas as pd

# Citirea fișierului CSV
df = pd.read_csv('train.csv')

# Numărul de linii si coloane
linii, coloane = df.shape

# Numărul de valori lipsă pentru fiecare coloană
lipsa = df.isnull().sum()

# Filtrarea coloanelor care au valori lipsă (numărul de valori lipsă diferit de 0)
lipsa = lipsa[lipsa > 0]

# Determinarea proportiilor valorilor lipsa
m = lipsa.shape[0]
proportii = []
for i in range (0, m):
    proportii.append(lipsa.iloc[i] * 100 / linii)

# Afișarea rezultatelor
print(f"Numărul de valori lipsă pentru fiecare coloană:\n{lipsa}\n")
print(f"Proportia valorilor lipsă:\n{proportii}\n")

# Df doar cu cei morti
morti = df[df['Survived'] == 0]
# Df doar cu cei vii
vii = df[df['Survived'] == 1]

# Reducerea Df-ului doar la valorile lipsa pentru vii
lipsa_vii = vii.isnull().sum()
lipsa_vii = lipsa_vii[lipsa_vii > 0]
# Reducerea Df-ului doar la valorile lipsa pentru morti
lipsa_morti = morti.isnull().sum()
lipsa_morti = lipsa_morti[lipsa_morti > 0]

# Creare vector de proportii in functie de numarul total de valorile lipsa
m = lipsa_vii.shape[0]
proportii = []
for i in range (0, m):
    proportii.append(lipsa_vii.iloc[i] * 100 / linii)

# Aici acelasi lucru dar pentru cei morti
m = lipsa_morti.shape[0]
prop2 = []
for i in range (0, m):
    prop2.append(lipsa_morti.iloc[i] * 100 / linii)

# Afisare rezultate
print(f"Numărul de valori lipsă pentru morti:\n{lipsa_morti}\n")
print(f"Procentul lipsa pentru morti:\n{prop2}\n")
print(f"Proportia valorilor lipsă pentru vii:\n{lipsa_vii}\n")
print(f"Procentul lipsa pentru vii:\n{proportii}\n")