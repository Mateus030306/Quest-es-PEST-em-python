from math import floor
import matplotlib.pyplot as plt

def separatriz(l: list, k: float) -> float:
    n = len(l)
    if((n*k).is_integer): m = (int(n*k),int((n*k)+1))
    else: m = (int(floor(n*k)+1),0)
    if(m[1]!=0):
        return ((l[m[0]-1]+l[m[1]-1])/2);
    else: return (l[m[0]-1]);

def IQR(Q1: float, Q2: float) -> float:
    if(Q1>Q2): return Q1-Q2;
    else: return Q2-Q1;

def media(l: list) -> float:
    m = 0
    m = 0 if(len(l)==0) else sum(l)
    return m/len(l);

def mediana(l: list) -> float:
    if(len(l)%2==1): return (l[len(l)//2]);
    else: return (l[(len(l)//2)-1]+l[(len(l)//2)])/2;

def desvio_padrao(l: list, m: float) -> float:
    dp = sum((i-m)**2 for i in l) / (len(l)-1)
    return dp**0.5

def padroniza(l:list, S: float, m: float) -> list[float]:
    """Função que retorna uma amostra padronizada de outra amostra. """
    K = []
    for i in l:
        K.append((i-m)/S)
    return K;

def criterio_de_box(l: list, I: float, Q1: float, Q2: float) -> list:
    """Devolve uma lista dos dados que se configuram como outliers
    pelo critério de box. """
    outs = []
    if Q1>Q2:
        for i in l:
            if i<Q2-1.5*I or i>Q1+1.5*I: outs.append(i)
    else:
        for i in l:
            if i<Q1-1.5*I or i>Q2+1.5*I: outs.append(i)
    return outs;

def criterio_da_var(l: list, media: float, desvio_padrao: float) -> list:
    """Devolve uma lista dos outliers nos dados pela regra empírica 68-95-99.7. """
    k = []
    for i in l:
        if i>=media+3*desvio_padrao or i<=media-3*desvio_padrao: k.append(i)
    return k;

def box_plot(l: list) -> None:
    """Imprime na tela um boxplot usando uma lista. Função criada utilizando a biblioteca matplotlib. """
    plt.boxplot(l)
    plt.xlabel("Valores")
    plt.ylabel("Box plot")
    plt.show();

def assimetria(Media: float, Mediana: float, Desvio_Padrao: float) -> float:
    return (3*(Media-Mediana))/Desvio_Padrao;

def momento_central_amostral(l: list, Momento: int, Media: float) -> float:
    return sum((i-Media)**Momento for i in l) / len(l);

def curtose(M2: float, M4: float) -> float:
    return M4/(M2**2);
