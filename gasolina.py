
sns.set(style='whitegrid')
ax = sns.lineplot(data=data, x='dia', y='venda')
plt.xlabel('Dia')
plt.ylabel('Preço em R$')
plt.title('Preço da Gasolina na primeira semana de Junho/21')

plt.savefig('gasolina.png')

plt.show()

