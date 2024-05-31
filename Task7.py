import pandas as pd
import matplotlib.pyplot as plt

# Citirea fișierului CSV
df = pd.read_csv('train.csv')

# Adăugarea unei coloane suplimentare pentru a indica dacă persoana este copil (vârstă < 18 ani) sau adult
df['IsChild'] = df['Age'] < 18
print(f"Procentul copiilor aflați la bord: {df['IsChild']}%")
# Calcularea procentului copiilor și adulților aflați la bord
pasageri = df.shape[0]
copii = df['IsChild'].sum()
adulti = pasageri - copii

pr_copii = copii * 100 / pasageri
pr_adulti = adulti * 100 / pasageri

print(f"Procentul copiilor aflați la bord: {pr_copii:.2f}%")
print(f"Procentul adulților aflați la bord: {pr_adulti:.2f}%")

# Calcularea ratei de supraviețuire pentru copii și pentru adulți
rata_copii = df[df['Survived'] == 1]
m = rata_copii.shape[0]
rata_copii = rata_copii['IsChild'].sum()
rata_adulti = m - rata_copii
rata_copii = rata_copii * 100 / copii
rata_adulti = rata_adulti * 100 / adulti

print(f"Rata de supraviețuire pentru copii: {rata_copii:.2f}%")
print(f"Rata de supraviețuire pentru adulți: {rata_adulti:.2f}%")

# Realizarea unui grafic pentru a vizualiza rata de supraviețuire
labels = ['Children', 'Adults']
survival_rates = [rata_copii, rata_adulti]

fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(labels, survival_rates, color=['#ff9999','#66b3ff'])
ax.set_xlabel('Group')
ax.set_ylabel('Survival Rate (%)')
ax.set_title('Survival Rate by Age Group')
plt.ylim(0, 100)
plt.show()
