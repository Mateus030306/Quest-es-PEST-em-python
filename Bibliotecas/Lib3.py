from math import sqrt
#Implementação das funções da lista da AP2, agora com dados bivariados.

def covariancia_amostral(soma_cruzada: float, soma_x: float, soma_y: float, tam: int) -> float:
    """Devolve a covariância amostral recebendo a soma dos produtos cruzados das amostras, o produto das somas das amostras e o tamanho da amostra. """
    return (1/(tam-1))*(soma_cruzada-((soma_x*soma_y)/tam));

def variancia_marginal(soma_quadrados: float, soma: float, tam: int) -> float:
    """Devolve a variancia marginal amostral para dados bivariados, recebendo a soma dos quadrados, a soma e o tamanho amostral.  """
    return (1/(tam-1))*(soma_quadrados-((soma**2)/tam));

def correlacao(cov: float, var_x: float, var_y: float) -> float:
    """Devolve a o coeficiente r de correlação amostral, recebendo a covariância entre as duas amostras e as variâncias marginais. """
    return cov / (sqrt(var_x*var_y));

def teste_t(tam: int, r: float) -> float:
    """Calcula o t de student. Recebe o tamanho e o r da amostra.  """
    return abs(r) * (sqrt((tam-2)/(1-(r**2))));

def erro_padrao_med(tam: int, r: float) -> float:
    """Calcula o erro padrão da média da amostra. """
    return sqrt((1-(r**2))/(tam-2));
