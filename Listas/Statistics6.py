import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ..Bibliotecas.Lib1 import *
from ..Bibliotecas.Lib3 import *
    #Tabela de questões ->
    #a) Determine qual é a variável aleatória preditiva e qual é a variável aleatória resposta. Justifique;
    #b) Construa a tabela de correlação-regressão referente ao par de variáveis aleatórias;
    #c) Calcule a covariância (variância cruzada) entre os preços;
    #d) Calcule as variâncias marginais da distribuição;
    #e) Calcule o coeficiente de correlação linear r de pearson;
    #f) Podemos afirmar que existe ou não correlação linear entre P e G?
    #g) Teste a significância do r calculado;
    #h) Suponha que a hipótese da pesquisa é que, naquela região, o preço do pãozinho francês
    #e o preço da gasolina não estão correlacionados, como fazer para obter um r significante?

def main() -> None:
    prec_Pao = [8.00, 8.50, 8.20, 8.80, 8.70, 9.10, 9.40, 9.20, 8.80, 8.40, 7.80, 8.30]
    prec_Gas = [2.40, 2.50, 3.00, 3.20, 3.50, 3.60, 4.00, 4.40, 4.50, 4.80, 5.20, 5.50]
    tam = len(prec_Gas)
    
    #item a)
    #Não entendi muito bem o porquê de o preço da gasolina impactar no preço do pão frânces, mas o professor definiu assim. Portanto G->P mas P/->G
    x = prec_Gas
    y = prec_Pao
    
    #item b)
    #O professor usou uma técnica de normalização que, apesar de não ser necessária aqui, replicarei para manter os dados usados na lista.
    x.append(0)
    y.append(0)
    x = np.array(x)
    y = np.array(y)
    x = 10*x
    y = 10*y
    indice = list(range(1,13))
    indice.append('Soma') #type: ignore
    df = np.zeros((13,5))
    df = pd.DataFrame(
        data=df,
        index=indice,
        columns=['xi','yi','xi²','yi²','xiyi']
    )
    df['xi'] = x
    df.at['Soma','xi'] = df['xi'].sum()
    df['yi'] = y
    df.at['Soma','yi'] = df['yi'].sum()
    df['xi²'] = df['xi']**2
    df.at['Soma','xi²'] = df.loc[1:12,'xi²'].sum()
    df['yi²'] = df['yi']**2
    df.at['Soma','yi²'] = df.loc[1:12,'yi²'].sum()
    df['xiyi'] = df['xi']*df['yi']
    df.at['Soma','xiyi'] = df.loc[1:12,'xiyi'].sum()
    
    #item c)
    cov = covariancia_amostral(df.at['Soma','xiyi'],df.at['Soma','xi'],df.at['Soma','yi'],tam) #type: ignore 

    #item d)
    var_x = variancia_marginal(df.at['Soma','xi²'],df.at['Soma','xi'],tam) #type: ignore
    var_y = variancia_marginal(df.at['Soma','yi²'],df.at['Soma','yi'],tam) #type: ignore
    
    #item e)
    corc = correlacao(cov,var_x,var_y)
    
    #item f)
    #Só será possível confirmar correlação após a verificação do r calculado.

    #item g)
    t = teste_t(tam,corc)
    #Como t<t_tab então corroboramos com a hipótese nula e concluímos que o r calculado não é confiável

    #item h)
    #Devido ao baixo tamanho do dataset e pela ausência de correlação entre as variáveis, seria necessário um maior
    #conjunto de dados e com baixo ruído na amostra, tendo em vista que a reta de mínimos quadrados possui um baixo
    #poder preditivo no momento pois r² é baixo (<0.9).
main()