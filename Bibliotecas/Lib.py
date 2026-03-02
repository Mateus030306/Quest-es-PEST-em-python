from math import floor
import matplotlib.pyplot as plt
from math import log10

#Implementaçao das funções feitas com o formulário no final da lista em mente;

def MediaSimples(data: list) -> float:
    """Função que calcula a média aritmética simples de um conjunto de dados discretos. """
    if len(data)==0: return 0;
    else: return sum(data)/len(data);

def Separatriz(data: list, sep: float) -> float:
    """Retorna a separatriz de número sep. Exemplo: a entrada sep=0.25 resulta no primeiro quartil e sep=0.75 no terceiro. """
    if (len(data)*sep).is_integer(): return (data[int(len(data)*sep)-1]+data[int(len(data)*sep)])/2;
    else: return data[floor(len(data)*sep)];

def IQR(Q1: float, Q3: float) -> float:
    """Retorna a amplitue interquartílica. """
    if(Q1>Q3): return Q1-Q3;
    else: return Q3-Q1;

def Criterio_Box(data: list, iqr: float, Q1: float, Q3: float) -> list:
    """Retorna uma lista dos dados espúrios no dataset utilizando o critério de box. """
    l = []
    if(Q3>Q1):
        for i in data:
            if i>Q3+1.5*iqr or i<Q1-1.5*iqr: l.append(i)
        return l;
    else:
        for i in data:
            if i>Q1+1.5*iqr or i<Q3-1.5*iqr: l.append(i)
        return l;

def Criterio_Varianca(data: list, media: float, desvio: float) -> list:
    """Retorna um alista dos dados espúrios no dataset utilizando o criterío da variância. (Regra empírica 68-95-99.7) """
    l = []
    for i in data:
        if i<media-3*desvio or i>media+3*desvio: l.append(i)
    return l;

def Mediana(data: list) -> float:
    """Calcula mediana do dataset. """
    if (len(data)*0.5).is_integer: return (data[int(len(data)*0.5)-1]+data[int(len(data)*0.5)])/2;
    else: return data[int(floor(len(data)*0.5))];

def Box_Plot(data: list) -> None:
    """Simplesmente imprime um box-plot dos dados na tela (biblioteca matplotlib). """
    plt.figure(1)
    plt.boxplot(data)
    plt.show;

def Assimetria(Q3: float, Q1: float, mediana: float) -> float:
    """Calcula a assimetria pelo coeficiente de Bowley (Quartílico). """
    if(Q3>Q1): return (Q3+Q1-2*mediana)/(Q3-Q1);
    else: return (Q1+Q3-2*mediana)/(Q1-Q3);

def Verifica_Simetria(assimetria: float) -> str:
    if abs(assimetria==0): return "Simétrica. "
    elif abs(assimetria)<=0.1: return "Assimetria fraca. "
    elif abs(assimetria)<=0.3: return "Assimetria moderada. "
    else: return "Assimetria forte. "

def Curtose(iqr: float, p90: float, p10: float) -> float:
    """Calcula a curtose pelo coeficiente percentílico. """
    if(p90>p10): return iqr/(2*(p90-p10));
    else: return iqr/(2*(p10-p90));

def Verifica_Meso(curtose: float) -> bool:
    """Retorna verdadeiro se a curva tem desvio inexpressivo. """
    if abs(curtose-0.263)/0.263 < 0.05: return True;
    else: return False;

def Desvio_Padrao(data: list, media: float) -> float:
    """Retorna o desvio padrão (Sem o critério de correção de bessel, desvio populacional). """
    DP = sum((i-media)**2 for i in data)
    return (DP/len(data))**0.5;

def Selection_Sort(data: list) -> None:
    """Ordena a lista utilizando o método de ordenação por seleção. """
    for i in range(len(data)-1):
        for j in range(i,len(data)):
            if(data[i]>data[j]):
                temp = data[i]
                data[i] = data[j]
                data[j] = temp;

def Regra_Sturges(tamanho: int) -> float:
    """Calcula a quantidade de classes de uma lista pela regra de sturges. """
    return (1+3.3*log10(tamanho));

def Moda(data: list) -> int:
    """Utiliza conjuntos e um contador para calcular a moda. Não funciona em dados multimodais. """
    c = set(data)
    cont = []
    for i in c:
        count = 0
        for j in data:
            if i==j: count +=1
        cont.append((i,count))
    m = cont[0][1]
    moda = cont[0][0]
    for i, j in cont:
        if j>m:
            m = j
            moda = i
    return moda;

def Dist_Freq(data: list) -> list:
    """Devolve uma lista com elementos [(i-ésimo dado, i-ésima frequência absoluta)]"""
    c = set(data)
    cont = []
    for i in c:
        count = 0
        for j in data:
            if i==j: count +=1
        cont.append([i,count])
    return cont;

def Freq_Acul(dist_freq: list) -> list:
    """Recebe uma lista de (i-ésimo dado, i-ésima frequência abs) e devolve uma lista com
    a frequência absoluta acumulada do i-ésimo dado da amostra. """
    for i in range(1,len(dist_freq)):
        dist_freq[i][1] = dist_freq[i][1]+dist_freq[i-1][1]
    return dist_freq;

def Var_Per(desvio: float, media: float) -> float:
    """Calcula o Coeficiente de variação percentual (Desvio padrão relativo) da amostra. (Devolve em decimais)"""
    return desvio/media;

def Amplitude(data: list) -> float:
    """Calcula o limite superior e inferior da amostra e retorna a amplitude. """
    mai = data[0]
    men = data[0]
    for i in data:
        if i > mai: mai = i
        if i < men: men = i
    return mai-men;

def Variancia(data: list, media: float) -> float:
    """Calcula a variância amostral. """
    v = sum((i-media)**2 for i in data)
    return v/(len(data)-1);
