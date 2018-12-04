import os
from AlunoDAO import AlunoDAO

def cleanShell():
    if os.name != "nt":
        os.system("clear")
    else:
        os.system("cls")

def main():
    aluno = AlunoDAO()
    op = 0
    while op != 5:
        cleanShell()
        op = int(raw_input("Escolha uma opcao\n1- Cadastrar\n2- Consultar\n3- Deletar\n4- Atualizar\n5- Sair\n"))
        if op >= 1 and op <= 5:
            if op == 1:
                cleanShell()
                nome = raw_input("Digite o nome: ")
                endereco = raw_input("Digite o endereco: ")
                telefone = raw_input("Digite o telefone: ")
                aluno.insertAluno(nome, endereco, telefone)
            elif op == 2:
                cleanShell()
                aluno.getAlunos()
                raw_input("\naperte enter para continuar\n")
            elif op == 3:
                cleanShell()
                aluno.getAlunos()
                opDel = int(raw_input("\nDeseja apagar algum?\n1- SIM\n2- NAO\n"))
                if opDel == 1:
                    id = int(raw_input("\nDigite o numero que corresponde ao aluno que deve ser apagado: "))
                    aluno.deleteAluno(id)
            elif op == 4:
                cleanShell()
                aluno.getAlunos()
                opUp = int(raw_input("\nDeseja atualizar algum?\n1- SIM\n2- NAO\n"))
                if opUp == 1:
                    id = int(raw_input("\nDigite o numero que corresponde ao aluno que deve ser atualizado: "))
                    aluno.updateAluno(id)
            else:
                cleanShell()
                print "Ate a proxima xD"
        else:
            print "opcao invalida"

main()
