import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.stats import norm
import glob
import math

# takes a list as input and returns CNF list
def cumulative_standard_normal(df_column):
	epsilon = 1e-10
	return norm.cdf(df_column)+epsilon

def get_random_standard_normal():
    return np.random.standard_normal()


# iso_data_path is the directory which contains list of matches
# in excel format, each match has excel file
# returns pandas dataframe 
def get_iso_data(iso_data_path):
	csv_files = glob.glob(f'{iso_data_path}/*.csv')
	filtered_csv_files = [file for file in csv_files if not file.endswith('_info.csv')]
	print(filtered_csv_files[0:5])
	df = pd.concat([pd.read_csv(file) for file in filtered_csv_files], ignore_index = True)
	# first innings data
	df = df[df['innings']==1]
	df.to_csv('../data/combined_output.csv', index = False)
	print(df[0:5])
	df = df[['match_id', 'start_date', 'innings', 'ball', 'runs_off_bat', 'extras', 'wicket_type']]
	df['wickets_indicator'] = df['wicket_type'].notna().astype(int)
	df['balls_remaining'] = 300 - ((df['ball'].astype(int) * 6) + ((df['ball'] * 10) % 10).astype(int))
		
	# Calculate wickets remaining for each match and innings
	df['wickets_fallen'] = df.groupby(['match_id', 'innings'])['wickets_indicator'].cumsum()
	df['wickets_remaining'] = 10 - df['wickets_fallen']

	print(df[270:300])
	return df

# computes prob of wide of no ball based on given data
def get_prob_of_wide_or_no_ball(iso_df):
	extras_runs = iso_df['extras'].sum()
	total_no_of_balls = iso_df['ball'].count()
	prob_of_wide_or_no_ball = extras_runs/(total_no_of_balls+extras_runs)
	print(f'extras_runss: {extras_runs}, total_no_of_balls:{total_no_of_balls}')
	return prob_of_wide_or_no_ball




# Estimating the wicket process
def LLF(params, iso_df):
	pass

def get_wicket_params(iso_df):
	pass

def get_prob_of_wicket(wicket_params, balls_remaining, wickets_remaining):
	ip = -wicket_params[0] - wicket_params[1]*balls_remaining - wicket_params[2]*wickets_remaining - wicket_params[3]*balls_remaining*balls_remaining
	print(f'input to prob of wicket: {ip}')
	res = cumulative_standard_normal(-wicket_params[0] - wicket_params[1]*balls_remaining - wicket_params[2]*wickets_remaining - wicket_params[3]*balls_remaining*balls_remaining)
	return res 

def get_wicket_process(wicket_params, balls_remaining, wickets_remaining):
	res = params[0] + params[1]*balls_remaining + params[2]*wickets_remaining + params[3]*balls_remaining*balls_remaining + get_random_standard_normal()
	return res




# Estimating the runs process
def get_run_params(iso_df):
	pass

def LLF_runs(params, iso_df):
	pass

def get_prob_of_run(run_params, balls_remaining, wickets_remaining):
	pass

def get_runs_process(run_params, balls_remaining, wickets_remaining):
	res = params[0] + params[1]*balls_remaining + params[2]*wickets_remaining + params[3]*balls_remaining*balls_remaining + get_random_standard_normal()
	return res





# distribution function , compute log loss and plot distributin function

# computes distribution function, see equation 1 in paper
def compute_distribution_function(runs, balls_remaining, wickets_remaining):
	pass

def test_input(balls_remaining, wickets_remaining):
	pass

def calculate_log_loss(iso_df):
	pass

def plot_distribution_function():
	pass



def main(args):
	iso_df = get_iso_data(args['iso_data_path'])
	prob_of_wide_or_no_ball = get_prob_of_wide_or_no_ball(iso_df)
	print(f'prob_of_wide_or_no_ball:{prob_of_wide_or_no_ball}')

	# Example usage of Std normal dist
	# random_value = get_random_standard_normal()
	# print("Random value from standard normal distribution:", random_value)

	# testing values
	balls_remaining = 10
	wickets_remaining = 2

	# estimating the wickets process
	wicket_params = get_wicket_params(iso_df)
	prob_of_wicket = get_prob_of_wicket(wicket_params, balls_remaining, wickets_remaining)
	print(f'prob_of_wicket for {balls_remaining}, {wickets_remaining}:{prob_of_wicket}')

	# estimating the runs process
	# run_params = get_run_params(iso_df)
	# prob_of_runs = get_prob_of_run(run_params, balls_remaining, wickets_remaining)
	# print(f'prob_of_run for {balls_remaining}, {wickets_remaining}: {prob_of_runs}')

	# # testing input 
	# iso_target_score = test_input(balls_remaining, wickets_remaining)


if __name__ == '__main__':
	args = {
        "iso_data_path":"../data/recently_added_2_male_csv2", # ensure that the path exists
        "iso_model_path":"../models/iso_model.pkl",
        "plot_path": "../plots/plot.png"  # ensure that the path exists
    }
	main(args)