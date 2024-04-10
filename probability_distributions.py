import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kurtosis, skew

# UNIFORM DISTRIBUTION
# Generate random numbers uniformly distributed between -1 and 1
uniform_data = np.random.uniform(-1, 1, 1000)

# Plot a Histogram of the distribution
plt.hist(uniform_data, bins=20, density=True)
plt.title("Uniform Distribution")
plt.show()

# NORMAL DISTRIBUTION
# Generate Normal Distribution data
normal_data = np.random.normal(loc=0, scale=1, size=1000)

# Plot a Histogram of the distribution
plt.hist(normal_data, bins=20, density=True)
plt.title("Normal Distribution")
plt.show()

# Calculate properties
mean = np.mean(normal_data) # Mean
var  = np.var(normal_data) # Variance
skew = skew(normal_data) # Skewness
kurt = kurtosis(normal_data) # Kurtosis

# Print the results
print("Mean: ", round(mean, 2)) # a função round do Python pode ser utilizada para arredondar casas decimais => A função round() aceita dois argumentos: o primeiro é o número que você deseja arredondar e o segundo é o número de casas decimais para as quais você deseja arredondar. Neste caso, 2 é usado para arredondar para duas casas decimais.
print("Variance: ", round(var, 2))
print("Skew : ", round(skew, 2))
print("Kurtosis: ", round(kurt, 2))