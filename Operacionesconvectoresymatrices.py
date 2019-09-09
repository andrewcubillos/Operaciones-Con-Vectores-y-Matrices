from numeroscomplejos import *
def sumavalida(matriz1,matriz2):
    valid=True
    if len(matriz1)!=len(matriz2) or len(matriz1[0])!=len(matriz2[0]):
        valid=False
    return valid
def inversoparainversam(numero):
    ini2=((-1 * numero[0], -1 * numero[1]))
    return ini2

def sumav(vector1,vector2):
    resultado=[]
    for x,y in zip(vector1,vector2):
        resultado.append((suma(x,y)))
    return resultado
def inverso(vector1):
    in1=[]
    for q in (vector1):
        in1.append((-1*q[0],-1*q[1]))
    return in1
def escalarv(escalar, vector1):
    r=[]
    t=escalar
    for z in vector1:
        r.append(producto(t,z))
    return r
def sumam(M,N):
    if sumavalida(M,N):
        s=[[suma(M[i][j],N[i][j]) for j in range(len(M[0]))] for i in range(len(N))]
        return(s)
def inversam(matriz):
    ma=[[inversoparainversam(matriz[i][j]) for j in range(len(matriz))] for i in range(len(matriz[0]))]
    return ma
def escalarm(escalar,M):
    m=[[producto(escalar,M[i][j]) for j in range(len(M))] for i in range(len(M[0]))]
    return m
def trans(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
def conjugada(matriz):
    return[[conjugado(matriz[i][j]) for j in range(len(matriz))] for i in range(len(matriz[0]))]
def adjunta(matriz):
    return (conjugada(trans(matriz)))
def accion(X,Y):
    result = [[0 for j in range(len(Y[0]))] for i in range(len(Y))]


    ssum=(0,0)

    for j in range(len(Y)-1):
        
       for i in range(len(Y)):

           for k in range(len(Y)):
               result[i][j] =suma(ssum,producto(X[i][k],Y[k][j]))
               ssum=result[i][j]       

           ssum =(0,0)
        

    return (result)
    
def norma(Y):
    X=trans(Y)
    result = [[0 for j in range(len(X))] for i in range(len(Y[0]))]

    ssum=(0,0)
    for i in range(len(X)):
        
       for j in range(len(Y[0])):

           for k in range(len(Y)):
               result[i][j] =suma(ssum,producto(X[i][k],Y[k][j]))
               ssum=result[i][j]

           ssum =(0,0)

    traza=(0,0)
    for w in range(len(result)):
        traza=suma(traza,result[w][w])
   
    return ((((traza[0])**2)+((traza[1])**2))**(1/2))

def distancia(M,N):
    if sumavalida(M,N):
        s=[[resta(M[i][j],N[i][j]) for j in range(len(M[0]))] for i in range(len(N))]
        return norma(s)


        
    
def unitaria(Y):
    X=adjunta(Y)
    result = [[0 for j in range(len(X))] for i in range(len(Y[0]))]

    ssum=(0,0)
    for i in range(len(X)):
        
       for j in range(len(Y[0])):

           for k in range(len(Y)):
               result[i][j] =suma(ssum,producto(X[i][k],Y[k][j]))
               ssum=result[i][j]
           ssum =(0,0)
               

    midentidad=[[(1,0) if j == i else (0,0) for j in range(len(result))] for i in range(len(result[0]))]

    if result==midentidad:
        return "The matrix is a unitary matrix"
    else:
        return "The matrix is not a unitary matrix"
            
            
  
        
def hermitian(matriz):
    if matriz==adjunta(matriz):
        return "The matrix is hermitian"
    else:
        return "The matrix is not hermitian"
def tensor(X,Y):
    result = [[0 for j in range((len(X[0])*len(Y[0])))] for i in range((len(X[0])*len(Y[0])))]
    todo=[]
    for w in X:
       for e in w:
          todo.append(e)
    s=0
    q=0
    s1=0
    q1=0
    for r in todo:
       for i in range(len(Y[0])):
          for j in range(len(Y[0])):

             result[s][q] = producto(r,Y[i][j])
             
             q+=1
          
          q=q1
          s+=1
       
       s=s1
       q1=0

      
       if todo.index(r)==1:
          s+=2
          s1=s
          q=0
          q1=0
       else:
          q+=2
          q1=q
    return result
    









 
