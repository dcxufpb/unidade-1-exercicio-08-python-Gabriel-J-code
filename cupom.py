# coding: utf-8

class Loja:
  
	def __init__(self, nome_loja, logradouro, numero, complemento, bairro, 
               municipio, estado, cep, telefone, observacao, cnpj,
               inscricao_estadual):
		self.nome_loja = nome_loja
		self.logradouro = logradouro
		self.numero = numero
		self.complemento = complemento
		self.bairro = bairro
		self.municipio = municipio
		self.estado = estado
		self.cep = cep
		self.telefone = telefone
		self.observacao = observacao
		self.cnpj = cnpj
		self.inscricao_estadual = inscricao_estadual

def isEmpty(string):
	if (string == None) or (string == ""):
		return True
	return False
	


def dados_loja_objeto(loja):
	if isEmpty(loja.nome_loja):
		raise Exception("O campo nome da loja é obrigatório")

	if isEmpty(loja.logradouro):
		raise Exception("O campo logradouro do endereço é obrigatório")
		
	if isEmpty(loja.municipio):
		raise Exception("O campo município do endereço é obrigatório")

	if isEmpty(loja.estado):
		raise Exception("O campo estado do endereço é obrigatório")

	if isEmpty(loja.cnpj):
		raise Exception("O campo CNPJ da loja é obrigatório")	

	if isEmpty(loja.inscricao_estadual):
		raise Exception("O campo inscrição estadual da loja é obrigatório")

	_numero = "s/n" if not loja.numero else str(loja.numero)

	_complemento = " " + loja.complemento if not isEmpty(loja.complemento) else ""	

	_bairro = loja.bairro + " - " if not isEmpty(loja.bairro) else ""

	_cep = "CEP:" + loja.cep if not isEmpty(loja.cep) else ""

	_telefone = "Tel " + loja.telefone if not isEmpty(loja.telefone) else ""

	_telefone = " " + _telefone if not isEmpty(loja.cep) and not isEmpty(loja.telefone) else _telefone

	_observacao = loja.observacao if not isEmpty(loja.observacao) else ""

	nota = loja.nome_loja + "\n"
	nota += "%s, %s%s\n" %(loja.logradouro,_numero,_complemento)
	nota += "%s%s - %s\n" % (_bairro,loja.municipio,loja.estado)
	nota += "%s%s\n" % (_cep,_telefone)
	nota += "%s\n" % (_observacao)
	nota += "CNPJ: %s\n" %(loja.cnpj)
	nota += "IE: %s" % (loja.inscricao_estadual)

	return nota 

