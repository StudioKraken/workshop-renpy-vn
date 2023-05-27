# Definição dos personagens, com nome, cor do texto do nome e definição de largura e cor de contorno.
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

image bg fundo_preto = "#000000"

image bg cidade = "images/cenarios/cidade.png"

image bg barzinho = "images/cenarios/bar.png"

# Definição das músicas e dos efeitos sonoros

# Definição de uma variável com um valor booleano (verdadeiro ou falso)

default usou_magia = False

label start:

    scene black

    jump inicio

label fimdejogo:

    centered "{size=+30}OBRIGADO!{/size}\n\nstudiokraken.com.br"

    return
