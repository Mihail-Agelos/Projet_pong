import pygame

# Load fonts
def load_fonts():
    font_mm = pygame.font.Font("E:\\NSI\\TerminalNSI\\Projet_pong\\8_bit_arcade\\8-bit Arcade In.ttf", 45)
    font_mm2 = pygame.font.Font("E:\\NSI\\TerminalNSI\\Projet_pong\\8_bit_arcade\\8-bit Arcade In.ttf", 20)
    return font_mm, font_mm2

# Raquette class
class Raquette:
    def __init__(self, x_raquette, y_raquette):
        self.x_raquette = x_raquette
        self.y_raquette = y_raquette
        self.largeur_raq = 100
        self.hauteur_raq = 10
        self.deplacement_raq = 0
        self.dir = 1
        self.rect_raquette = pygame.Rect(x_raquette, y_raquette, self.largeur_raq, self.hauteur_raq)

    def afficher(self, fenetre):
        pygame.draw.rect(fenetre, (255, 255, 255), self.rect_raquette)

    def actualiser(self, LARGEUR):
        self.x_raquette += self.deplacement_raq
        # Assurer que la raquette reste dans les limites de la fenêtre
        self.x_raquette = max(0, min(self.x_raquette, LARGEUR - self.largeur_raq))
        self.rect_raquette = pygame.Rect(self.x_raquette, self.y_raquette, self.largeur_raq, self.hauteur_raq)

# Balle class
class Balle:
    def __init__(self, x_balle, y_balle):
        self.x_balle = x_balle
        self.y_balle = y_balle
        self.rayon_balle = 10
        self.couleur = (255, 255, 255)
        self.vitesse = 8
        self.x_direction = 1
        self.y_direction = 1

    def afficher(self, fenetre):
        pygame.draw.circle(fenetre, self.couleur, (self.x_balle, self.y_balle), self.rayon_balle)

    def auto_play(self, raquette_joueur):
        if raquette_joueur.dir == 1:
            raquette_joueur.deplacement_raq = self.vitesse
            raquette_joueur.x_raquette = self.x_balle - 45
        else:
            raquette_joueur.deplacement_raq = -self.vitesse
            raquette_joueur.x_raquette = self.x_balle - 55

    def actualiser(self, LARGEUR, HAUTEUR, raquette_joueur):
        self.x_balle += self.vitesse * self.x_direction
        self.y_balle += self.vitesse * self.y_direction

        if self.y_balle - self.rayon_balle <= 0:
            self.y_direction = -self.y_direction

        elif self.y_balle + self.rayon_balle >= HAUTEUR:
            self.reinitialiser_jeu()

        if self.x_balle - self.rayon_balle * 2 <= 0 or self.x_balle + self.rayon_balle * 2 >= LARGEUR:
            self.x_direction = -self.x_direction
            if self.x_balle + self.rayon_balle * 2 >= LARGEUR:
                raquette_joueur.dir = -1
            elif self.x_balle - self.rayon_balle * 2 <= 0:
                raquette_joueur.dir = 1

    def reinitialiser_jeu(self):
        pygame.mixer.music.load('End_of_game.mp3')
        pygame.mixer.music.play()  # Play the sound
        global game_end
        game_end = True