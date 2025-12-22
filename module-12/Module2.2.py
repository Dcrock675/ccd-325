def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

def main():
    nums = [10, 20, 30, 40, 50]
    avg = calculate_average(nums)
    print("The average is:", avg)

main()
