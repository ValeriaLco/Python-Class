estados = {}

def importar_estados():
    archivo = open('estados.txt')
    for linea in archivo:
        estado = linea.split('|')
        estados[estado[0]] = estado[1]
    archivo.close()

importar_estados()
curp = input()
cve_estado = curp[11:13]
print(estados.get(cve_estado,'Invalid key'))