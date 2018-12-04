from DataBase import DataBase

class AlunoDAO:

    collection = None

    def __init__(self):
        db = DataBase()
        self.collection = db.getCollection()

    def insertAluno(self, nome, endereco, telefone):
        aluno = {"nome": nome, "endereco": endereco, "telefone": telefone}
        self.collection.insert_one(aluno)

    def getAlunos(self):
        z = 0
        for x in self.collection.find():
            z = z + 1
            print str(z)+"- Nome: "+x['nome']+" | Endereco: "+x['endereco']+" | Telefone: "+x['telefone']+"\n"

    def deleteAluno(self, y):
        z = 0
        for x in self.collection.find():
            z = z + 1
            if z == y:
                query = {"_id": x['_id']}
                self.collection.delete_one(query)

    def updateAluno(self, y):
        z = 0
        for x in self.collection.find():
            z = z + 1
            if z == y:
                query = {"_id": x['_id']}
                print "Aperte enter no atributo que nao deseja modificar"
                nome = raw_input("\nNome: ")
                if nome == "":
                    nome = x['nome']
                endereco = raw_input("\nEndereco: ")
                if endereco == "":
                    endereco = x['endereco']
                telefone = raw_input("\nTelefone: ")
                if telefone == "":
                    telefone = x['telefone']
                update_query = {"$set": {"nome": nome, "endereco": endereco, "telefone": telefone}}
                self.collection.update_one(query, update_query)
