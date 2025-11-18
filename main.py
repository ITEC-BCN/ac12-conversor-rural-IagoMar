@namespace
class SpriteKind:
    arbol = SpriteKind.create()
    teleport = SpriteKind.create()
    comercial = SpriteKind.create()


def partePrincipal():
    global personajePrincipal, fons_bosc
    personajePrincipal = sprites.create(img("""
            . . . . . . . c c c . . . . . .
            . . . . . . c b 5 c . . . . . .
            . . . . c c c 5 5 c c c . . . .
            . . c c b c 5 5 5 5 c c c c . .
            . c b b 5 b 5 5 5 5 b 5 b b c .
            . c b 5 5 b b 5 5 b b 5 5 b c .
            . . f 5 5 5 b b b b 5 5 5 c . .
            . . f f 5 5 5 5 5 5 5 5 f f . .
            . . f f f b f e e f b f f f . .
            . . f f f 1 f b b f 1 f f f . .
            . . . f f b b b b b b f f . . .
            . . . e e f e e e e f e e . . .
            . . e b c b 5 b b 5 b f b e . .
            . . e e f 5 5 5 5 5 5 f e e . .
            . . . . c b 5 5 5 5 b c . . . .
            . . . . . f f f f f f . . . . .
            """),
        SpriteKind.player)
    controller.move_sprite(personajePrincipal)
    personajePrincipal.set_stay_in_screen(False)
    scene.camera_follow_sprite(personajePrincipal)
    sprites.create(img("""
            ....................e2e33e2e....................
            .................222eee33e2e222.................
            ..............222e22e2e33eee22e222..............
            ...........e22e22eeee2e33e2eeee22e22e...........
            ........eeee22e22e33e2e33e2e33e22e22eeee........
            .....222e22e22eeee33e2e33e2e33eeee22e22e222.....
            ...22eeee22e22e33e33eee33eee33e33e22e22eeee22...
            4cc22e33e22eeee33e33e3e33e3e33e33eeee22e22e22cc4
            6c6eee33e22e33e33e33e3e33e3e33e33e33e22e22eee6c6
            46633e33eeee33e33eeee3e33e3eeee33e33eeee22e33664
            46633e33e33e33eeee33e3e33e3e33eeee33e33e22e33664
            4cc33eeee33e33e33e33eee33eee33e33e33e33eeee33cc4
            6c633e33e33eeee33e33e3e33e3e33e33eeee33e33e336c6
            466eee33e33e33e33e33e3e33e3e33e33e33e33e33eee664
            46633e33eeee33e33e33e3e33e3e33e33e33eeee33e33664
            4cc33e33e33e33e33eeee3e33e3eeee33e33e33e33e33cc4
            6c633eeee33e33eeee22eee33eee22eeee33e33eeee336c6
            46633e33e33eeee22e22e2e33e2e22e22eeee33e33e33664
            466eee33e33e22e22e22e2e33e2e22e22e22e33e33eee664
            4cc33e33eeee22e22e22e2e33e2e22e22e22eeee33e33cc4
            6c633e33e22e22e22e22eee33eee22e22e22e22e33e336c6
            46633eeee22e22e22eeecc6666cceee22e22e22eeee33664
            46633e33e22e22eeecc6666666666cceee22e22e22e33664
            4cceee33e22eeecc66666cccccc66666cceee22e22eeecc4
            6c633e33eeecc66666cc64444446cc66666cceee22e336c6
            46633e33cc66666cc64444444444446cc66666cc22e33664
            46633cc6666ccc64444444444444444446ccc6666cc33664
            4ccc6666ccc6444bcc666666666666ccb4446ccc6666ccc4
            cccccccc6666666cb44444444444444bc6666666cccccccc
            64444444444446c444444444444444444c64444444444446
            66cb444444444cb411111111111111114bc444444444bc66
            666cccccccccccd166666666666666661dccccccccccc666
            6666444444444c116eeeeeeeeeeeeee611c4444444446666
            666e2222222e4c16e4e44e44e44e44ee61c4e2222222e666
            666eeeeeeeee4c16e4e44e44e44e44ee61c4eeeeeeeee666
            666eddddddde4c66f4e4effffffe44ee66c4eddddddde666
            666edffdffde4c66f4effffffffff4ee66c4edffdffde666
            666edccdccde4c66f4effffffffffeee66c4edccdccde666
            666eddddddde4c66f4eeeeeeeeeeeeee66c4eddddddde666
            c66edffdffde4c66e4e44e44e44e44ee66c4edffdffde66c
            c66edccdccde4c66e4e44e44e44e44ee66c4edccdccde66c
            cc66666666664c66e4e44e44e44feeee66c46666666666cc
            .c66444444444c66e4e44e44e44ffffe66c44444444466c.
            ..c64eee4eee4c66f4e44e44e44f44fe66c4eee4eee46c..
            ...c4eee4eee4c66f4e44e44e44effee66c4eee4eee4c...
            ....644444444c66f4e44e44e44e44ee66c444444446....
            .....64eee444c66f4e44e44e44e44ee66c444eee46.....
            ......6ccc666c66e4e44e44e44e44ee66c666ccc6......
            """),
        SpriteKind.teleport).set_position(-20, -20)
    info.set_score(0)
    fons_bosc = image.create(160, 120)
    fons_bosc.fill(7)
    scene.set_background_image(fons_bosc)
    for i in range(21):
        # filas
        for j in range(21):
            # columnas
            x = 20 + j * 30
            y = 20 + i * 50
            sprites.create(assets.image("""
                arbol
                """), SpriteKind.arbol).set_position(x, y)
def gestionar_mercat():
    # Bucle del menú principal
    while True:
        game.show_long_text("" + "LLISTA DE PREUS:\n" + """
                1. Gallina (6kg llenya)
                """ + """
                2. Patata (Variable)
                """ + """
                3. Cabra (5kg llenya)
                """ + """
                4. Ous (3kg/dotzena)
                """ + """
                5. Cavall (12kg llenya)
                """ + "6. Sortir\n" + "(Prem A per triar)",
            DialogLayout.FULL)
        opcio = game.ask_for_number("Escriu el número de l'opció:", 1)
        if opcio == 6:
            game.show_long_text("Adéu! ", DialogLayout.BOTTOM)
            break
        if opcio < 1 or opcio > 6:
            game.show_long_text("Opció no vàlida. No venem targetes RTX 5090 jejeje",
                DialogLayout.BOTTOM)
            continue
        quantitat = game.ask_for_number("Quantes unitats")
        # 1. Control de negatius
        if quantitat < 0:
            game.show_long_text("El numero ha de ser positiu",
                DialogLayout.BOTTOM)
            continue
        # 2. Control de zero
        if quantitat == 0:
            game.show_long_text("adeu",
                DialogLayout.BOTTOM)
            continue
        # 3. Control d'animals sencers (Gallina, Cabra, Cavall, Ous)
        # Si la quantitat té decimals (ex: 1.5), el residu de dividir per 1 no és 0.
        if (opcio == 1 or opcio == 3 or opcio == 5 or opcio == 4) and quantitat % 1 != 0:
            game.show_long_text("ERROR CRÍTIC: nomes venem animals sencers",
                DialogLayout.BOTTOM)
            continue
        # --- CÀLCUL DE LA LLENYA ---
        quilograms_llenya = 0
        producte_nom = ""
        if opcio == 1:
            # Gallina
            # 1 Gallina = 6 kg
            quilograms_llenya = quantitat * 6
            producte_nom = "Gallines"
        elif opcio == 2:
            # Patata
            # 2 kg llenya = 1.5 kg patata -> 1 kg patata = 2/1.5 kg llenya
            # Ràtio: 1.3333...
            ratio = 2 / 1.5
            quilograms_llenya = quantitat * ratio
            producte_nom = "Kg de Patata"
        elif opcio == 3:
            # Cabra
            # 1 Cabra = 5 kg
            quilograms_llenya = quantitat * 5
            producte_nom = "Cabres"
        elif opcio == 4:
         
            quilograms_llenya = quantitat * 0.25
            producte_nom = "Ous"
        elif opcio == 5:
            
            quilograms_llenya = quantitat * 12
            producte_nom = "Cavalls"
       
        resultat_final = Math.round(quilograms_llenya * 100) / 100
      
        game.show_long_text("Per " + ("" + str(quantitat)) + " " + producte_nom + "\nNecessites: " + ("" + str(resultat_final)) + " Kg de llenya de pi.",
            DialogLayout.BOTTOM)


def on_on_overlap(sprite, otherSprite):
   
    zonaComercial.say_text("A: Mercat", 100, False)
    
    if controller.A.is_pressed():
        gestionar_mercat()
sprites.on_overlap(SpriteKind.player, SpriteKind.comercial, on_on_overlap)



def on_on_overlap2(sprite2, otherSprite2):
    global zonaComercial
    personajePrincipal.say_text("A: Entrar", 100, False)
    if controller.A.is_pressed():
      
        scene.set_background_image(img("""
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444e444e4444444eeeeeeeeeeeeee4beeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444e444e4444444eeeeeeeee444444beeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444e444e4444444eeeeeeeee444444beeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444e444e4444444eeeeeeeee444444beeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444e444e4444444eeeeeeeeee44444beeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444e444e4444444eeeeeeeeeeeeeeebeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444e444e4444444eeeeeeeeee44444beeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444e444e4444444eeeeeeeeee44444beeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444e444e4444444eeeeeeeeee44444beeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444e444e4444444eeeeeeeeee44444beeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444e444e4444444eeeeeeeeeeeeeeebeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444e444e4444444eeeeeeeeeeeeeeebeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444e444e4444444eeeeeeeeeeeeeeebeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444e444e4444444eeeeeeeeeeeeeeebeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444e444e4444444eeeeeeeeeeeeeebbeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeceeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeee44ee444eeeeeeeeeeeeeebbeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeee44ebbeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeee44cdbceeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeee4ebbbcceeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444e44444444444444eeeeeeeeebbbbbbeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444e44444444444444eeeeeeeeedddddddeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeee4ddddddd4eeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeeedddddddd4eeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeeedddddddddeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeeddddddddd4eeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444e444e444e444eeeeeeeeee44444444444eeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444e444e444e444eeeeeeeee4444d44d4444eeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444e444e444e444eeeeeeeee444444444444eeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444e444e444e444eeeeeeeeeeeeeeeeee444eeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444e4eee444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            999999999beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            999999999beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            999999999beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            999999999beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            999999999beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            999999999beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            999999999beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeef4444444444444444444444444444444444444444444444444eeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            999999999beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeec444444444444444444444444e444444444444444444444444eeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            999999999beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeec4444eeeeeeeeeeeeeeeee444e444eeeeeeeeeeeeeeeeee444eeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            999999999beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeec4e444eeeeeeeeeeeeeeee444e4444eeeeeeeeeeeeeeee4444eeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            999999999beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee444444444444e444eeeeeeeeeeeeeee4444e4e444eeeeeeeeeeeeee44444eeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            999999999beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeec4ee444eeeeeeeeeeeee444e4e4ee444eeeeeeeeeeeee444e4eeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            999999999beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeec4eee444eeeeeeeeeee444ee4e4ee444eeeeeeeeeeee444ee4eeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            999999999beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeec4eeee444eeeeeeeeee444ee4e4eee444eeeeeeeeee444eee4e4444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            999999999beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeec4eeee444eeeeeeeee444eee4e4eeee444eeeeeeee444eeee4eeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            999999999beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeec4eeeee444eeeeeee444eeee4e4eeeee444eeeeeee444eeee4eeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeb999999999999999999..
            999999999beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeec4eeeeee444eeeee444eeeee4e4eeeee444eeeeee444eeeee4eeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeb999999999999999999..
            999999999beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeec4eeeeeee444eeee444eeeee4e4eeeeee444eeee444eeeeee4eeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeb999999999999999999..
            999999999beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeec4eeeeeee444eee444eeeeee4e4eeeeeee444ee444eeeeeee4eeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeb999999999999999999..
            999999999beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeec4eeeeeeee444e444eeeeeee4e4eeeeeeee444e44eeeeeeee4eeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeb999999999999999999..
            999999dcfceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeec4eeeeeeeec444e4eeeeeeee4e4eeeeeeee444e44eeeeeeee4eeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeb999999999999999999..
            9bcfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeec4eeeeeeeeee444eeeeeeeee4e4eeeeeeeee444eeeeeeeeee4eeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeb999999999999999999..
            beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeec4eeeeeeeeeee444eeeeeeee4e4eeeeeeeeee444eeeeeeeee4eeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeb999999999999999999..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeec4eeeeeeeee4e444eeeeeeee4e4eeeeeeee44e444eeeeeeee4eeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeb999999999999999999..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeec4eeeeeeee444e444eeeeeee4e4eeeeeeee44ee444eeeeeee4eeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeb999999999999999999..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeeec4eeeeeee444eee444eeeeee4e4eeeeeee444ee444eeeeeee4eeeeee44444eeeeeeeeeeeeeeeeeeeeeeeeeb999999999999999999..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeecc4eeeeeee444eeee444eeeee4e4eeeeee444eeee444eeeeee4eeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeb999999999999999999..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeecc4eeeeee444eeeee444eeeee4e4eeeee444eeeeee444eeeee4eeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeb999999999999999999..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44e4eeeeecc4eeeec444eeeeeec444eeee4e4eeeee444eeeeeee444eeee4eeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeb999999999999999999..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44e44eeeecc4eeec444eeeeeeeee444cee4e4eeee444eeeeeeee444eeee4eeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeb999999999999999999..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44e44eeeecc4eeee444eeeeeeeeee444ee4e4eec444eeeeeeeeec444eee4eeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeb999999999999999999..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44e444444444eee444eeeeeeeeeee4444e4e4ec444eeeeeeeeeeee444ce444444444444eeeeeeeeeeeeeeeeeeeeeeeeeb999999999999999999..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444eeeecc4ef444eeeeeeeeeeeec444e4e4e444eeeeeeeeeeeeee444e4eeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeb999999999999999999..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44eeeeecc4c444eeeeeeeeeeeeeec4444e4e444eeeeeeeeeeeeee444e4eeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeb999999999999999999..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444eeeeecc4e444eeeeeeeeeeeeeeee444e4444eeeeeeeeeeeeeeec44e4eeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444444e4eeeeecc4444ceeeeeeeeeeeeeeeee44e444eeeeeeeeeeeeeeeeec4e4eeeeeee4444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444444444444444eeeeecc444444444444444444444444e444444444444444444444444eeeeeee444444444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeeeeee4444444444444bec4444eeccccc444444444444444444444444e444444444444444444444444cccccce4444eeb4444444444444eeeeeeeeeeeeeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeeeeeeeeee44444444444bc44cccc4444eecccccccccccccccccccccccccccccccccccccccccccccccccccccccccccce4444eccc4bcb444444444444eeeeeeeeeeeeeeeeeeeeeeee..
            eeeeeeeeeeeeeeeeee44444444444444cccccc44cccc444eeeccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccb4444eccc4bccccce44444444444444eeeeeeeeeeeeeeeeee..
            eeeeeeeeeeee444444444444444cccb4eccccc44cccc444eeeccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccb4444eccc44cccccc44ccce44444444444444eeeeeeeeeeee..
            eeeeeee44444444444444e44ecccccb4eccccc44cccc444eeeccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccb4444eccc44cccccc44ccccce4ee44444444444444eeeeeee..
            ee44444444444444eccccc44ecccccb4cccccc44eccc44e4eeccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccb4444eccc44cccccc44ccccce4eccccce44444444444444ee..
            44444444444eccb4eccccc44ecccccb4cccccc44eccc4444eeccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccb4444eccc44cccccc44ccccce4eccccce44cce44444444444..
            44444becccccccb4eccccc44ecccccb4cccccc44eccc4444eeccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccb4444eccc4bcccccc44ccccce4eccccce44cccccce4b44444..
            bcc44eccccccccb4eccccc44ecccccb4cccccc44eccc4444eeccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccb4444ecce4bcccccc44ccccce4eccccce44cccccce4cccccb..
            ccc44eccccccccb4eccccc44ecccccb4cccccc44eccc4444eeccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccb4444ecce4bcccccc44ccccce4eccccce4ecccccce4cccccc..
            ccc44eccccccccb4eccccc44ecccccb4cccccb44eccc4444eeccccccccccccccccccccccccccccccccccccccccccccccccbcccccccccccb4444ecce4bcccccc44ccccce4eccccce4ecccccce4cccccc..
            ccc44eccccccccb4eccccc44ecccccb4cccccc44eccc4444eeccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccb4444ebce4bcccccc4bccccce4eccccce4ecccccce4cccccc..
            ccc44eccccccccb4eccccc44ecccccb4cccccc44eccc4444eeccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccb4444ebce4bccccbc4bccccce4eccccce4ecccccce4cccccc..
            ccc44eccccccccb4eccccc44ecccccb4cccccc44eccc4444eeccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccb4444ebce4bcccccc4bccccce4bccccce4ecccccce4cccccc..
            ccc44eccccccccb4eccccce4ecccccb4cccccc44eceeee44eebbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb44eeeece4bcccccc4bccccce4eccccce4ecccccce4cccccc..
            ccc44eccccccccb4ebcccce4ecccccb4cccccc44eee444e4eebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb44444eee4bbccccc4bccccce4eccccce4ecccccce4cccccc..
            ccc44eccccccccb4ebcccce4ecccccb4bbbbeee444444444eebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb444444444eeebbbb4bccccce4eccccce4bcccccc44cccccc..
            ccc44eccccccccb4ebcccce4ebbbbbb4eeee444444444444eebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbbbbbbbbbbbbbbb444444444444eeee4bbbbbbe4eccccce4bcccccc44cccccc..
            ccc44eccccccccb4ebbbbbb4ebbbbe44e444444444bb4444eebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb4444eb444444444e4eebbbbe4bbbccce4bcccccc44cccccc..
            ccc44ecccccccbb4ebbbbbe4ebeee444e444444bbbbc4444eebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcb4444ebbbb444444e444eeebe4bbbbbbe4bbccccce4cccccc....
            ccc44ecccbbbbbb4ebbbbbe4eee44444444bbbbbbbcc44444ebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcce4444ecbbbbbbb44444444eee4ebbbbbe4bbbbcbce4cccccc..
            ccc44ebbbbcbbbb4ebbeeee4e444444bbbbbbbbbbbbccceeccbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbccceeecbbbbbbbbbbb4444444e4eeeebbe4bbbbbbbe4cccccc..
            cbb44ebbbbbbbbb4eee444444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb444444444eee4bbbbbbbe4bbbbcc..
            bbb44ebbbbbbeee4e44444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb44444444e4eeebbbbe4bbbbbb..
            bbb44ebbbeee444444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb44444444eeeebe4cbbbbb..
            bbb44eeee444444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb444444444ee4bbbbbb..
            bbe44e444444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb4444444e44eeebb..
            ee444e444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb4444444444ee..
            44444444bbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb44444444..
            4444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb4444
            4bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb4..
            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb....
            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbb..
            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb..
            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb....
            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb....
            bbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb..
            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb....
            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb....
            bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb....
            """))
        scene.center_camera_at(0, 0)
        sprites.destroy_all_sprites_of_kind(SpriteKind.teleport)
        sprites.destroy_all_sprites_of_kind(SpriteKind.arbol)
     
        zonaComercial = sprites.create(img("""
                .......ffffffffffffffffff.......
                ......ffeeeeeeeeeeeeeeeeff......
                .....ffeeeeeeeeeeeeeeeeeeff.....
                ....ffeeeeeeeeeeeeeeeeeeeeff....
                ...ffeeeeeeeeeeeeeeeeeeeeeeff...
                ..ffeeeeeeeeeeeeeeeeeeeeeeeeff..
                .ffeeeeeeeeeeeeeeeeeeeeeeeeeeff.
                .feeeeeeeeeeeeeeeeeeeeeeeeeeeef.
                .f2e2eee2e22e2eeee2e22e2eee2e2f.
                .f2ee222ef22ee2222ee22fe222ee2f.
                .f22eeeeffe22eeeeee22effeeee22f.
                .ff222fffefe22222222efefff222ff.
                ..fffeeeeeffe222222effeeeeefff..
                ..feeee22e2fffeeeefff2e22eeeef..
                ..feeee22e2fffeeeefff2e22eeeef..
                ..f22e22e2effeeeeeeffe2e22e22e..
                .e22e22e22fffeeeeeefff22e22e22e.
                .eee22222fffeeeeeeeefff22222eee.
                .e22222effffeeeeeeeeffffe22222e.
                ..ffeffffffeeeeeeeeeeffffffeff..
                ..f2eefffffeeeeeeeeeefffffee2f..
                ..f222ffffeeeeeeeeeeeeffff222f..
                .eeeeeffffbbbddddddbbbffffeeeee.
                .e22222ffbbddddddddddbbff22222e.
                ee22222efbddddddddddddbfe22222ee
                e22e2e22ebbddddddddddbbe22e2e22e
                eeeeeeeebbbbbddddddbbbbbeeeeeeee
                cbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbc
                cbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbc
                cccccccccccccccccccccccccccccccc
                .cccccccccccccccccccccccccccccc.
                ..cccccccccccccccccccccccccccc..
                """),
            SpriteKind.comercial)
        
        zonaComercial.set_position(personajePrincipal.x + 30, personajePrincipal.y)
sprites.on_overlap(SpriteKind.player, SpriteKind.teleport, on_on_overlap2)

zonaComercial: Sprite = None
fons_bosc: Image = None
personajePrincipal: Sprite = None
# Execució inicial
partePrincipal()