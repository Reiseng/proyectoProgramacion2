import requests
api_url = 'https://randomuser.me/api/'
parametros = {
    'inc': 'name,phone,id,email,login',
    'password': 'number'
}
response = requests.get(api_url,params=parametros)
data = response.json()
randomUser={}
randomUser["nombre"]=data["results"][0]["name"]["first"]
print("Nombre: ",randomUser["nombre"])
randomUser["apellido"]=data["results"][0]["name"]["last"]
print("Apellido: ",randomUser["apellido"])
randomUser["email"]= data["results"][0]["email"]
print("Email: ",randomUser["email"])
randomUser["phone"]= data["results"][0]["phone"]
print("Phone: ",randomUser["phone"])
randomUser["dni"]= data["results"][0]["id"]["value"]
print("DNI: ",randomUser["dni"])
randomUser["matricula"]= data["results"][0]["login"]["password"]
print("Matricula: ",randomUser["matricula"])

def getRandomUser(type:str)->dict:
    if type=="medico":
        randomUser["matricula"]= data["results"][0]["login"]["password"]
        #test pull request
        #hola
    elif type=='paciente':
        pass
        ##