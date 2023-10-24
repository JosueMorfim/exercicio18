
# Importando bibliotecas

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#abrindo 'gasolina.csv'

with open('./gasolina.csv', 'r', encoding= 'utf8') as file:
  data = pd.read_csv('gasolina.csv')

#gerando o grafico de linha
sns.set(style='whitegrid')
ax = sns.lineplot(data=data, x='dia', y='venda')
plt.xlabel('Dia')
plt.ylabel('Preço em R$')
plt.title('Preço da Gasolina na primeira semana de Julho/21')

plt.savefig('gasolina.png')

plt.show()
