weights = [25, 30, 40, 55, 76, 77, 82, 85, 90, 94, 123, 134]
maxsize = 132


def sack(index, space_left):
    if index == 0 or space_left == 0:  # base case
        return 0
    elif weights[index] > space_left:  # skip if current element doesn't fit
        return sack(index - 1, space_left)
    else:
        way1 = sack(index - 1, space_left)
        way2 = weights[index] + sack(index - 1, space_left - weights[index])
        return max(way1, way2)  # find the most optimal variant through recursion


print(sack(len(weights)-1, maxsize))  # print out the result
