import pandas as pd



def queries():
    # abrir e ler arquivo
    arquivo = pd.read_excel('Vendas - DataAnalysis 2.xlsx')
    pd.set_option('display.max_columns', None)
    # <-----------------------------------------------------------------------------> #
    # 1. Análise de vendas por loja -> Qual loja vendeu mais e qual vendeu menos.
    # a) Qual loja vendeu mais.
    lojas_agrupadas = arquivo.groupby('ID Loja')
    lojamax = lojas_agrupadas['Valor Final'].sum().idxmax()
    nomelojamax = arquivo.loc[arquivo['ID Loja'] == lojamax, 'ID Loja'].iloc[0]

    # b) Qual loja vendeu menos.
    lojamin = lojas_agrupadas['Valor Final'].max().idxmin()
    nomelojamin = arquivo.loc[arquivo['ID Loja'] == lojamin, 'ID Loja'].iloc[0]

    # Printar análise de vendas por loja
    print('Análise de vendas por loja:\n')
    print('Loja que mais vendeu:',nomelojamax)
    print('Loja que menos vendeu:',nomelojamin)
    print('-'*45)
    # <-----------------------------------------------------------------------------> #
    # 2. Análise de vendas por produto -> Quais produtos foram mais vendidos e quais foram menos. Calcular qnt. média de cada produto por transação e quais produtos são mais lucrativos.
    # a) Qual produto foi mais vendido.
    produtos_agrupados = arquivo.groupby('Produto')
    maisvend = produtos_agrupados['Valor Final'].sum().idxmax()
    nomeprdtmaisvend = arquivo.loc[arquivo['Produto'] == maisvend, 'Produto'].iloc[0]

    # b) Qual produto foi menos vendido
    menosvend = produtos_agrupados['Valor Final'].max().idxmin()
    nomeprdtmenosvend = arquivo.loc[arquivo['Produto'] == menosvend, 'Produto'].iloc[0]

    # c) Qnt. média de cada produto por transação.
    med_por_trnsç = produtos_agrupados['Quantidade'].mean()
    med_por_trnsç_df = pd.DataFrame(med_por_trnsç)

    # Printar análise de vendas por produto
    print('Análise de vendas por produto:\n')
    print('Produto que mais vendeu:', nomeprdtmaisvend)
    print('Produto que menos vendeu:', nomeprdtmenosvend)
    
    print(f'''Quantidade média aproximada de produtos por transação: 
{round(med_por_trnsç, 0).to_string(name=False)}\n''')
    print('-'*45)
    # <-----------------------------------------------------------------------------> #
    # 3. Análise de vendas por data -> Análise das vendas ao longo do tempo para identificar as tendências sazonais. Verificar se há períodos específicos onde as vendas aumentam ou diminuem.
    
queries()