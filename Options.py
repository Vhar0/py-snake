import pygame
import tkinter
import os.path
from tkinter import messagebox
from pygame.locals import *

pygame.init()
clk = pygame.time.Clock()

font = pygame.font.SysFont('Comic Sans MS', 20)


def selection_loop():
    Display_W = 800
    Display_H = 600
    sector = 0
    mouse_X = 0  # mouse X
    mouse_Y = 0  # mouse Y

    pygame.font.init()  # inizializzo la funzione font
    # font per txt
    font_coords = pygame.font.SysFont('Leaner Typeface', 20)                                        # font specifico per coordinate e nuimeri
    text1 = font.render("Display: ", False,(0, 0, 0))                                               # attribuisco a text_surface le impostazioni del render della parola

    red = (255, 0, 0)
    black = (0, 0, 0)

    display_X = (800, 1152, 1280, 1280, 1280, 1366, 1440, 1600, 1920)                               # possibili risoluzioni per il display del gioco (X)
    display_Y = (600, 864, 720, 800, 1024, 768, 1080, 1024, 1080)                                   # possibili risoluzioni per il display del gioco (Y)

    logo = pygame.image.load(os.path.join('res', 'logo.png'))                                          # aggiungo a logo le impostazioni dell' immagine logo
    play_button = pygame.image.load(
        os.path.join('res', "play-button.png"))                                                        # aggiungo a play_button le impostazioni dell' immagine di start

    rect = Rect(80, 113, 25,8)                                                                      # rect(starting x, starting y, width = divisione in 9 per scelta risoluzione display, hight = 7 larghezza linea

    screen1 = pygame.display.set_mode((400, 200))

    pygame.display.init()

    if not pygame.display.get_init:
        tkinter.messagebox.showerror(title="Display ERROR!",message="error during the initialization of display module")
        exit()

    pygame.display.set_caption("SNAKE options menu")

    done = False
    while not done:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                exit()
            if 80 <= pygame.mouse.get_pos()[0] <= 305 and pygame.mouse.get_pos()[1] < 150:
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    W = pygame.mouse.get_pos()[0]                                                   # posizione mouse X
                    H = pygame.mouse.get_pos()[1]                                                   # posizione mouse Y
                    rect = Rect(W - 25, 113, 25, 8)                                                 # rect(starting x, starting y, width = divisione in 9 per scelta risoluzione display, hight = 7 larghezza linea
                    #if 150 >= W >= 250 and 145 >= H >= 180:
                    if 80 <= W <= 305:                                                          # controllo che il mouse sia effettivamente sulla linea di "checkbox"
                        if 80 <= W <= 105:
                                sector = 0
                        if 105 <= W <= 130:
                                sector = 1
                        if 130 <= W <= 155:
                                sector = 2
                        if 155 <= W <= 180:                                                     # che dolore vedere sta roba, ma non avevo altra scelta o non ne conoscevo una
                                sector = 3
                        if 180 <= W <= 205:
                                sector = 4
                        if 205 <= W <= 230:
                                sector = 5
                        if 230 <= W <= 255:
                                sector = 6
                        if 255 <= W <= 280:
                                sector = 7
                        if 280 <= W <= 305:
                                sector = 8
                    Display_W = display_X[sector]                                                   # dalla lista delle risoluzioni perendo quella scelta dall' utente
                    Display_H = display_Y[sector]                                                   # dalla lista delle risoluzioni perendo quella scelta dall' utente
            if 150 <= pygame.mouse.get_pos()[0] <= 250 and 145 <= pygame.mouse.get_pos()[1] <= 180:
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    done = True

        mouse_X = pygame.mouse.get_pos()[0]
        mouse_Y = pygame.mouse.get_pos()[1]

        mouse_pos = font_coords.render("(" + str(mouse_X) + ";" + str(mouse_Y) + ")", False, (0, 0, 0))
        new_resolution = font_coords.render("(" + str(Display_W) + ";" + str(Display_H) + ")", False, (0, 0, 0))

        screen1.fill((255, 255, 255))

        screen1.blit(logo, (110, 0))                                                                # stampo l' immagine del logo
        screen1.blit(play_button, (150, 145))                                                       # stampo il play button l=100px, h=35px

        screen1.blit(text1, (0, 100))                                                               # stampo il testo alle coordinate dietro la checkbox
        screen1.blit(new_resolution, (310, 100))                                                    # stampo le coordinate dopo la checkbox
        screen1.blit(mouse_pos, (0, 0))

        pygame.draw.line(screen1, red, (80, 117), (305, 117),8)                                     # disegno la checkbox per accedere alle impostazioni schermo
        pygame.draw.rect(screen1, black, rect)

        # blolck
        pygame.draw.line(screen1, black, (105, 110), (105, 124), 2)
        pygame.draw.line(screen1, black, (130, 110), (130, 124), 2)
        pygame.draw.line(screen1, black, (155, 110), (155, 124), 2)
        pygame.draw.line(screen1, black, (180, 110), (180, 124), 2)
        pygame.draw.line(screen1, black, (205, 110), (205, 124), 2)
        pygame.draw.line(screen1, black, (230, 110), (230, 124), 2)
        pygame.draw.line(screen1, black, (255, 110), (255, 124), 2)
        pygame.draw.line(screen1, black, (280, 110), (280, 124), 2)

        pygame.display.flip()                                                                       # aggiorno lo schermo per il prossimo frame

        clk.tick(60)
    return Display_W, Display_H