import time

################################################################################################################################################################

""" Question 1.A - Fibonacci - Brute force approach """

print('LAB-5 DAA')
print('Question 1 - Fibonacci series\n')

bf_count = 0  # to count how many times the brute force function gets called


def fibonacci_bf(num):
    if num <= 1:  # trivial case
        return num
    global bf_count
    bf_count += 1  # counter
    return fibonacci_bf(num - 2) + fibonacci_bf(num - 1)  # recursively calling the function


################################################################################################################################################################

""" Question 1.B - Fibonacci - Dynamic Programming and Memoization approach """


def fibonacci_dp(num):  # dynamic programming function
    tic = time.time()
    # outputs the n value's fibonacci number from the dictionary
    print('Fibonacci {0} = {1}'.format(num, fibonacci_mem(num, dict())))
    toc = time.time()
    return 'Time taken to get Fibonacci number: {}s'.format(f"{toc - tic:0.6f}")


def fibonacci_mem(num, mem_dict):  # memoization function
    if num in mem_dict:
        return mem_dict[num]  # returns the fibonacci value of n if already calculated

    if num in [0, 1]:
        mem_dict[num] = num  # trivial cases

    else:
        # if the n value and it's fibonacci number hasn't already been calculated, this calculates it and places it in the dictionary
        mem_dict[num] = fibonacci_mem(num - 1, mem_dict) + fibonacci_mem(num - 2, mem_dict)
    return mem_dict[num]  # returns the fibnacci value that corresponds to n


################################################################################################################################################################

""" Question 1.C - Fibonacci - Bottom Up approach (and space optimized) """


def fibonacci_botup(num):
    nums = [0, 1]
    tic = time.time()
    if num in nums:  # trivial cases
        return num

    # this loop gets the next fibonacci number while removing the first value in the list
    for x in range(num - 1):
        nums.append(nums[-1] + nums[-2])  # getting next fibonacci
        nums.pop(0)  # to keep list size constant
    toc = time.time()

    print('Fibonnaci  {0} = {1}'.format(num, "{:,}".format(nums[-1])))
    return 'Time taken to get Fibonacci number: {}s\n'.format(f"{toc - tic:0.6f}")


################################################################################################################################################################

# getting valid input
while True:
    try:
        num = int(input('Enter n for Fibonacci: '))
        break
    except:
        print('Enter valid positive integer!\n')
        continue

print('\nBrute Force approach - ')
tic = time.time()
print('Fibonacci {0} = {1}'.format(num, fibonacci_bf(num)))
toc = time.time()
print('Time taken to get Fibonacci number: {}s'.format(f"{toc - tic:0.6f}"))
print('The function was called {} times'.format(bf_count))
_ = input('\nPress anything to continue...\n')
print('Dynamic programming with memoization approach - ')
print(fibonacci_dp(num))
_ = input('\nPress anything to continue...\n')
print('Bottom to up approach - ')
print(fibonacci_botup(num))
