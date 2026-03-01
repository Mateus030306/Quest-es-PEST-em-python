from ..Bibliotecas.Lib1 import *

    #Tabela de questões ->
    #a) Calcule a amplitude interquartilica dos dados brutos;
    #b) Julgue possiveis outliers utilizando o Criterio de Box;
    #c) Julgue tais outliers a partir do Criterio da Variancia. Considere que, dentro do contexto da pesquisa,
    #nao ha mais como investigar fenomenologicamente os outliers porque as amostras ja foram descartadas;
    #d) Calcule a mediana dos dados depurados e a sua nova amplitude interquartilica
    #e) Construa o Box-Plot (grafico de caixas);
    #f) Calcule a assimetria da distribuicao;
    #g) Calcule a curtose da distribuicao;
    #h) Julgue se essa distribuicao de dados pode ser ou nao considerada como aproximadamente normal e justifique sua conclusao

def main() -> None:
    dados = [21, 21, 42, 49, 49, 51, 51, 58, 58, 58, 60, 61, 61, 61, 67, 71, 71, 73, 75, 98]
    
    #item a)
    #print(IQR(Separatriz(dados,0.25),Separatriz(dados,0.75)))

    #item b)
    #print(Criterio_Box(dados,IQR(Separatriz(dados,0.25),Separatriz(dados,0.75)),Separatriz(dados,0.25),Separatriz(dados,0.75)))

    #item c)
    #Nesse item precisamos de uma análise mais qualitativa do que quantitativa de fato. O que ocorre é que. devido à natureza discreta dos dados,
    #o critério da variancia não identifica 98 como outlier espúrio pois a quantidade de dados é muito pequena, mas caso plotemos os dados utilizando
    #um box plot ou ferramenta de visualização mais específica, podemos ver que, apesar de ser outlier, o 21 não é espúrio, então editando o dataset
    #obtemos:
    #dados.remove(98)

    #item d)
    #print(IQR(Separatriz(dados,0.25),Separatriz(dados,0.75)),Mediana(dados),end="\n")

    #item e)
    #Box_Plot(dados)

    #item f)
    #print(Assimetria(Separatriz(dados,0.75),Separatriz(dados,0.25),Mediana(dados)))

    #item g)
    #print(Curtose(IQR(Separatriz(dados,0.25),Separatriz(dados,0.75)),Separatriz(dados,0.9),Separatriz(dados,0.1)))
    
    #item h)
    #A distribuição não é aproximadamente normal pois não é mesocúrtica (Curtose<0.263).

main()
