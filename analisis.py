dataset=[10,25,37,42,58,63,71,89]

def promedio(datos):
    return sum(datos)/len(datos) 

def maximo(datos):
    return max(datos)

def resumen(datos):
    print(f"Total de ingresos: {len(datos)}")
    print(f"promedio         : {promedio(datos):.2f}")
    print(f"Máximo           : {maximo(datos)}")
    
resumen(dataset)

print("estoy modificando este archivo")

print("desde la rama Edison")
print("Edison desarrollador")