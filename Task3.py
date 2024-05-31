import pandas as pd
import matplotlib.pyplot as plt

# Citirea fișierului CSV
df = pd.read_csv('train.csv')

# Identificarea coloanelor cu valori numerice
coloana_numerica = df.select_dtypes(include=['int64', 'float64']).columns

# Generarea histogramei pentru fiecare coloană numerică
for coloana in coloana_numerica:
    plt.figure(figsize=(8, 6))
    plt.hist(df[coloana].dropna(), bins=100, color='skyblue', edgecolor='black')
    plt.title(f'Histograma pentru coloana "{coloana}"')
    plt.xlabel('Valoare')
    plt.ylabel('Număr de exemple')
    plt.grid(True)
    plt.show()