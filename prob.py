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

#Función para normalizar un vector
def normalizar_vec(v):
    norma=numpy.linalg.norm(v)
    for i in range(len(v)):
        v[i]=v[i]/norma
    return v

#Función que calcula la amplitud de transición
def amp_tran(v1,v2):
    """"""
    v1=normalizar_vec(v1)
    v2 = normalizar_vec(v2)
    for i in range(len(v1)):
        v1[i]=v1[i].conjugate()
    prod_inter=numpy.inner(v1,v2)
    return prod_inter

#Función para buscar la probabilidad de transitar del primer vector al segundo.
def prob_trans(v1,v2):
    return abs(amp_tran(v1,v2))**2

amp_tran([1j, 1], [1, -1j])
prob_trans([1j, 1], [1, -1j])

#Función que calcula la media y la varianza del observable en el estado dado.
def media_varianza(m,v):
    new_m=numpy.matrix.H
    if m!=new_m:
        raise Exception("La matriz no es hermitiana")




