from ..Bibliotecas.Lib1 import *

    #Tabela de questões ->
    #a) Supondo que os dados são todos representativos, coloque-os em rol;
    #b) Quantas classes há ao todo?
    #c) Construa a distribuição de frequências com dados discretos para o rol que você obteve. Utilize as regras da ABNT;
    #d) Calcule a média aritmética do dataset;
    #e) Determine a moda da distribuição;
    #f) Determine a mediana da distribuição;
    #g) Determine os quartis da distribuição pelo método CDF;
    #h) Calcule a amplitude interquartílica da distribuição;
    #i) Verifique se há ou não outliers dentro do rol. Utilize o critério de Box;
    #j) Calcule a amplitude total da distribuição;
    #k) Calcule a variância da distribuição. Utilize a fórmula desenvolvida;
    #l) Calcule o desvio padrão dos dados;
    #m) Calcule o coeficiente de variação percentual ou desvio padrão relativo da distribuição;

def main() -> None:
    dados = [16, 17, 18, 8, 14, 14, 10, 10, 14, 15, 15, 20, 12, 13, 17, 14, 14, 15, 16, 12]
    
    #item a)
    Selection_Sort(dados)
    
    #item b)
    #len(set(dados))
    
    #item c)
    #Teoricamente essa questão deveria ser resolvida desenhando, mas devido às limitações do escopo do projeto
    #vou apenas fazer uma lista de listas com as frequências absoluta, acumulada e relativa.
    #l = Freq_Acul(Dist_Freq(dados))
    #m = Dist_Freq(dados)
    #for i in range(len(m)):
    #    m[i].append(l[i][1])
    #for i in range(len(m)):
    #    m[i].append(m[i][1]/len(m))
    #Note que devido a limitações da linguagem, a frequência relativa está um pouco imprecisa, mas infelizmente
    #é o máximo que consigo fazer com o python "puro".
    
    #item d)
    #MediaSimples(dados)
    
    #item e)
    #Moda(dados)
    
    #item f)
    #Precisa que os dados estejam ordenados, então ative a função Selection_Sort() antes;
    #print(Separatriz(dados,0.5))
    
    #item g)
    #O método usado pela função já é dito pelo enunciado.
    #Separatriz(dados,0.25)
    #Separatriz(dados,0.75)
    
    #item h)
    #IQR(Separatriz(dados,0.25),Separatriz(dados,0.75))
    
    #item i)
    #Criterio_Box(dados,IQR(Separatriz(dados,0.25),Separatriz(dados,0.75)),Separatriz(dados,0.25),Separatriz(dados,0.75))
    #Caso queira remover os possíveis outliers, segue:
    #k = dados.copy()
    #for i in Criterio_Box(k,IQR(Separatriz(k,0.25),Separatriz(k,0.75)),Separatriz(k,0.25),Separatriz(k,0.75)):
    #    for j in k:
    #        if i == j: k.remove(i)
    #No caso não remove nada, porque não tem;

    #item j)
    #Amplitude(dados)

    #item k)
    #print(Variancia(dados,MediaSimples(dados)))
    
    #item l)
    #Note que o professor usa o desvio padrão amostral, eu estou considerando o populacional,
    #Mas caso queira o amostral apenas faça Variancia(dados,MediaSimples(dados))**0.5
    #Desvio_Padrao(dados,MediaSimples(dados))
    
    #item m)
    #Var_Per(Desvio_Padrao(dados,MediaSimples(dados)),MediaSimples(dados))
main()
