from ..Bibliotecas.Lib1 import *
from ..Bibliotecas.Lib2 import *
import numpy as np
import pandas as pd

    #Tabela de questões ->
    #a) Complete os campos faltantes na distribuição de frequências com dados agrupados em intervalos de classe acima;
    #b) Calcule as medidas de tendência central: média, moda e mediana. Moda pelo método de King;
    #c) Calcule as seguintes medidas de dispersão: variância, desvio padrão e coeficiente de variação
    #percentual (ou desvio padrão relativo);
    #d) Utilize o método da interpolação linear da ogiva para estimar o número de pessoas vacinadas entre
    #37 e 49 anos de idade
    #e) Utilize o método do desenho para calcular as seguintes separatrizes: Primeiro quartil, terceiro quartil
    # décimo percentil e nonagésimo percentil;
    #f) Utilize a fórmula de bowley e o coeficiente percentílico de curtose para calcular as medidas de forma (assimetria e curtose);
    #g) Classifique a distribuição quanto à forma do histograma de frequências e determine se ela pode ou
    #não ser considerada como aproximadamente normal;

def main() -> None:
    #Devido a forma que a questão deve ser feita, usarei outra biblioteca, feita apenas para ela
    #e que colocarei numa lib separada. Também usarei pandas e numpy pois eles facilitarão o tratamento da tabela
    
    #item a)
    idades_inf = [15,25,35,45,55,65,0]
    idades_sup = [25,35,45,55,65,75,0]
    fi = [9,13,22,18,8,5,0]
    indices = [1,2,3,4,5,6,"Soma"]

    df = np.zeros((7,10))
    
    df = pd.DataFrame(
        data= df,
        index= indices,
        columns= ["idades_inf","idades_sup","xi","fi","Fac","xi²","fixi","fixi²","fri","Facri"]
    )
    
    df["fi"] = fi
    
    df.at["Soma","fi"] = df.loc[1:6,"fi"].sum() #type: ignore
    
    df["idades_inf"] = idades_inf
    
    df["idades_sup"] = idades_sup
    
    df["xi"] = (df["idades_sup"]+df["idades_inf"])/2
    
    j = 1
    for i in df.loc[1:6,"fi"]:
        if i == df.at[1,"fi"]: df.at[1,"Fac"] = df.at[1,"fi"]
        else: 
            df.at[j,"Fac"] = df.at[j,"fi"]+df.at[j-1,"Fac"] #type: ignore
        j+=1
    
    df["xi²"] = df["xi"]**2
    
    df["fixi"] = df["xi"] * df["fi"]
    df.at["Soma","fixi"] = df.loc[1:6,"fixi"].sum()
    
    df["fixi²"] = df["xi²"] * df["fi"]
    df.at["Soma","fixi²"] = df.loc[1:6,"fixi²"].sum()
    
    df["fri"] = df["fi"]/df.at["Soma","fi"] #type: ignore
    
    j = 1
    for i in df.loc[1:6,"fri"]:
        if i == df.at[1,"fri"]: df.at[1,"Facri"] = df.at[1,"fri"]
        else: 
            df.at[j,"Facri"] = df.at[j,"fri"]+df.at[j-1,"Facri"] #type: ignore
        j+=1
    
    #item b)
    mediaAmostral = (df.loc[1:6,"fixi"].sum())/df.at["Soma","fi"] #type: ignore
    
    maior_fre = [1,df.at[1,"fi"]]
    for i,j in enumerate(df.loc[1:6,"fi"],1):
        if maior_fre[1]<j:
            maior_fre[0] = i
            maior_fre[1] = j
    modaAmostral = moda_King(df.at[maior_fre[0], "idades_inf"], df.at[maior_fre[0],"idades_sup"], df.at[maior_fre[0]-1,"fi"], df.at[maior_fre[0]+1,"fi"]) #type: ignore
    
    len = df.at["Soma","fi"] 

    freqs_md = encontra_classe(len/2, df.loc[1:6,"idades_sup"]) #type: ignore
    medianaAmostral = mediana_Desenho(df.at[freqs_md[0],"idades_inf"], len, df.at[freqs_md[0],"fi"], df.at[freqs_md[0]-1,"Fac"], df.at[freqs_md[0],"idades_sup"]-df.at[freqs_md[0],"idades_inf"]) #type: ignore
    
    #item c)
    variancia = (df.at["Soma","fixi²"]-(1/len)*(df.at["Soma","fixi"]**2))/(len-1) #type: ignore
    
    desvio_padrao = (variancia)**(1/2)
    
    desvio_padrao_relativo = (desvio_padrao/mediaAmostral)*100

    #item d)

    val_foc1 = 37
    clas_foc1 = encontra_classe(val_foc1,df.loc[1:6,"idades_sup"]) #type: ignore
    F1 = linear_Interpol(df.at[clas_foc1[0],"idades_sup"], df.at[clas_foc1[0],"idades_inf"], df.at[clas_foc1[0]-1,"Fac"], df.at[clas_foc1[0],"Fac"], val_foc1) #type: ignore

    val_foc2 = 49
    clas_foc2 = encontra_classe(val_foc2,df.loc[1:6,"idades_sup"]) #type: ignore
    F2 = linear_Interpol(df.at[clas_foc2[0],"idades_sup"], df.at[clas_foc2[0],"idades_inf"], df.at[clas_foc2[0]-1,"Fac"], df.at[clas_foc2[0],"Fac"], val_foc2) #type: ignore
    
    F_chapeu = int(F2-F1)+1 #a função int faz o floor do valor, e para obter seu ceil somamos 1
    
    #item e)

    #O primeiro quartil tem separatriz 1/4, então tomemos sep1 = 1/4
    sep1 = 1/4
    class_Q1 = encontra_classe(sep1*len,df.loc[1:6,"Fac"]) #type: ignore
    Q1 = separatriz_classes(sep1, len, df.at[class_Q1[0],"idades_inf"], df.at[class_Q1[0]-1,"Fac"], df.at[class_Q1[0],"fi"], df.at[class_Q1[0],"idades_sup"] - df.at[class_Q1[0],"idades_inf"]) #type: ignore

    #O terceiro quartil tem separatriz 3/4, então tomemos sep3 = 3/4
    sep3 = 3/4
    class_Q3 = encontra_classe(sep3*len, df.loc[1:6,"Fac"]) #type: ignore
    Q3 = separatriz_classes(sep3, len, df.at[class_Q3[0],"idades_inf"], df.at[class_Q3[0]-1,"Fac"], df.at[class_Q3[0], "fi"], df.at[class_Q3[0],"idades_sup"] - df.at[class_Q3[0],"idades_inf"]) #type: ignore
    
    #O décimo percentil tem separatriz 1/10, então tomemos sep10 = 1/10
    sep10 = 1/10
    class_P10 = encontra_classe(sep10*len, df.loc[1:6,"Fac"]) #type: ignore
    if(class_P10[0]==1): P10 = separatriz_classes(sep10,len,df.at[class_P10[0],"idades_inf"], 0, df.at[class_P10[0],"Fac"], df.at[class_P10[0],"idades_sup"] - df.at[class_P10[0],"idades_inf"]) #type: ignore
    else: P10 = separatriz_classes(sep10,len,df.at[class_P10[0],"idades_inf"], 0, df.at[class_P10[0],"Fac"], df.at[class_P10[0],"idades_sup"] - df.at[class_P10[0],"idades_inf"]) #type: ignore
    
    #O nonagésimo percentil tem separatriz 9/10, então tomemos sep90 = 9/10
    sep90 = 9/10
    class_P90 = encontra_classe(sep90*len,df.loc[1:6,"Fac"]) #type: ignore
    P90 = separatriz_classes(sep90, len, df.at[class_P90[0],"idades_inf"], df.at[class_P90[0]-1,"Fac"], df.at[class_P90[0],"fi"], df.at[class_P90[0],"idades_sup"] - df.at[class_P90[0],"idades_inf"]) #type: ignore
    
    #item f)
    assmtr = Assimetria(Q3,Q1,medianaAmostral)
    curt = Curtose(Q3-Q1,P90,P10)

    #item g)
    ass_B = False
    if(abs(assmtr)<=0.05):
        print("Sua distribuição é simétrica. ")
        ass_B = True
    else: print("Sua distribuição não é simétrica.")
    
    cur_B = False
    if( (0.263-curt)/0.263 < 0.05):
        print("Sua distribuição é mesocúrtica. ")
        cur_B = True
    else: print("Sua distribuição não é mesocúrtica. ")

    if(ass_B and cur_B): print("Sua distribuição é aproximadamente normal. ")
    
main()