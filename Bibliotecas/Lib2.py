import matplotlib.pyplot as plt

#Biblioteca criada especialmente para a lista 3 da AP1.
def encontra_classe(val_find: float, intervalo_amostra: list) -> tuple:
    """Encontra a classe a qual o valor pertence recebendo uma classe da amostr e devolvendo um par (nºclasse, supremo). """
    ls = ()
    for i, j in enumerate(intervalo_amostra,1):
        if j>val_find:
            ls = (i,j)
            break;
    return ls;

def moda_King(l_sup: float, l_inf: float, f_post: int,f_ant: int) -> float:
    """Calcula a moda amostral pelo método de king. Recebe: Supremo, Ínfimo e Frequência posterior e inferior da classe. """
    return l_inf + ((f_post/(f_ant+f_post))*(l_sup-l_inf));

def mediana_Desenho(l_inf: float, len: int, f_class: int, f_ac_ant: int, ampl: float) -> float:
    """Calcula a mediana pelo método do desenho. Recebe: Ínfimo Frequência e da classe, Frequência acumulada anterior da classe, e amplitude. """
    return l_inf + (((len/2)-f_ac_ant)/(f_class))*ampl;

def linear_Interpol(l_sup: float, l_inf: float, f_ac_ant: int, f_ac: int, val_foc: float) -> float:
    """Faz o cálculo da frequência de uma faixa aproximada de dados na interpolação pela ogiva de galton. Recebe: 
    Supremo, Ínfimo, Frequência acumulada e Frequência acumulada anterior da classe e o valor focal. """
    return f_ac_ant + ((val_foc-l_inf)*(f_ac-f_ac_ant))/(l_sup-l_inf);

def separatriz_classes(sep: float,len: int, l_inf: float, f_ac_ant: int, f_class: int, ampl: float) -> float:
    """Calcula a separatriz qualquer pelo método do desenho para dados agrupados em intervalos de classe. """
    return l_inf + (((len*sep)-f_ac_ant)/f_class)*ampl;