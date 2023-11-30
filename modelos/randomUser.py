import requests

def apiComunicacion(cantidad_de_resultados)->tuple:
    api_url = 'https://randomuser.me/api/?inc=name,phone,id,email,location,login,value&password=number,6&nat=us'+f"&results={cantidad_de_resultados}"
    try:
        response = requests.get(api_url)
    except Exception as e:
        print("Error en funcion apiComunicacion",e)
        error_mensaje="Error de respuesta con la api"
        return (error_mensaje,e)
    if(response.status_code==200):
        data = response.json()
        return (data,200)
    
def getRandomUsers(type:str,cantidad:int)->list:
    '''
    type puede ser: medico o paciente
    Si seleccionas medico se agregara el dato matricula
    y si se selecciona paciente se agregara la direccion
    cantidad: la cantidad de pedidos que se le haran a la api
    '''
    api=apiComunicacion(cantidad)
    if api[1]!=200:
        print("Error en funcion getRandomUsers")
        return False
    data=api[0]
    type.lower()

    lista_de_usuarios=[]
    for ind in range(0,cantidad):
        randomUser={}
        dniconguiones= data["results"][ind]["id"]["value"]
        dniconguiones=dniconguiones.replace('-',"")[0:8]
        randomUser["dni"]=dniconguiones
        randomUser["nombre"]=data["results"][ind]["name"]["first"]
        randomUser["apellido"]=data["results"][ind]["name"]["last"]
        randomUser["email"]= data["results"][ind]["email"]
        randomUser["telefono"]= data["results"][ind]["phone"]
        # #debug
        # print("DNI: ",randomUser["dni"])
        # print("Nombre: ",randomUser["nombre"])
        # print("Phone: ",randomUser["phone"])
        # print("Email: ",randomUser["email"])
        # print("Apellido: ",randomUser["apellido"])

        
        if type=="medico":
            randomUser["matricula"]= data["results"][ind]["login"]["password"]
            # print("Matricula: ",randomUser["matricula"])
        elif type=='paciente':
            randomUser["direccion_calle"] = data["results"][ind]["location"]["street"]["name"]
            randomUser["direccion_numero"] = data["results"][ind]["location"]["street"]["number"]
            # print(f"Direccion_calle:{randomUser['direccion_calle']}")
            # print(f"Direccion_numero:{randomUser['direccion_numero']}")
        else:
            return "Error de tipo"
        lista_de_usuarios.append(randomUser)
    return lista_de_usuarios

#tests
# lista= getRandomUsers("medico",10)
# for x in lista:
#     print(x)