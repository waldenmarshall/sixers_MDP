# sixers_MDP
Matlab and Python code used in my ENGS 177 project on optimal policies for ''Sixers'' dice game

Classes:
  - MDPstate.m: Only includes attributes necessary to check legality/probability of transitions and generate state lists
  - CompleteState.m: Includes attributes and methods necessary to simulate a policy

Executables:
  - generating_states.py: creates 'states.txt' file with every possible nondecreasing sequence of dice values
  - create_states.mlx: uses 'states.txt' file to create 'states.mat' file with every possible MDPstate object
  - create_transition_matrices.mlx: uses 'states.mat' file to create transition probability matrices in two folders depending on which turn the transition is occuring at
  - determining_terminal_rewards_score.mlx: uses data files 'f_dv_scores.mat' and 'f_ts_scores.mat' to create 'terminal_rewards_by_score.mat' file which assigns a terminal reward based on the final score achieved
  - determining_terminal_rewards_state.mlx: uses 'terminal_rewards_by_score.mat' file to create 'terminal_rewards_by_state.mat' file which has the rewards indexed according to the states in 'states.mat'
  - solve_mdp.py: uses 'terminal_rewards_by_state.mat' and the transition probability matrices to create optimal policy file 'pi.txt'. This code was modified from coded provided by Wesley Marrero (https://engineering.dartmouth.edu/community/faculty/wesley-marrero) to Dartmouth College's ENGS 177 class
  - evaluate_optimal.mlx: uses the optimal policy 'pi.txt' to simulate many runs and store the scores of the optimal policy in 'scores_opt.mat'. Also evaluates many runs of the dice value threshold plicy from previous work using and stores in 'scores_fdv.mat'
  - create_dist_figure.mlx: visualizes data from 'scores_opt.mat'
  - head_to_head.mlx: creates visuals for comparing optimal policy to dice value threshold
