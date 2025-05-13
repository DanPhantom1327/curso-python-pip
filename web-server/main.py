import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI() #creamos nuestro primer recurso

@app.get('/') #agregamos decorador --> ruta
def get_list():
    return [1,2,3,4]


@app.get('/contact', response_class=HTMLResponse) #agregamos decorador --> ruta y un apartado HTML para la web

def get_list(): #respuesta en HTML, hacemos su renderizado
    return """ 
    <h1>Hola soy parte de la primera pagina con Python de Dan</h1>
    <h1>Y esto es solo el inicio de cosas grandes</h1>
    """


def run():
    store.get_categories()


if __name__ == '__main__':#Se correra como script
    run()

#ejecutamos desde terminal
