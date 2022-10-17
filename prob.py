import numpy

def acc(v,m):
    ans=[0]*len(m)
    for i in range(len(m)):
        aux=0
        for j in range(len(m[i])):
            aux+=m[i][j]*v[j]
        ans[i]=aux
    return ans
def in_prod(v1,v2):
    ans=0
    for i in range(len(v1)):
        v1[i]=v1[i].conjugate()
        ans+=v1[i]*v2[i]
    return ans

def prod_m(m1,m2):
    ans=[[0 for j in range(len(m2[0]))] for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            aux=0
            for k in range(len(m2)):
                aux=m1[i][k]*m2[k][j]
            ans[i][j]=aux
    return ans

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

def bra(v):
    for i in range(len(v)):
        v[i]=v[i].conjugate()
    return v

#Función que calcula la media y la varianza del observable en el estado dado.
def media_varianza(m,v):
    bra_v=bra(v)
    aux_v=acc(v,m)
    media=in_prod(aux_v,bra_v)
    mat=[[media * -1 for i in range(len(m[0]))] for j in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m)):
            mat[i][j] += m[i][j]
    matriz=prod_m(mat,mat)
    var=in_prod(acc(v,matriz),bra_v)
    return media,var

def valores_propios(m):
    val_p,vect_p=numpy.linalg.eig(m)
    val=[]
    vect=[]
    for i in range(len(val_p)):
        val+=[(val_p[i].real,val_p[i].imag)]
    for i in range(len(vect_p)):
        aux=[]
        for j in range(len(vect_p[0])):
            aux+=[(vect_p[i][j].real,vect_p[i][j].imag)]
        vect += [aux]
    return val, vect

print("Ejercicio 4.3.1")
v=[1,0]
m=[[0,1],[1,0]]
val,vect=valores_propios(m)
print("Observacciónes", acc(v,m))
print("Valores propios",val)
print("Vectores propios",vect)
print("")
print("------------------------")
print("")
print("Ejercicio 4.3.2")
v=[1,0]
m=[[0,1],[1,0]]
val,vect=valores_propios(m)
for i in vect:
    print(prob_trans(i,vect))


