# This program developed by :
# Mohsen BehzadAsl
# Sadra Khanjari
# Mohammad Rahimi
# pouya Zarifi

import time

import pygame
import matplotlib
from numpy import pi

matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import pylab
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

fig = pylab.figure(figsize=[4.9, 3.3],  # Inches
                   dpi=100,  # 100 dots per inch, so the resulting buffer is 400x400 pixels
                   )
ax = fig.gca()

canvas = agg.FigureCanvasAgg(fig)
canvas.draw()
renderer = canvas.get_renderer()
raw_data = renderer.tostring_rgb()

from pygame.locals import *

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
purple = (60, 25, 60)
gray1 = (90, 90, 80)
gray2 = (128, 128, 128)

pygame.init()

width = 1250
height = 750

x_change = 0
y_change = 0

gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('EC Project!')
screen = pygame.display.get_surface()
size = canvas.get_width_height()
surf = pygame.image.fromstring(raw_data, size, "RGB")
screen.blit(surf, (50, 50))

# defining a font
smallfont5 = pygame.font.SysFont('Corbel', 60)
smallfont2 = pygame.font.SysFont('Corbel', 35)
smallfont = pygame.font.SysFont('Corbel', 30)
smallfont1 = pygame.font.SysFont('Corbel', 15)
smallfont3 = pygame.font.SysFont('Corbel', 18)
smallfont4 = pygame.font.SysFont('Corbel', 25)
# rendering a text written in
text100k = smallfont.render('100k', True, white)
text10k = smallfont.render('10k', True, white)
text1k = smallfont.render('1k', True, white)
text100 = smallfont.render('100', True, white)
text10 = smallfont.render('10', True, white)
text1 = smallfont.render('1', True, white)
textsin = smallfont1.render('sinusoidal', True, white)
textsqr = smallfont1.render('square', True, white)
textswt = smallfont1.render('sawtooth', True, white)
texttext0 = smallfont.render('0', True, white)
texttext1 = smallfont.render('1', True, white)
texttext2 = smallfont.render('2', True, white)
texttext3 = smallfont.render('3', True, white)
texttext4 = smallfont.render('4', True, white)
texttext5 = smallfont.render('5', True, white)
texttext6 = smallfont.render('6', True, white)
texttextn1 = smallfont.render('-1', True, white)
texttextn2 = smallfont.render('-2', True, white)
texttextn3 = smallfont.render('-3', True, white)
texttext04 = smallfont.render('0.4', True, white)
texttext08 = smallfont.render('0.8', True, white)
texttext16 = smallfont.render('1.6', True, white)
texttext10 = smallfont.render('10', True, white)
texttext05m = smallfont.render('0.5m', True, white)
texttext01m = smallfont.render('0.1m', True, white)
texttext50m = smallfont.render('50m', True, white)
texttext10m = smallfont.render('10m', True, white)
texttext05 = smallfont.render('0.5', True, white)
texttext01 = smallfont.render('0.1', True, white)
texttextp = smallfont5.render('+', True, white)
texttextn = smallfont5.render('-', True, white)
textdes = smallfont4.render('des', True, white)
textasc = smallfont4.render('asc', True, white)
frequency_select = smallfont4.render('FREQUENCY SELECT', True, white)
waveform_select = smallfont4.render('WAVEFORM SELECT', True, white)
ttl = smallfont4.render('TTL', True, white)
output = smallfont4.render('OUTPUT', True, white)
frequency_multiplier = smallfont3.render('FREQUENCY MULTIPLIER', True, white)
dc_offset = smallfont4.render('DC OFFSET', True, white)
amplitude = smallfont4.render('AMPLITUDE', True, white)
ver = smallfont4.render('VERTICAL POS', True, white)
hor = smallfont4.render('HORIZONTAL POS', True, white)
ch = smallfont4.render('CH1', True, white)
voldiv = smallfont4.render('volts/div', True, white)
timdiv = smallfont4.render('time/div', True, white)
trigger = smallfont4.render('TRIGGER', True, white)
lev = smallfont4.render('LEVEL', True, white)
slo = smallfont4.render('SLOP', True, white)
frequency_select1 = smallfont1.render('FREQUENCY SELECT', True, white)
waveform_select1 = smallfont1.render('WAVEFORM SELECT', True, white)
frequency_multiplier1 = smallfont1.render('FREQUENCY MULTIPLIER', True, white)
dc_offset1 = smallfont1.render('DC OFFSET', True, white)
amplitude1 = smallfont1.render('AMPLITUDE', True, white)
voldiv1 = smallfont1.render('volts/div', True, white)
timdiv1 = smallfont1.render('time/div', True, white)
lev1 = smallfont1.render('LEVEL', True, white)
slo1 = smallfont1.render('SLOP', True, white)
ver1 = smallfont1.render('VERTICAL POS', True, white)
hor1 = smallfont1.render('HORIZONTAL POS', True, white)

frequency_select1num11 = 1
frequency_multiplier1num11 = 1
dc_offset1num11 = 0
amplitude1num11 = 1
ver1num11 = 0
hor1num11 = 0
voltdiv1num11 = 1
timdiv1num11 = 1
lev1num11 = 0
slo1num11 = "ascending"

frequency_select1num = smallfont4.render('10k', True, black)
waveform_select1num = smallfont1.render('sinusoidal ', True, black)
frequency_multiplier1num = smallfont4.render(str(frequency_multiplier1num11), True, black)
dc_offset1num = smallfont4.render(str(dc_offset1num11), True, black)
amplitude1num = smallfont4.render(str(amplitude1num11), True, black)
ver1num = smallfont4.render(str(ver1num11), True, black)
hor1num = smallfont4.render(str(hor1num11), True, black)
voldiv1num = smallfont4.render(str(voltdiv1num11), True, black)
timdiv1num = smallfont4.render(str(timdiv1num11), True, black)
lev1num = smallfont4.render(str(lev1num11), True, black)
slo1num = smallfont4.render(slo1num11, True, black)


def initialize():
    pygame.draw.rect(gameDisplay, gray1, pygame.Rect(240, 15, 780, 330))
    pygame.draw.rect(gameDisplay, gray1, pygame.Rect(230, 5, 800, 350), 10, 15)

    pygame.draw.rect(gameDisplay, gray2, [240, 70, 70, 45])
    gameDisplay.blit(text10k, (257, 80))
    pygame.draw.rect(gameDisplay, gray2, [320, 70, 70, 45])
    gameDisplay.blit(text1k, (340, 80))
    pygame.draw.rect(gameDisplay, gray2, [400, 70, 70, 45])
    gameDisplay.blit(text100, (415, 80))
    pygame.draw.rect(gameDisplay, gray2, [480, 70, 70, 45])
    gameDisplay.blit(text10, (505, 80))
    pygame.draw.rect(gameDisplay, gray2, [560, 70, 70, 45])
    gameDisplay.blit(text1, (589, 80))
    pygame.draw.rect(gameDisplay, gray2, [640, 70, 70, 45])
    gameDisplay.blit(texttext01, (660, 80))

    pygame.draw.rect(gameDisplay, gray2, [790, 70, 70, 45])
    gameDisplay.blit(textsin, (797, 85))
    pygame.draw.rect(gameDisplay, gray2, [870, 70, 70, 45])
    gameDisplay.blit(textsqr, (885, 85))
    pygame.draw.rect(gameDisplay, gray2, [950, 70, 70, 45])
    gameDisplay.blit(textswt, (957, 85))

    # pygame.draw.rect(gameDisplay, gray2, pygame.Rect(250, 140, 190, 190))
    pygame.draw.rect(gameDisplay, gray2, pygame.Rect(240, 130, 210, 210), 10, 15)
    # pygame.draw.rect(gameDisplay, gray2, pygame.Rect(470, 140, 190, 190))
    pygame.draw.rect(gameDisplay, gray2, pygame.Rect(460, 130, 210, 210), 10, 15)
    # pygame.draw.rect(gameDisplay, gray2, pygame.Rect(690, 140, 190, 190))
    pygame.draw.rect(gameDisplay, gray2, pygame.Rect(680, 130, 210, 210), 10, 15)

    pygame.draw.rect(gameDisplay, gray2, [310, 250, 70, 40])
    gameDisplay.blit(texttextn, (335, 240))
    pygame.draw.rect(gameDisplay, gray2, [310, 200, 70, 40])
    gameDisplay.blit(texttextp, (330, 190))

    pygame.draw.rect(gameDisplay, gray2, [530, 250, 70, 40])
    gameDisplay.blit(texttextn, (555, 240))
    pygame.draw.rect(gameDisplay, gray2, [530, 200, 70, 40])
    gameDisplay.blit(texttextp, (550, 190))

    pygame.draw.rect(gameDisplay, gray2, [750, 250, 70, 40])
    gameDisplay.blit(texttextn, (775, 240))
    pygame.draw.rect(gameDisplay, gray2, [750, 200, 70, 40])
    gameDisplay.blit(texttextp, (770, 190))

    pygame.draw.circle(gameDisplay, (60, 60, 60), [960, 200], 25, 200)
    pygame.draw.circle(gameDisplay, (20, 20, 20), [960, 200], 20, 200)
    pygame.draw.circle(gameDisplay, (255, 255, 255), [960, 200], 10, 200)
    pygame.draw.circle(gameDisplay, (20, 20, 20), [960, 200], 5, 200)

    pygame.draw.circle(gameDisplay, (60, 60, 60), [960, 295], 30, 200)
    pygame.draw.circle(gameDisplay, (20, 20, 20), [960, 295], 25, 200)

    pygame.draw.rect(gameDisplay, gray1, pygame.Rect(110, 370, 1040, 370))
    pygame.draw.rect(gameDisplay, gray1, pygame.Rect(100, 360, 1060, 380), 10, 15)

    pygame.draw.rect(gameDisplay, black, pygame.Rect(130, 380, 500, 350))
    pygame.draw.rect(gameDisplay, gray2, pygame.Rect(120, 370, 520, 360), 10, 15)

    # pygame.draw.rect(gameDisplay, gray2, pygame.Rect(670, 380, 210, 250))
    pygame.draw.rect(gameDisplay, gray2, pygame.Rect(680, 370, 210, 225), 10, 15)

    pygame.draw.rect(gameDisplay, gray2, [750, 420, 30, 27])
    gameDisplay.blit(texttextn, (755, 405))
    pygame.draw.rect(gameDisplay, gray2, [790, 420, 30, 27])
    gameDisplay.blit(texttextp, (790, 404))

    pygame.draw.rect(gameDisplay, gray2, [712, 555, 70, 25])
    gameDisplay.blit(texttext10m, (720, 551))
    pygame.draw.rect(gameDisplay, gray2, [792, 555, 70, 25])
    gameDisplay.blit(texttext50m, (800, 551))
    pygame.draw.rect(gameDisplay, gray2, [712, 520, 70, 25])
    gameDisplay.blit(texttext01, (730, 514))
    pygame.draw.rect(gameDisplay, gray2, [792, 520, 70, 25])
    gameDisplay.blit(texttext05, (805, 514))
    pygame.draw.rect(gameDisplay, gray2, [712, 485, 70, 25])
    gameDisplay.blit(texttext1, (740, 482))
    pygame.draw.rect(gameDisplay, gray2, [792, 485, 70, 25])
    gameDisplay.blit(texttext5, (818, 479))

    # pygame.draw.rect(gameDisplay, gray2, pygame.Rect(920, 380, 210, 350))
    pygame.draw.rect(gameDisplay, gray2, pygame.Rect(930, 370, 210, 225), 10, 15)

    pygame.draw.rect(gameDisplay, gray2, [1000, 420, 30, 27])
    gameDisplay.blit(texttextn, (1005, 405))
    pygame.draw.rect(gameDisplay, gray2, [1040, 420, 30, 27])
    gameDisplay.blit(texttextp, (1040, 404))

    pygame.draw.rect(gameDisplay, gray2, [962, 555, 70, 25])
    gameDisplay.blit(texttext10m, (970, 551))
    pygame.draw.rect(gameDisplay, gray2, [1040, 555, 70, 25])
    gameDisplay.blit(texttext50m, (1050, 551))
    pygame.draw.rect(gameDisplay, gray2, [962, 520, 70, 25])
    gameDisplay.blit(texttext01, (980, 514))
    pygame.draw.rect(gameDisplay, gray2, [1040, 520, 70, 25])
    gameDisplay.blit(texttext05, (1055, 514))
    pygame.draw.rect(gameDisplay, gray2, [962, 485, 70, 25])
    gameDisplay.blit(texttext1, (990, 482))
    pygame.draw.rect(gameDisplay, gray2, [1040, 485, 70, 25])
    gameDisplay.blit(texttext5, (1067, 479))

    # pygame.draw.rect(gameDisplay, gray2, pygame.Rect(920, 380, 210, 350))
    pygame.draw.rect(gameDisplay, gray2, pygame.Rect(680, 605, 330, 120), 10, 15)

    pygame.draw.rect(gameDisplay, gray2, [700, 670, 45, 40])
    gameDisplay.blit(texttextn, (713, 660))
    pygame.draw.rect(gameDisplay, gray2, [752, 670, 45, 40])
    gameDisplay.blit(texttextp, (760, 660))

    pygame.draw.rect(gameDisplay, gray2, [895, 670, 45, 40])
    gameDisplay.blit(textdes, (900, 680))
    pygame.draw.rect(gameDisplay, gray2, [948, 670, 45, 40])
    gameDisplay.blit(textasc, (955, 680))

    pygame.draw.circle(gameDisplay, (60, 60, 60), [1080, 670], 30, 200)
    pygame.draw.circle(gameDisplay, (20, 20, 20), [1080, 670], 25, 200)

    pygame.draw.rect(gameDisplay, black, [365, 25, 217, 30])
    gameDisplay.blit(frequency_select, (365, 30))
    pygame.draw.rect(gameDisplay, black, [800, 25, 210, 30])
    gameDisplay.blit(waveform_select, (800, 30))
    pygame.draw.rect(gameDisplay, black, [250, 145, 190, 30])
    gameDisplay.blit(frequency_multiplier, (250, 150))
    pygame.draw.rect(gameDisplay, black, [510, 145, 117, 30])
    gameDisplay.blit(dc_offset, (510, 150))
    pygame.draw.rect(gameDisplay, black, [720, 145, 127, 30])
    gameDisplay.blit(amplitude, (720, 150))
    pygame.draw.rect(gameDisplay, black, [940, 149, 42, 22])
    gameDisplay.blit(ttl, (940, 150))
    pygame.draw.rect(gameDisplay, black, [915, 238, 92, 22])
    gameDisplay.blit(output, (915, 237))
    pygame.draw.rect(gameDisplay, black, [710, 385, 152, 30])
    gameDisplay.blit(ver, (710, 390))
    pygame.draw.rect(gameDisplay, black, [745, 455, 83, 25])
    gameDisplay.blit(voldiv, (745, 455))
    pygame.draw.rect(gameDisplay, black, [940, 385, 190, 30])
    gameDisplay.blit(hor, (940, 390))
    pygame.draw.rect(gameDisplay, black, [995, 455, 81, 25])
    gameDisplay.blit(timdiv, (995, 455))

    pygame.draw.rect(gameDisplay, black, [797, 620, 95, 20])
    gameDisplay.blit(trigger, (797, 620))
    pygame.draw.rect(gameDisplay, black, [715, 645, 65, 20])
    gameDisplay.blit(lev, (715, 645))
    pygame.draw.rect(gameDisplay, black, [915, 645, 56, 20])
    gameDisplay.blit(slo, (915, 645))

    pygame.draw.rect(gameDisplay, black, [10, 65, 200, 25])
    gameDisplay.blit(frequency_select1, (10, 70))
    pygame.draw.rect(gameDisplay, white, [145, 66, 65, 23])
    gameDisplay.blit(frequency_select1num, (158, 67))

    pygame.draw.rect(gameDisplay, black, [10, 90, 200, 25])
    gameDisplay.blit(waveform_select1, (10, 95))
    pygame.draw.rect(gameDisplay, white, [145, 91, 65, 23])
    gameDisplay.blit(waveform_select1num, (148, 94))

    pygame.draw.rect(gameDisplay, black, [10, 115, 200, 25])
    gameDisplay.blit(frequency_multiplier1, (10, 120))
    pygame.draw.rect(gameDisplay, white, [172, 116, 38, 23])
    gameDisplay.blit(frequency_multiplier1num, (180, 115))

    pygame.draw.rect(gameDisplay, black, [10, 140, 200, 25])
    gameDisplay.blit(dc_offset1, (10, 145))
    pygame.draw.rect(gameDisplay, white, [90, 141, 120, 23])
    gameDisplay.blit(dc_offset1num, (100, 140))

    pygame.draw.rect(gameDisplay, black, [10, 165, 200, 25])
    gameDisplay.blit(amplitude1, (10, 170))
    pygame.draw.rect(gameDisplay, white, [90, 166, 120, 23])
    gameDisplay.blit(amplitude1num, (100, 165))

    pygame.draw.rect(gameDisplay, black, [10, 190, 200, 25])
    gameDisplay.blit(ver1, (10, 195))
    pygame.draw.rect(gameDisplay, white, [103, 191, 107, 23])
    gameDisplay.blit(ver1num, (105, 190))

    pygame.draw.rect(gameDisplay, black, [10, 215, 200, 25])
    gameDisplay.blit(hor1, (10, 220))
    pygame.draw.rect(gameDisplay, white, [130, 216, 80, 23])
    gameDisplay.blit(hor1num, (135, 215))

    pygame.draw.rect(gameDisplay, black, [10, 240, 200, 25])
    gameDisplay.blit(voldiv1, (10, 245))
    pygame.draw.rect(gameDisplay, white, [65, 241, 145, 23])
    gameDisplay.blit(voldiv1num, (70, 240))

    pygame.draw.rect(gameDisplay, black, [10, 265, 200, 25])
    gameDisplay.blit(timdiv1, (10, 270))
    pygame.draw.rect(gameDisplay, white, [65, 266, 145, 23])
    gameDisplay.blit(timdiv1num, (70, 265))

    pygame.draw.rect(gameDisplay, black, [10, 290, 200, 25])
    gameDisplay.blit(lev1, (10, 295))
    pygame.draw.rect(gameDisplay, white, [65, 291, 145, 23])
    gameDisplay.blit(lev1num, (80, 290))

    pygame.draw.rect(gameDisplay, black, [10, 315, 200, 25])
    gameDisplay.blit(slo1, (10, 320))
    pygame.draw.rect(gameDisplay, white, [65, 316, 145, 23])
    gameDisplay.blit(slo1num, (70, 315))
    delete = False
    amplitude1num11 = 1
    frequency = 0


def draw(draw_frequency, frequency_coef, signal_type, triger_slope_type, time_dev, voltage_dev, draw_amplitude,
         draw_dc_offset, triger_value, vertiacl_value, horizontal_value):
    # f = plt.figure()
    freq = (draw_frequency * frequency_coef) * 2 * np.pi
    i_frequency = int(freq)
    if (int(freq) <= 0):
        i_frequency = 1
    triger_slope_val = -1
    if (triger_slope_type == "ascending"):
        triger_slope_val = 1
    x = np.linspace((time_dev * -1000), (time_dev * 1000), 100000 + 1)
    y = x
    if (signal_type == 1):
        plt.cla()
        y = triger_slope_val * draw_amplitude * np.sin(x * freq) + draw_dc_offset
    if (signal_type == 2):
        plt.cla()
        y = triger_slope_val * draw_amplitude * signal.square(x * freq,
                                                              1 / 2) + draw_dc_offset
    if (signal_type == 3):
        plt.cla()
        y = -triger_slope_val * draw_amplitude * signal.sawtooth(x * freq, 1 / 2) + draw_dc_offset
        horizontal_value += np.pi/(2*freq)
    if (draw_amplitude != 0):
        real_triger_value = (triger_value + vertiacl_value - draw_dc_offset) / draw_amplitude
    else:
        triger_value = 0
    if (abs(real_triger_value)<=1):
        if (triger_value != float(0)):
            phase = 0
            if (triger_slope_type == "ascending"):
                alpha = np.arcsin(np.sin(-time_dev * 4 * freq)) / freq
                betha = np.arcsin(real_triger_value) / freq
                horizontal_value += alpha - betha
            else:
                alpha = np.arcsin(-np.sin(-time_dev * 4 * freq)) / freq
                betha = np.arcsin(-real_triger_value) / freq
                horizontal_value += alpha - betha
        plt.xlim(-time_dev * 4, time_dev * 4)
        plt.ylim(-voltage_dev * 4, voltage_dev * 4)
        plt.grid()
        ax.plot(x + horizontal_value, y - vertiacl_value)
        ax.plot(x + horizontal_value, (x / x) * (-vertiacl_value), c='green')
        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        surf = pygame.image.fromstring(raw_data, size, "RGB")
        screen.blit(surf, (135, 385))
    else:
        plt.xlim(-time_dev * 4, time_dev * 4)
        plt.ylim(-voltage_dev * 4, voltage_dev * 4)
        plt.grid()
        ax.plot(x + horizontal_value, y - vertiacl_value)
        ax.plot(x + horizontal_value, (x / x) * (-vertiacl_value), c='green')
        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        surf = pygame.image.fromstring(raw_data, size, "RGB")
        screen.blit(surf, (135, 385))



flag = True

gameDisplay.fill(purple)
initialize()
signalVersion = 1
frequency = 1
amplitude1num11 = 1
frequency_multiplier1num11 = 1
dc_offset1num11 = 0
voltdiv1num11 = 1
timdiv1num11 = 1
hor1num11 = 0
ver1num11 = 0
slo1num11 = "ascending"
lev1num11 = 0
t = 1
phase = 0
plus_coef = 1
gameRunning = True
while gameRunning:
    maxsignal = abs(amplitude1num11) + dc_offset1num11 - ver1num11
    minsignal = - abs(amplitude1num11) + dc_offset1num11 - ver1num11
    # checks if a mouse is clicked
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
        elif ev.type == pygame.MOUSEBUTTONDOWN:

            if 235 <= mouse[0] <= 315 and 65 <= mouse[1] <= 120:
                frequency_select1num11 = 10000
                frequency = 10000
                frequency_select1num = smallfont4.render('10k', True, black)
                gameDisplay.fill(purple)
                initialize()

            elif 320 <= mouse[0] <= 395 and 65 <= mouse[1] <= 120:
                frequency_select1num11 = 1000
                frequency = 1000
                frequency_select1num = smallfont4.render('1k', True, black)
                gameDisplay.fill(purple)
                initialize()

                t = 0

            elif 400 <= mouse[0] <= 475 and 65 <= mouse[1] <= 120:
                frequency_select1num11 = 100
                frequency = 100
                frequency_select1num = smallfont4.render('100', True, black)
                gameDisplay.fill(purple)
                initialize()

                t = 0

            elif 480 <= mouse[0] <= 555 and 65 <= mouse[1] <= 120:
                frequency_select1num11 = 10
                frequency = 10
                frequency_select1num = smallfont4.render('10', True, black)
                gameDisplay.fill(purple)
                initialize()

                t = 0
            elif 560 <= mouse[0] <= 635 and 65 <= mouse[1] <= 120:
                frequency_select1num11 = 1
                frequency = 1
                frequency_select1num = smallfont4.render('1', True, black)
                gameDisplay.fill(purple)
                initialize()

                t = 0
            elif 640 <= mouse[0] <= 715 and 65 <= mouse[1] <= 120:
                frequency_select1num11 = 0.1
                frequency = 0.1
                frequency_select1num = smallfont4.render('0.1', True, black)
                gameDisplay.fill(purple)
                initialize()

                t = 0

            if 785 <= mouse[0] <= 865 and 65 <= mouse[1] <= 120:
                waveform_select1num = smallfont1.render('sinusoidal ', True, black)
                gameDisplay.fill(purple)
                signalVersion = 1
                initialize()

            elif 870 <= mouse[0] <= 945 and 65 <= mouse[1] <= 120:
                waveform_select1num = smallfont1.render('square ', True, black)
                gameDisplay.fill(purple)
                signalVersion = 2
                initialize()

            elif 950 <= mouse[0] <= 1025 and 65 <= mouse[1] <= 120:
                waveform_select1num = smallfont1.render('sawtooth ', True, black)
                gameDisplay.fill(purple)
                signalVersion = 3
                initialize()

            if 305 <= mouse[0] <= 385 and 245 <= mouse[1] <= 295:

                frequency_multiplier1num11 = frequency_multiplier1num11 - 0.5
                if (frequency_multiplier1num11 == 0):
                    frequency_multiplier1num11 = frequency_multiplier1num11 + 0.5
                frequency_multiplier1num = smallfont4.render(str(frequency_multiplier1num11), True, black)
                gameDisplay.fill(purple)
                initialize()

            elif 305 <= mouse[0] <= 385 and 195 <= mouse[1] <= 245:
                frequency_multiplier1num11 = frequency_multiplier1num11 + 0.5
                if (frequency_multiplier1num11 >= 10):
                    frequency_multiplier1num11 = frequency_multiplier1num11 = 10
                frequency_multiplier1num = smallfont4.render(str(frequency_multiplier1num11), True, black)
                gameDisplay.fill(purple)
                initialize()

            if 525 <= mouse[0] <= 575 and 250 <= mouse[1] <= 295:
                dc_offset1num11 = dc_offset1num11 - 1
                dc_offset1num = smallfont4.render(str(dc_offset1num11), True, black)
                gameDisplay.fill(purple)
                initialize()

            elif 525 <= mouse[0] <= 575 and 200 <= mouse[1] <= 245:
                dc_offset1num11 = dc_offset1num11 + 1
                dc_offset1num = smallfont4.render(str(dc_offset1num11), True, black)
                gameDisplay.fill(purple)
                initialize()

            if 745 <= mouse[0] <= 825 and 250 <= mouse[1] <= 295:
                amplitude1num11 = amplitude1num11 - 1
                if (amplitude1num11 < 0):
                    amplitude1num11 = 0
                amplitude1num = smallfont4.render(str(amplitude1num11), True, black)
                gameDisplay.fill(purple)
                initialize()

            elif 745 <= mouse[0] <= 825 and 200 <= mouse[1] <= 245:
                amplitude1num11 = amplitude1num11 + 1
                amplitude1num = smallfont4.render(str(amplitude1num11), True, black)
                gameDisplay.fill(purple)
                initialize()

            if 745 <= mouse[0] <= 783 and 415 <= mouse[1] <= 450:
                ver1num11 = ver1num11 + 1
                ver1num = smallfont4.render(str(-ver1num11), True, black)
                gameDisplay.fill(purple)
                initialize()

            elif 787 <= mouse[0] <= 825 and 415 <= mouse[1] <= 450:
                ver1num11 = ver1num11 - 1
                ver1num = smallfont4.render(str(-ver1num11), True, black)
                gameDisplay.fill(purple)
                initialize()

            if 710 <= mouse[0] <= 785 and 555 <= mouse[1] <= 580:
                voltdiv1num11 = 0.01
                voldiv1num = smallfont4.render(str(voltdiv1num11), True, black)
                gameDisplay.fill(purple)
                initialize()

            elif 790 <= mouse[0] <= 965 and 555 <= mouse[1] <= 580:
                voltdiv1num11 = 0.05
                voldiv1num = smallfont4.render(str(voltdiv1num11), True, black)
                gameDisplay.fill(purple)
                initialize()

            elif 710 <= mouse[0] <= 785 and 520 <= mouse[1] <= 545:
                voltdiv1num11 = 0.1
                voldiv1num = smallfont4.render(str(voltdiv1num11), True, black)
                gameDisplay.fill(purple)
                initialize()

            elif 790 <= mouse[0] <= 965 and 520 <= mouse[1] <= 545:
                voltdiv1num11 = 0.5
                voldiv1num = smallfont4.render(str(voltdiv1num11), True, black)
                gameDisplay.fill(purple)
                initialize()

            elif 710 <= mouse[0] <= 785 and 485 <= mouse[1] <= 510:
                voltdiv1num11 = 1
                voldiv1num = smallfont4.render(str(voltdiv1num11), True, black)
                gameDisplay.fill(purple)
                initialize()

            elif 790 <= mouse[0] <= 965 and 485 <= mouse[1] <= 510:
                voltdiv1num11 = 5
                voldiv1num = smallfont4.render(str(voltdiv1num11), True, black)
                gameDisplay.fill(purple)
                initialize()

            if 995 <= mouse[0] <= 1033 and 415 <= mouse[1] <= 450:
                hor1num11 = hor1num11 - 0.5
                hor1num = smallfont4.render(str(hor1num11), True, black)
                gameDisplay.fill(purple)
                initialize()

            elif 1037 <= mouse[0] <= 1075 and 415 <= mouse[1] <= 450:
                hor1num11 = hor1num11 + 0.5
                hor1num = smallfont4.render(str(hor1num11), True, black)
                gameDisplay.fill(purple)
                initialize()

            if 960 <= mouse[0] <= 1032 and 555 <= mouse[1] <= 580:
                timdiv1num11 = 0.01
                timdiv1num = smallfont4.render(str(timdiv1num11), True, black)
                gameDisplay.fill(purple)
                initialize()

            elif 1037 <= mouse[0] <= 1115 and 555 <= mouse[1] <= 580:
                timdiv1num11 = 0.05
                timdiv1num = smallfont4.render(str(timdiv1num11), True, black)
                gameDisplay.fill(purple)
                initialize()

            elif 960 <= mouse[0] <= 1032 and 520 <= mouse[1] <= 545:
                timdiv1num11 = 0.1
                timdiv1num = smallfont4.render(str(timdiv1num11), True, black)
                gameDisplay.fill(purple)
                initialize()

            elif 1037 <= mouse[0] <= 1115 and 520 <= mouse[1] <= 545:
                timdiv1num11 = 0.5
                timdiv1num = smallfont4.render(str(timdiv1num11), True, black)
                gameDisplay.fill(purple)
                initialize()

            elif 960 <= mouse[0] <= 1032 and 485 <= mouse[1] <= 510:
                timdiv1num11 = 1
                timdiv1num = smallfont4.render(str(timdiv1num11), True, black)
                gameDisplay.fill(purple)
                initialize()

            elif 1037 <= mouse[0] <= 1115 and 485 <= mouse[1] <= 510:
                timdiv1num11 = 5
                timdiv1num = smallfont4.render(str(timdiv1num11), True, black)
                gameDisplay.fill(purple)
                initialize()

            if 695 <= mouse[0] <= 745 and 665 <= mouse[1] <= 715:
                lev1num11 = lev1num11 - 0.5
                lev1num = smallfont4.render(str(lev1num11), True, black)
                gameDisplay.fill(purple)
                initialize()

            elif 750 <= mouse[0] <= 800 and 665 <= mouse[1] <= 715:
                lev1num11 = lev1num11 + 0.5
                lev1num = smallfont4.render(str(lev1num11), True, black)
                gameDisplay.fill(purple)
                initialize()

            if 890 <= mouse[0] <= 943 and 665 <= mouse[1] <= 715:
                slo1num11 = "descending"
                slo1num = smallfont4.render(slo1num11, True, black)
                gameDisplay.fill(purple)
                initialize()

            elif 946 <= mouse[0] <= 995 and 665 <= mouse[1] <= 715:
                slo1num11 = "ascending"
                slo1num = smallfont4.render(slo1num11, True, black)
                gameDisplay.fill(purple)
                initialize()
        if(lev1num11 <=maxsignal and lev1num11 >=minsignal):
            draw(frequency, frequency_multiplier1num11, signalVersion, slo1num11, timdiv1num11, voltdiv1num11,
             amplitude1num11, dc_offset1num11, lev1num11, ver1num11, hor1num11)
        else:
            phase += timdiv1num11/40
            if(phase > timdiv1num11*4):
                phase -= timdiv1num11
            draw(frequency, frequency_multiplier1num11, signalVersion, slo1num11, timdiv1num11, voltdiv1num11,
                 amplitude1num11, dc_offset1num11, 0 , ver1num11,  hor1num11 + phase)

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    pygame.display.update()