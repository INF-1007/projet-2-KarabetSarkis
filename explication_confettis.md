Dans ma classe Confetti, pour la position horizontale x, j’utilise random.randint(0, largeur_ecran) afin que les confettis apparaissent à différents endroits en haut de l’écran, sur toute la largeur disponible. Pour la position verticale y, j’ai choisi random.randint(0, 30) pour que les confettis ne commencent pas tous exactement sur la même ligne, ce qui évite un effet trop rigide et rend l’apparition plus réaliste.

J’ai aussi utilisé random.randint(4, 10) pour la taille afin que les confettis aient des dimensions différentes. Pour la vitesse, j’ai utilisé random.uniform(3, 5) afin que certains tombent un peu plus vite que d’autres, cela donne une animation moins uniforme.

Pour la couleur, j’ai utilisé random.choice(...) avec une liste de plusieurs couleurs.

La méthode tomber() sert simplement à faire descendre le confetti en augmentant sa position verticale selon sa vitesse. La méthode afficher() utilise pygame.draw.rect(...) parce que l’énoncé demandait des confettis de forme carrée.


Partie main.py

        for vehi in ls_vehicule:
            position_x = vehi.get_position()[0]
            if position_x >= FINISH_LINE_X and gagnant is None:
                gagnant = vehi

        if gagnant is not None:
            txt = font.render(gagnant.celebrer(), True, (0, 0, 0))
            screen.blit(txt, (350, 35))
            
            for i in range(2):
                confettis.append(Confetti(screen.get_width()))
                
            for confetti in confettis:
                confetti.tomber()
                confetti.afficher(screen) 

Dans cette partie du code, je parcours d’abord la liste des véhicules avec une boucle for vehi in ls_vehicule. Pour chaque véhicule, je récupère sa position en x avec vehi.get_position()[0]. J’utilise l’indice [0] parce que la position est stockée sous forme de coordonnées, donc la première valeur correspond à l’axe horizontal. Cela me permet de vérifier si le véhicule a franchi la ligne d’arrivée. Ensuite, j’utilise la condition if position_x >= FINISH_LINE_X and gagnant is None: pour détecter le premier véhicule qui atteint ou dépasse la ligne d’arrivée. J’ai ajouté gagnant is None pour m’assurer que le gagnant n’est enregistré qu’une seule fois. Ainsi, dès qu’un premier véhicule gagne, il est sauvegardé dans la variable gagnant avec gagnant = vehi, et les autres véhicules ne peuvent plus remplacer ce gagnant. Après cela, j’utilise if gagnant is not None: pour vérifier qu’un gagnant a bien été trouvé. Si c’est le cas, j’affiche le message de victoire avec font.render(gagnant.celebrer(), True, (0, 0, 0)). J’ai choisi cette méthode parce qu’elle permet d’afficher à l’écran le texte retourné par la méthode celebrer() du véhicule gagnant.
Ensuite, j’ajoute des confettis avec for i in range(2): confettis.append(Confetti(screen.get_width())). J’ai choisi d’en créer un petit nombre à chaque image pour donner un effet continu, au lieu de créer tous les confettis en une seule fois. Cela rend l’animation plus naturelle. Enfin, avec for confetti in confettis:, je parcours tous les confettis déjà créés. La méthode tomber() sert à mettre à jour leur position verticale pour les faire descendre, tandis que afficher(screen) sert à les mettre à l’écran