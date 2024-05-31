import pandas as pd
import matplotlib.pyplot as plt

# Citirea fișierului CSV
df = pd.read_csv('task5_output.csv')

df = df[df['Survived'] == 1]
df = df[df['Sex'] == 'male']
df = df.dropna()
categorie = df['AgeCategory'].value_counts()

# Afișarea rezultatelor
print(f"Numărul de pasageri pentru fiecare categorie de vârstă:\n{categorie}\n")

fig, ax = plt.subplots(figsize=(10, 6))
categorie.plot(kind='bar', color=['#ff9999','#66b3ff','#99ff99','#ffcc99'], ax=ax)
ax.set_xlabel('Categorie de vârstă')
ax.set_ylabel('Numărul de supravietuitori')
ax.set_title('Numărul de supravietuitori in functie de varsta')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('Task6.png')