# Dados fornecidos
meses = [
    "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro", "Janeiro", "Fevereiro"
]

estoques = [1501, 902, 1783, 1527, 2158, 2134, 1459, 1492, 1492, 2857, 2916, 2654]
consumos = [2112, 2084, 1313, 1626, 1759, 2167, 2258, 1091, 1091, 48, 1110, 1025]

# Cálculos
media_estoque = sum(estoques) / len(estoques)
media_consumo = sum(consumos) / len(consumos)

indice_percentual_estoque = (media_estoque / max(estoques)) * 100
indice_percentual_consumo = (media_consumo / max(consumos)) * 100

# Resultados
print("Resumo dos Indicadores Mensais:")
for i, mes in enumerate(meses):
    print(f"\n{mes}:")
    print(f"    Estoque: {estoques[i]}")
    print(f"    Consumo: {consumos[i]}")

print("\nResumo dos Indicadores Médios e Percentuais:")
print(f"\nMédia do Estoque: {media_estoque:.2f}")
print(f"Média do Consumo: {media_consumo:.2f}")
print(f"Índice Percentual de Estoque: {indice_percentual_estoque:.2f}%")
print(f"Índice Percentual de Consumo: {indice_percentual_consumo:.2f}%")
