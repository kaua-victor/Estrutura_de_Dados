from pais import Pais

pais1 = Pais('Alemanha', 'Brasília', 200000000)
pais1.paisFronteira = 'argentina'
print(pais1.listaFronteiras)
print(pais1)
pais2 = Pais('França', 'Bom ar', 125615325761)
pais2.paisFronteira = 'brasil'
print(pais2.listaFronteiras)
print(pais2)
print(pais1.fazFronteiraCom(pais2))