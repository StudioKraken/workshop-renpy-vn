label encerrando:

    scene bg barzinho with dissolve

    show gian at center

    show alex at left

    show nat at right

    with dissolve

    gian "Bom, é isso. Essa foi a nossa workshop sobre criação de jogos narrativos com o Ren'Py."

    nat "Esperamos que tenham gostado e façam muitas Visual Novels!"

    alex "Agora é só estudar, praticar com o Ren'Py e dar vida às suas obras!"

    gian "Muito obrigado pela presença de vocês e ATÉ A PRÓXIMA! <3"

    # Verificando o valor da variável. Se ele for verdadeiro, serão mostradas linhas de diálogo adicionais.
    if usou_magia == True:

        hide gian at center

        hide alex at left

        hide nat at right

        with dissolve

        pause 1

        scene bg cidade with dissolve

        play music synth2

        show gian at center

        show alex at left

        show nat at right

        with dissolve

        alex "Poxa, foi legal o evento, né? Tomara que tenha de novo ano que vem."

        gian "Né? Mas eu ia gostar mais se a gente puder voltar pra casa num passe de mágica, que nem a gente veio."

        gian "Quebra esse galho pra gente, Nat?"

        nat "Hmmm... vou pensar no caso de vocês, hehehe!"

        hide gian at center

        hide alex at left

        hide nat at right

        with dissolve

        scene bg fundo_preto with Pixellate(5, 10)

        jump fimdejogo

    else:

        hide gian at center

        hide alex at left

        hide nat at right

        with dissolve

        scene bg fundo_preto with dissolve

        jump fimdejogo