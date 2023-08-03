from matricula import Escola

def principal():
    escola = Escola()
    while True:
        print("========= MENU =========")
        print("1 - Cadastrar Aluno")
        print("2 - Consultar Aluno")
        print("3 - Excluir Aluno")
        print("4 - Mostrar Turmas")
        print("5 - Mostrar Alunos de uma Turma")
        print("0 - Sair")
        print("========================")

        try:
            opcao = int(input("Digite o número da opção desejada: "))

            if opcao == 1:
                nome = input("Digite o nome do aluno: ")
                ano = int(input("Digite o ano/série do aluno: "))
                escola.cadastrar_aluno(nome, ano)
                print("Aluno cadastrado com sucesso!")

            elif opcao == 2:
                nome = input("Digite o nome do aluno: ")
                aluno = escola.consultar_aluno(nome)
                if aluno is not None:
                    print("Aluno encontrado!")
                    aluno.mostrar_dados()
                else:
                    print("Aluno não encontrado.")

            elif opcao == 3:
                nome = input("Digite o nome do aluno a ser excluído: ")
                aluno = escola.consultar_aluno(nome)
                if aluno is not None:
                    escola.excluir_aluno(aluno)
                    print("Aluno excluído com sucesso!")
                else:
                    print("Aluno não encontrado.")

            elif opcao == 4:
                escola.mostrar_turmas()

            elif opcao == 5:
                num_turma = int(input("Digite o número da turma para mostrar os alunos: "))
                turma = escola.encontrar_turma(num_turma)
                if turma is not None:
                    turma.mostrar_alunos()
                else:
                    print("Turma não encontrada.")

            elif opcao == 0:
                print("Encerrando o programa.")
                break

            else:
                print("Opção inválida! Digite um número válido.")

        except ValueError:
            print("Opção inválida! Digite um número.")

if __name__ == "__main__":
    principal()
