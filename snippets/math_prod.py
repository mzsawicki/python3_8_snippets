import math

prior = 0.8
likelihoods = [0.625, 0.84, 0.30]
math.prod(likelihoods, start=prior)