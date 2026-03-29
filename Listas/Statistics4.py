import pandas as pd
import numpy as np
from ..Bibliotecas.Lib1 import *
from ..Bibliotecas.Lib3 import *

    #Tabela de questões ->
    #a) Identifique a variável aleatória preditiva e a variável aleatória resposta e justifique seus critérios;
    #b) Construa a tabela de correlação-regressão de acordo com as normas da ABNT;
    #c) Calcule as variâncias marginais de C e P;
    #d) Calcule a covariância (variância cruzada) do dataset. Discuta o sinal da covariância e seu módulo;
    #e) Calcule o coeficiente de correlação linear r de Pearson. Podemos concluir que existe ou inexiste correlação linear neste caso?;
    #f) Teste a significância do r de Pearson obtido;
    #g) Calcule o erro padrão da média;
    #h) Calcule o coeficiente de determinação e interprete-o;
    #i) Convém determinar/desenhar uma lei empírica relacionando P com C? Justifique;
    #j) Classifique a correlação obtida;
    #k) Qual das variáveis aleatórias envolvidas é a mais dispersa comparativamente?
    #l) Faça uma estimativa da ordem de grandeza da produção de grãos na propriedade quando a concentração de
    #carbonatos chegar a 80 mol/l

def main() -> None:
    concen_carbono = [20,35,42,58,69,84,90,120,0]
    producao = [73,78,85,80,88,138,140,163,0]
    tamanho_amostra = len(concen_carbono) - 1
    #item a)
    #Seja um aumento na concentração de carbono a proposição P, e um aumento na produção a proposição Q.
    #Dessa relação conseguimos deduzir que sempre P->Q, mas a recíproca não. Um aumento na quantidade da carbono
    #numa hortaliça sempre impacta no desenvolvimento dos vegetais devido as necessidades de nutrientes, porém
    #uma alta produção não necessariamente implica numa alta concentraço de carbono, podendo ser devido a diversos
    #outros fatores que não estão sendo medidos aqui, portanto escolheremos P como variável preditora e Q como
    #variável resposta.
    
    #item b)
    indice = [1,2,3,4,5,6,7,8,"Soma"]
    df = pd.DataFrame(
        data=np.zeros((9,5)),
        index= indice,
        columns= ["xi", "yi", "xi²", "yi²", "xiyi"]
    )
    df["xi"] = concen_carbono
    df["yi"] = producao
    df["xi²"] = df["xi"]**2
    df["yi²"] = df["yi"]**2
    df["xiyi"] = df["xi"] * df["yi"]
    df.at["Soma", "xi"] = df.loc[1:8,"xi"].sum()
    df.at["Soma", "yi"] = df.loc[1:8,"yi"].sum()
    df.at["Soma", "xi²"] = df.loc[1:8,"xi²"].sum()
    df.at["Soma", "yi²"] = df.loc[1:8,"yi²"].sum()
    df.at["Soma", "xiyi"] = df.loc[1:8,"xiyi"].sum()

    #item c)
    var_marg_C = variancia_marginal(df.at["Soma","xi²"],df.at["Soma","xi"],tamanho_amostra) #type: ignore
    var_marg_P = variancia_marginal(df.at["Soma","yi²"],df.at["Soma","yi"],tamanho_amostra) #type: ignore
    
    #item d)
    cov = covariancia_amostral(df.at["Soma","xiyi"], df.at["Soma","xi"], df.at["Soma","yi"],tamanho_amostra) #type: ignore
    #Como podemos ver, a variância é positiva, portanto o sinal do r de pearson também será positivo.

    #item e)
    corc = correlacao(cov, var_marg_C, var_marg_P)
    #análise do r de pearson no próximo item!

    #item f)
    t_student = teste_t(tamanho_amostra,corc)
    #Pelo resultado de t_student = 5.995, e admitindo uma significância de 5%, com confiança de 95% (100%-5% = 95%), pelo t_tabelado ser 2.447, como t_student>t_tabelado
    #então rejeitamos a hipótese nula e corroboramos com a hipótese alternativa de que o r calculado é significante.

    #item g)    
    err = erro_padrao_med(tamanho_amostra,corc)

    #item h)
    r2 = corc**2
    #Pelo valor de r², apesar de a reta de regressão existir e ter poder preditivo, seu poder preditivo é baixo (inferior ao considerado satisfatório)
    #pois apenas 85% dos dados são explicados pela reta, já que r² = 0.85 então r² não está em [0.9, 1]

    #item i)
    #Não, pois a reta de regressão tem baixo poder preditivo devido a r²<0.9

    #item j)
    #Quanto ao sinal, por ser >0, a correlação evidencia uma proporcionalidade positiva entre as variáveis, evidenciando que à medida que uma cresce,
    #a outra também cresce. Quanto ao módulo de r, evidencia uma correlação forte, pois 0.9<=r<=1

    #item k)
    cvc = sqrt(var_marg_C)/MediaSimples(df.loc[1:8,"xi"].set_axis(range(8))) #type: ignore #Coeficiente de variacao percentual de CO2
    cvp = sqrt(var_marg_P)/MediaSimples(df.loc[1:8,"yi"].set_axis(range(8))) #type: ignore #Coeficiente de variacao percentual da produção
    #print("Concentracao de CO2 mais dispersa. ") if cvc>cvp else print("Producao mais dispersa. ")

    #item l)
    b1 = estimadorbeta1(cov, var_marg_C)
    b0 = estimadorbeta0(tamanho_amostra,df.at["Soma","xi"],df.at["Soma","yi"], b1) #type: ignore
    #print(f"Estimativa de {b1*80+b0} de produção quando a concentração de carbono ser 80mol/l. ")

main()
