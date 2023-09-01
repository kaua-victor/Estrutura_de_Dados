class Pais:
    def __init__(self, nomePais, nomeCapital, dimensao:int):
        self.__nomePais = nomePais
        self.__nomeCapital = nomeCapital
        self.__dimensao = dimensao
        self.listaFronteiras = []
    
    @property
    def paisFronteira(self):
        return self.paisFronteira
    
    @paisFronteira.setter
    def paisFronteira(self, paisFronteira):
        if paisFronteira not in self.listaFronteiras:
            self.listaFronteiras.append(paisFronteira.title())
        return self.listaFronteiras

    def fazFronteiraCom(self, outroPais: 'Pais')->bool:
        if outroPais.__nomePais in self.listaFronteiras:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.__nomePais},capital  {self.__nomeCapital}, {self.__dimensao} Km²'

if __name__ == "__main__":
    pais1 = Pais('Brasil', 'Brasília', 200000000)
    pais1.paisFronteira = 'argentina'
    print(pais1.listaFronteiras)
    print(pais1)
    pais2 = Pais('Argentina', 'Bom ar', 125615325761)
    pais2.paisFronteira = 'brasil'
    print(pais2.listaFronteiras)
    print(pais2)
    print(pais1.fazFronteiraCom(pais2))