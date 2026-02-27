from ..Bibliotecas.Lib1 import *

    #Um fato importante é que: computação numérica no geral costuma tomar dados do tipo double para melhor precisão,
    #mas devido ao caratér educativo das listas usarei float para melhor eficiência do código, mesmo que com uma
    #precisão piorada;

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
    data = [21,21,42,49,49,51,51,58,58,58,60,61,61,61,67,71,71,73,75,98]
    L = data.copy()
    #Setando os dados da lista;
    Q1 = separatriz(L,0.25)
    Q3 = separatriz(L,0.75)
    I = IQR(Q3,Q1)
    m = media(L)
    DP = desvio_padrao(L,m)
    #Julgamento pelo criterio da varianca (regra empirica - 68,95,99.7);
    print(criterio_da_var(L,m,DP))
    # Julgamento pelo criterio de Box;
    print(criterio_de_box(L,I,Q1,Q3))
    #Calculo da nova mediana, mediana antiga x nova
    print(mediana(L))
    k = criterio_de_box(L,I,Q1,Q3)
    for i in L:
        for j in k:
            if i == j:
                L.remove(i)
    print(mediana(L))
    #Fazendo o box plot
    box_plot(L)
    #Fazendo a assimetria
    print(assimetria(m,mediana(L),DP))
    #Fazendo a curtose
    print(curtose(momento_central_amostral(L,2,m),momento_central_amostral(L,4,m)))

    #Pelos valores da curtose de ~ 3.8 e assimetria de ~ -0.2 chegamos a conclusão que a distribuição é
    #aproximadamente normal pois sua curtose está próxima de 3 e sua assimetria de 0, portanto a distribuição é
    #aproximadamente normal;
    
main()
