import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as mpla

L_STEP = 0.05

### SYSTEM VARIABLES
SYS = {
    "P" : 1,
    "S" : 9.17e5,
    "L" : 0.6,
    "q": 2.06e9,
    "SIGMA" : 5.75e-5,
    "ALBEDO_WHITE" : 0.75,
    "ALBEDO_GROUND" : 0.5,
    "ALBEDO_BLACK" : 0.25,
    "MAX_DAYS" : 1000,
    "DAY" : 1, 
    "GAMMA" : 0.3,
    "AREA_WHITE" : 0.01,
    "AREA_BLACK" : 0.01
    }

### calculations
def calc_albedo():
    Ag = (1 - SYS["AREA_BLACK"] - SYS["AREA_WHITE"]) * SYS["ALBEDO_GROUND"]
    Ab = SYS["AREA_BLACK"] * SYS["ALBEDO_BLACK"]
    Aw = SYS["AREA_WHITE"] * SYS["ALBEDO_WHITE"]
    A = Ag + Ab + Aw
    return A

def earth_temp():
    nuemrator = SYS["S"] * SYS["L"] * (1 - calc_albedo()) # SL(1-A)
    denominator = SYS["SIGMA"]

    return (nuemrator/denominator)**0.25

def local_temp(daisy_type):
    temp_e = earth_temp()
    A = SYS["ALBEDO_BLACK"]
    if (daisy_type == "white"):
        A = SYS["ALBEDO_WHITE"]   

    temp_i = (SYS["q"] * (calc_albedo() - A) + temp_e**4)**0.25

    return temp_i 

def calc_betta(daisy_type):
    temp_i = local_temp(daisy_type)

    if (daisy_type == "white"):
        return 1 - 0.003265 * (290.5 - temp_i)**2
    return 1 - 0.003265 * (300.5 - temp_i)**2
    
def calc_dw(daisy_type):
    x = 1 - SYS["AREA_BLACK"] - SYS["AREA_WHITE"]
    area = SYS["AREA_BLACK"]
    if (daisy_type == "white"):
        area = SYS["AREA_WHITE"]

    betta = calc_betta(daisy_type)

    dw = area * (x * betta - SYS["GAMMA"])
    return dw

def update_day():
    dw_white = calc_dw("white")
    dw_black = calc_dw("black")

    SYS["AREA_WHITE"] += dw_white
    SYS["AREA_BLACK"] += dw_black

    if SYS["AREA_WHITE"] <= 0:
        SYS["AREA_WHITE"] = 0
    if SYS["AREA_BLACK"] <= 0:
        SYS["AREA_BLACK"] = 0

### GUI

### SIMULATION

temp_data = []
black_data = []
white_data = []
L_data = []
black_temp = []
white_temp = []


while SYS["L"] < 1.7:
    while SYS["DAY"] < SYS["MAX_DAYS"]:
        update_day()
        SYS["DAY"] += 1
    
    black_data.append(SYS["AREA_BLACK"]*100)
    white_data.append(SYS["AREA_WHITE"]*100)
    temp_data.append(earth_temp()-273)
    L_data.append(SYS["L"])
    white_temp.append(local_temp("white") - 273)
    black_temp.append(local_temp("black") - 273)

    SYS["DAY"] = 0
    if SYS["AREA_WHITE"] <= 0:
        SYS["AREA_WHITE"] = 0.01
    if SYS["AREA_BLACK"] <= 0:
        SYS["AREA_BLACK"] = 0.01

    SYS["L"] = round(SYS["L"] + L_STEP ,3) # upade L to next simulation


fig, axis = plt.subplots(1, 2, figsize=(12, 6))

# Plot data in the first subplot
axis[0].plot(L_data, white_data, marker='o', linestyle='solid', color='r', label='white')
axis[0].plot(L_data, black_data, marker='o', linestyle='dotted', color='b', label='black')
axis[0].set_title("Area")
axis[0].set_xlabel('Luminosity')
axis[0].set_ylabel('Area Percentage')
axis[0].grid(True)
axis[0].legend()


axis[1].plot(L_data, temp_data, marker='o', linestyle='-', color='r', label=' Temperture')
axis[1].set_title("Temperture")
axis[1].set_xlabel('Luminosity')
axis[1].set_ylabel('Temperture C')
axis[1].grid(True)
axis[1].legend()

plt.show()