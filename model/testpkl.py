# this file illustrates how to load these files

import pickle
import numpy as np

with open('wicket_params.pkl', 'rb') as file:
    wicket_params = pickle.load(file)

print(f'wicket_params: {wicket_params}')

with open('runs_params.pkl', 'rb') as file:
    runs_params = pickle.load(file)

print(f'runs_params: {runs_params}')

# Load the float value from the .npy file
px = np.load('px.npy')

print(f'px: {px}')  # This should print 3.14
# Load the float value from the .npy file
F = np.load('F.npy')

print(f'F:{F}')  # This should print 3.14