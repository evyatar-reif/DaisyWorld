P = 1
S = 9.17e5
Q = 2.06e9
GAMMA = 0.3
SIGMA = 5.75e-5
GROUND_ALBEDO = 0.5

### calculations
def calc_x (daisies):
    x = 1
    for daisy in daisies:
        x -= daisy.area
    
    return x 

def calc_albedo (daisies):
    Ag = calc_x(daisies) * GROUND_ALBEDO
    total_Ai = 0
    for daisy in daisies:
        Ai = daisy.area * daisy.albedo # == areea
        total_Ai += Ai
    A = Ag + total_Ai
    return A

    A = calc
def earth_temp(L, daisies):
    nuemrator = S * L * (1 - calc_albedo(daisies)) # SL(1-A)
    denominator = SIGMA

    return (nuemrator/denominator)**0.25

def local_temp(daisy, daisies, L):
    temp_e = earth_temp(L, daisies)
    
    A = daisy.albedo

    temp_i = (Q * (calc_albedo(daisies) - A) + temp_e**4)**0.25

    return temp_i 

def calc_betta(daisy, daisies, L):
    temp_i = local_temp(daisy, daisies, L)
    betta = 1 - 0.003265 * (295.5 - temp_i)**2
    
    return betta

def calc_dw(daisy, daisies, L):
    x = calc_x(daisies)
    betta = calc_betta(daisy, daisies, L)

    dw = daisy.area * (x * betta - GAMMA)
    return dw

### SIMULATION 
def update_day(daisies, L):
    dw = {}

    for index, daisy in enumerate(daisies):
        dw[index] = calc_dw(daisy, daisies, L)
    
    for index, daisy in enumerate(daisies):
        daisy.update_area(dw[index])
        if (daisy.area <= 0):
          daisy.area = 0

def simulate_l(daisies, L, MAX_DAYS, DEFAULT_AREA):
    for day in range(MAX_DAYS):
        update_day(daisies, L)

    for daisy in daisies:
        daisy.record_data()
        if (daisy.area <= 0):
          daisy.area = DEFAULT_AREA
