import pandas as pd
import plotly.express as px

# passo 1: importar a base de dados
tabela = pd.read_csv("telecom_users.csv")



# passso 2: vvizualizar a base de dados
# - entender as informações disponiveis
# - descobrir as cagadas da base da dados
#axis == 9 ->linha // axis ==1 ->coluna
tabela = tabela.drop("Unnamed: 0", axis=1)
print(tabela)





# passo 3: tratamento de dados
#valores reconhecidos de forma errada
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

#Resolver valores vazios

#excluir colunas completamentes vazias (todos valores vazios)
tabela = tabela.dropna(how="all", axis=1)

#excluir linhas com pelo menos um valor vazio
tabela = tabela.dropna(how="any", axis=0)

print(tabela.info())

# passo 4: analise inicial
print(tabela["Churn"].value_counts())

print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# passo 5: analise detalhada - descobrir as causass do cancelamento

#comparar cada coluna da base com a coluna chhurn

#cria o grafico para cada coluna
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn")
    grafico.show()
