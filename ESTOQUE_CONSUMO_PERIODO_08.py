import matplotlib.pyplot as plt

# Dados fornecidos
meses = [
    "Março", "Abril", "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro", "Janeiro", "Fevereiro"
]

estoques = [1501, 902, 1783, 1527, 2158, 2134, 1459, 1492, 1492, 2857, 2916, 2654]
consumos = [2112, 2084, 1313, 1626, 1759, 2167, 2258, 1091, 1091, 48, 1110, 1025]

# Criação do gráfico de barras horizontais
fig, ax = plt.subplots()

# Barras para o Estoque
ax.barh(meses, estoques, label='Estoque')

# Barras para o Consumo
ax.barh(meses, consumos, left=estoques, label='Consumo')

# Configurações do gráfico
ax.set_xlabel('Valores')
ax.set_ylabel('Meses')
ax.set_title('Desempenho Mês a Mês - Barras Horizontais')
ax.legend()

# Exibição do gráfico
plt.show()
