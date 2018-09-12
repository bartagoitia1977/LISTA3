###############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF969 -- Algoritmos e Estruturas de Dados
#
# Autor:    Bruno Artagoitia Vicente do Nascimento
# Email:    bavn@cin.ufpe.br
# Data:        2018-09-12
#
# Descricao:  Lista Duplamente Encadeada LISTA3 Q1
#
# Licenca: Copyright(c) 2018 Bruno Artagoitia Vicente do Nascimento
#
###############################################################################

class Knot:
	def __init__(self,objeto = None,anterior = None,proximo = None,indice = 0):
		self.objeto = objeto
		self.anterior = anterior
		self.proximo = proximo
		self.indice = indice

	def __repr__(self):
		if (type(self.objeto) == str):
			self.objetostring = "'"+str(self.objeto)+"'"
		else:
			self.objetostring = str(self.objeto)
		return self.objetostring

class ListaDupla:

	def __init__(self,iteravel = None):
		self.__iteravel = iteravel
		self.__cabeca = self.__rabo = Knot()
		if not(self.__iteravel is None):
			for self.__x in self.__iteravel:
				self.anexar(self.__x)

	def anexar(self,item):
		self.__item = item
		self.__novono = Knot(self.__item,None,None,0)
		aux = self.__cabeca.proximo
		index = 0
		while not(aux is None):
			aux = aux.proximo
			index += 1
		if (aux is None):
			self.__rabo.proximo = self.__novono
			self.__novono.anterior = self.__rabo
			self.__rabo = self.__novono
			self.__rabo.indice = index

	def __str__(self):
		self.__LDEstring = "["
		aux = self.__cabeca.proximo
		if (aux is None):
			self.__LDEstring = self.__LDEstring+"]"
			return self.__LDEstring
		else:
			while not(aux is None):
				self.__LDEstring += str(aux)+";"
				aux = aux.proximo
			self.__LDEstring = self.__LDEstring[:-1]+"]"
			return self.__LDEstring

	def __repr__(self):
		return "ListaDupla("+self.__str__()+")"

	def __len__(self):
		if (self.__cabeca == self.__rabo):
			return 0
		else:
			return self.__rabo.indice + 1

	def __getitem__(self,item):
		self.__item = item
		finder = self.__cabeca.proximo
		if (finder is None):
			raise KeyError
		else:
			while not(finder is None) and (finder.indice != self.__item):
				finder = finder.proximo
			if (finder is None):
				raise KeyError
			else:
				if (finder.indice == self.__item):
					return finder.objeto

	def __setitem__(self,item,valor):
		self.__item = item
		self.__valor = valor
		finder = self.__cabeca.proximo
		if (finder is None):
			raise KeyError
		else:
			while not(finder is None) and (finder.indice != self.__item):
				finder = finder.proximo
			if (finder is None):
				raise KeyError
			else:
				if (finder.indice == self.__item):
					finder.objeto = self.__valor


	def procurar(self,valor):
		self.__valor = valor
		valor_finder = self.__cabeca.proximo
		if (valor_finder is None):
			raise ValueError
		else:
			while not(valor_finder is None) and (valor_finder.objeto != self.__valor):
				valor_finder = valor_finder.proximo
			if (valor_finder is None):
				raise ValueError
			else:
				if (valor_finder.objeto == self.__valor):
					return valor_finder.indice

	def estender(self,iteravel):
		self.__iteravel = iteravel
		for objeto in self.__iteravel:
			self.anexar(objeto)

	def inserir(self,indice,valor):
		self.__indice = indice
		self.__valor = valor
		self.__novono = Knot(self.__valor,None,None,self.__indice)
		finder = self.__cabeca.proximo
		if (finder is None):
			self.anexar(self.__valor)
		else:
			while not(finder is None) and (finder.indice != self.__indice):
				finder = finder.proximo
			if (finder is None):
				self.anexar(self.__valor)
			else:
				if (finder.indice == self.__indice):
					self.__noanterior = finder.anterior
					self.__noanterior.proximo = self.__novono
					self.__novono.anterior = self.__noanterior
					self.__novono.proximo = finder
					finder.anterior = self.__novono
					aux = finder
					while not(aux is None):
						aux.indice = ((aux.indice) + 1)
						aux = aux.proximo

	def tirar(self,indice = None):
		self.__indice = indice
		if (self.__indice == None):
			self.__indice = self.__rabo.indice
		finder = self.__cabeca.proximo
		if (finder is None):
			raise KeyError
		else:
			while not(finder is None) and (finder.indice != self.__indice):
				finder = finder.proximo
			if (finder is None):
				raise KeyError
			else:
				guarda = finder
				self.__noanterior = finder.anterior
				self.__noposterior = finder.proximo
				if not(finder.proximo is None):
					self.__noanterior.proximo = self.__noposterior
					self.__noposterior.anterior = self.__noanterior
					aux = self.__noposterior
					while not(aux is None):
						aux.indice = ((aux.indice) - 1)
						aux = aux.proximo
					return guarda.objeto
					del finder
				else:
					self.__noanterior.proximo = None
					self.__rabo = self.__noanterior
					return guarda.objeto
					del finder
										
	def trocar(self,indice1,indice2):
		a = self.tirar(indice1)
		b = self.tirar(indice2 - 1)
		self.inserir(indice1,b)
		self.inserir(indice2,a)


	def remover(self,valor):
		self.__valor = valor
		valor_finder = self.__cabeca.proximo
		if (valor_finder is None):
			raise ValueError
		else:
			while not(valor_finder is None) and (valor_finder.objeto != self.__valor):
				valor_finder = valor_finder.proximo
			if (valor_finder is None):
				raise ValueError
			else:
				if (valor_finder.objeto == self.__valor):
					self.tirar(valor_finder.indice)

	def eliminar(self,valor):
		self.__valor = valor
		valor_finder = self.__cabeca.proximo
		self.__flag = 0
		if (valor_finder is None):
			raise ValueError
		else:
			while not(valor_finder is None):
				if (valor_finder.objeto == self.__valor):
					self.tirar(valor_finder.indice)
					self.__flag += 1
				valor_finder = valor_finder.proximo
			if (self.__flag == 0):
				raise ValueError

	def copiar(self):
		return self

	def __contains__(self,valor):
		self.__valor = valor
		valor_finder = self.__cabeca.proximo
		if (valor_finder is None):
			return False
		else:
			while not(valor_finder is None) and (valor_finder.objeto != self.__valor):
				valor_finder = valor_finder.proximo
			if (valor_finder is None):
				return False
			else:
				if (valor_finder.objeto == self.__valor):
					return True

def concatenar(lista1,lista2):
	listasaida = ListaDupla()
	indexer = 0
	for item in range(len(lista1)):
		listasaida.anexar(lista1[indexer])
		indexer += 1
	indexer = 0
	for item in range(len(lista2)):
		listasaida.anexar(lista2[indexer])
		indexer += 1
	return listasaida