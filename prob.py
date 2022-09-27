import numpy
#Función para calcular la probabilidad de encontrarlo en una posición en particular.
def prob(v,p):
    """A la función le ingresan un vector complejo y una posición del mismo, el vector debe estar escrito
    de la siguiente forma: [(3,5),(5,1),(2,4)] y la posición tiene que ser menor a la longitud del vector
    """
    aux=[]
    for i in range(len(v)):
        aux.append(complex(v[i][0],v[i][1]))
    mod=0
    for i in range(len(aux)):
        mod=mod+(abs(aux[i]))**2
    print((abs(aux[p])**2)/mod)

#Función para buscar la probabilidad de transitar del primer vector al segundo.
def prob_trans(v1,v2):
    """"""
    v1_norm=numpy.linalg.norm(v1)
    for i in range(len(v1)):
        v1[i]=v1[i]/v1_norm
    v2_norm=numpy.linalg.norm(v2)
    for i in range(len(v2)):
        v2[i]=v2[i]/v2_norm
    print(v1)
    v1_adj=numpy.matrix.getH(v1_norm)
    print()
prob_trans([1,-1j],[1j,1])




