import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

# Suppose we're analyzing the number of card games won out of 10 night games, it is a binomial distribution
np.random.seed(42) # for reproducibility
card_game_wins = np.random.binomial(10, 0.5, 10000)

# Visualizing the distribution
plt.hist(card_game_wins, bins=11, alpha=0.5, color='b')
plt.show()

# We simulate a card game where you have equal chances (Uniform distribution) to draw any card between 1 and 14
cards = np.random.uniform(1, 15, 10000)

# We visualize the results
plt.hist(cards, bins=14, alpha=0.5, color='b') 
plt.show()

# Generate card data
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cards = [f'{rank} of {suit}' for suit in suits for rank in ranks]

card_data = np.random.choice(cards, size=520, replace=True)
# This code creates a list of all possible cards, with 13 ranks for each of the 4 suits. It then uses the np.random.choice function to randomly select 520 cards from the list, with replacement. This simulates drawing cards from a well-shuffled deck, where there is an equal probability of drawing any card. The resulting card_data array will contain 520 strings representing randomly selected cards.

# Visualizes the distribution using a histogram
plt.hist(card_data, bins=52, alpha=0.5, color='r')
plt.show()

# TODO: Generate 1000 data points between 0 and 10 using numpy's random.uniform()

# Generate 1000 data points
data_points = np.random.uniform(0, 10, 1000)

# Plot a histogram of a uniform distribution
plt.hist(data_points, bins=20, color='g')    # Visualising score distribution
plt.show()

# Displaying skewness and kurtosis for the scores
print("Skewness: {:.2f}".format(skew(data_points)))
print("Kurtosis: {:.2f}".format(kurtosis(data_points))) # Displaying skewness and kurtosis for the scores

# Generate test scores for 10,000 students
test_scores = np.random.normal(loc=6, scale=1.5, size=10000)

# Scale the test scores to be out of 10
test_scores = test_scores / 1.5 * 10

# Plot a histogram of the test scores
plt.hist(test_scores, bins=20, alpha=0.5, color='b')  # Visualising score distribution
plt.show()

# Display the skewness and kurtosis of the test scores
print("Skewness: {:.2f}".format(skew(test_scores)))
print("Kurtosis: {:.2f}".format(kurtosis(test_scores)))  # Displaying skewness and kurtosis for the scores