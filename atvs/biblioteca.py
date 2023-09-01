class Livro:

  def __init__(self, titulo, autor, disponivel):
    self.titulo = titulo
    self.autor = autor
    self.disponivel = disponivel
    if disponivel == True:
      print(self.titulo)
      print(self.autor)
      print('O livro está disponível para empréstimo')
    elif disponivel == False:
      print(self.titulo)
      print(self.autor)
      print('O livro não está disponível para empréstimo')
    else:
      print('Escolha um livro válido')
      return


biblioteca = Livro('Os três porquinhos', 'Não sei', True)
