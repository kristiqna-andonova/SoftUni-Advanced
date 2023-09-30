def numbers(*args):
    negative_sum = 0
    positive_sum = 0

    for num in args:
        if num < 0:
            negative_sum += num
        else:
            positive_sum += num

    return negative_sum, positive_sum


number = [int(x) for x in input().split()]
print(numbers(*number)[0])
print(numbers(*number)[1])

if abs(numbers(*number)[0]) > numbers(*number)[1]:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")


