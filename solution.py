# Day 1
def solution1(input_file: str)-> tuple[int,int]:
    with open(input_file) as f:
        meals = f.read()
    bags = [[int(meal) for meal in bag.split('\n')] for bag in meals.split('\n\n')]
    sorted_cals = sorted([sum(bag) for bag in bags])
    # return the top calorie count and the sum of the top 3 calorie counts
    return sorted_cals[-1], sum(sorted_cals[-3:])

def solution1_oneliner(input_file: str)-> tuple[int,int]:
    return tuple(f(sorted([sum([int(meal) for meal in bag.split('\n')]) for bag in open(input_file).read().split('\n\n')])[-3:]) for f in (max, sum))

# Day 2
def solution2(input_file: str)-> tuple[int,int]:
    with open(input_file) as f:
        rounds = f.read().splitlines() 
    scores_p1 = []
    scores_p2 = []
    for round in rounds:
        # part 1
        shape_m1 = (ord(round[-1])-1)%3+1
        m1 = 6-3*((ord(round[0])-ord(round[-1]))%3)
        scores_p1.append(shape_m1+m1)
        # part 2
        shape_m2 = 1+(ord(round[0])-2+((ord(round[-1])-1)%3-1))%3
        m2 = 3*((ord(round[-1])-1)%3)
        scores_p2.append(shape_m2+m2)
    return sum(scores_p1), sum(scores_p2)

def solution2_oneliner(input_file: str)-> tuple[int,int]:
    return sum((ord(round[-1])-1)%3+1+6-3*((ord(round[0])-ord(round[-1]))%3) for round in open(input_file).read().splitlines()),sum(1+(ord(round[0])-2+((ord(round[-1])-1)%3-1))%3+3*((ord(round[-1])-1)%3) for round in open(input_file).read().splitlines())

if __name__ == '__main__':
    # Day1
    print(f"Day1 solution: {solution1('./inputs/day1.txt')}")
    print(f"Day1 solution: {solution1_oneliner('./inputs/day1.txt')}")
    assert solution1('./inputs/day1.txt') == solution1_oneliner('./inputs/day1.txt')
    # Day2
    print(f"Day2 solution: {solution2('./inputs/day2.txt')}")
    print(f"Day2 solution: {solution2_oneliner('./inputs/day2.txt')}")
    assert solution2('./inputs/day2.txt') == solution2_oneliner('./inputs/day2.txt')