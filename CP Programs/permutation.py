def permute(elements):
    # Base case: if there's only one element, return it as a single-element list
    if len(elements) == 1:
        return [elements]

    # List to store permutations
    permutations = []

    # Generate permutations for each element in the list
    for i in range(len(elements)):
        # Extract the current element
        current = elements[i]

        # Generate permutations of the remaining elements
        remaining = elements[:i] + elements[i+1:]
        sub_permutations = permute(remaining)

        # Add the current element to each permutation of the remaining elements
        for permutation in sub_permutations:
            permutations.append([current] + permutation)

    return permutations

# Example usage
elements = ['A', 'B', 'C']
result = permute(elements)
print(result)
