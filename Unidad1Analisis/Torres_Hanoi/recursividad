
def TorresHanoi(n, o, d, aux):
    if(n > 0):
        TorresHanoi(n-1, o, aux, d)
        print("\nSe mueve anillo desde torre:" + str(o) + " Hasta torre:  " + str (d))
        TorresHanoi(n-1, aux, d, o)
       

n = int(input("\nIngresa la cantidad de anillos: "))
TorresHanoi(n,1,3,2)
