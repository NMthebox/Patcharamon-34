def sum_of_squares(numbers):
    total = 0
    for n in numbers:
        total += n ** 2
    return total
nums = [50, 500, 5000]
result = sum_of_squares(nums)
print("ผลบวกกำลังสอง =", result)
