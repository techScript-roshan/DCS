#from sympy import symbols, Eq, solve, Symbol, sqrt
from IPython.display import display, Markdown, Latex
import numpy as np, matplotlib.pyplot as plt
import handcalcs.render, forallpeople, math
forallpeople.environment('structural', top_level=True)
pi = math.pi
sqrt = math.sqrt

# Possible grades of reinforcement used in structural design (using a dictionary)
steel_rebar_grades = {
    'Fe 250': 250 * MPa,
    'Fe 415': 415 * MPa,
    'Fe 500': 500 * MPa
}

# Possible grades of cement concrete used in structural design (using a dictionary)

E_s = 200 * 10 ** 3 * MPa
E_c = 20 * 10 ** 3 * MPa

concrete_grades = {
    'M 20': 20 * MPa,
    'M 25': 25 * MPa,
    'M 30': 30 * MPa,
    'M 35': 35 * MPa,
    'M 40': 40 * MPa,
    'M 45': 45 * MPa,
    'M 50': 50 * MPa,
    'M 55': 55 * MPa
}

