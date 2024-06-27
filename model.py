from daisy import Daisy
from utils import *
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as mpla

### GRAPHS
def show_gui(daisies):
    plot_daisies(daisies)
    plt.show()
    

def plot_daisies(daisies):
    plt.figure(figsize=(8, 6))
    
    for daisy in daisies:
        plt.plot(l_data, daisy.area_data, label=daisy.color, marker='', linestyle="-")

    plt.title('AREA OF DAISIES')
    plt.xlabel('Luminosity')
    plt.ylabel('Area %')
    plt.legend()
    plt.ylim(0, 100)  # Set y-axis limits from 0 to 100

### SIMULATION

MAX_DAYS = 2000
MAX_L = 1.7
MIN_L = 0.6
L_STEP = 0.05
DEFAULT_AREA = 0.01

white = Daisy("white", 0.75, DEFAULT_AREA)
black = Daisy("black", 0.25, DEFAULT_AREA)

daisies = [white, black]

temp_data = []
l_data = []

L = MIN_L
while L < MAX_L:
    simulate_l(daisies, L, MAX_DAYS, DEFAULT_AREA)

    l_data.append(L)
    temp_data.append(earth_temp(L, daisies) - 273)
    
    L = round(L + L_STEP, 3) 

show_gui(daisies)