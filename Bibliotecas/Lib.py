from math import floor
import matplotlib.pyplot as plt

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
