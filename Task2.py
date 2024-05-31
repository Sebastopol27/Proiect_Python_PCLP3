import pandas as pd
import matplotlib.pyplot as plt

# Citirea fișierului CSV
df = pd.read_csv('train.csv')

# Numărul de linii si coloane
linii, coloane = df.shape

# Determinarea procentului persoanelor care au supraviețuit și care nu au supraviețuit
oameni = df['Survived'].value_counts()
pr_vii = oameni.get(1) * 100 / linii
pr_morti = oameni.get(0) * 100 / linii

# Determinarea procentului pasagerilor pentru fiecare tip de clasă (Pclass)
tipuri_clase = df['Pclass'].value_counts()
pr_clasa1 = tipuri_clase.get(1) * 100 / linii
pr_clasa2 = tipuri_clase.get(2) * 100 / linii
pr_clasa3 = tipuri_clase.get(3) * 100 / linii

# Determinarea procentului bărbaților și femeilor
sex = df['Sex'].value_counts()
pr_barbati = sex.get('male') * 100 / linii
pr_femei = sex.get('female') * 100 / linii

# Afișarea rezultatelor
print(f"Procentul persoanelor care au supraviețuit: {pr_vii:.2f}%")
print(f"Procentul persoanelor care nu au supraviețuit: {pr_morti:.2f}%\n")
print("Procentul pasagerilor pentru fiecare tip de clasă:")
print(f"Clasa 1: {pr_clasa1:.2f}%\nClasa 2: {pr_clasa2:.2f}%\nClasa 3: {pr_clasa3:.2f}%\n")
print("Procentul bărbaților și femeilor:")
print(f"Barbati: {pr_barbati:.2f}%\nFemei: {pr_femei:.2f}%")

# Crearea graficelor
fig, graf = plt.subplots(1, 3, figsize=(20, 5))

# Grafic pentru supraviețuire
graf[0].pie([pr_vii, pr_morti], labels=['Au supraviețuit', 'Nu au supraviețuit'], autopct='%1.2f%%', colors=['blue','red'])
graf[0].set_title('Procentul persoanelor care au supraviețuit')

# Grafic pentru clase
graf[1].bar(['Clasa 1', 'Clasa 2', 'Clasa 3'], [pr_clasa1, pr_clasa2, pr_clasa3], color=['blue','red','green'])
graf[1].set_ylabel('Procent')
graf[1].set_title('Procentul pasagerilor pentru fiecare clasă')

# Grafic pentru gen
graf[2].pie([pr_barbati, pr_femei], labels=['Bărbați', 'Femei'], autopct='%1.2f%%', colors=['blue','red'])
graf[2].set_title('Procentul bărbaților și femeilor')

plt.tight_layout()
plt.savefig('Task2.png')