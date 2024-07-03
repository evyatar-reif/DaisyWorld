from daisy import Daisy
from utils import *
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as mpla

### GRAPHS
def show_gui(daisies, temp_data):
    plot_daisies(daisies)
    plot_world_temp(temp_data)
    plt.show()
    

def plot_daisies(daisies):
    plt.figure(figsize=(8, 6))
    
    for daisy in daisies:
        plt.plot(l_data, daisy.area_data, label=daisy.color, marker='', linestyle="-")

    plt.title('AREA OF DAISIES')
    plt.xlabel('Luminosity')
    plt.ylabel('Area %')
    plt.legend()
    plt.gca().invert_xaxis()
    plt.ylim(0, 100)  # Set y-axis limits from 0 to 100


def plot_world_temp(temp_data):
    plt.figure(figsize=(8, 6))

    plt.plot(l_data, temp_data, label='Temperatue', marker='', linestyle="-")

    plt.title('WORLD TEMPERATURES')
    plt.xlabel('Luminosity')
    plt.ylabel('Temperature C')
    plt.gca().invert_xaxis()
    plt.legend()


### SIMULATION

MAX_DAYS = 2000
END_L = 0.5
START_L = 1.7
L_STEP = -0.05
DEFAULT_AREA = 0.01

white = Daisy("white", 0.75, DEFAULT_AREA)
black = Daisy("black", 0.25, DEFAULT_AREA)
yellow = Daisy("yellow", 0.6, DEFAULT_AREA)
purple = Daisy("purple", 0.4, DEFAULT_AREA)


daisies = [white, black, yellow, purple]

temp_data = []
l_data = []

L = START_L
while L > END_L:
    simulate_l(daisies, L, MAX_DAYS, DEFAULT_AREA)

    l_data.append(L)
    temp_data.append(earth_temp(L, daisies) - 273)
    
    L = round(L + L_STEP, 3) 

show_gui(daisies, temp_data)