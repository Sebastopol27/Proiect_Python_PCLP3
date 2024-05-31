import pandas as pd

# Citirea fișierului CSV
df = pd.read_csv('train.csv')

# Numărul de linii si coloane
linii, coloane = df.shape

# Tipurile datelor din fiecare coloană
tip_date = df.dtypes

# Numărul de valori lipsă pentru fiecare coloană
lipsa = df.isnull().sum()

# Verificarea dacă există linii duplicate
duplicate = df.duplicated().sum()

# Afișarea rezultatelor
print(f"1.Numărul de coloane: {coloane}\n")
print(f"2.Tipurile datelor din fiecare coloană:\n{tip_date}\n")
print(f"3.Numărul de valori lipsă pentru fiecare coloană:\n{lipsa}\n")
print(f"4.Numărul de linii: {linii}\n")
print(f"5.Numărul de linii duplicate: {duplicate}")
