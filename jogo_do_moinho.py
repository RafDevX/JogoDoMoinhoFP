# 99311 Rafael Serra e Oliveira

##### TAD posicao #####

## Baixo Nivel

def cria_posicao(c, l):
	if c in ('a', 'b', 'c') and l in ('1', '2', '3'):
		return [c, l]

	raise ValueError('cria_posicao: argumentos invalidos')

def cria_copia_posicao(p):
	if eh_posicao(p):
		return p.copy()
	
	raise ValueError('cria_copia_posicao: argumento invalido')

def obter_pos_c(p):
	return p[0]

def obter_pos_l(p):
	return p[1]

def eh_posicao(arg):
	return (type(arg) == list and len(arg) == 2
		and arg[0] in ('a', 'b', 'c') and arg[1] in ('1', '2', '3'))

def posicoes_iguais(p1, p2):
	return (eh_posicao(p1) and eh_posicao(p2)
	and p1[0] == p2[0] and p1[1] == p2[1])

def posicao_para_str(p):
	return p[0] + p[1]

## Alto Nivel

def obter_posicoes_adjacentes(p):
	adj = {
		'a1': ('b1', 'a2', 'b2'),
		'b1': ('a1', 'c1', 'b2'),
		'c1': ('b1', 'b2', 'c2'),
		'a2': ('a1', 'b2', 'a3'),
		'c2': ('c1', 'b2', 'c3'),
		'a3': ('a2', 'b2', 'b3'),
		'b3': ('b2', 'a3', 'c3'),
		'c3': ('b2', 'c2', 'b3'),
	}
	adj['b2'] = tuple(adj.keys())
	return tuple(cria_posicao(x[0], x[1]) for x in adj[posicao_para_str(p)])


##### TAD peca #####

## Baixo Nivel

def cria_peca(s):
	if s in ('X', 'O', ' '):
		return [s]
	
	raise ValueError('cria_peca: argumento invalido')

def cria_copia_peca(j):
	if eh_peca(j):
		return j.copy()

	raise ValueError('cria_copia_peca: argumento invalido')

def eh_peca(arg):
	return type(arg) == list and len(arg) == 1 and arg[0] in ('X', 'O', ' ')

def pecas_iguais(j1, j2):
	return eh_peca(j1) and eh_peca(j2) and j1 == j2

def peca_para_str(j):
	return '[' + j[0] + ']'

# Alto Nivel

def peca_para_inteiro(j):
	inteiros = {
		'[O]': -1,
		'[ ]': 0,
		'[X]': 1,
	}
	return inteiros[peca_para_str(j)]