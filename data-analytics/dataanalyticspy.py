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
    # a) Análise das vendas antes do dia 10 (Até 24 dias pro Natal)
    print ('Análise de vendas por data:\n')
    analise1 = arquivo.loc[arquivo['Data'] < '2019/12/11']
    analise1_df = pd.DataFrame(analise1)
    analise1_df_sum = analise1_df['Valor Final'].sum()
    print('Receita total nos 10 primeiros dias de Dezembro: R${:,.2f}'.format(analise1_df_sum))

    # b) Análise das vendas entre o dia 11 e 20 (inclusos)
    analise2 = arquivo.loc[(arquivo['Data'] < '2019/12/21') & (arquivo['Data'] > '2019/12/10')]
    analise2_df = pd.DataFrame(analise2)
    analise2_df_sum = analise2_df['Valor Final'].sum()
    print('Receita total de vendas no período entre os dias 11 e 20 de dezembro: R${:,.2f}'.format(analise2_df_sum))

    # c) Análise das vendas nos ultimos 10 dias de dezembro (Pré e pós Natal).
    analise3 = arquivo.loc[(arquivo['Data'] <= '2019/12/31') & (arquivo['Data'] > '2019/12/20')]
    analise3_df = pd.DataFrame(analise3)
    analise3_df_sum = analise3_df['Valor Final'].sum()
    print('Receita total de vendas nos ultimos 10 dias de dezembro: R${:,.2f}'.format(analise3_df_sum))
    
    # d) Conclusões
    print ('\n')
    analise1_2 = analise1_df_sum / analise2_df_sum * 100
    print ('Comparando os 10 primeiros dias com os 10 dias da metade de dezembro, podemos observar uma queda de aproximadamente {:.2f}%'.format(analise1_2))
    analise2_3 = analise3_df_sum / analise2_df_sum * 100
    print ('Comparando os 10 dias da metade de dezembro com os 10 ultimos dias de dezembro, podemos observar um aumento de aproximadamente {:.2f}%'.format(analise2_3))
    analise1_3 = analise3_df_sum / analise1_df_sum * 100
    print ('Comparando os 10 primeiros dias com os 10 ultimos dias de dezembro, podemos observar um aumento de aproximadamente {:.2f}%'.format(analise1_3))
    print ('-'*45)
    # <-----------------------------------------------------------------------------> #
    # 4. Análise de preço: Analise o preço médio de cada produto e identifique se existe algum padrão em relação aos produtos mais caros ou mais baratos. Compare os preços entre diferentes lojas e verifique se há variações significativas.
    # a) Analise o preço médio de cada produto e identifique se existe algum padrão em relação aos produtos mais caros ou mais baratos.
    print("Análise de preço por produto:\n")
    med_prod = produtos_agrupados['Valor Unitário'].mean()
    med_prod_df = pd.DataFrame(med_prod)
    print('Valor Unitário')
    print(med_prod_df.to_string)



queries()