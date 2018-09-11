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
