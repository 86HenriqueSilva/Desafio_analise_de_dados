import plotly.graph_objects as go

# Dados fornecidos
meses = [
    "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro", "Janeiro", "Fevereiro"
]

estoques = [1501, 902, 1783, 1527, 2158, 2134, 1459, 1492, 1492, 2857, 2916, 2654]
consumos = [2112, 2084, 1313, 1626, 1759, 2167, 2258, 1091, 1091, 48, 1110, 1025]

# Criação do gráfico de barras horizontais
fig = go.Figure()

fig.add_trace(go.Bar(
    x=estoques,
    y=meses,
    orientation='h',
    name='Estoque'
))

fig.add_trace(go.Bar(
    x=consumos,
    y=meses,
    orientation='h',
    name='Consumo'
))

# Atualização do layout
fig.update_layout(
    title='Desempenho Mês a Mês - Barras Horizontais',
    xaxis_title='Valores',
    yaxis_title='Meses',
    barmode='stack',  # 'stack' para empilhar as barras horizontalmente
)

# Exibição do gráfico
fig.show()
