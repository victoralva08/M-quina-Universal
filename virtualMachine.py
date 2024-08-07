import random

memoriaDados = [0] * 1000 # inicializacao da memoria para armazenamento de dados
memoriaDeInstrucoes = []

def montarRam():
    for i in range(1000): 
        memoriaDados[i] = random.randint(0, 100)

def compilar(memoriaInstrucoes):  # funcao que retorna as instrucoes compiladas
    return memoriaInstrucoes  # apenas retorna a matriz de instrucoes

def armazenaValorNaMemoria(valor, end):
    umaInstrucao = [0] * 4 
    umaInstrucao[0] = 2  # opcode 2: levar para memoria
    umaInstrucao[1] = valor  # valor a ser armazenado
    umaInstrucao[2] = end  # endereco 
    umaInstrucao[3] = -1 
    maquinaInterpretada(umaInstrucao)

def maquinaInterpretada(umaInstrucao):
    opcode = umaInstrucao[0] # opcode recebe a instrucao fornecida pelo usuario

    if opcode == 0:  # se o opcode for 0, realiza a operação de soma
        end1, end2, end3 = umaInstrucao[1], umaInstrucao[2], umaInstrucao[3] # end1, end2 e end3 recebem os enderecos de memoria 
        conteudoRam1, conteudoRam2 = memoriaDados[end1], memoriaDados[end2] # os valores contidos nos enderecos de memoria end1 e end2 sao armazenados para a operacao seguinte

        soma = conteudoRam1 + conteudoRam2
        memoriaDados[end3] = soma # o resultado da operacao eh armazenado no endereco de memoria end3
        print(f"Somando {conteudoRam1} com {conteudoRam2} e gerando {soma}.")

    elif opcode == 1:  # se o opcode for 1, realiza a operação de subtração, sendo a logica a mesma da operacao de soma
        end1, end2, end3 = umaInstrucao[1], umaInstrucao[2], umaInstrucao[3]
        conteudoRam1, conteudoRam2 = memoriaDados[end1], memoriaDados[end2]

        subtr = conteudoRam1 - conteudoRam2
        
        memoriaDados[end3] = subtr
        print(f"Subtraindo {conteudoRam2} de {conteudoRam1} e gerando {subtr}.")

    elif opcode == 2:  # se o opcode for 2, carrega um valor na memória
        content, end = umaInstrucao[1], umaInstrucao[2]  # obtem o valor e o endereco
        memoriaDados[end] = content  # armazena o valor no endereco especificado

    elif opcode == 3:  # se o opcode for 3, traz um valor da memória
        end = umaInstrucao[2]
        umaInstrucao[1] = memoriaDados[end]  # atualiza o valor na instrucao com o valor do endereço de memoria especificado
            
    elif opcode == -1:  # se o opcode for -1, para a execução (HALT)
        print("HALT")

    return opcode    

def maquina(memoriaDeInstrucoes):  # funcao que executa todas as instrucoes na memoria

    memoriaDeInstrucoesCompilada = compilar(memoriaDeInstrucoes)

    PC = 0  # inicializa o contador de programa (PC) em 0
    valorMax = float('inf') # define o opcode inicial como infinito (valor maximo possivel)
    opcode = valorMax  
    while opcode != -1:  # loop até encontrar o opcode de parada (-1)
        umaInstrucao = memoriaDeInstrucoesCompilada[PC]  # obtem a instrucao atual
        opcode = maquinaInterpretada(umaInstrucao)  # Interpreta a instrucao
        PC += 1  # incrementa o contador de programa

def montarInstrucoesProgramaMultiplicacao(multiplicando, multiplicador, memoriaDados):
        
    memoriaDeInstrucoes = [
        [0, 0, 0, 0] for _ in range(multiplicador + 3)
    ] # o tamanho da matriz eh (multiplicador + 3) para acomodar todas as intrucoes necessarias, incluindo as de carga, soma repetida e a instrucao de parada (HALT).
    
    # configurando o valor na memoriaDeInstrucoes
    umaInstrucao = [0] * 4  
    umaInstrucao[0] = 2 # opcode eh 2, ou seja, para realizar operacao de carregar valor na memoria
    umaInstrucao[1] = multiplicando # valor a ser carregado
    umaInstrucao[2] = 0 # endereco na memoria
    umaInstrucao[3] = -1 # nao eh utilizado	

    memoriaDeInstrucoes[0] = umaInstrucao

    # a instrucao abaixo atribui o valor 0 para o endereco 1 na memoria, onde o resultado das sucessivas somas sera armazenado
    umaInstrucao = [0] * 4 
    umaInstrucao[0] = 2
    umaInstrucao[1] = 0
    umaInstrucao[2] = 1
    umaInstrucao[3] = -1	

    memoriaDeInstrucoes[1] = umaInstrucao

    # realizadas as duas instrucoes de configuracao da memoria, inciam-se as multiplicacoes sucessivas:
    for i in range(multiplicador): # loop gera (multiplicador) instrucoes para somar o valor armazenado no endereco 0 (o multiplicando) ao valor no endereco 1 (acumulador).
        umaInstrucao = [0] * 4 
        umaInstrucao[0] = 0 # opcode eh 0, ou seja, para realizar operacao de soma
        umaInstrucao[1] = 0
        umaInstrucao[2] = 1
        umaInstrucao[3] = 1
        
        memoriaDeInstrucoes[i + 2] = umaInstrucao
    
    
    memoriaDeInstrucoes[multiplicador + 2] = [-1, -1, -1, -1] # HALT da operacao


    maquina(memoriaDeInstrucoes)

    # armazenaValorNaMemoria(multiplicador, 12)
    # print(memoriaDados[12])
    print(f'Resultado da multiplicação: {memoriaDados[1]}')

def montarInstrucoesProgramaDivisao(dividendo, divisor, memoriaDados):
    memoriaDeInstrucoes = [
        [0, 0, 0, 0] for _ in range(5)
    ] # o tamanho da matriz eh (divisor + 3) para acomodar todas as intrucoes necessarias, incluindo as de carga, soma repetida e a instrucao de parada (HALT).

    # configurando o valor na memoriaDeInstrucoes
    umaInstrucao = [0] * 4  
    umaInstrucao[0] = 2 # opcode eh 2, ou seja, para realizar operacao de carregar valor na memoria
    umaInstrucao[1] = dividendo # valor a ser carregado
    umaInstrucao[2] = 0 # endereco na memoria
    umaInstrucao[3] = -1 # nao eh utilizado	

    memoriaDeInstrucoes[0] = umaInstrucao

    # a instrucao abaixo atribui o valor (divisor) para o endereco 1 na memoria, onde o resultado das sucessivas substracoes sera armazenado
    umaInstrucao = [0] * 4 
    umaInstrucao[0] = 2
    umaInstrucao[1] = divisor
    umaInstrucao[2] = 1
    umaInstrucao[3] = -1 # nao eh utilizado

    memoriaDeInstrucoes[1] = umaInstrucao

    umaInstrucao = [0] * 4 
    umaInstrucao[0] = 2
    umaInstrucao[1] = 1
    umaInstrucao[2] = 2
    umaInstrucao[3] = -1		
    memoriaDeInstrucoes[2] = umaInstrucao
    # memoriaDados[2] = 1
    # representa uma variavel de incremento
    
    umaInstrucao = [0] * 4 
    umaInstrucao[0] = 2
    umaInstrucao[1] = 0
    umaInstrucao[2] = 3
    umaInstrucao[3] = -1		
    memoriaDeInstrucoes[3] = umaInstrucao
    # memoriaDeDados[3] = 0
    # representa quantas subtracoes foram feitas
    # representa o resultado da divisão
        
    memoriaDeInstrucoes[4] = [-1, -1, -1, -1] # HALT da operacao

    maquina(memoriaDeInstrucoes)
    
    # Executa a divisao atraves de subtracao sucessivas
    while memoriaDados[0] >= memoriaDados[1]:
        # Subtrai o divisor do dividendo
        umaInstrucao = [0] * 4 
        umaInstrucao[0] = 1  # opcode 1: subtrair
        umaInstrucao[1] = 0  # Dividendo
        umaInstrucao[2] = 1  # Divisor
        umaInstrucao[3] = 0  # endereco para o resultado da subtracao
        maquinaInterpretada(umaInstrucao)

        # Incrementa o contador de divisões
        umaInstrucao = [0] * 4 
        umaInstrucao[0] = 0  # opcode 0: somar
        umaInstrucao[1] = 2  # endereco do contador
        umaInstrucao[2] = 3  # endereco do contador
        umaInstrucao[3] = 3  # endereco onde armazenar o resultado
        maquinaInterpretada(umaInstrucao)
    

    print(f"Resultado da divisão: {memoriaDados[3]}")
    
def exponenciacao(base, expoente, memoriaDados):

    armazenaValorNaMemoria(base, 2)

    for _ in range(expoente - 1):
        montarInstrucoesProgramaMultiplicacao(memoriaDados[2], base, memoriaDados)
        armazenaValorNaMemoria(memoriaDados[1], 2)
    
    print(f'Resultado da exponenciação: {memoriaDados[2]}')

def fatorial(numero, memoriaDados):

    armazenaValorNaMemoria(numero, 1)
    # armazena o numero para operacao fatorial

    armazenaValorNaMemoria(1, 11)
    # armazena o 1 na memoria

    umaInstrucao = [0] * 4 
    umaInstrucao[0] = 1  # opcode 1: realizar operacao de subtracao
    umaInstrucao[1] = 1  # endereco do contador
    umaInstrucao[2] = 11  # endereco do contador
    umaInstrucao[3] = 12  # endereco para armazenar o resultado
    maquinaInterpretada(umaInstrucao)
    # subtrai 1 do valor inicial do fatorial

    while (memoriaDados[12] >= 1):
        montarInstrucoesProgramaMultiplicacao(memoriaDados[1], memoriaDados[12], memoriaDados)

        # quando a funcao de multiplicacao eh executada, a funcao maquina reseta os valores na memoria ram, por isso eh preciso armazenar os valores novamente

        # armazenaValorNaMemoria(memoriaDados[1], 1)
        # armazenaValorNaMemoria(1, 11)

        umaInstrucao = [0] * 4 
        umaInstrucao[0] = 1  # opcode 1: realizar operacao de subtracao
        umaInstrucao[1] = 12  # endereco do contador
        umaInstrucao[2] = 11  # endereco do contador
        umaInstrucao[3] = 12  # endereco para armazenar o resultado
        maquinaInterpretada(umaInstrucao)
        
        # subtrai 1 do valor inicial do fatorial
    
    print(f"Resultado de {numero}!: {memoriaDados[1]}")

def areaCirculo(r, memoriaDados):
    exponenciacao(r, 2, memoriaDados)
    montarInstrucoesProgramaMultiplicacao(3, memoriaDados[2], memoriaDados)
    print(f"Área aproximada do circulo de raio {r}: {memoriaDados[1]} u.a.²")

def areaRetangulo(l1, l2, memoriaDados):
    montarInstrucoesProgramaMultiplicacao(l1, l2, memoriaDados)
    
    if l1 == l2:
        print(f"Area aproximada do quadrado: {memoriaDados[1]} u.a.²")    
    else:
        print(f"Area aproximada do retangulo: {memoriaDados[1]} u.a.²")

def areaTrapezio(baseMaior, baseMenor, altura, memoriaDados):

    armazenaValorNaMemoria(baseMaior, 0)
    armazenaValorNaMemoria(baseMenor, 1)

    umaInstrucao = [0] * 4 
    umaInstrucao[0] = 0  # opcode 0: realizar operacao de soma
    umaInstrucao[1] = 0
    umaInstrucao[2] = 1  
    umaInstrucao[3] = 5  # endereco para armazenar o resultado
    maquinaInterpretada(umaInstrucao)

    montarInstrucoesProgramaMultiplicacao(memoriaDados[5], altura, memoriaDados)
    montarInstrucoesProgramaDivisao(memoriaDados[1], 2, memoriaDados)

    print(f"Área do trapézio: {memoriaDados[3]} u.a.²")

montarRam()

# montarInstrucoesProgramaMultiplicacao(3, 5, memoriaDados)
# montarInstrucoesProgramaDivisao(27, 3, memoriaDados)
# exponenciacao(3, 2, memoriaDados)
# areaCirculo(3, memoriaDados)
# areaRetangulo(2, 2, memoriaDados)
# areaTrapezio(2, 3, 2, memoriaDados)

fatorial(3, memoriaDados) 

