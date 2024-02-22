import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Dados fornecidos
meses = [
    "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro", "Janeiro", "Fevereiro"
]

estoques = [1501, 902, 1783, 1527, 2158, 2134, 1459, 1492, 1492, 2857, 2916, 2654]
consumos = [2112, 2084, 1313, 1626, 1759, 2167, 2258, 1091, 1091, 48, 1110, 1025]

# Cálculos
percentuais_estoque = [(estoque / max(estoques)) * 100 for estoque in estoques]
percentuais_consumo = [(consumo / max(consumos)) * 100 for consumo in consumos]

# Plotagem do gráfico
plt.figure(figsize=(10, 6))

plt.plot(meses, percentuais_estoque, marker='o', label='Estoque (%)')
plt.plot(meses, percentuais_consumo, marker='o', label='Consumo (%)')

plt.title('Desempenho Mês a Mês com Percentuais')
plt.xlabel('Meses')
plt.ylabel('Percentual em Relação ao Máximo Mensal')
plt.legend()
plt.grid(True)

plt.show()
