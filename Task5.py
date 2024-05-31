import pandas as pd
import matplotlib.pyplot as plt

# Citirea fișierului CSV
df = pd.read_csv('train.csv')

# Definirea categoriilor de vârstă și etichetelor
bins = [0, 20, 40, 60, df['Age'].max()]
labels = ['0-20', '21-40', '41-60', '61+']

# Crearea unei coloane suplimentare pentru categoriile de vârstă
df['AgeCategory'] = pd.cut(df['Age'], bins=bins, labels=labels, right=True)

# Determinarea numărului de pasageri din fiecare categorie de vârstă
age_category_counts = df['AgeCategory'].value_counts().sort_index()

# Crearea fisierului cu noua coloana
df.to_csv('task5_output.csv', index=False)

# Afișarea rezultatelor
print(f"Numărul de pasageri pentru fiecare categorie de vârstă:\n{age_category_counts}\n")

# Realizarea graficului
fig, ax = plt.subplots(figsize=(10, 6))
age_category_counts.plot(kind='bar', color=['#ff9999','#66b3ff','#99ff99','#ffcc99'], ax=ax)
ax.set_xlabel('Categorie de vârstă')
ax.set_ylabel('Numărul de pasageri')
ax.set_title('Numărul de pasageri pentru fiecare categorie de vârstă')
plt.xticks(rotation=0)
plt.show()

