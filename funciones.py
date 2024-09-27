import matplotlib.pyplot as plt
from collections import Counter

def ordernarNombres():
        listaNombresOrdenados = []

        try:
            with open('nombres.txt', 'r', encoding='utf-8') as archivo:
                contenido = archivo.readlines()
                if not contenido: 
                    raise ValueError("El archivo está vacío.")
                
                for linea in contenido:
                    listaNombresOrdenados.append(linea.strip())
            
            def quitar_acento(palabra):
                acentos = {
                    'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
                    'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'
                }
                for acento, sin_acento in acentos.items():
                    palabra = palabra.replace(acento, sin_acento)
                return palabra.lower()
            
            lista_limpia = []   
            for palabra in listaNombresOrdenados:
                lista_limpia.append(quitar_acento(palabra))
            
            lista_limpia = sorted(lista_limpia)
            return lista_limpia

        except FileNotFoundError:
            print("Error: El archivo no existe")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error: {e}")
            
            

def removeApellidos(lista):
    listaSinApellido = []
    for nombreCompleto in lista:
        nombre = nombreCompleto.split()[0]
        listaSinApellido.append(nombre)
    return listaSinApellido

def convertirDiccionario(listaNombres):
    try:
        if not listaNombres:
            raise ValueError("La lista de nombres está vacia")

        listaNombres = removeApellidos(listaNombres)  

        diccionario = {}
        for nombres in listaNombres:
            if nombres in diccionario:
                diccionario[nombres] += 1
            else:
                diccionario[nombres] = 1

        return diccionario

    except ValueError as ve:
        print(f"Error: {ve}")
    except TypeError:
        print("Error: se esperaba una lista de nombres")
    except Exception as e:
        print(f"Error: {e}")
    


def txtFrecuenciaNombres(dicNombres):    
    with open('frecuencia_nombres.txt', 'w') as archivo:
        for nombre, cantidad in dicNombres.items():
            archivo.write(f"{nombre}: {cantidad} \n")
    

def graficoFrecuenciaNombres():
    with open('nombres.txt', 'r', encoding='utf-8') as archivo:
        listaNombreCompleto = [line.strip() for line in archivo]
    
    listaNombres = removeApellidos(listaNombreCompleto)
    contadorFrecuencia = Counter(listaNombres)
    contadorNombres = 0
    for nombres in listaNombres:
        contadorNombres += 1
            
    nombres_comunes = dict(contadorFrecuencia.most_common(contadorNombres))
        
    plt.figure(figsize=(12, 6))
    bars = plt.bar(nombres_comunes.keys(), nombres_comunes.values())
        
    plt.title("Los nombres mas frecuentes")
    plt.xlabel("Nombres")
    plt.ylabel("Frecuencia")   
    plt.xticks(rotation=45, ha='right') 
        
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., height, f"{height}", ha="center", va="bottom")
        
    plt.tight_layout()
    
    plt.savefig('grafico_frecuencia_nombres.png')
        
    plt.show()
    


    
def inicialMayuscula(cadena):
    listaExepciones = ["y", "el", "la", "en", "de", "con", "si", "es", "o", "ser"]
    palabras = cadena.split()
    for palabra in palabras:
        if palabra not in listaExepciones:
            cadena = cadena.replace(palabra, palabra[0].upper() + palabra[1:]) 
    
    return cadena