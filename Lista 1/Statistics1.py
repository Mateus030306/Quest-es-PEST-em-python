from Lib import *
#Pra diferenciar meus comentarios totalmente producentes dos por IA, eu nao uso acentos e sempre termino com ';'!;
def main() -> None:
    data = [21,21,42,49,49,51,51,58,58,58,60,61,61,61,67,71,71,73,75,98]
    L = []
    #copiando a lista, tentei fazer data.copy mas nao deu certo;
    for i in data:
        L.append(i)
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
