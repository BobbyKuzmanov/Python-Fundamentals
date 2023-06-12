numbers = input().split(', ')
positive = [number for number in numbers if int(number) >= 0]
negatives = [number for number in numbers if int(number) < 0]
even = [number for number in numbers if int(number) % 2 == 0]
odd = [number for number in numbers if int(number) % 2 != 0]
print(f"Positive: {','.join(positive)}")
print(f"Negative: {','.join(negatives)}")
print(f"Even: {','.join(even)}")
print(f"Odd: {','.join(odd)}")
