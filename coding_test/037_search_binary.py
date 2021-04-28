def binary_search(array, target, start, end):
    if start>end:
        return None
    mid = (start+end) // 2