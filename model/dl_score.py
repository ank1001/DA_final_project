import math
import numpy as np
params = np.load('DL_params.npy')
L = params[10]
Z0 = [0, params[0], params[1], params[2], params[3], params[4], params[5], params[6], params[7], params[8], params[9]]
# balls_remaining: for team 2
# wickets_remaining: for team 2
# updated_no_of_remaining_overs: after interruption how many more overs to play
def compute_DL_score( balls_remaining, wickets_remaining, updated_no_of_remaining_overs, Team1_score):
	u = balls_remaining//6 # overs remaining
	w = wickets_remaining
	v = updated_no_of_remaining_overs
	S = Team1_score
	Z_u_w = Z0[w]*(1 - math.exp((-L*u)/Z0[w]))
	Z_v_w = Z0[w]*(1 - math.exp((-L*v)/Z0[w]))
	Z_50_10 = Z0[10]*(1 - math.exp((-L*50)/Z0[10]))
	P_u_w = Z_u_w/Z_50_10 # frac of resc remaining
	P_v_w = Z_v_w/Z_50_10
	
	R2 = 1 - P_u_w + P_v_w # resc available for team 2
	T = S*R2 # par score
	par_score = math.ceil(T)
	return par_score

print(compute_DL_score(150, 1, 10, 250))