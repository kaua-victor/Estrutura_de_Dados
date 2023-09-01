class Calculadora:

  def __init__(self, registrador, numero):
    self.registrador = registrador
    self.numero = numero
    self.registrador += self.numero

  def adicao(self, somar, somar_numero):
    self.somar = somar
    self.somar_numero = somar_numero
    if somar == True:
      self.registrador += somar_numero
    elif somar == False:
      return

  def subtracao(self, subtrair, subtrair_numero):
    self.subtrair = subtrair
    self.subtrair_numero = subtrair_numero
    if subtrair == True:
      self.registrador -= subtrair_numero
    elif subtrair == False:
      return

  def multiplicacao(self, multiplicar, multiplicar_numero):
    self.multiplicar = multiplicar
    self.multiplicar_numero = multiplicar_numero
    if multiplicar == True:
      self.registrador *= multiplicar_numero
    elif multiplicar == False:
      return

  def divisao(self, dividir, dividir_numero):
    self.dividir = dividir
    self.dividir_numero = dividir_numero
    if dividir == True:
      self.registrador /= dividir_numero
    elif dividir == False:
      return

  def exibir(self, exibe):
    self.exibe = exibe
    if exibe == True:
      print(self.registrador)
    else:
      return

  def reset(self, resetar):
    self.resetar = resetar
    if resetar == True:
      self.registrador = 0
    else:
      return


calcular = Calculadora(registrador=0, numero=2)

calcular.adicao(True, 3)
calcular.exibir(True)

calcular.adicao(True, 5)
calcular.exibir(True)

calcular.reset(True)
calcular.exibir(True)

calcular.subtracao(True, 5)
calcular.exibir(True)

calcular.multiplicacao(True, 2)
calcular.exibir(True)

calcular.divisao(True, 5)
calcular.exibir(True)
