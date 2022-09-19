DATA_PATH = '../ex00/data.csv'
DATA_HAS_HEADER = True
N_OF_PREDICTIONS = 3
HAS_HEADER = True
REPORT="""Report
We have made {n_obs} observations from tossing a coin: {tails} of them were tails and {heads} of \
them were heads. \nThe probabilities are {p_tails:.2f}% and {p_heads:.2f}%, respectively.\
Our forecast is that in the next {n_preds} observations we will have: {pr_tails} tails and {pr_heads} heads."""