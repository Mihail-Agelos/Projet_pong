# game.py

import pygame
import sys
import functions

# Couleurs RVB
NOIR = (152, 151, 153)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
CYAN = (0, 255, 255)

# Taille de la fenêtre
LARGEUR = 900
HAUTEUR = 600

# Initialisation de Pygame
pygame.init()
pygame.mixer.init()  # Initialize Pygame mixer
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption('Ping Pong')
bg = pygame.image.load("Background3.jpg")
main_menu = pygame.image.load("new_game.jpg")

# Load fonts
font_mm, font_mm2 = functions.load_fonts()

# Create objects
raquette_joueur = functions.Raquette(HAUTEUR - 30, LARGEUR // 2)
balle = functions.Balle(LARGEUR // 2, HAUTEUR // 2)

# Main game loop
en_cours = False
score = 0
H_score = 0
mm = True
game_end = False

while mm:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mm = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mm = False
                en_cours = True

    # Vérifier la collision avec la raquette
    if pygame.Rect.colliderect(balle.afficher(fenetre), raquette_joueur.rect_raquette):
        pygame.mixer.music.load('Colision_Sound.mp3')
        pygame.mixer.music.play()  # Play the sound
        balle.y_direction = -balle.y_direction

    # Mettre à jour les objets
    raquette_joueur.actualiser(LARGEUR)
    balle.auto_play(raquette_joueur)
    balle.actualiser(LARGEUR, HAUTEUR, raquette_joueur)

    # Dessiner les objets
    fenetre.fill(NOIR)
    fenetre.blit(bg, (0, 0))
    raquette_joueur.afficher(fenetre)
    balle.afficher(fenetre)

    texte_mm = font_mm.render('NEW GAME', True, BLANC)
    fenetre.blit(texte_mm, ((LARGEUR // 2) - 240, (HAUTEUR // 2) - 100))

    texte_mm_d = font_mm2.render('PRESS SPACE TO START', True, BLANC)
    fenetre.blit(texte_mm_d, ((LARGEUR // 2) - 255, (HAUTEUR // 2) - 20))

    pygame.display.update()
    pygame.time.Clock().tick(30)

raquette_joueur = functions.Raquette(HAUTEUR - 30, LARGEUR // 2)
balle = functions.Balle(LARGEUR // 2, HAUTEUR // 2)
score_txt = 0

while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                raquette_joueur.deplacement_raq = -20
            elif event.key == pygame.K_RIGHT:
                raquette_joueur.deplacement_raq = 20
        elif event.type == pygame.KEYUP:
            raquette_joueur.deplacement_raq = 0

    # Vérifier la collision avec la raquette
    if pygame.Rect.colliderect(balle.afficher(fenetre), raquette_joueur.rect_raquette):
        pygame.mixer.music.load('Colision_Sound.mp3')
        pygame.mixer.music.play()  # Play the sound
        if balle.vitesse > 20:
            balle.vitesse += 0.25
        else:
            balle.vitesse += 0.5
        balle.vitesse = min(50.5, balle.vitesse)
        balle.y_direction = -balle.y_direction
        score += 1
        score_txt = score

    # Mettre à jour les objets
    raquette_joueur.actualiser(LARGEUR)
    balle.actualiser(LARGEUR, HAUTEUR, raquette_joueur)

    # Dessiner les objets
    fenetre.fill(NOIR)
    fenetre.blit(bg, (0, 0))
    raquette_joueur.afficher(fenetre)
    balle.afficher(fenetre)

    # Afficher le score
    fonte = pygame.font.Font("E:\\NSI\\TerminalNSI\\Projet_pong\\8_bit_arcade\\8-bit Arcade In.ttf", 15)
    texte_score = fonte.render('SCORE : ' + str(score), True, BLANC)
    fenetre.blit(texte_score, ((LARGEUR // 2) - 100, 0))

    Highscore = pygame.font.Font("E:\\NSI\\TerminalNSI\\Projet_pong\\8_bit_arcade\\8-bit Arcade In.ttf", 15)
    texte_timer = fonte.render('BEST: ' + str(H_score), True, BLANC)
    fenetre.blit(texte_timer, ((LARGEUR - 155), 0))

    pygame.display.update()
    pygame.time.Clock().tick(30)

    while game_end:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_end = False
                en_cours = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_end = False

        # Dessiner les objets
        fenetre.fill(NOIR)
        fenetre.blit(bg, (0, 0))

        texte_mm = font_mm.render('GAME OVER', True, BLANC)
        fenetre.blit(texte_mm, ((LARGEUR // 2) - 275, (HAUTEUR // 2) - 100))

        fonteS = pygame.font.Font("E:\\NSI\\TerminalNSI\\Projet_pong\\8_bit_arcade\\8-bit Arcade In.ttf", 17)
        texte_mms = fonteS.render('YOUR SCORE  ' + str(score_txt), True, BLANC)
        fenetre.blit(texte_mms, ((LARGEUR // 2) - 150, (HAUTEUR // 2) + 23))

        texte_mmbs = fonteS.render('BEST SCORE  ' + str(H_score), True, BLANC)
        fenetre.blit(texte_mmbs, ((LARGEUR // 2) - 150, (HAUTEUR // 2) - 20))

        texte_mm_d = font_mm2.render('PRESS SPACE TO RESTART', True, BLANC)
        fenetre.blit(texte_mm_d, ((LARGEUR // 2) - 295, (HAUTEUR // 2) + 80))

        pygame.display.update()
        pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()