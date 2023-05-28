# Definição dos personagens, com nome, cor do texto do nome e definição de largura e cor de contorno.
# - https://www.renpy.org/doc/html/dialogue.html#defining-character-objects
define gian = Character(
    "Gian",
    color="#f00",
    who_outlines=[ (2, "#222") ],
    what_outlines=[ (2, "#222") ]
)

define nat = Character(
    "Nataly",
    color="#0f0",
    who_outlines=[ (2, "#222") ],
    what_outlines=[ (2, "#222") ]
)

define alex = Character(
    "Alexandre",
    color="#0ff",
    who_outlines=[ (2, "#222") ],
    what_outlines=[ (2, "#222") ]
)

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

# Início do ciclo de progressão do jogo
# O comando label permite dar um nome identificável - uma etiqueta - a um trecho do jogo, do qual e para o qual o fluxo de progressão pode fluir.
label start:

    scene black

    # Use o comando jump para permitir que o jogador salte para qualquer label que desejar, alterando o fluxo de progressão.
    jump inicio

# Final do ciclo de progressão do jogo
label fimdejogo:

    # Use o comando centered para exibir texto simples no meio da tela.
    centered "{size=+30}OBRIGADO!{/size}\n\nstudiokraken.com.br"

    return
