label inicio:
    # Recomenda-se usar os comandos "scene bg" para exibir cenários e "show" para exibir personagens. O comando "hide" serve para esconder tanto cenários quanto personagens.

    # Usa-se o comando "scene bg nome-do-cenario" para fazer aparecer o cenário desejado no jogo. Acrescenta-se o efeito de suavização a partir do preto com o comando "with dissolve"
    scene bg fundo_preto with dissolve

    scene bg cidade with dissolve

    # Mostrando um personagem no centro da tela com o comando "show nome-do-personagem"
    show gian at center

    # Esta é uma linha de diálogo. Você define quem vai falar e o que será falado escrevendo o nome do personagem, seguido da fala entre aspas.
    gian "Olá! Meu nome é Giancarlo."

    # Mostrando um personagem à esquerda da tela
    show alex at left

    # Esta é outra linha de diálogo. Para mudar o personagem que está falando, basta chamar um personagem diferente e escrever sua fala em seguida, sempre entre aspas.
    alex "E eu sou Alexandre."

    # Mostrando um personagem à direita da tela
    show nat at right

    nat "Prazer, Nataly."

    gian "Hoje nós vamos apresentar uma workshop sobre criação de jogos narrativos lá no SESC Rio Branco."

    nat "E pra isso, vamos apresentar uma ferramenta muito bacana chamada Ren'Py!"

    alex "E o melhor: vocês vão poder praticar usando esta Visual Novel aqui como exemplo!!"

    gian "Bom... o evento já vai começar e a gente ainda tá aqui na parada esperando o busão."

    # Menus de escolhas como este permitem dar rumos diferentes à história de um jogo.
    menu:
        alex "Pois é... será que a gente vai chegar a tempo?"

        "Ah, relaxa! A gente vai chegar lá num passe de mágica.":
            jump magica

        "Opa! O ônibus tá chegando!":
            jump busao

label magica:

    nat "Ah, relaxa! A gente vai chegar lá num passe de mágica."

    alex "Como assim, Nat?!"

    nat "Só segurem na minha mão e confiem."

    nat "XABLAU!"

    # Para esconder os personagens antes de mudar de cenário, use o comando "hide".
    hide gian

    hide alex

    hide nat

    with dissolve

    # O comando "hide" pode ser acompanhado do efeito Pixellate. O primeiro número é o tempo, em segundos. O segundo é a intensidade da pixelização.
    hide bg cidade with pixellate

    jump xablau

label busao:

    nat "Opa! O ônibus tá chegando!"

    alex "Hehe, foi só você falar hein, Gian!"

    gian "Ainda bem que demos sorte, hehe! Bom, vamos nessa!"

    hide gian

    hide alex

    hide nat

    with dissolve

    hide bg cidade with dissolve

    jump onibus