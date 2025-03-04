def CentrosCuadradoE(seed, n):
    resu = []
    valor = seed
    for _ in range(n):
        cuadrado = str(valor ** 2).zfill(4)  
        mid = len(cuadrado) // 2  
        value = int(cuadrado[mid - 1: mid + 1])
        resu.append(cuadrado)
    return resu
def CentrosCuadradoF(seed, n):
    resu = []
    valor = seed
    for _ in range(n):
        cuadrado =f"{valor ** 2:.10f}"[2:8] 
        print(cuadrado)
        mid = len(cuadrado) // 2
        valor = float("0." + cuadrado[mid - 2: mid + 1]) 
        print(valor)
        resu.append(float("0."+cuadrado))
    return resu
def MediosCuadrados(seed, n):
    resu = []
    valor = seed
    for _ in range(n):
        cuadrado = str(valor ** 2).zfill(8)
        mid = len(cuadrado) // 2 
        value = int(cuadrado[mid - 2: mid + 2]) 
        resu.append(cuadrado)
    return resu
# semillas
seed_int = 83  # semilla entera para centros al cuadrado 
seed_frac = 0.528  # semilla fraccionaria para centros al cuadrado
seed_cuad = 2152  # semilla para medios cuadrados
n = 10  # numero iteraciones
cce = CentrosCuadradoE(seed_int, n)
ccf = CentrosCuadradoF(seed_frac, n)
mc = MediosCuadrados(seed_cuad, n)
print("Números generados por Centros al Cuadrado (Enteros):")
print(cce)
print("Números generados por Centros al Cuadrado (Fraccionarios):")
print(ccf)
print("Números generados por Medios Cuadrados:")
print(mc)