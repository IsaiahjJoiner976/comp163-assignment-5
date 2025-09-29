step_count = 0

print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number: Sequence: "))
print(current_number, end=" ")
while current_number > 1:
    if current_number % 2 == 0:
        current_number //= 2
    else:
        current_number = current_number * 3 + 1
    step_count += 1
    if current_number == 1:
        print(current_number, end="")
        break
    else: 
        print(current_number, end=" ")
print(f"\nSteps: {step_count}")
print()

print("=== Challenge 2: Prime Number Checker ===")
current_number = int(input("Enter a number: "))
print(f"Testing divisors from 2 to {current_number - 1}...")
if current_number > 1:
    if current_number % 3 != 0:
        print(f"{current_number} is prime!")
        print()
    else:
        print(f"{current_number} is not prime (divisible by 3)")
        print()
