# Definição dos personagens, com nome, cor do texto do nome e definição de largura e cor de contorno, seguida da definição do sprite de cada personagem.
# - https://www.renpy.org/doc/html/dialogue.html#defining-character-objects

# Gian: nome e cores do nome
define gian = Character(
    "Gian",
    color="#3C586E",
    who_outlines=[ (2, "#fff") ]
)

# Gian: sprite do personagem
image gian_s = "images/personagens/Gian.png"

# Nataly: nome e cores do nome
define nat = Character(
    "Nataly",
    color="#360202",
    who_outlines=[ (2, "#fff") ]
)

# Nataly: sprite da personagem
image nat_s = "images/personagens/Nataly.png"

# Alexandre: nome e cores do nome
define alex = Character(
    "Alexandre",
    color="#f00",
    who_outlines=[ (2, "#222") ]
)

# Alexandre: sprite do personagem
image alex_s = "images/personagens/Alexandre.png"

# Definição dos cenários
# - https://www.renpy.org/doc/html/displaying_images.html#scene-statement
image bg fundo_preto = "#000000"

image bg cidade = "images/cenarios/cidade.png"

image bg barzinho = "images/cenarios/bar.png"

# Definição das músicas e dos efeitos sonoros
# - https://www.renpy.org/doc/html/audio.html#audio
define audio.synth1 = "musica/Shooter_Synthwave_4.mp3"
define audio.synth2 = "musica/Shooter_Synthwave_7.ogg"

define audio.magia = "sfx/magia.mp3"
define audio.onibus = "sfx/onibus.mp3"

# Definição de uma variável com um valor booleano (verdadeiro ou falso)
# - https://www.renpy.org/doc/html/python.html
default usou_magia = False

# Início do ciclo de progressão do jogo: a progressão começará pela label "start" e terminará na label "fimdejogo".
# O comando label permite dar um nome identificável - uma etiqueta - a um trecho do jogo, do qual e para o qual o fluxo de progressão pode fluir.
label start:

    # Use o comando "jump" para permitir que o jogador salte para qualquer label que desejar, alterando o fluxo de progressão.
    # - https://www.renpy.org/doc/html/screen_actions.html#Jump
    jump inicio

# Final do ciclo de progressão do jogo
label fimdejogo:

    # Use o comando centered para exibir texto simples no meio da tela.
    # - https://www.renpy.org/doc/html/dialogue.html#special-characters
    centered "{size=+50}MUITO OBRIGADO!{/size}\n\n{size=+30}studiokraken.com.br{/size}"

    return
