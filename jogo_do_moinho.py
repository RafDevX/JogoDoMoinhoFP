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
	return (isinstance(arg, list) and len(arg) == 2
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
	return isinstance(arg, list) and len(arg) == 1 and arg[0] in ('X', 'O', ' ')

def pecas_iguais(j1, j2):
	return eh_peca(j1) and j1 == j2

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


##### TAD tabuleiro #####

# Baixo Nivel

def cria_tabuleiro():
	t = {}
	for s in ('a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3'):
		t[s] = cria_peca(' ')
	return t

def cria_copia_tabuleiro(t):
	if eh_tabuleiro(t):
		return t.copy()
	
	raise ValueError('cria_copia_tabuleiro: argumento invalido')

def obter_peca(t, p):
	return t[posicao_para_str(p)]

def obter_vetor(t, s):
	v = ()
	for ps in t.keys():
		if s in ps:
			v += (t[ps],)
	return v

def coloca_peca(t, j, p):
	t[posicao_para_str(p)] = j
	return t

def remove_peca(t, p):
	t[posicao_para_str(p)] = cria_peca(' ')
	return t

def move_peca(t, p1, p2):
	return remove_peca(coloca_peca(t, obter_peca(t, p1), p2), p1)

def eh_tabuleiro(arg):
	if not (isinstance(arg, dict) and len(arg) == 9):
		return False
	
	peca_o, peca_x, peca_livre = cria_peca('O'), cria_peca('X'), cria_peca(' ')
	total_o, total_x = 0, 0

	chaves_usadas = {}
	for p in arg.keys():
		if (p not in ('a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3')
			or p in chaves_usadas.keys()):
			return False
		chaves_usadas[p] = True
		if pecas_iguais(arg[p], peca_x):
			total_x += 1
		elif pecas_iguais(arg[p], peca_o):
			total_o += 1
		elif not pecas_iguais(arg[p], peca_livre):
			return False
	if max(total_o, total_x) > 3 or abs(total_x - total_o) > 1:
		return False

	return True

def eh_posicao_livre(t, p):
	return pecas_iguais(obter_peca(t, p), cria_peca(' '))

def tabuleiros_iguais(t1, t2):
	return eh_tabuleiro(t1) and t1 == t2

def linha_tabuleiro_para_str(t, l): # l e um str numerico!
	s = l + ' '
	primeira = True
	for peca in obter_vetor(t, l):
		if primeira:
			primeira = False
		else:
			s += '-'
		s += peca_para_str(peca)
	return s

def tabuleiro_para_str(t):
	s = '   a   b   c\n'
	s += linha_tabuleiro_para_str(t, '1') + '\n'
	s += '   | \\ | / |\n'
	s += linha_tabuleiro_para_str(t, '2') + '\n'
	s += '   | / | \\ |\n'
	s += linha_tabuleiro_para_str(t, '3')
	return s

def tuplo_para_tabuleiro(t):
	tab = {}
	for s in ('a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3'):
		inteiro = t[int(s[1]) - 1][ord(s[0]) - ord('a')]
		jog = ' '
		if inteiro == 1:
			jog = 'X'
		elif inteiro == -1:
			jog = 'O'
		tab[s] = cria_peca(jog)
	return tab

# Alto Nivel

def obter_ganhador(t):
	for i in ('a', 'b', 'c', '1', '2', '3'):
		v = obter_vetor(t, i)
		if v[0] == v[1] == v[2]:
			return v[0]
	return cria_peca(' ')

def obter_posicoes_livres(t):
	return obter_posicoes_jogador(t, cria_peca(' '))

def obter_posicoes_jogador(t, j):
	posicoes = ()
	for s in ('a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3'):
		p = cria_posicao(s[0], s[1])
		if pecas_iguais(obter_peca(t, p), j):
			posicoes += (p,)
	return posicoes


##### Funcoes Adicionais #####

def obter_fase(t, j): # aux
	return 'movimento' if len(obter_posicoes_jogador(t,j)) == 3 else 'colocacao'

def obter_movimento_manual(t, j):
	fase = obter_fase(t, j)
	if fase == 'colocacao':
		p_str = input('Turno do jogador. Escolha uma posicao: ')
		if len(p_str) == 2:
			if p_str[0] in ('a', 'b', 'c') and p_str[1] in ('1', '2', '3'):
				p = cria_posicao(p_str[0], p_str[1])
				if eh_posicao_livre(t, p):
					return (p,)
	elif fase == 'movimento':
		p_str = input('Turno do jogador. Escolha um movimento: ')
		if len(p_str) == 4:
			if p_str[0] in ('a', 'b', 'c') and p_str[1] in ('1', '2', '3') \
				and p_str[2] in ('a', 'b', 'c') and p_str[3] in ('1', '2', '3'):
				p1 = cria_posicao(p_str[0], p_str[1])
				p2 = cria_posicao(p_str[2], p_str[3])
				if pecas_iguais(obter_peca(t,p1), j) and eh_posicao_livre(t,p2):
					return (p1, p2)
	raise ValueError('obter_movimento_manual: escolha invalida')

# <Criterios de Colocacao Automatica>

def criterio_colocacao_vitoria(t, j):
	for s in ('a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3'):
		p = cria_posicao(s[0], s[1])
		t_tmp = cria_copia_tabuleiro(t)
		if pecas_iguais(obter_ganhador(coloca_peca(t_tmp, j, p)), j):
			return p
	return None

def criterio_colocacao_bloqueio(t, j):
	outro = cria_peca('X') if 'O' in peca_para_str(j) else cria_peca('O')
	return criterio_colocacao_vitoria(t, outro)

def criterio_colocacao_centro(t, j):
	p = cria_posicao('b', '2')
	return eh_posicao_livre(t, p) and p

def criterio_colocacao_canto_vazio(t, j):
	for s in ('a1', 'c1', 'a3', 'c3'):
		p = cria_posicao(s[0], s[1])
		if eh_posicao_livre(t, p):
			return p
	return None

def criterio_colocacao_lateral_vazio(t, j):
	for s in ('b1', 'a2', 'c2', 'b3'):
		p = cria_posicao(s[0], s[1])
		if eh_posicao_livre(t, p):
			return p
	return None

# </Criterios de Colocacao Automatica>

def escolher_posicao_colocacao_auto(t, j):
	criterios = (
		criterio_colocacao_vitoria, criterio_colocacao_bloqueio,
		criterio_colocacao_centro, criterio_colocacao_canto_vazio,
		criterio_colocacao_lateral_vazio,
	)
	for crit in criterios:
		p = crit(t, j)
		if p is not None:
			return p

	raise RuntimeError('escolher_posicao_colocacao_auto: ' \
		+ 'nenhum criterio de colocacao e aplicavel') 

def escolher_movimento_facil_auto(t, j):
	for p in obter_posicoes_jogador(t, j):
		for adj in obter_posicoes_adjacentes(p):
			if eh_posicao_livre(t, adj):
				return (p, adj)
	return None

def minimax(t, j, profundidade, seq_movimentos = ()):
	ganhador_int = peca_para_inteiro(obter_ganhador(t))
	if ganhador_int or profundidade == 0:
		return ganhador_int, seq_movimentos
	j_int = peca_para_inteiro(j)
	melhor_resultado = -j_int
	melhor_seq_movimentos = ()
	for p in obter_posicoes_jogador(t, j):
		for adj in obter_posicoes_adjacentes(p):
			if eh_posicao_livre(t, adj):
				novo_t = move_peca(cria_copia_tabuleiro(t), p, adj)
				(novo_resultado, nova_seq_movimentos) = minimax(novo_t, \
					cria_peca('X' if j_int == -1 else 'O'), profundidade - 1, \
					seq_movimentos + ((p, adj),))
				if (not melhor_seq_movimentos
					or ((j_int * novo_resultado) > (j_int * melhor_resultado))):
					melhor_resultado = novo_resultado
					melhor_seq_movimentos = nova_seq_movimentos
	return (melhor_resultado, melhor_seq_movimentos)

def obter_movimento_auto(t, j, dificuldade):
	fase = obter_fase(t, j)
	mov_redundante = 2*((obter_posicoes_jogador(t, j))[0],)
	if fase == 'colocacao':
		return (escolher_posicao_colocacao_auto(t, j),)
	elif dificuldade == 'facil':
		return escolher_movimento_facil_auto(t, j) or mov_redundante
	else:
		(_, seq_movs) = minimax(t, j, 1 if dificuldade == 'normal' else 5)
		return seq_movs[0] if seq_movs else mov_redundante

def faz_jogada(t, j, movimento):
	if len(movimento) == 2:
		move_peca(t, movimento[0], movimento[1])
	else:
		coloca_peca(t, j, movimento[0])

def moinho(ext_peca, dificuldade):
	if not (ext_peca in ('[X]', '[O]')
		and dificuldade in ('facil', 'normal', 'dificil')):
		raise ValueError('moinho: argumentos invalidos')
	peca_humano, peca_computador = cria_peca('X'), cria_peca('O')
	if ext_peca == '[O]':
		peca_humano, peca_computador = peca_computador, peca_humano
	print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade ' \
		+ dificuldade + '.')
	t = cria_tabuleiro()
	peca_livre = cria_peca(' ')
	ganhador = peca_livre
	jogada_humano = True
	print(tabuleiro_para_str(t))
	while pecas_iguais(ganhador, peca_livre):
		j = peca_humano if jogada_humano else peca_computador
		if jogada_humano:
			faz_jogada(t, j, obter_movimento_manual(t, j))
		else:
			print('Turno do computador (' + dificuldade + ')')
			faz_jogada(t, j, obter_movimento_auto(t, j, dificuldade))
		print(tabuleiro_para_str(t))
		jogada_humano = not jogada_humano
		ganhador = obter_ganhador(t)
	return ganhador