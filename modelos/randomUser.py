import requests

def apiComunicacion(cantidad_de_resultados)->tuple:
    api_url = 'https://randomuser.me/api/?inc=name,phone,id,email,location,login,value&password=number,6&nat=us'+f"&results={cantidad_de_resultados}"
    response = requests.get(api_url)
    if(response.status_code==200):
        data = response.json()
        return (data,200)
    else:
        error_mensaje="Error de respuesta con la api"
        return (error_mensaje,response.status_code)
    
def getRandomUsers(type:str,cantidad:int)->list:
    api=apiComunicacion(cantidad)
    if api[1]!=200:
        return api[0]
    data=api[0]
    type.lower()
    '''
    type puede ser: medico o paciente
    Si seleccionas medico se agregara el dato matricula
    y si se selecciona paciente se agregara la direccion
    cantidad: la cantidad de pedidos que se le haran a la api
    '''
    lista_de_usuarios=[]
    for ind in range(0,cantidad):
        randomUser={}
        randomUser["nombre"]=data["results"][ind]["name"]["first"]
        randomUser["apellido"]=data["results"][ind]["name"]["last"]
        randomUser["email"]= data["results"][ind]["email"]
        randomUser["phone"]= data["results"][ind]["phone"]
        randomUser["dni"]= data["results"][ind]["id"]["value"]
        # #debug
        # print("DNI: ",randomUser["dni"])
        # print("Nombre: ",randomUser["nombre"])
        # print("Phone: ",randomUser["phone"])
        # print("Email: ",randomUser["email"])
        # print("Apellido: ",randomUser["apellido"])

        
        if type=="medico":
            randomUser["matricula"]= data["results"][ind]["login"]["password"]
            print("Matricula: ",randomUser["matricula"])
            randomUser["habilitado"]= True
        elif type=='paciente':
            randomUser["direccion_calle"] = data["results"][ind]["location"]["street"]["name"]
            randomUser["direccion_numero"] = data["results"][ind]["location"]["street"]["number"]
            print(f"Direccion_calle:{randomUser['direccion_calle']}")
            print(f"Direccion_numero:{randomUser['direccion_numero']}")
        else:
            return "Error de tipo"
        lista_de_usuarios.append(randomUser)
    return lista_de_usuarios

#tests
# lista= getRandomUsers("paciente",10)
# for x in lista:
#     print(x)
# getRandomUser("medico",10)