
def produto_interno(vetor1,vetor2):
    """
    Args:
        vetor1 (tuple): Vetor 1
        vetor2 (tuple): Vetor 2

    Returns:
        float: Produto interno dos dois vetores
    """
    res = 0
    for i in range (len(vetor1)):
        res = res + vetor1[i] * vetor2[i]
    return float(res)

def verifica_convergencia(matriz,constantes,solucao,precisao):
    """
    Args:
        matriz (tuple): Constituído por um conjunto de tuplos cada um representando 
    uma coluna da matriz quadrada
        constantes (tuple): Vetor de constantes
        solucao (tuple): Solução atual
        presisao (float): Precisão pretendida
    Returns:
        bool:  Deverá retornar True caso se verifique convergencia, 
    e False caso contrário
    """
    convergente = True
    for i in range(len(matriz)):
        if abs(produto_interno(matriz[i],solucao)-constantes[i])>=precisao:
            convergente=False
            return convergente
    return convergente

def retira_zeros_diagonal(matriz,constantes):
    """
    Args:
        matriz (tuple): Um tuplo de tuplos, representando a matriz de entrada. 
        constantes (tuple): Um tuplo de números, representando o vetor das constantes.

    Returns:
        tuple: A função retorna uma nova matriz com as mesmas linhas que a de
    entrada, mas com estas reordenadas de forma a não existirem valores 0 na diagonal
    e também o vetor de entrada com a mesma reordenação de linhas que a aplicada à matriz
    """
    matriz = list(matriz)
    constantes= list(constantes)
    for i in range(len(matriz)):
        if matriz[i][i]==0:
            for j in range(len(matriz)):
                if matriz[j][i]!=0 and matriz[i][j]!=0:
                    matriz[i],matriz[j]=matriz[j],matriz[i]
                    constantes[i],constantes[j]=constantes[j],constantes[i]
                    break
    return tuple(matriz),tuple(constantes)

def eh_diagonal_dominante(matriz):
    """
    Args:
        matriz (tuple): Tuplo de tuplos representando uma matriz quadrada

    Returns:
        bool:  Deverá retornar True caso seja uma matriz diagonalmente dominante, 
    e False caso contrário
    """
    for i in range (len(matriz)):
        soma=0
        for j in range (len(matriz[i])):
            soma+=abs(matriz[i][j])
        soma-=abs(matriz[i][i])
        if abs(matriz[i][i]) < soma or matriz[i][i]==0:
            return False
        return True

def verifica_condicoes_sistema(matriz,constantes,precisao):
    """
    Args:
        matriz (tuple): Constituído por um conjunto de tuplos cada um representando 
    uma coluna da matriz quadrada
        constantes (tuple): Vetor de constantes
        precisao (float): Precisão pretendida

    Raises:
        ValueError: Levanta erro se a matriz não for um tuplo de tuplos, quadrada, com números
    inteiros ou reais e se o vetor das constantes não for um tuplo com o mesmo comprimento que 
    a matriz.
        ValueError: Levanta erro se a precisao não for real ou maior que 0
    """
    if not (type(matriz)==tuple and type(constantes)==tuple and len(matriz)==len(constantes)\
        and type(precisao)==float and precisao>0):
        raise ValueError ("resolve_sistema: argumentos invalidos")
    for i in range(len(matriz)):
        if not((type(constantes[i])==int or type(constantes[i])==float) and \
            type(matriz[i])==tuple and len(matriz)==len(matriz[i])):
            raise ValueError ("resolve_sistema: argumentos invalidos")
        for j in range(len(matriz)):
            if not (type(matriz[i][j])==int or type(matriz[i][j])==float):
                raise ValueError ("resolve_sistema: argumentos invalidos")

def resolve_sistema(matriz,constantes,precisao):
    """
    Args:
        matriz (tuple): Constituído por um conjunto de tuplos cada um representando 
    uma coluna da matriz quadrada
        constantes (tuple): Vetor de constantes
        precisao (tuple): Precisão pretendida

    Raises:
        ValueError: Levanta erro se a matriz não for diagonal dominante

    Returns:
        tuple: Solução do sistema de equações
    """
    verifica_condicoes_sistema(matriz,constantes,precisao)
    matriz,constantes=retira_zeros_diagonal(matriz,constantes)    
    if not eh_diagonal_dominante(matriz):
        raise ValueError ("resolve_sistema: matriz nao diagonal dominante")
    j=0
    sol=()   
    while j<(len(matriz)):
        sol+=(0,)
        j+=1
    
    while not verifica_convergencia(matriz,constantes,sol,precisao):
        nova_sol=()
        for i in range(len(constantes)):
            nova_sol += (sol[i] + (constantes[i] - produto_interno(matriz[i],sol))/matriz[i][i],)
        sol=nova_sol
    return sol

def limpa_texto(cad):
    """
    Args:
        cad (str): Cadeia de carateres

    Returns:
        str: Cadeia de carateres limpa (remoção de carateres brancos)
    """
    lst_palavras = cad.split()
    return " ".join(lst_palavras)

def corta_texto(cad,largura):
    """
    Args:
        cad (str): Texto limpo
        largura (int): Largura da coluna

    Returns:
        tuple: Duas subcadeias de carateres limpas
    """
    if cad=="":
        return cad[:],""
    cortar=0
    for i in range(largura):
        if cad[i]==" ":
            cortar=i-1
        elif i==len(cad)-1:
            return cad[:],""
    if cad[i+1]==" ":
        cortar=i
    return cad[:cortar+1],cad[cortar+2:]

def espacos(cad,total_espacos):
    """Esta função é uma função auxiliar que funciona como um ciclo, recebe uma cadeia de 
    carateres e um inteiro positivo correspondentes a um texto limpo e o total de espaços 
    necessários para inserir na cadeira de caracteres respetivamente, e devolve um tuplo.

    Args:
        cad (str): Cadeira de caracteres
        total_espacos (int): Total de espaços necessários para
    inserir na cadeira de caracteres

    Returns:
        tuple: tuple[0]: Cadeia de caracteres final com os espaços em branco
               tuple[1]: Total de espaços restantes
    """
    res = ""
    for i in range(len(cad)):
        if cad[i]==" " and total_espacos!=0 and cad[i+1]!=" ":
            res += cad[i] + " "
            total_espacos = total_espacos-1
        else:
            res+=cad[i]
    return res,total_espacos

def insere_espacos(cad,largura):
    """
    Args:
        cad (str): Texto limpo;
        largura (int): Largura da coluna.

    Returns:
        str: Devolve uma cadeia de caracteres a partir da função auxiliar
    """
    total_espacos= largura-len(cad)
    if cad.count(" ")==0:
        return cad[:]+" "*total_espacos
    else:
        falta_espacos = True
        while falta_espacos == True:
            resultado = espacos(cad,total_espacos)
            if resultado[1] == 0:
                falta_espacos = False
            else:
                cad = resultado[0]
                total_espacos = resultado[1]
        return resultado[0]

def justifica_texto(cad,largura):
    """
    Args:
        cad (str): Texto qualquer;
        largura (int): Lagura da coluna.

    Raises:
        ValueError: Se o comprimento do texto for vazio ou a lagura negativa
    ou o primeiro argumento (cad) não for uma string ou o segundo argumento (largura)
    não for um inteiro; levanta-se um erro com a mensegem "argumentos invalidos".

    Returns:
        tuple: Tuplo de cadeias de carateres justificadas.
    """
    if type(cad)!=str or type(largura)!=int or largura<=0 or len(cad)==0 or len(limpa_texto(cad).split()[0])>largura:
        raise ValueError ("justifica_texto: argumentos invalidos")
    elif len(limpa_texto(cad))<=largura:
        return (limpa_texto(cad) + " "*(largura-len(limpa_texto(cad))),)
    else:
        parte_do_texto = corta_texto(limpa_texto(cad),largura)
        texto_justificado=()
        corta=True
        while corta==True:
            texto_justificado += (insere_espacos(parte_do_texto[0],largura),)
            if len(parte_do_texto[1])<=largura:
                corta=False
            else:
                parte_do_texto=corta_texto(parte_do_texto[1],largura)
        else:
            texto_justificado+=(parte_do_texto[1]+" "*(largura-len(parte_do_texto[1])),)
        return texto_justificado

def calcula_quocientes(votos_circulo,num_deputados):
    """
    Args:
        votos_circulo (dict): Dicionário com os votos apurados num círculo 
    (com pelo menos um partido)
        num_deputados (int): Inteiro positivo representando o número de deputados

    Returns:
        dict: Dicionário com os quocientes calculados com o método de Hondt 
    ordenados em ordem decrescente
    """
    calc_quocientes={}
    lst=[]
    for key, values in votos_circulo.items():
        lst=[]
        for i in range(1,num_deputados+1):
            lst += [values/i]
        calc_quocientes[key] = lst
    return calc_quocientes

def atribui_mandatos(votos_circulo,num):
    """
    Args:
        votos_circulo (dict): Dicionário com os votos apurados num círculo
        num (int): Inteiro representando o número de deputados

    Returns:
        list: Lista ordenada de tamanho igual ao número de deputados contendo as cadeias de carateres 
        dos partidos que obtiveram cada mandato
    """
    lst,lst2=[],[]
    n=0
    calc_quocientes = calcula_quocientes(votos_circulo,num)
    for key, values in calc_quocientes.items():
        lst+=[key,values]
    while n<num:
        j=1
        for i in range(3,len(lst),2):
            if lst[j][0]<lst[i][0]:
                j=i
            elif lst[j][0]==lst[i][0]:
                if len(lst[j])<len(lst[i]):
                    j=i
        lst2.append(lst[j-1])
        del(lst[j][0])
        n+=1
    return lst2

def obtem_partidos(info_eleicoes):
    """
    Args:
        info_eleicoes (dict): Dicionário com a informação sobre as 
    eleições num território com vários círculos eleitorais

    Returns:
        list: Lista por ordem alfabética com o nome de todos 
    os partidos que participaram nas eleições
    """
    lst=[]
    for resultados in info_eleicoes.values():
        for partidos in resultados["votos"].keys():
            lst.append(partidos)
    res = [lst[0]]
    for el in lst:
        if el not in res:
            res += [el]
    return sorted(res)

def verifica_info_eleicoes(info_eleicoes):
    """
    Args:
        info_eleicoes (dict): Informação sobre as eleições num território com
    vários círculos eleitorais

    Raises:
        ValueError: Levanta erro caso os argumentos contidos no dicioário forem inválidos
    """
    if type(info_eleicoes)!=dict or info_eleicoes=={} or len(info_eleicoes.keys())<1 or\
        not all(type(locais)==str for locais in list(info_eleicoes.keys())):
        raise ValueError ("obtem_resultado_eleicoes: argumento invalido")
    for res in info_eleicoes.values():
        if type(res)!=dict or len(res)<=1 or not all(list(chave.keys())==["deputados","votos"] for chave in info_eleicoes.values()) or\
            not all(isinstance(info_eleicoes[local]["votos"],dict) for local in list(info_eleicoes.keys())) or\
                not all(isinstance(n,int) for n in list(res["votos"].values()))\
                    or not all(type(partido)==str for partido in list(res["votos"].keys())) or \
                        not all(n>0 for n in list(res["votos"].values()))\
                            or not all(type(c)==str for c in list(res["votos"].keys()))\
                                or type(res["deputados"])!=int or len(list(res["votos"].keys()))<1\
                                    or res["deputados"]<1:
                                    raise ValueError ("obtem_resultado_eleicoes: argumento invalido")

def obtem_resultado_eleicoes(info_eleicoes):
    """
    Args:
        info_eleicoes (dict): Informação sobre as eleições num território com
    vários círculos eleitorais

    Returns:
        list: Lista ordenada de comprimento igualao número total de partidos 
    com os resultados das eleições
    """
    verifica_info_eleicoes(info_eleicoes)
    lst=[]
    nome=obtem_partidos(info_eleicoes)
    for el in nome:
        soma,t_deputados=0,0
        for resultados in info_eleicoes.values():
            n_deputados=atribui_mandatos(resultados["votos"],resultados["deputados"])
            if el in resultados["votos"]:
                t_deputados+=n_deputados.count(el)   
                soma+=resultados["votos"][el]
        lst+=[(el,t_deputados,soma),]
    return sorted(lst, key=lambda item: (item[1], item[2]), reverse=True)
