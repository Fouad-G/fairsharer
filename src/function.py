def fair_sharer(values, num_iterations, share=0.1):
    """
    Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neighbor of the rightmost field.
    
    Args:
        values: 1D array of values (list or numpy array)
        num_iterations: Integer to set the number of iterations
        share: Fraction of value to share with neighbors (default is 0.1)
    
    Returns:
        values_new: Updated values after num_iterations
    """
    values = list(values)  # Ensure it's mutable
    n = len(values)
    for _ in range(num_iterations):
        max_idx = values.index(max(values))
        left_idx = (max_idx - 1) % n
        right_idx = (max_idx + 1) % n
        share_value = values[max_idx] * share
        values[max_idx] -= 2 * share_value
        values[left_idx] += share_value
        values[right_idx] += share_value
    return values
