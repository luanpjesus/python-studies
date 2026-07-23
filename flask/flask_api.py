from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello world"



@app.route("/about")
def about():
    return "Pagina Sobre!"

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
#REST - REPRESENTATIONAL STATE TRANSFER
#ESTILO DE ARCH PARA API



#RESTFUL
#QUANDO A API RESPEITA TODOS OS PRINCIPIOS DO REST



#  - HTTP
#        *GET
#        *POST
#        *DELETE
#        *PUT
#        *PATCH




 


    
    