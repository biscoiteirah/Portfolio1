import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Suppress warnings (optional)
import warnings
warnings.filterwarnings("ignore")

# Data for campaign performance
dados_campanha = {
    'Plataforma': ['Facebook', 'Instagram', 'Facebook', 'Instagram'],
    'Período': ['Antes', 'Antes', 'Depois', 'Depois'],
    'Curtidas': [1000, 5000, 2000, 10000],
    'Comentários': [50, 200, 100, 500],
    'Compartilhamentos': [20, 100, 50, 200]
}

# Create a DataFrame
df = pd.DataFrame(dados_campanha)

# Convert 'Período' to categorical for better plotting
df['Período'] = pd.Categorical(df['Período'], categories=['Antes', 'Depois'], ordered=True)

# Bar plot for comments
plt.figure(figsize=(10, 6))  # Fixed typo in figsize
sns.barplot(data=df, x='Plataforma', y='Comentários', hue='Período')
plt.title('Comentários nas Redes Sociais')
plt.xlabel('Plataforma')
plt.ylabel('Número de Comentários')
plt.legend(title='Período')
plt.show()

# Data for brand perception
percepcao_marca = {
    'Período': ['Antes', 'Depois'],
    'Positiva': [60, 80],
    'Negativa': [20, 10]
}

# Create a DataFrame
df_percepcao = pd.DataFrame(percepcao_marca)

# Convert 'Período' to categorical for better plotting
df_percepcao['Período'] = pd.Categorical(df_percepcao['Período'], categories=['Antes', 'Depois'], ordered=True)

# Line plot for brand perception
plt.figure(figsize=(8, 6))
sns.lineplot(data=df_percepcao, x='Período', y='Positiva', label='Positiva', marker='o')
sns.lineplot(data=df_percepcao, x='Período', y='Negativa', label='Negativa', marker='o')
plt.title('Percepção da Marca')
plt.xlabel('Período')
plt.ylabel('Percentual (%)')
plt.legend(title='Sentimento')
plt.show()