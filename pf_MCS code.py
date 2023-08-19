import numpy as np

# Define input distributions
mean = 0
std_dev =1.0

U1 = np.random.normal(mean, std_dev, size=100000)
U2 = np.random.normal(mean, std_dev, size=100000)

# Evaluate limit-state function for each sample
#G2={((U1-3)^2)/(2)^2}+{((U2-2)^2)/(1)^2}-1
G2 = ((U1 - 3)**2) / (2**2) + ((U2 - 2)**2) / (1**2) - 1


# Count number of failed simulations
num_failed = np.count_nonzero(G2 <= 0)

# Estimate probability of failure
pf_MCS = num_failed / len(G2)

print("shape", U1.shape)
print("shape", U2.shape)
print("total number of samples in U1:", len(U1))
print("total number of samples in U2:", len(U2))
print("U1 samples:", U1)
print("U2 samples:", U2)
print("mean of U1:", U1.mean())
print("mean of U2:", U2.mean())
print("standard deviation of U1:", U1.std())
print("standard deviation of U2:", U2.std())
print("TOTAL NUMER OF FAIL SUMULATION ",num_failed )
print("pf_MCS =", pf_MCS)
