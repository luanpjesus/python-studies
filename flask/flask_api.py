from flask import Flask, request
from models.task import Task
app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return "Hello world"



# @app.route("/about")
# def about():
#     return "Pagina Sobre!"



tasks = []
task_id_control = 1 
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    
    new_task = Task(
        id=task_id_control,title=data.['title'],description= data.get()
        
        )
    task_id_control += 1
    return "Teste"





if __name__ == "__main__":
    app.run(debug=True)
    
#CRUD
#Create, Read, Update and Delete
#Tarefa:    
    
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




 


    
    