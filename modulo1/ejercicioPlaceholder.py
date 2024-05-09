import requests

base_url = 'https://jsonplaceholder.typicode.com'

def get():
    response = requests.get(f"{base_url}/posts")
    print(response.json())
def post():
    nuevoTitulo = input("Introduce el titulo: ")
    nuevoID = int(input("Introduce el ID del post: "))
    new_post = {
        "userId": nuevoID,
        "title": nuevoTitulo,
        "body": ''
    }

    response = requests.post(f"{base_url}/posts", json=new_post)
    print("POST realizado con exito")
    print(response.json())
#post()

def put():
    modificacionTitulo = input("Introduce el nuevo titulo: ")
    modificacionId = input("Introduce el nuevo ID: ")
    new_put = {
        "userId": modificacionId,
        "title": modificacionTitulo,
        "body": ''
    
    }
    response = requests.put(f"{base_url}/posts", json=new_put)
    print("PUT realizado con exito")
    print(response.json())

def path():
    modificacionTitulo = input("Introduce el nuevo titulo: ")
    new_path = {
        "title": modificacionTitulo,
    
    }
    response = requests.path(f"{base_url}/posts", json=new_path)
    print("PUT realizado con exito")
    print(response.json())
def delete():
    idDel = int(input("Introduce el Id del post que quieres eliminar: "))
    requests.delete(f"{base_url}/posts/{idDel}")
    print("DELETE ejecutado correctamente")
get()
post()
put()
path()
delete()