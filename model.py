import tkinter as tk
import matplotlib.pyplot as plt

DELAY = 250

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
    "MAX_DAYS" : 100000,
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

    return (SYS["q"] * (calc_albedo() - A) + temp_e**4)**0.25

def calc_betta(daisy_type):
    temp_i = local_temp(daisy_type)
    return 1 - 0.003265 * (295.5 - temp_i)**2

def calc_dw(daisy_type):
    x = 1 - SYS["AREA_BLACK"] - SYS["AREA_WHITE"]
    area = SYS["AREA_BLACK"]
    if (daisy_type == "white"):
        area = SYS["AREA_WHITE"]

    betta = calc_betta(daisy_type)

    dw = area * (x * betta - SYS["GAMMA"])
    return dw

def update_day():
   #print(f"--- DAY {SYS["DAY"]} L {SYS["L"]} ---")
    dw_white = calc_dw("white")
    dw_black = calc_dw("black")
    #print(f"white: {SYS["AREA_WHITE"]} dw: {dw_white}")
    #print(f"black: {SYS["AREA_BLACK"]} dw: {dw_black}\n")

    SYS["AREA_WHITE"] += dw_white
    SYS["AREA_BLACK"] += dw_black

    if SYS["AREA_WHITE"] <= 0:
        SYS["AREA_WHITE"] = 0
    if SYS["AREA_BLACK"] <= 0:
        SYS["AREA_BLACK"] = 0


### SIMULATION
temp_data = []
black_data = []
white_data = []
L_data = []

while SYS["L"] < 1.7:
    #print("\n--------------------------- NEW L ---------------------------")
    while SYS["DAY"] < SYS["MAX_DAYS"]:
        update_day()
        SYS["DAY"] += 1
    
    #print(f"RESULT: day: {SYS["DAY"]} L:{ SYS["L"]} black:{SYS["AREA_BLACK"]} white:{SYS["AREA_WHITE"]}% temp:{earth_temp()-273}C")

    black_data.append(SYS["AREA_BLACK"])
    white_data.append(SYS["AREA_WHITE"])
    temp_data.append(earth_temp()-273)
    L_data.append(SYS["L"])
    
    SYS["DAY"] = 0
    if SYS["AREA_WHITE"] <= 0:
        SYS["AREA_WHITE"] = 0.01
    if SYS["AREA_BLACK"] <= 0:
        SYS["AREA_BLACK"] = 0.01
    #print(f"BEFORE NEW L: black: {SYS["AREA_BLACK"]} white: {SYS["AREA_WHITE"]}")
    SYS["L"] = round(SYS["L"] + 0.05 ,3)

plt.figure()  # Optional: set figure size

plt.plot(L_data, white_data, marker='o', linestyle='-', color='r', label='white')
plt.plot(L_data, black_data, marker='o', linestyle='-', color='b', label='black')


# Adding labels and title
plt.xlabel('L')
plt.ylabel('Temp')
plt.title('Simple Line Plot')

# Adding grid
plt.grid(True)

# Adding legend
plt.legend()

# Display the plot
plt.show()