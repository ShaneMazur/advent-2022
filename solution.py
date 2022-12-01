def solution1(input_file: str)-> tuple[int,int]:
    with open(input_file) as f:
        meals = f.read()
    bags = [[int(meal) for meal in bag.split('\n')] for bag in meals.split('\n\n')]
    sorted_cals = sorted([sum(bag) for bag in bags])
    # return the top calorie count and the sum of the top 3 calorie counts
    return sorted_cals[-1], sum(sorted_cals[-3:])

if __name__ == '__main__':
    print(f"Day1 solution: {solution1('./inputs/day1.txt')}")