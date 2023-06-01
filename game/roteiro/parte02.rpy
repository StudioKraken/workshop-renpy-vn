label onibus:

    centered "Alguns minutos de viagem depois..."

    scene bg barzinho with dissolve

    show gian_s at center

    show alex_s at left

    show nat_s at right

    with dissolve

    nat "Beleza, chegamos a tempo."

    jump sesc

label xablau:

    scene bg barzinho with Pixellate(2.5, 10)

    show gian_s at center

    show alex_s at left

    show nat_s at right

    with dissolve

    nat "Pronto. Chegamos!"

    gian "Caramba! E não é que funcionou mesmo?!"

    alex "Eita! Como você fez isso, Nat?!?! Que poder estranho é esse que você tem??"

    nat "Uma dádiva dos ninjas! ;)"

    jump sesc

label sesc:

    gian "E já tá lotado de gente no evento!"

    alex "Né? Tomara que venha mais gente aprender a criar Visual Novels com a gente!"

    nat "Bom, já temos uma galerinha aqui na sala, né?"

    gian "Verdade! Bom, vamos nos preparar e nos apresentar."

    hide gian_s

    hide alex_s

    hide nat_s

    with dissolve

    pause 1.0

    play music synth1

    show gian_s at center with dissolve

    gian "Olá, pessoal! Boas vindas à nossa workshop Ren'Py: criando universos literários interativos!"

    gian "Meu nome é {color=#3C586E}Giancarlo Silva{/color}. Sou diretor técnico, game designer e programador."

    hide gian_s

    show nat_s at center with dissolve

    nat "Prazer, me chamo {color=#360202}Nataly Silva{/color}. Sou game designer, diretora de arte e especialista em usabilidade e experiência de usuário."

    hide nat_s

    show alex_s at center with dissolve

    alex "E eu sou {color=#900000}Alexandre Melo{/color}. Também sou programador, game designer e cuido do controle de qualidade."

    hide alex_s

    with dissolve

    show krakenlogo at imgcenter with dissolve

    gian "Nós três, juntamente com outros valorosos e importantes profissionais, formamos o {color=#9900bb}Studio Kraken{/color}, que desde 2016 vem trabalhando na criação de experiências narrativas lúdicas, cativantes e divertidas."

    hide krakenlogo with dissolve

    show nvdasteam at imgcenter with dissolve
# "#a3ffff"
    nat "Fomos nós quem criamos {color=#a3ffff}NVDA{/color}, nosso primeiro jogo Visual Novel, que foi fruto de um bem-sucedido projeto apoiado pela Lei Aldir Blanc e que está à venda no Steam por apenas {color=#a3ffff}R$ 14,99{/color}."

    hide nvdasteam with dissolve

    show gian_s at center

    show alex_s at left

    show nat_s at right

    with dissolve

    gian "Hoje nós vamos apresentar uma oficina sobre criação de jogos narrativos."

    nat "E pra isso, vamos apresentar uma ferramenta muito bacana chamada Ren'Py, além de ensinar conceitos sobre elaboração de roteiro e arte para Visual Novels."

    alex "E o melhor: vocês vão poder praticar usando esta Visual Novel aqui como exemplo!"

    gian "Então é isso. Vamos começar!"

    hide gian_s

    hide alex_s

    hide nat_s

    with dissolve

    scene bg fundo_preto with dissolve

    centered "Hora do slideshow."

    pause 10.0

    jump encerrando