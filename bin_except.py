class TargetNotFound(Exception):
    """Exception raised when the target is not found in the list."""
    pass


def bin_except(lst, target):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]

        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    raise TargetNotFound("Target not found in the list.")