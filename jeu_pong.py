"""module principal"""
import pygame
from random import*
from math import*



"""Couleurs RGB"""
NOIR = (152, 151, 153)
BLANC = (255, 255, 255)
CYAN = (15, 240, 254)


"""Taille de la fenêtre"""
LARGEUR = 900
HAUTEUR = 600
"""Liste pour stocker le score de chaque jeu"""
L_scores=[]

"""Initalisations des modules de pygame"""
pygame.init()
"""Inialisation du module qui perrmetre d'avoir du son"""
pygame.mixer.init()
"""Creation du fenetre"""
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
"""Nomage du fenetre"""
pygame.display.set_caption('Pong')
#"""Enregistration de l'image du font-arrier"""
bg = pygame.image.load("Background3.jpg")

"""Enregistration des fonts"""
font_mm = pygame.font.Font(r'8-bit Arcade In.ttf', 45)
font_mm2 = pygame.font.Font(r'8-bit Arcade In.ttf', 20)


class Raquette:
#Creation de la classe raquette  
    def __init__(self, x_raquette, y_raquette):
        """Initialisations de la raquette et ses proprietes"""
        self.x_raquette = x_raquette
        self.y_raquette = y_raquette
        self.largeur_raq = 100
        self.hauteur_raq = 10
        self.deplacement_raq = 0
        self.dir=1
        self.rect_raquette = pygame.Rect(x_raquette, y_raquette, self.largeur_raq, self.hauteur_raq)

    def afficher(self):
        """Afichage de la raquette dans le fenetre"""
        pygame.draw.rect(fenetre, BLANC, self.rect_raquette)

    def actualiser(self):
        """Deplacement de la raquette et assuration qu'elle reste aux limites du fenetre"""
        self.x_raquette += self.deplacement_raq
        # Assurer que la raquette reste dans les limites de la fenêtre
        self.x_raquette = max(0, min(self.x_raquette, LARGEUR - self.largeur_raq))
        self.rect_raquette = pygame.Rect(self.x_raquette, self.y_raquette, self.largeur_raq, self.hauteur_raq)

"""Mise au fenetre de la raquete"""
raquette_joueur = Raquette(HAUTEUR - 30, LARGEUR // 2)



    

class Balle:
    
    
    def __init__(self, x_balle, y_balle):
        """Initialisation de la balle et ses proprietes"""
        self.x_balle = x_balle
        self.y_balle = y_balle
        self.rayon_balle = 10
        self.couleur = BLANC
        self.vitesse = 8
        self.x_direction = 1
        self.y_direction = 1

    def afficher(self):
        """Affichage de la balle"""
        return pygame.draw.circle(fenetre, self.couleur, (self.x_balle, self.y_balle), self.rayon_balle)
      
      
    def auto_play(self):
        """Jeu automatique"""
        if raquette_joueur.dir==1:
            raquette_joueur.deplacement_raq =  self.vitesse
            raquette_joueur.x_raquette=self.x_balle-45
        else:
            raquette_joueur.deplacement_raq =  -self.vitesse
            raquette_joueur.x_raquette=self.x_balle-55
            
        
            
            
    
        
     
        

    def actualiser(self):
        """Parametres pour le deplacement et barriers de la balle"""
        
        self.x_balle += self.vitesse * self.x_direction
        self.y_balle += self.vitesse * self.y_direction
        


        if self.y_balle - self.rayon_balle <= 0:
            self.y_direction = -self.y_direction
            if en_cours:
                pygame.mixer.music.load('Wall_sound.mp3')
                pygame.mixer.music.play()  # Play the sound
        elif self.y_balle + self.rayon_balle >= HAUTEUR:
            self.reinitialiser_jeu()
        if self.x_balle - self.rayon_balle*2 <= 0 or self.x_balle + self.rayon_balle*2 >= LARGEUR:
            self.x_direction = -self.x_direction
            if self.x_balle + self.rayon_balle*2 >= LARGEUR:
               raquette_joueur.dir=-1
            elif self.x_balle - self.rayon_balle*2 <= 0:
                raquette_joueur.dir=1
            if en_cours:
                pygame.mixer.music.load('Wall_sound.mp3')
                pygame.mixer.music.play()  # Play the sound
            
           
           

    def reinitialiser_jeu(self):
        """Reinitialisation du jeu"""
        pygame.mixer.music.load('End_of_game.mp3')
        pygame.mixer.music.play()  # Play the sound
        global game_end
        game_end=True
        raquette_joueur.x_raquette=550
        self.vitesse = 8
        self.x_balle = LARGEUR // 2
        self.y_balle = HAUTEUR // 2
        self.x_direction = 1
        self.y_direction = 1
        global score  # Accéder à la variable globale du score
        global H_score
        L_scores.append(score)
        score = 0  # Réinitialiser le score
        H_score = max(L_scores)

            
        
        
        
class Triangle:
    
    def __init__(self, x_triangle, y_triangle,sommets):
        self.x_triangle=x_triangle
        self.y_triangle=y_triangle
        self.couleur=BLANC
        self.sommets=sommets
        self.game_mode=0

        
    def afficher(self):
        return pygame.draw.polygon(fenetre, self.couleur, self.sommets)
    
    def deplacement(self,y_offset):
        sommets=self.sommets
        if y_offset<0:
            self.game_mode-=1
        else:
            self.game_mode+=1
        for i in range(3):
            sommets[i]=(sommets[i][0],sommets[i][1]+y_offset)
        return pygame.draw.polygon(fenetre, self.couleur, self.sommets)
    
    
class Raquette_H:
    
    def __init__(self, x_raquette_H, y_raquette_H):
        """Initialisations de la raquette et ses proprietes"""
        self.x_raquette_H = x_raquette_H
        self.y_raquette_H = y_raquette_H
        self.largeur_raq_H = 10
        self.hauteur_raq_H = 100
        self.deplacement_raq_H = 0
        self.dir_H=1
        self.rect_raquette_H = pygame.Rect(x_raquette_H, y_raquette_H, self.largeur_raq_H, self.hauteur_raq_H)

    def afficher(self):
        """Afichage de la raquette dans le fenetre"""
        pygame.draw.rect(fenetre, BLANC, self.rect_raquette_H)

    def actualiser(self):
        """Deplacement de la raquette et assuration qu'elle reste aux limites du fenetre"""
        self.y_raquette_H += self.deplacement_raq_H
        # Assurer que la raquette reste dans les limites de la fenêtre
        self.y_raquette_H = max(0, min(self.y_raquette_H, HAUTEUR - self.hauteur_raq_H))
        self.rect_raquette_H = pygame.Rect(self.x_raquette_H, self.y_raquette_H, self.largeur_raq_H, self.hauteur_raq_H)
    

score2j1=0
score2j2=0

class Balle_H:
    
    
    def __init__(self, x_balle_H, y_balle_H):
        """Initialisation de la balle et ses proprietes"""
        self.x_balle_H = x_balle_H
        self.y_balle_H = y_balle_H
        self.rayon_balle_H = 10
        self.couleur_H = BLANC
        self.vitesse_H = 8
        self.x_direction_H = -1
        self.y_direction_H = 1

    def afficher(self):
        """Affichage de la balle"""
        return pygame.draw.circle(fenetre, self.couleur_H, (self.x_balle_H, self.y_balle_H), self.rayon_balle_H)
      
          

    def actualiser(self):
        """Parametres pour le deplacement et barriers de la balle"""
        
        self.x_balle_H += self.vitesse_H * self.x_direction_H
        self.y_balle_H += self.vitesse_H * self.y_direction_H
        


        if self.x_balle_H + self.rayon_balle_H>=LARGEUR:
            global score2j1
            score2j1 += 1
            self.reinitialiser_jeu()
            if en_cours2:
                pygame.mixer.music.load('Wall_sound.mp3')
                pygame.mixer.music.play()  # Play the sound
        elif self.x_balle_H<=0 :
            global score2j2
            score2j2 += 1
            self.reinitialiser_jeu()
        if self.y_balle_H - self.rayon_balle_H <= 0 or self.y_balle_H + self.rayon_balle_H>=HAUTEUR :
            self.y_direction_H = -self.y_direction_H
            if en_cours2:
                pygame.mixer.music.load('Wall_sound.mp3')
                pygame.mixer.music.play()  # Play the sound
            
           
           

    def reinitialiser_jeu(self):
        """Reinitialisation du jeu"""
        pygame.mixer.music.load('End_of_game.mp3')
        pygame.mixer.music.play()  # Play the sound
        self.y_direction_H= round(self.y_direction_H,0)
        self.vitesse_H = 10
        self.x_balle_H = LARGEUR // 2
        self.y_balle_H = HAUTEUR // 2
        if score2j1>score2j2:
            self.x_direction_H = -1
        elif score2j1<score2j2:
            self.x_direction_H = 1
        else:
            self.y_direction_H = -self.y_direction_H



class Obstacle:
    
     
    def __init__(self,x_obs,y_obs,largeur_obs,hauteur_obs):
        self.x_obs=x_obs
        self.y_obs=y_obs
        self.largeur_obs=largeur_obs
        self.hauteur_obs=hauteur_obs
        self.dessiner_obs = pygame.Rect(x_obs,y_obs,largeur_obs,hauteur_obs)
    
    
    def afficher(self):
        return pygame.draw.rect(fenetre, BLANC, self.dessiner_obs)
     
     
     
     
def dist_points(x1,y1,x2,y2):
    s=(x2-x1)**2+(y2-y1)**2
    return sqrt(s)
    


# Création des objets 
raquette_joueur = Raquette(HAUTEUR - 30, 550)
balle = Balle(LARGEUR // 2, HAUTEUR // 2)
triangle=Triangle(0,0,[(180, 385), (180, 415), (210, 400)])
en_cours = False
en_cours2 = False
score = 0
H_score=0
mm=True
game_end=False
game_end2=False
x = True



# Boucle principal pour afficher le menu du jeu
while x:
    pygame.mixer.music.load('mihele 2.mp3')
    pygame.mixer.music.play(-1)  # Play the sound
    raquette_joueur.x_raquette=550
    while mm:
        H_score=0
        L_scores[:]=[]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mm = False
                x = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mm=False
                    en_cours=True
                if event.key == pygame.K_DOWN and triangle.game_mode<2:
                    triangle.deplacement(60)
                elif event.key == pygame.K_UP and triangle.game_mode>0:
                    triangle.deplacement(-60)
                if event.key == pygame.K_RETURN and triangle.sommets == [(180, 385), (180, 415), (210, 400)]:
                    mm=False
                    en_cours=True
                elif event.key == pygame.K_RETURN and triangle.sommets == [(180, 445), (180, 475), (210, 460)]:
                    mm=False
                    en_cours2=True
                elif event.key == pygame.K_RETURN and triangle.sommets == [(180, 505), (180, 535), (210, 520)]:
                    mm=False
                    en_cours=True
                    
                    

            
                    
                

        
       
        # Dessiner les objets
        fenetre.fill(NOIR)  # It is mandatory to have a backround, if not the  moving things will stretch
        fenetre.blit(bg, (0, 0))
        triangle.afficher()

        texte_mm = font_mm.render('NEW GAME', True, BLANC)
        fenetre.blit(texte_mm, ((LARGEUR // 2)-240 , (HAUTEUR//2)-100))
         
        texte_mm_d = font_mm2.render('SELECT A GAME MODE', True, BLANC)
        fenetre.blit(texte_mm_d, ((LARGEUR // 2)-225 , (HAUTEUR//2)-20))
        
        texte_mm_m1 = font_mm2.render('CLASSIC MODE', True, BLANC)
        fenetre.blit(texte_mm_m1, (300 , 380))
        
        texte_mm_m2 = font_mm2.render('TWO PLAYER GAME', True, BLANC)
        fenetre.blit(texte_mm_m2, (270 , 440))
        
        texte_mm_m3 = font_mm2.render('SPECIAL MODE', True, BLANC)
        fenetre.blit(texte_mm_m3, (300 , 500))

        pygame.display.update()
        pygame.time.Clock().tick(30)
     
    if en_cours:
        raquette_joueur = Raquette(HAUTEUR - 30, LARGEUR // 2)
        balle = Balle(LARGEUR // 2, HAUTEUR // 2)
        score_txt=0

    
    #boucle principale du jeu
    
    while en_cours:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_cours = False
                x=False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    raquette_joueur.deplacement_raq = -20
                elif event.key == pygame.K_RIGHT:
                    raquette_joueur.deplacement_raq = 20
            elif event.type == pygame.KEYUP:
                raquette_joueur.deplacement_raq = 0
            

                

        
        # Vérifier la collision avec la raquette
        if pygame.Rect.colliderect(balle.afficher(), raquette_joueur.rect_raquette):
            pygame.mixer.music.load('Colision_Sound.mp3')
            pygame.mixer.music.play()  # Play the sound
            if balle.vitesse>25:
                balle.vitesse+=0.25
            else:
                balle.vitesse+=0.5
            balle.vitesse=min(55,balle.vitesse) 
            balle.y_direction = -balle.y_direction+random()/100
            score += 1
            score_txt=score

        # Mettre à jour les objets
        raquette_joueur.actualiser()
        balle.actualiser()
        
        
        

        # Dessiner les objets
        fenetre.fill(NOIR)  # It is mandatory to have a backround, if not the  moving things will stretch
        fenetre.blit(bg, (0, 0))
        raquette_joueur.afficher()
        balle.afficher()

        # Afficher le score
        fonte = pygame.font.Font(r"8-bit Arcade In.ttf", 15)
        texte_score = fonte.render('SCORE  ' + str(score), True, BLANC)
        fenetre.blit(texte_score, ((LARGEUR // 2) - 100, 0))
        
        #afficher le meilleur score
        
        Highscore = pygame.font.Font(r"8-bit Arcade In.ttf", 15)
        texte_timer = fonte.render('BEST  '+str(H_score), True, BLANC)
        fenetre.blit(texte_timer, ((LARGEUR-165),0))

        pygame.display.update()
        pygame.time.Clock().tick(30)
        

        #boucle du fin de jeu
        while game_end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_end = False
                    en_cours=False
                    x=False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_end = False
                elif event.type == pygame.MOUSEBUTTONDOWN :
                    mouse_pos = pygame.mouse.get_pos()
                    if 700 <= mouse_pos[0] <= 900 and 0 <= mouse_pos[1] <= 30:
                        game_end = False
                        en_cours = False
                        mm = True
                        L_scores = []
                        score = 0
                        raquette_joueur = Raquette(HAUTEUR - 30, LARGEUR // 2)
                        balle = Balle(LARGEUR // 2, HAUTEUR // 2)
                                    
            fenetre.fill(NOIR)  # It is mandatory to have a backround, if not the  moving things will stretch
            fenetre.blit(bg, (0, 0))

            texte_mm = font_mm.render('GAME OVER', True, BLANC)
            fenetre.blit(texte_mm, ((LARGEUR // 2)-275 , (HAUTEUR//2)-100))
            
            fonteS = pygame.font.Font(r"8-bit Arcade In.ttf", 17)
            texte_mms=fonteS.render('YOUR SCORE  '+str(score_txt), True, BLANC)
            fenetre.blit(texte_mms, ((LARGEUR // 2)-150 , (HAUTEUR//2)-10))
                
            texte_mmbs=fonteS.render('BEST SCORE  '+str(H_score), True, BLANC)
            fenetre.blit(texte_mmbs, ((LARGEUR // 2)-150 , (HAUTEUR//2)+37))
            
            texte_mm_d = font_mm2.render('PRESS SPACE TO RESTART', True, BLANC)
            fenetre.blit(texte_mm_d, ((LARGEUR // 2)-295 , (HAUTEUR//2)+80))
            
            texte_mm_mm = fonteS.render('MAIN MENU', True, BLANC)
            fenetre.blit(texte_mm_mm, (LARGEUR-220 , 0))
                    
            pygame.display.update()
            pygame.time.Clock().tick(30)

            
    
    raquette_joueur1_H = Raquette_H(30, HAUTEUR // 2)
    balle_H =  Balle_H(LARGEUR // 2, HAUTEUR // 2)
    raquette_joueur2_H = Raquette_H(LARGEUR-30, HAUTEUR // 2)
    obstacle1 = Obstacle(LARGEUR//2-90,200,50,50)
    obstacle2 = Obstacle(LARGEUR//2+90,200,50,50)
    obstacle3 = Obstacle(LARGEUR//2-115,350,300,30)
        
    while en_cours2:
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_cours2 = False
                x=False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    en_cours2 = False
                    game_end2 = True
                if event.key == pygame.K_UP:
                    raquette_joueur1_H.deplacement_raq_H = -20
                elif event.key == pygame.K_DOWN:
                    raquette_joueur1_H.deplacement_raq_H = 20
                elif event.key == pygame.K_w:
                    raquette_joueur2_H.deplacement_raq_H = -20
                elif event.key == pygame.K_s:
                    raquette_joueur2_H.deplacement_raq_H = 20
            elif event.type == pygame.KEYUP:
                raquette_joueur1_H.deplacement_raq_H = 0
                raquette_joueur2_H.deplacement_raq_H = 0
            
                
                
        
        
        if pygame.Rect.colliderect(balle_H.afficher(), raquette_joueur1_H.rect_raquette_H):
            pygame.mixer.music.load('Colision_Sound.mp3')
            pygame.mixer.music.play()  # Play the sound
            balle_H.vitesse_H+=1
            balle_H.x_direction_H = -balle_H.x_direction_H#+random()/10
            
        if pygame.Rect.colliderect(balle_H.afficher(), raquette_joueur2_H.rect_raquette_H):
            pygame.mixer.music.load('Colision_Sound.mp3')
            pygame.mixer.music.play()  # Play the sound
            balle_H.vitesse_H+=1
            balle_H.x_direction_H = -balle_H.x_direction_H#+random()/10
            
            
            
        if pygame.Rect.colliderect(balle_H.afficher(), obstacle1.dessiner_obs):
            pygame.mixer.music.load('Colision_Sound.mp3')
            pygame.mixer.music.play()  # Play the sound
            # Check collision with vertical sides
            if obstacle1.dessiner_obs.left <= balle_H.x_balle_H <= obstacle1.dessiner_obs.right:
                balle_H.y_direction_H = -balle_H.y_direction_H
                print('obs1u',balle_H.x_balle_H, obstacle1.x_obs)
                # Check collision with horizontal sides
            elif obstacle1.dessiner_obs.top <= balle_H.y_balle_H <= obstacle1.dessiner_obs.bottom:
                balle_H.x_direction_H = -balle_H.x_direction_H
                print('obs1d',balle_H.y_balle_H, obstacle1.y_obs)
                
            
        if pygame.Rect.colliderect(balle_H.afficher(), obstacle2.dessiner_obs):
            pygame.mixer.music.load('Colision_Sound.mp3')
            pygame.mixer.music.play()  # Play the sound
            # Check collision with vertical sides
            if obstacle2.dessiner_obs.left <= balle_H.x_balle_H <= obstacle2.dessiner_obs.right:
                balle_H.y_direction_H = -balle_H.y_direction_H
                print('obs2u',balle_H.x_balle_H, obstacle1.x_obs)
                # Check collision with horizontal sides
            elif obstacle2.dessiner_obs.top <= balle_H.y_balle_H <= obstacle2.dessiner_obs.bottom:
                balle_H.x_direction_H = -balle_H.x_direction_H
                print('obs2d',balle_H.y_balle_H, obstacle1.y_obs)
                
        if pygame.Rect.colliderect(balle_H.afficher(), obstacle3.dessiner_obs):
            pygame.mixer.music.load('Colision_Sound.mp3')
            pygame.mixer.music.play()  # Play the sound
            # Check collision with vertical sides
            if obstacle3.dessiner_obs.left <= balle_H.x_balle_H <= obstacle3.dessiner_obs.right:
                balle_H.y_direction_H = -balle_H.y_direction_H
                print('obs3u',balle_H.x_balle_H, obstacle1.x_obs)
                # Check collision with horizontal sides
            elif obstacle3.dessiner_obs.top <= balle_H.y_balle_H <= obstacle3.dessiner_obs.bottom:
                balle_H.x_direction_H = -balle_H.x_direction_H
                print('obs3d',balle_H.y_balle_H, obstacle1.y_obs)
                 
        
        
        
        
        raquette_joueur1_H.actualiser()
        raquette_joueur2_H.actualiser()
        balle_H.actualiser()
        
        
        
        
        # Dessiner les objets
        fenetre.fill(NOIR)  # It is mandatory to have a backround, if not the  moving things will stretch
        fenetre.blit(bg, (0, 0))
        raquette_joueur1_H.afficher()
        raquette_joueur2_H.afficher()
        balle_H.afficher()
        obstacle1.afficher()
        obstacle2.afficher()
        obstacle3.afficher()
       

        # Afficher le score
        fonte = pygame.font.Font(r"8-bit Arcade In.ttf", 15)
        texte_score = fonte.render('SCORE  ' + str(score2j1)+" - "+str(score2j2), True, BLANC)
        fenetre.blit(texte_score, ((LARGEUR // 2) - 100, 0))
        
        #afficher le meilleur score
        
        

        pygame.display.update()
        pygame.time.Clock().tick(30)
        
        while game_end2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_end2 = False
                    en_cours2=False
                    x=False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_end2 = False
                        en_cours2=True
                        raquette_joueur1_H = Raquette_H(30, HAUTEUR // 2)
                        balle_H =  Balle_H(LARGEUR // 2, HAUTEUR // 2)
                        raquette_joueur2_H = Raquette_H(LARGEUR-30, HAUTEUR // 2)
                elif event.type == pygame.MOUSEBUTTONDOWN :
                    mouse_pos = pygame.mouse.get_pos()
                    if 700 <= mouse_pos[0] <= 900 and 0 <= mouse_pos[1] <= 30:
                        game_end2 = False
                        en_cours2 = False
                        mm = True
                        L_scores = []
                        score = 0
                        raquette_joueur_H = Raquette_H(30, LARGEUR // 2)
                        balle_H = Balle_H(LARGEUR // 2, HAUTEUR // 2)
                                    
            fenetre.fill(NOIR)  # It is mandatory to have a backround, if not the  moving things will stretch
            fenetre.blit(bg, (0, 0))

            texte_mm = font_mm.render('GAME OVER', True, BLANC)
            fenetre.blit(texte_mm, ((LARGEUR // 2)-275 , (HAUTEUR//2)-100))
            
            fonteS = pygame.font.Font(r"8-bit Arcade In.ttf", 17)
            texte_mms=fonteS.render('YOUR SCORE  '+str(score2j1)+" - "+str(score2j2), True, BLANC)
            fenetre.blit(texte_mms, ((LARGEUR // 2)-150 , (HAUTEUR//2)-10))
            
            if score2j1>score2j2:
                RES = pygame.font.Font(r"8-bit Arcade In.ttf", 17)
                texte_res=RES.render('PLAYER ONE WINNS', True, BLANC)
                fenetre.blit(texte_res, ((LARGEUR // 2)-150 , (HAUTEUR//2)+35))
            
            elif score2j1==score2j2:
                RES = pygame.font.Font(r"8-bit Arcade In.ttf", 17)
                texte_res=RES.render("IT'S A DRAW", True, BLANC)
                fenetre.blit(texte_res, ((LARGEUR // 2)-100 , (HAUTEUR//2)+35))
                
            else:
                RES = pygame.font.Font(r"8-bit Arcade In.ttf", 17)
                texte_res=RES.render('PLAYER TWO WINNS', True, BLANC)
                fenetre.blit(texte_res, ((LARGEUR // 2)-150 , (HAUTEUR//2)+35))
                
            
                
            
            texte_mm_d = font_mm2.render('PRESS SPACE TO RESTART', True, BLANC)
            fenetre.blit(texte_mm_d, ((LARGEUR // 2)-295 , (HAUTEUR//2)+80))
            
            texte_mm_mm = fonteS.render('MAIN MENU', True, BLANC)
            fenetre.blit(texte_mm_mm, (LARGEUR-220 , 0))
                    
            pygame.display.update()
            pygame.time.Clock().tick(30)
            
            
pygame.quit()



