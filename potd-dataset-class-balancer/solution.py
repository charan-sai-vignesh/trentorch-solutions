from typing import List


def dataset_class_balancer(counts: List[int]) -> List[float]:
    """
    counts: non-negative class counts, length C, summing to N.

    For each class c with count n_c > 0, return N / (C * n_c). A class
    with n_c == 0 gets weight 0 (and so does every class if N == 0).
    """
    N = sum(counts)
    C = len(counts)
    weights = []
    for count in counts:
        if count == 0:
            weights.append(0.0)
        else:
            weight = N / (C * count)
            weights.append(round(weight, 6))

    return weights
