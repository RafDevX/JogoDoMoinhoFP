# 99311 Rafael Serra e Oliveira

##### TAD posicao #####

## Baixo Nivel

def cria_posicao(c, l):
	# str x str -> posicao
	"""Constroi uma posicao.

	Recebe como argumentos duas cadeias de caracteres correspondentes
	a coluna e a linha de uma posicao e devolve a posicao correspondente.
	Gera um ValueError caso algum dos argumentos seja invalido.
	"""
	if c in ('a', 'b', 'c') and l in ('1', '2', '3'):
		return [c, l]

	raise ValueError('cria_posicao: argumentos invalidos')

def cria_copia_posicao(p):
	# posicao -> posicao
	"""Constroi uma posicao identica a outra.

	Recebe como argumento uma posicao e devolve outra posicao que e
	uma copia da dada.
	"""
	if eh_posicao(p):
		return p.copy()
	
	raise ValueError('cria_copia_posicao: argumento invalido')

def obter_pos_c(p):
	# posicao -> str
	"""Obtem a coluna correspondente a uma posicao.

	Recebe como argumento uma posicao e devolve a sua componente coluna.
	"""
	return p[0]

def obter_pos_l(p):
	# posicao -> str
	"""Obtem a linha correspondente a uma posicao.

	Recebe como argumento uma posicao e devolve a sua componente linha.
	"""
	return p[1]

def eh_posicao(arg):
	# universal -> booleano
	"""Determina se um objeto e uma posicao.

	Recebe um argumento e devolve True se esse argumento for uma posicao,
	devolvendo False caso contrario.
	"""
	return (isinstance(arg, list) and len(arg) == 2
		and arg[0] in ('a', 'b', 'c') and arg[1] in ('1', '2', '3'))

def posicoes_iguais(p1, p2):
	# posicao x posicao -> booleano
	"""Determina se duas posicoes sao iguais.

	Recebe duas posicoes como argumentos e devolve True se sao identicas
	ou False caso contrario.
	"""
	return eh_posicao(p1) and p1 == p2

def posicao_para_str(p):
	# posicao -> str
	"""Obtem a representacao em cadeia de caracteres de uma posicao.

	Recebe uma posicao como argumento e devolve a cadeia de caracteres
	que a representa, na forma 'cl' (sendo c a sua coluna e l a sua linha).
	"""
	return p[0] + p[1]

## Alto Nivel

def obter_posicoes_adjacentes(p):
	# posicao -> tuplo de posicoes
	"""Obtem as posicoes adjacentes a uma posicao.

	Recebe uma posicao como argumento e devolve um tuplo com todas as
	posicoes adjacentes a esta, por ordem de leitura do tabuleiro.
	"""
	adj = {
		'a1': ('b1', 'a2', 'b2'),
		'b1': ('a1', 'c1', 'b2'),
		'c1': ('b1', 'b2', 'c2'),
		'a2': ('a1', 'b2', 'a3'),
		'b2': ('a1', 'b1', 'c1', 'a2', 'c2', 'a3', 'b3', 'c3'),
		'c2': ('c1', 'b2', 'c3'),
		'a3': ('a2', 'b2', 'b3'),
		'b3': ('b2', 'a3', 'c3'),
		'c3': ('b2', 'c2', 'b3'),
	}
	return tuple(cria_posicao(x[0], x[1]) for x in adj[posicao_para_str(p)])


##### TAD peca #####

## Baixo Nivel

def cria_peca(s):
	# str -> peca
	"""Constroi uma peca.

	Recebe como argumento uma cadeia de caracteres correspondente a um dos
	dois jogadores ('X' ou 'O') ou a uma peca livre (' ') e devolve uma
	nova peca que lhe corresponde.
	Gera um ValueError se o argumento for invalido.
	"""
	if s in ('X', 'O', ' '):
		return [s]
	
	raise ValueError('cria_peca: argumento invalido')

def cria_copia_peca(j):
	# peca -> peca
	"""Constroi uma peca identica a outra.

	Recebe como argumento uma peca e devolve outra peca que e uma copia desta.
	"""
	if eh_peca(j):
		return j.copy()

	raise ValueError('cria_copia_peca: argumento invalido')

def eh_peca(arg):
	# universal -> booleano
	"""Determina se um objeto e uma peca.

	Recebe um argumento e devolve True se esse argumento for uma peca,
	devolvendo False caso contrario.
	"""
	return isinstance(arg, list) and len(arg) == 1 and arg[0] in ('X', 'O', ' ')

def pecas_iguais(j1, j2):
	# peca x peca -> booleano
	"""Determina se duas posicoes sao iguais.

	Recebe duas posicoes como argumentos e devolve True se sao identicas
	ou False caso contrario.
	"""
	return eh_peca(j1) and j1 == j2

def peca_para_str(j):
	# peca -> str
	"""Obtem a representacao em cadeia de caracteres de uma peca.

	Recebe uma peca como argumento e devolve a cadeia de caracteres
	que a representa, ou seja, '[O]', '[X]' ou '[ ]'.
	"""
	return '[' + j[0] + ']'

# Alto Nivel

def peca_para_inteiro(j):
	# peca -> N
	"""Obtem a representacao em inteiro de uma peca.

	Recebe uma peca como argumento e devolve o inteiro que a representa, ou
	seja, 1, -1 ou 0 para uma peca do jogador 'X', 'O' ou livre, respetivamente.
	"""
	inteiros = {
		'[O]': -1,
		'[ ]': 0,
		'[X]': 1,
	}
	return inteiros[peca_para_str(j)]


##### TAD tabuleiro #####

# Baixo Nivel

def cria_tabuleiro():
	# {} -> tabuleiro
	"""Constroi um tabuleiro.

	Nao recebe argumentos. Devolve um tabuleiro de jogo do moinho 3x3
	com todas as suas posicoes livres.
	"""
	t = {}
	for s in ('a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3'):
		t[s] = cria_peca(' ')
	return t

def cria_copia_tabuleiro(t):
	# tabuleiro -> tabuleiro
	"""Constroi um tabuleiro identico a outro.

	Recebe como argumento um tabuleiro e devolve outro tabuleiro que e
	uma copia deste.
	"""
	if eh_tabuleiro(t):
		return t.copy()
	
	raise ValueError('cria_copia_tabuleiro: argumento invalido')

def obter_peca(t, p):
	# tabuleiro x posicao -> peca
	"""Obtem a peca numa posicao de um tabuleiro.

	Recebe como argumento um tabuleiro e uma posicao, devolvendo a peca
	que esta na posicao indicada desse tabuleiro.
	"""
	return t[posicao_para_str(p)]

def obter_vetor(t, s):
	# tabuleiro x str -> tuplo de pecas
	"""Obtem uma linha ou uma coluna de um tabuleiro.

	Recebe como argumentos um tabuleiro e uma cadeia de caracteres que
	identifica uma linha ou uma coluna. Devolve um tuplo de todas as pecas
	nessa linha/coluna do tabuleiro dado.
	"""
	v = ()
	for ps in ('a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3'):
		if s in ps:
			v += (t[ps],)
	return v

def coloca_peca(t, j, p):
	# tabuleiro x peca x posicao -> tabuleiro
	"""Coloca uma peca numa posicao de um tabuleiro.

	Recebe como argumentos um tabuleiro, uma peca e uma posicao. Altera
	destrutivamente o tabuleiro, colocando na posicao a peca dada.
	Devolve o tabuleiro.
	"""
	t[posicao_para_str(p)] = j
	return t

def remove_peca(t, p):
	# tabuleiro x posicao -> tabuleiro
	"""Remove a peca que esta numa posicao de um tabuleiro.

	Recebe como argumentos um tabuleiro e uma posicao. Altera destrutivamente
	o tabuleiro, colocando uma peca livre nessa posicao do tabuleiro.
	Devolve o tabuleiro.
	"""
	t[posicao_para_str(p)] = cria_peca(' ')
	return t

def move_peca(t, p1, p2):
	# tabuleiro x posicao x posicao -> tabuleiro
	"""Move a peca que esta numa posicao de um tabuleiro para outra.

	Recebe como argumentos um tabuleiro, uma posicao de origem e uma posicao de
	destino. Altera destrutivamente esse tabuleiro, movendo a peca que esta na
	primeira posicao para a segunda. Devolve o tabuleiro.
	"""
	return remove_peca(coloca_peca(t, obter_peca(t, p1), p2), p1)

def eh_tabuleiro(arg):
	# universal -> booleano
	"""Determina se um objeto e um tabuleiro.

	Recebe um argumento e devolve True se esse argumento for um tabuleiro,
	devolvendo False caso contrario.
	"""
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

	ganhador = obter_ganhador(arg)
	if (not pecas_iguais(ganhador, peca_livre)
		and not pecas_iguais(obter_ganhador(remove_peca(arg.copy(), \
			obter_posicoes_jogador(arg, ganhador)[0])), peca_livre)):
			return False # dois ganhadores

	return True

def eh_posicao_livre(t, p):
	# tabuleiro x posicao -> booleano
	"""Determina se uma posicao esta livre num tabuleiro.

	Recebe um tabuleiro e uma posicao. Devolve True se essa posicao estiver
	livre no tabuleiro dado, caso contrario devolve False.
	"""
	return pecas_iguais(obter_peca(t, p), cria_peca(' '))

def tabuleiros_iguais(t1, t2):
	# tabuleiro x tabuleiro -> booleano
	"""Determina se dois tabuleiros sao iguais.

	Recebe dois tabuleiros como argumentos e devolve True se sao identicos
	ou False caso contrario.
	"""
	return eh_tabuleiro(t1) and t1 == t2

def linha_tabuleiro_para_str(t, l): # l e um str numerico!
	# tabuleiro x str -> str
	"""Obtem a representacao em cadeia de caracteres de uma linha dum tabuleiro.

	Recebe como argumentos um tabuleiro e uma cadeia de caracteres que
	identifica uma linha, devolvendo a cadeia de caracteres que a representa.
	"""
	s = l + ' '
	for peca in obter_vetor(t, l):
		s += peca_para_str(peca) + '-'
	return s[:-1]

def tabuleiro_para_str(t):
	# tabuleiro -> str
	"""Obtem a cadeia de caracteres que representa um tabuleiro.

	Recebe como argumento um tabuleiro e devolve a sua representacao externa.
	"""
	return '   a   b   c\n' + linha_tabuleiro_para_str(t, '1') + '\n' \
		+ '   | \\ | / |\n' + linha_tabuleiro_para_str(t, '2') + '\n' \
		+ '   | / | \\ |\n' + linha_tabuleiro_para_str(t, '3')

def tuplo_para_tabuleiro(t):
	# tuplo -> tabuleiro
	"""Transforma um tuplo num tabuleiro.

	Recebe como argumento um tuplo de tuplos (linhas), cada um com 3 inteiros
	(1, -1 ou 0). Devolve o tabuleiro correspondente.
	"""
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
	# tabuleiro -> peca
	"""Determina o ganhador num tabuleiro.

	Recebe como argumento um tabuleiro e devolve uma peca do jogador com 3 pecas
	em linha ou coluna. Se nao existir ganhador, devolve uma peca livre.
	"""
	peca_livre = cria_peca(' ')
	for i in ('a', 'b', 'c', '1', '2', '3'):
		v = obter_vetor(t, i)
		if (not pecas_iguais(v[0], peca_livre) and pecas_iguais(v[0], v[1])
			and pecas_iguais(v[0], v[2])):
			return v[0]
	return peca_livre

def obter_posicoes_livres(t):
	# tabuleiro -> tuplo de posicoes
	"""Obtem todas as posicoes livres num tabuleiro.

	Recebe como argumento um tabuleiro e devolve um tuplo com todas as posicoes
	livres nele, por ordem de leitura.
	"""
	return obter_posicoes_jogador(t, cria_peca(' '))

def obter_posicoes_jogador(t, j):
	# tabuleiro x peca -> tuplo de posicoes
	"""Obtem todas as posicoes de um jogador num tabuleiro.

	Recebe como argumento um tabuleiro e uma peca de um jogador, devolvendo um
	tuplo com todas as posicoes em que esse tabuleiro tenha pecas desse jogador,
	por ordem de leitura.
	"""
	posicoes = ()
	for s in ('a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3'):
		p = cria_posicao(s[0], s[1])
		if pecas_iguais(obter_peca(t, p), j):
			posicoes += (p,)
	return posicoes


##### Funcoes Adicionais #####

def obter_fase(t, j):
	# tabuleiro x peca -> str
	"""Determina a fase de jogo para um jogador com base num tabuleiro.

	Recebe como argumentos um tabuleiro e uma peca, devolvendo uma cadeia de
	caracteres ('movimento' ou 'colocacao') correspondente a fase de jogo em
	que esse jogador se encontra, relativamente ao tabuleiro dado.
	"""
	return 'movimento' if len(obter_posicoes_jogador(t,j)) == 3 else 'colocacao'

def obter_movimento_manual(t, j):
	# tabuleiro x peca -> tuplo de posicoes
	"""Pede uma jogada ao utilizador.

	Recebe como argummentos um tabuleiro e uma peca correspondente ao jogador
	humano. Na fase de colocacao, devolve um tuplo com uma posicao onde o humano
	deseja colocar uma peca. Na fase de movimento, devolve um tuplo com duas
	posicoes: por esta ordem, a de origem e a de destino.
	"""
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
	# tabuleiro x peca -> posicao/nenhum
	"""Tenta aplicar o criterio de colocacao "vitoria".

	Recebe como argumentos um tabuleiro e uma peca. Devolve a posicao em que o
	jogador a que corresponde a peca pode jogar para ganhar o jogo. Caso nao
	exista uma posicao nesta situacao, devolve None.
	"""
	for s in ('a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3'):
		p = cria_posicao(s[0], s[1])
		t_tmp = cria_copia_tabuleiro(t)
		if pecas_iguais(obter_ganhador(coloca_peca(t_tmp, j, p)), j):
			return p
	return None

def criterio_colocacao_bloqueio(t, j):
	# tabuleiro x peca -> posicao/nenhum
	"""Tenta aplicar o criterio de colocacao "bloqueio".

	Recebe como argumentos um tabuleiro e uma peca. Devolve a posicao em que o
	jogador a que corresponde a peca pode jogar para bloquear uma vitoria do 
	adversario. Caso nao exista uma posicao nesta situacao, devolve None.
	"""
	outro = cria_peca('X') if 'O' in peca_para_str(j) else cria_peca('O')
	return criterio_colocacao_vitoria(t, outro)

def criterio_colocacao_centro(t, j):
	# tabuleiro x peca -> posicao/nenhum
	"""Tenta aplicar o criterio de colocacao "centro".

	Recebe como argumentos um tabuleiro e uma peca. Devolve a posicao central do
	tabuleiro se esta estiver livre; caso contrario, devolve None.
	"""
	p = cria_posicao('b', '2')
	return p if eh_posicao_livre(t, p) else None

def criterio_colocacao_canto_vazio(t, j):
	# tabuleiro x peca -> posicao/nenhum
	"""Tenta aplicar o criterio de colocacao "canto vazio".

	Recebe como argumentos um tabuleiro e uma peca. Devolve a posicao do
	primeiro canto, por ordem de leitura, que esta livre no tabuleiro, ou None
	se nenhum estiver.
	"""
	for s in ('a1', 'c1', 'a3', 'c3'):
		p = cria_posicao(s[0], s[1])
		if eh_posicao_livre(t, p):
			return p
	return None

def criterio_colocacao_lateral_vazio(t, j):
	# tabuleiro x peca -> posicao/nenhum
	"""Tenta aplicar o criterio de colocacao "lateral vazio".

	Recebe como argumentos um tabuleiro e uma peca. Devolve a posicao da
	primeira lateral, por ordem de leitura, que esta livre no tabuleiro, ou None
	se nenhuma estiver.
	"""
	for s in ('b1', 'a2', 'c2', 'b3'):
		p = cria_posicao(s[0], s[1])
		if eh_posicao_livre(t, p):
			return p
	return None

# </Criterios de Colocacao Automatica>

def escolher_posicao_colocacao_auto(t, j):
	# tabuleiro x peca -> posicao
	"""Escolhe uma posicao onde colocar uma peca.

	Recebe um tabuleiro e uma peca e devolve a posicao identificada como otima
	pelo primeiro criterio aplicavel (gerando um RuntimeError se nenhum o for).
	"""
	criterios = (criterio_colocacao_vitoria, criterio_colocacao_bloqueio, \
		criterio_colocacao_centro, criterio_colocacao_canto_vazio,
		criterio_colocacao_lateral_vazio)
	for crit in criterios:
		p = crit(t, j)
		if p is not None:
			return p

	raise RuntimeError('escolher_posicao_colocacao_auto: ' \
		+ 'nenhum criterio de colocacao e aplicavel') 

def escolher_movimento_facil_auto(t, j):
	# tabuleiro x peca -> posicao
	"""Escolhe um movimento na dificuldade 'facil'.

	Recebe um tabuleiro e uma peca e devolve a primeira posicao adjacente a uma
	posicao do jogador correspondente a peca dada que esteja livre, ou None.
	"""
	for p in obter_posicoes_jogador(t, j):
		for adj in obter_posicoes_adjacentes(p):
			if eh_posicao_livre(t, adj):
				return (p, adj)
	return None

def minimax(t, j, profundidade, seq_movimentos = ()):
	# tabuleiro x peca x inteiro x tuplo -> tuplo(inteiro x tuplo)
	"""Implementa o algoritmo minimax.

	Recebe um tabuleiro, uma peca, uma profundidade e sequencia de movimentos.
	Analisa as jogadas possiveis ate a dada profundidade, devolvendo o resultado
	do melhor cenario para o jogador da peca dada, tal como a sequencia de
	movimentos a efetuar para chegar a essa situacao.
	"""
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
	# tabuleiro x peca x str -> tuplo de posicoes
	"""Calcula o movimento para um jogador num tabuleiro numa dificuldade.

	Recebe um tabuleiro, uma peca de um jogador e uma cadeia de caracteres de
	uma dificuldade ('facil', 'normal', 'dificil'), devolvendo um tuplo com uma
	(na fase de colocacoes) ou duas (na fase de movimento) posicoes que
	corresponde a uma jogada do computador.
	"""
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
	# tabuleiro x peca x tuplo -> nenhum
	"""Executa uma jogada para um jogador num tabuleiro.

	Recebe como argumentos um tabuleiro, a peca de um jogador e um tuplo com um
	(na fase de colocacao) ou dois elementos (na fase de movimento), executando
	essa jogada. Nao devolve nada.
	"""
	if len(movimento) == 2:
		move_peca(t, movimento[0], movimento[1])
	else:
		coloca_peca(t, j, movimento[0])

def moinho(ext_peca, dific):
	# str x str -> str
	"""Corre um jogo completo do Jogo do Moinho.

	Recebe como argumentos a representacao externa da peca com que o humano
	deseja jogar ('[X]', '[O]') e a dificuldade da partida ('facil', 'normal' ou
	'dificil'). Devolve a representacao externa de uma peca do jogador ganhador.
	"""
	if not (ext_peca in ('[X]', '[O]')
		and dific in ('facil', 'normal', 'dificil')):
		raise ValueError('moinho: argumentos invalidos')
	peca_humano, peca_computador = cria_peca('X'), cria_peca('O')
	if ext_peca == '[O]':
		peca_humano, peca_computador = peca_computador, peca_humano
	print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade ' + dific + '.')
	t, peca_livre = cria_tabuleiro(), cria_peca(' ')
	ganhador, jogada_humano = peca_livre, True
	print(tabuleiro_para_str(t))
	while pecas_iguais(ganhador, peca_livre):
		j = peca_humano if jogada_humano else peca_computador
		if jogada_humano:
			faz_jogada(t, j, obter_movimento_manual(t, j))
		else:
			print('Turno do computador (' + dific + ')')
			faz_jogada(t, j, obter_movimento_auto(t, j, dific))
		print(tabuleiro_para_str(t))
		jogada_humano = not jogada_humano
		ganhador = obter_ganhador(t)
	return ganhador