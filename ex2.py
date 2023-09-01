class Aluno:
    def __init__(self, matricula , nome , nota):
        self.matricula = matricula
        self.nome = nome
        self.nota = nota

    def __str__(self):
        return f'{self.matricula} - {self.nome} : Notas - {self.nota}'