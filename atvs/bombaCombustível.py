class BombaCombustivel:

  def __init__(self, preco_gasolina, preco_alcool):
    self.preco_gasolina = preco_gasolina
    self.preco_alcool = preco_alcool
    self.litros_vendidos = 0
    self.total_a_pagar = 0
    self.tipo_combustivel = None

  def selecionar_combustivel(self, tipo_combustivel):
    if tipo_combustivel == "gasolina":
      self.tipo_combustivel = tipo_combustivel
    elif tipo_combustivel == "alcool":
      self.tipo_combustivel = tipo_combustivel
    else:
      print("Tipo de combustível inválido")

  def abastecer(self, valor_a_pagar):
    if self.tipo_combustivel is None:
      print("Selecione um tipo de combustível primeiro")
      return

    if self.tipo_combustivel == "gasolina":
      preco_por_litro = self.preco_gasolina
    else:
      preco_por_litro = self.preco_alcool

    litros_abastecidos = valor_a_pagar / preco_por_litro
    self.litros_vendidos += litros_abastecidos
    self.total_a_pagar += valor_a_pagar

    print(
      f"Abastecidos {litros_abastecidos:.2f} litros de {self.tipo_combustivel}"
    )
    print(f"Total a pagar: R${self.total_a_pagar:.2f}")
    print(f"Total de litros vendidos: {self.litros_vendidos:.2f}")

  def reajustar_precos(self, novo_preco_gasolina, novo_preco_alcool):
    self.preco_gasolina = novo_preco_gasolina
    self.preco_alcool = novo_preco_alcool
    print("Preços de combustível reajustados")


bomba = BombaCombustivel(preco_gasolina=5.0, preco_alcool=3.5)
bomba.selecionar_combustivel("gasolina")
bomba.abastecer(50)
bomba.reajustar_precos(novo_preco_gasolina=5.2, novo_preco_alcool=3.7)
bomba.selecionar_combustivel("alcool")
bomba.abastecer(30)
