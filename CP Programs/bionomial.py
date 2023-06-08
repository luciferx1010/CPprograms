def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)

# Example usage
N = 5
K = 2
C = binomial_coefficient(N, K)
print(f"The binomial coefficient C({N}, {K}) is: {C}")
