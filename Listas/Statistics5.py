from ..Bibliotecas.Lib1 import *
from ..Bibliotecas.Lib3 import *
import numpy as np
import pandas as pd

    #Tabela de questões ->
    #a) Determine qual é a variável aleatória preditiva, qual é a variável resposta e justifique tecnicamente;
    #b) Construa a
    #  tabela de correlação-regressão de acordo com as normas da ABNT;
    #c) Calcule as variâncias marginais;
    #d) Qual das suas variáveis aletaórias é a mais dispersa?
    #e) Calcule a covariância do dataset. Interprete-a;
    #f) Calcule o coeficiente de correlação linear r de pearson;
    #g) Podemos afirmar que existe correlação entre a concentração da substância S no aditivo A e o tempo de secagem da tinta? Verifique;
    #h) Convém desenhar uma lei empírica do tipo T_chapeu = F(s)? (Ou seja, uma lei que permite estimar o tempo de secagem da tinta
    #a partir da concentração adotada para a susbtância S dentro do aditivo utilizado?)
    #i) Interprete o significado Geométrico do coeficiente de determinação;
    #j) Calcule os estimadores da reta de regressão;
    #l) Interprete os estimadores;

def main() -> None:
    conct_tinta = [2,4,6,8,10,12,14,16]
    temp_min = [4.8,4.3,3.9,3.2,2.7,2.5,2.1,1.6]
    tam = len(conct_tinta)
    #Tabela inicial da questão:
    tab = pd.DataFrame(
        data=np.vstack([conct_tinta,temp_min]),
        index=["S(%)","T(Min)"],
        columns=range(1,9)
    )

    #item a)
    #Perceba que a concentração de aditivo impacta diretamente no tempo que a tinta levará para secar, todavia o tempo não impacta de forma
    #alguma no aditivo. portanto S->T mas T-/>S. Logo faremos X = S e Y = T

    #item b)
    df = pd.DataFrame(
        data=np.zeros((9,5)),
        index=[1,2,3,4,5,6,7,8,"Soma"],
        columns=["xi","yi","xi²","yi²","xiyi"]
    )

    df.loc[1:8,"xi"] = tab.loc["S(%)",1:8]
    df.at["Soma","xi"] = df.loc[1:8,"xi"].sum()
    df.loc[1:8,"yi"] = tab.loc["T(Min)",1:8]*10 #Farei a mesma conversão que o professor fez na lista, mas o ideal seria com os dados sem conversão
    df.at["Soma","yi"] = df.loc[1:8,"yi"].sum()
    df.loc[1:8,"xi²"] = df.loc[1:8,"xi"]**2
    df.at["Soma","xi²"] = df.loc[1:8,"xi²"].sum()
    df.loc[1:8,"yi²"] = df.loc[1:8,"yi"]**2
    df.at["Soma","yi²"] = df.loc[1:8,"yi²"].sum()
    df.loc[1:8,"xiyi"] = df.loc[1:8,"xi"] * df.loc[1:8,"yi"]
    df.at["Soma","xiyi"] = df.loc[1:8,"xiyi"].sum()
    
    #item c)
    var_marg_S = variancia_marginal(df.at["Soma","xi²"],df.at["Soma","xi"],tam) #type: ignore
    var_marg_T = variancia_marginal(df.at["Soma","yi²"],df.at["Soma","yi"],tam) #type: ignore
    
    #item d)
    var_percentual_S = Var_Per(sqrt(var_marg_S),MediaSimples(df.loc[1:8,"xi"].set_axis(range(8)))) #type: ignore
    var_percentual_T = Var_Per(sqrt(var_marg_T),MediaSimples(df.loc[1:8,"yi"].set_axis(range(8)))) #type: ignore
    #print("Amostra S é mais dispersa. ") if var_percentual_S>var_percentual_T else print("Amostra T é mais dispersa. ")

    #item e)
    cov = covariancia_amostral(df.at["Soma","xiyi"],df.at["Soma","xi"],df.at["Soma","yi"],tam) #type: ignore
    #print("Pelo sinal da covariância, à medida que S cresce T decresce. ") if cov<0 else print("Pelo sinal da covariância, à medida que S cresce T também cresce. ")

    #item f)
    corc = correlacao(cov,var_marg_S,var_marg_T)
    
    #item g)
    t_student = teste_t(tam,corc)
    #Pelo valor do t calculado de 22.98 (ou 23 aproximadamente), quando observamos o t tabelado vemos que Ttab = 2.44, e como t>Ttab concluímos
    #a hipótese alternativa e admitimos que o r calculado é confiável. Portanto existe correlação entre as variáveis.

    #item h)
    #print("A reta possui alto poder preditivo. ") if corc**2>0.9 else print("A reta possui baixo poder preditivo. ")
    #Sim, pois o valor de r² é maior que 0.9, portanto a reta de mínimos quadrados possui alto poder preditivo.

    #item i)
    #Como r²=0.98, então cerca de 98% dos pontos são explicados pelo modelo linear.

    #item j)
    b1 = estimadorbeta1(cov,var_marg_S)
    b0 = estimadorbeta0(tam,df.at["Soma","xi"],df.at["Soma","yi"],b1) #type: ignore
    #Como b1 e b0 estão em 0.1*min/%, então dividimos por 10 para consertar a unidade de medida
    b1/=10
    b0/=10
    
    #item l)
    #Como b1 = -0.23, então a cada 1% de aumento de concentração na substância S, acrescenta-se 0.23 minutos no tempo de secagem;
    #Como b0 = 5.18, então na ausência de concentração de S, tem-se que o tempo de secagem da tinta é cerca de 5.18 minutos;
    
main()