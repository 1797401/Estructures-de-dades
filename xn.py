def invertir(paraula: str):
    if paraula=="":
        return paraula
    return invertir(paraula[1:])+paraula[0] 


def funcio(n):
    return int(invertir(str(n)))    


print(funcio(12345))