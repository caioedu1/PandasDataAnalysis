import pandas as pd



def queries():
    # abrir e ler arquivo
    arquivo = pd.read_excel('Vendas.xlsx')
    pd.set_option('display.max_columns', None)

    # 1. Análise de vendas por loja -> Qual loja vendeu mais e qual vendeu menos.
    # a) Qual loja vendeu mais.
    lojas_agrupadas = arquivo.groupby('ID Loja')
    lojamax = lojas_agrupadas['Valor Final'].sum().idxmax()
    nomelojamax = arquivo.loc[arquivo['ID Loja'] == lojamax, 'ID Loja'].iloc[0]
    # Iguatemi Campinas vendeu mais

    # b) Qual loja vendeu menos.
    lojamin = lojas_agrupadas['Valor Final'].max().idxmin()
    nomelojamin = arquivo.loc[arquivo['ID Loja'] == lojamin, 'ID Loja'].iloc[0]

    # Printar lojas que venderam mais e menos
    print('Loja que mais vendeu:',nomelojamax)
    print('Loja que menos vendeu:',nomelojamin)
queries()