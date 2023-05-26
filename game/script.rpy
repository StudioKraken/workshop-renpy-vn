# Definição dos personagens
define gian = Character(
    "Gian",
    color="#fff",
    who_outlines=[ (2, "#222") ],
    what_outlines=[ (2, "#222") ]
)

define nat = Character(
    "Nataly",
    color="#fff",
    who_outlines=[ (2, "#222") ],
    what_outlines=[ (2, "#222") ]
)

define alex = Character(
    "Alexandre",
    color="#fff",
    who_outlines=[ (2, "#222") ],
    what_outlines=[ (2, "#222") ]
)

# Definição dos cenários

image bg fundo_preto = "#000000"

image bg cidade = "images/cenarios/cidade.png"

image bg barzinho = "images/cenarios/bar.png"

# Definição das músicas e dos efeitos sonoros

label start:

    jump inicio

label fimdejogo:

    return
