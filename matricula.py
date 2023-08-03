import random

class Aluno:
    def __init__(self, nome, matricula, ano):
        self.nome = nome
        self.matricula = matricula
        self.ano = ano

    def mostrar_dados(self):
        print("Nome: ", self.nome)
        print("Matrícula: ", self.matricula)
        print("Ano/Série: ", self.ano)


class Turma:
    def __init__(self, numero):
        self.numero = numero
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def remover_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)

    def mostrar_alunos(self):
        if self.alunos:
            print(f"========= ALUNOS DA TURMA {self.numero} =========")
            for aluno in self.alunos:
                aluno.mostrar_dados()
                print("----------------------")
        else:
            print("Turma vazia.")


class Escola:
    def __init__(self):
        self.turmas = []

    def cadastrar_aluno(self, nome, ano):
        matricula = random.randint(1000, 9999)
        aluno = Aluno(nome, matricula, ano)
        turma = self.encontrar_turma(ano)
        if turma is None:
            turma = Turma(ano)
            self.turmas.append(turma)
        turma.adicionar_aluno(aluno)

    def consultar_aluno(self, nome):
        for turma in self.turmas:
            for aluno in turma.alunos:
                if aluno.nome.lower() == nome.lower():
                    return aluno
        return None

    def excluir_aluno(self, aluno):
        for turma in self.turmas:
            turma.remover_aluno(aluno)

    def encontrar_turma(self, ano):
        for turma in self.turmas:
            if turma.numero == ano:
                return turma
        return None

    def mostrar_turmas(self):
        if self.turmas:
            print("======= TURMAS DISPONÍVEIS =======")
            for i, turma in enumerate(self.turmas, 1):
                print(f"Turma {i} Ano/Série: {turma.numero}")
            print("---------------------------------")
        else:
            print("Nenhuma turma cadastrada.")

