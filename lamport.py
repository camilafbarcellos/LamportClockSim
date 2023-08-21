import random


def generate_clocks(num_processes):
    '''
    Gera vetores de tempos aleatórios para cada processo.

    Args:
        num_processes (int): Número de processos a serem gerados.

    Returns:
        clocks (list of lists): Lista de listas representando os vetores de tempos de cada processo.
    '''

    # Cria a lista para conter os vetores de tempos dos processos
    clocks = []

    for i in range(1, num_processes + 1):
        # Gera um valor aleatório entre 1 e 10 para o incremento
        increment = random.randint(1, 10)
        # Gera um vetor de tempos de 10 elementos com essa frequência
        process_clocks = [j * increment for j in range(10)]
        # Adiciona o vetor de tempos do processo à lista de vetores
        clocks.append(process_clocks)

    # Retorna a lista de vetores de tempos gerados
    return clocks


def print_clocks(clocks):
    '''
    Imprime os vetores de tempos de cada processo em formato de tabela.

    Args:
        clocks (list of lists): Lista de listas representando os vetores de tempos de cada processo.
    '''

    # Imprime o cabeçalho da coluna de PROCESSO
    print('P', end='\t')

    # Percorre os o tamanho dos vetores de tempos
    for i in range(len(clocks[0])):
        # Imprime os cabeçalhos das colunas de TEMPO
        print(f't{i}\t', end='')

    # Linha para separar o cabeçalho do restante da tabela
    print('\n' + '-' * 82)

    # Percorre a lista de vetores de tempos dos processos
    for i, process_clocks in enumerate(clocks, start=1):
        # Imprime o número do processo
        print(f'P{i}\t', end='')

        # Percorre os tempos do vetor e imprime cada um
        for time in process_clocks:
            print(f'{time}\t', end='')
        print()  # Pula para a próxima linha


def lamport_algorithm(clocks, src_process, src_time, dest_process, dest_time):
    '''
    Simula o algoritmo de Lamport para atualizar os relógios lógicos.

    Args:
        clocks (list of lists): Lista de listas representando os vetores de tempos de cada processo.
        src_process (int): Número do processo de origem.
        src_time (int): Índice do tempo de origem no vetor de tempos do processo de origem.
        dest_process (int): Número do processo de destino.
        dest_time (int): Índice do tempo de destino no vetor de tempos do processo de destino.

    Returns:
        clocks (list of lists): Vetores de tempos atualizados após a simulação.
    '''

    # Representação visual do evento com os processos e tempos envolvidos
    print(
        f'\nEVENTO P{src_process+1}({clocks[src_process][src_time]}) → P{dest_process+1}({clocks[dest_process][dest_time]})'
        f'\n  Emissor: P[{src_process}][{src_time}] = {clocks[src_process][src_time]}'
        f'\n  Receptor: P[{dest_process}][{dest_time}] = {clocks[dest_process][dest_time]}'
    )

    # Verifica se os indices dos tempos informados estao dentro dos limites dos vetores
    if src_time >= len(clocks[src_process]) or dest_time >= len(clocks[dest_process]):
        print('Tempo de origem ou destino fora dos limites do vetor de tempos!')
        return clocks  # Retorna os vetores de tempos sem alterações

    if clocks[dest_process][dest_time] < clocks[src_process][src_time]:
        # Descobre a frequência do clock
        freq = clocks[dest_process][2] - clocks[dest_process][1]

        # Atualiza o tempo de destino para o tempo de origem + 1
        clocks[dest_process][dest_time] = clocks[src_process][src_time] + 1

        # Percorre todo o vetor do processo de destino
        for i in range(len(clocks[dest_process])):
            # Altera todos os tempos diferentes do de destino (já alterado) e do tempo 0
            if i != dest_time and i != 0:
                # Assume o tempo anterior + a frequência descoberta
                clocks[dest_process][i] = clocks[dest_process][i-1] + freq
    else:
        print('O tempo de destino é maior que o tempo de origem! Nenhuma ação realizada...')

    # Retorna os vetores de tempos atualizados após a simulação
    return clocks


def main():
    '''
    Função principal que solicita os valores de entrada e simula o algoritmo de Lamport.
    '''

    # Banner da aplicação
    print(
        '\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *'
        '\n*           > Simulador de Relógios Lógicos de Lamport  <           *'
        '\n*                                                                   *'
        '\n*                 Desenvolvido por Camila Barcellos                 *'
        '\n*                 Sistemas Distribuídos II - 2023/2                 *'
        '\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *'
    )

    # Solicita a quantidade de processos ao usuário
    num_processes = int(input('Número de processos: '))

    # Gera os vetores de tempos para cada processo apenas se ainda não foram gerados
    if 'clocks' not in globals():
        clocks = generate_clocks(num_processes)

    # Imprime os vetores de tempos de cada processo
    print('\nRelógios lógicos:')
    print_clocks(clocks)

    # Loop principal para manter o programa em execução
    while True:
        # Solicita os dados de entrada ao usuário
        src_process = int(input('\nProcesso de origem: '))
        src_time = int(input('Tempo de origem: '))
        dest_process = int(input('Processo de destino: '))
        dest_time = int(input('Tempo de destino: '))

        # Verifica se os processos informados são válidos
        if src_process < 1 or src_process > num_processes or dest_process < 1 or dest_process > num_processes:
            print(f'\nProcesso inválido... Selecione entre 1 e {num_processes}!')
            continue

         # Verifica se os tempos informados são válidos
        if src_time < 0 or src_time >= len(clocks[src_process - 1]) or dest_time < 0 or dest_time >= len(clocks[dest_process - 1]):
            print('\nTempo inválido para os processos informados... Tente novamente!')
            continue

        # Imprime os vetores de tempos antes da simulação
        print('\nRelógios lógicos antes da simulação:')
        print_clocks(clocks)

        # Simula o algoritmo de Lamport e atualiza os vetores de tempos
        clocks = lamport_algorithm(
            clocks, src_process - 1, src_time, dest_process - 1, dest_time)

        # Imprime os vetores de tempos após a simulação
        print('\nRelógios lógicos após a simulação:')
        print_clocks(clocks)

        # Pergunta ao usuário se deseja continuar ou sair
        choice = input('\nDeseja fazer outra simulação? (s/n): ').lower()
        # Sai do loop e encerra o programa caso 's'
        if choice != 's':
            print('Saindo do programa...\n')
            break


if __name__ == '__main__':
    main()
