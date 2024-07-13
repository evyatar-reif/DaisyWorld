from daisy import Daisy
from utils import *
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as mpla

### GRAPHS
def show_gui(daisies, temp_data):
    #plot_daisies(daisies)
    #plot_world_temp(temp_data)
    two_graphs(daisies, temp_data)
    #plot_daisies_temp(daisies)
    plt.show()
    

def plot_daisies(daisies):
    plt.figure(figsize=(8, 6))
    
    for daisy in daisies:
        plt.plot(l_data, daisy.area_data, label=daisy.color,linewidth='3', marker='', linestyle="-", color=daisy.graph_color)

    plt.title('AREA OF DAISIES')
    plt.xlabel('Luminosity')
    plt.ylabel('Area %')
    plt.legend()
    plt.grid(True, which='both', zorder=10)
    plt.ylim(0, 100)  # Set y-axis limits from 0 to 100
    #plt.gca().invert_xaxis()


def plot_daisies_temp(daisies):
    plt.figure(figsize=(8, 6))

    for daisy in daisies:
        plt.plot(l_data, daisy.temp_data, label=daisy.color, linewidth='3', marker='', linestyle="-",
                 color=daisy.graph_color)

    plt.title('TEMPERATURE OF DAISIES C')
    plt.xlabel('Luminosity')
    plt.ylabel('TEMPERATURE C')
    plt.legend()
    plt.grid(True, which='both', zorder=10)
    # plt.gca().invert_xaxis()

def plot_world_temp(temp_data):
    plt.figure(figsize=(8, 6))

    plt.plot(l_data, temp_data, label='Temperatue', marker='', linestyle="-", linewidth='3', color='black')
    plt.grid(True, which='both', zorder=10)

    plt.title('WORLD TEMPERATURES')
    plt.xlabel('Luminosity')
    plt.ylabel('Temperature C')
    #plt.gca().invert_xaxis()
    plt.legend()

def two_graphs(daisies, temp_data):
    # Create a figure and axis
    fig, ax1 = plt.subplots()

    # Plot the first graph
    for daisy in daisies:
        ax1.plot(l_data, daisy.area_data, label=daisy.color, marker='', linestyle="-", color=daisy.graph_color)
        ax1.set_xlabel('Luminosity')
        ax1.set_ylabel('Area %', color='black')
        ax1.tick_params('y', colors='black')

    ax1.set_ylim(0, 100)

    # Create a second y-axis sharing the same x-axis
    ax2 = ax1.twinx()
    ax2.plot(l_data, temp_data, label='Temperature', marker='', linestyle="dotted", color='black', linewidth='4')
    ax2.set_ylabel('Temperature C', color='black')
    ax2.tick_params('y', colors='black')
    ax2.grid(True, which='both', zorder=10)
    ax2.set_zorder(1)
    ax2.set_ylim(-10, 80)  # Set y-axis limits from 0 to 100

    # Show the plot
    plt.show()


### SIMULATION
MAX_DAYS = 2000
END_L = 1.8
START_L = 0.6
L_STEP = 0.05
DEFAULT_AREA = 0.01

white = Daisy("white", 0.75,'blue', DEFAULT_AREA, 27.5)
black = Daisy("black", 0.25,'orange', DEFAULT_AREA, 17.5)
gray = Daisy("gray", 0.5,'gray', DEFAULT_AREA)
purple = Daisy("purple", 0.4,'purple', DEFAULT_AREA)
green = Daisy("green", 0.6,'green', DEFAULT_AREA)

daisies = [black,white]

temp_data = []
l_data = []

L = START_L
while L < END_L:
    simulate_l(daisies, L, MAX_DAYS, DEFAULT_AREA)

    l_data.append(L)
    temp_data.append(earth_temp(L, daisies) - 273)
    
    L = round(L + L_STEP, 3) 

show_gui(daisies, temp_data)