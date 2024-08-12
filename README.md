# Projeto-1---Sistemas-Operacionais---MATA58

# Jogo de Competição

## Descrição

O jogo competição foi pensado para ser entre dois jogadores. Cada jogador tenta capturar sistemas operacionais que caem da tela para ganhar pontos. O jogo termina quando o tempo acaba, e o jogador com mais pontos vence.

## Como Jogar

### Controles

- **Jogador 1**:
  - **Mover para a esquerda**: Tecla `←` (seta para a esquerda)
  - **Mover para a direita**: Tecla `→` (seta para a direita)

- **Jogador 2**:
  - **Mover para a esquerda**: Tecla `A`
  - **Mover para a direita**: Tecla `D`

### Objetivo

- **Capturar Sistemas Operacionais**:
  - **Linux**: Ao capturar o Linux, o jogador ganha um ponto.
  - **Windows**: Ao capturar o Windows, o jogador perde um ponto.

### Vencedor

- O jogo termina quando o tempo chega a zero.
- O jogador com mais pontos ao final do tempo vence. Se os pontos forem iguais, o resultado é um empate.

## Instruções para Iniciar

1. **Primeiro se certifique de que o Python e o Pygame Zero estão instalados.**
2. **Coloque as imagens e sons necessários na pasta de recursos do projeto.**
3. **Execute o jogo com o seguinte comando:**
   ```bash
   pgzrun main.py
