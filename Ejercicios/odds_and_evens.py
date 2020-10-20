import math
import sys
from statistics import mean

def odds_and_evens(numbers):
    odds = []
    even = []
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odds.append(number)
    return odds, even

def print_stats(string, list_of_numbers):
    if len(list_of_numbers) > 0:
        print(string + ". #Elements:", len(list_of_numbers), "Sum of elements:", sum(list_of_numbers), "Average:", round(mean(list_of_numbers),2), "Smallest:", min(list_of_numbers), "Greatest:", max(list_of_numbers))
    else:
        print(string + ". #Elements:", len(list_of_numbers), "Sum of elements:", sum(list_of_numbers), "Average: N/A", "Smallest: N/A", "Greatest: N/A")

all_numbers = []

while True:
    data = input().strip()
    if data == '*':
        break
    try:
        num = int(math.floor(float(data)))
        all_numbers.append(num)
    except:
        print('ERROR')
        sys.exit()
        
odds_numbers, even_numbers = odds_and_evens(all_numbers)
print_stats("All numbers", all_numbers)
print_stats("Odds", odds_numbers)
print_stats("Evens", even_numbers)