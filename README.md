# Simulador de Relógios Lógicos de Lamport (_Lamport Clock Simulator_)

Este é um simulador em Python que implementa o **algoritmo de Lamport para relógios lógicos**. O programa permite que você defina o número de processos e gere vetores de tempos para cada processo, com incrementos aleatórios. Você também pode simular eventos entre processos, onde os tempos são atualizados de acordo com as regras do algoritmo de Lamport.

Programa desenvolvido como atividade da disciplina de Sistemas Distribuídos II no semestre 2023/2 do IFSul.

## Como Utilizar

1. Insira o **número de processos** que deseja simular.

> Será gerado um vetor de tempos para cada processo com incrementos aleatórios.

2. Insira o número do **processo de origem** e o **tempo de origem** para o evento.

3. Insira o número do **processo de destino** e o **tempo de destino** para o evento.

> **Obs.:** ao informar o tempo de origem/destino, deve-se informar o seu **índice** no vetor do processo

4. Após a simulação, informe se deseja ou não realizar outra (s/n).

## Notas

- O programa utiliza a biblioteca ``random`` para gerar incrementos aleatórios nos vetores de tempos.

- O algoritmo de Lamport atualiza os tempos de acordo com as regras do algoritmo, garantindo que o tempo de destino seja maior que o tempo de origem.

- Caso o tempo de destino seja menor que o tempo de origem, o algoritmo de Lamport irá ajustar todo o vetor de tempos do processo de destino mantendo a frequência original.

- Certifique-se de seguir as instruções no terminal para inserir valores válidos para os processos e tempos conforme o exemplo a seguir.

## Exemplo de Uso

```
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                  > Simulador de Relógios Lógicos de Lamport  <                  *
*                                                                                 *
*                        Desenvolvido por Camila Barcellos                        *
*                        Sistemas Distribuídos II - 2023/2                        *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Número de processos: 3

Relógios lógicos:
P       t0      t1      t2      t3      t4      t5      t6      t7      t8      t9
----------------------------------------------------------------------------------
P1      0       1       2       3       4       5       6       7       8       9
P2      0       3       6       9       12      15      18      21      24      27
P3      0       8       16      24      32      40      48      56      64      72

Processo de origem: 3
Tempo de origem: 2
Processo de destino: 1
Tempo de destino: 4

Relógios lógicos antes da simulação:
P       t0      t1      t2      t3      t4      t5      t6      t7      t8      t9
----------------------------------------------------------------------------------
P1      0       1       2       3       4       5       6       7       8       9
P2      0       3       6       9       12      15      18      21      24      27
P3      0       8       16      24      32      40      48      56      64      72

EVENTO P3(16) → P1(4)
  Emissor: P[2][2] = 16
  Receptor: P[0][4] = 4

Relógios lógicos após a simulação:
P       t0      t1      t2      t3      t4      t5      t6      t7      t8      t9
----------------------------------------------------------------------------------
P1      0       1       2       3       17      18      19      20      21      22
P2      0       3       6       9       12      15      18      21      24      27
P3      0       8       16      24      32      40      48      56      64      72
```

_© [Camila Barcellos](https://github.com/camilafbarcellos) 2023 - IFSul_