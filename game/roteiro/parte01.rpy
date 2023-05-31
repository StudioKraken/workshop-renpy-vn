label inicio:
    # Para tocar uma música de fundo, use o comando "play music" seguido do nome que você definiu para a música lá no arquivo script.rpy.
    # Caso prefira, também pode chamar o arquivo de música diretamente: play music "arquivo.mp3".
    play music synth2

    # Recomenda-se usar os comandos "scene bg" para exibir cenários e "show" para exibir personagens. O comando "hide" serve para esconder tanto cenários quanto personagens.
    scene bg fundo_preto

    # Comando de pausa, seguido do tempo de pausa, em segundos.
    pause 1

    # Usa-se o comando "scene bg nome-do-cenario" para fazer aparecer o cenário desejado no jogo. Acrescenta-se o efeito de suavização a partir do preto com o comando "with dissolve"
    # - https://www.renpy.org/doc/html/transitions.html
    scene bg cidade with dissolve

    # Mostrando um personagem no centro da tela com o comando "show nome-do-personagem"
    show gian_s at center with dissolve

    gian "Caramba... o evento lá no SESC já vai começar e a gente ainda tá aqui na parada esperando o busão."

    gian "Vai ser um evento muito massa. Não quero perder de jeito nenhum!"

    # Mostrando um personagem à esquerda da tela
    show alex_s at left with dissolve

    alex "Fora que fomos convidados, né? Vai ficar feio a gente chegar atrasado."

    # Mostrando um personagem à direita da tela
    show nat_s at right with dissolve

    nat "Verdade. A não ser que..."

    # Menus de escolhas como este permitem dar rumos diferentes à história de um jogo.
    menu:
        alex "Será que a gente vai chegar a tempo?"

        "Nataly: Tive uma ideia! A gente vai chegar lá num passe de mágica.":
            # Se esta opção de escolha for selecionada no menu, a variável "usou_magia" receberá um valor verdadeiro (True). Em seguida, o fluxo saltará para o trecho do jogo com a label "magica"
            $ usou_magia = True
            jump magica

        "Nataly: Opa! O ônibus tá chegando!":
            # Se esta opção de escolha for selecionada no menu, o fluxo saltará para o trecho do jogo com a label "busao"
            jump busao

label magica:

    nat "Ah, relaxa! A gente vai chegar lá num passe de mágica."

    alex "Como assim, Nat?!"

    gian "É, que história é essa de \"num passe de mágica\"?"

    nat "Só segurem na minha mão e confiem."

    nat "XABLAU!"

    # Para tocar um efeito sonoro, use o comando "play sound" seguido do nome que você definiu para o efeito lá no arquivo script.rpy.
    # Caso prefira, também pode chamar o arquivo de efeito sonoro diretamente: play sound "arquivo.mp3".
    play sound magia

    alex "AAAAHHHHHH!!"

    gian "AAAAHHHHHH!!"

    # Para esconder os personagens antes de mudar de cenário, use o comando "hide".
    hide gian

    hide alex

    hide nat

    # defina o efeito "dissolve" em uma linha separada logo após os três "hides" acima para fazer os personagens sumirem suavemente, todos ao mesmo tempo.
    with dissolve

    # Use este comando para parar uma música que esteja sendo tocada.
    stop music

    # O comando "hide" pode ser acompanhado do efeito Pixellate. O primeiro número é o tempo, em segundos. O segundo é a intensidade da pixelização.
    scene bg fundo_preto with Pixellate(3.5, 10)

    jump xablau

label busao:

    nat "Opa! O ônibus tá chegando! Prestem atenção, meninos!"

    alex "Hehe, foi só você falar hein, Gian!"

    gian "Ainda bem que demos sorte. Valeu por avisar, Nat."

    gian "Bom, vamos nessa!"

    hide gian

    hide alex

    hide nat

    with dissolve

    stop music

    play sound onibus

    scene bg fundo_preto with dissolve

    jump onibus