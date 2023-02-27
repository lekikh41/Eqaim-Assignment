import json

def generate_steps(num1, num2):
    num1_str, num2_str = str(num1), str(num2)
    num1_len, num2_len = len(num1_str), len(num2_str)
    max_len = max(num1_len, num2_len)

    steps = {}
    carry = 0

    for i in range(max_len):
        idx1 = num1_len - i - 1
        idx2 = num2_len - i - 1

        digit1 = int(num1_str[idx1]) if idx1 >= 0 else 0
        digit2 = int(num2_str[idx2]) if idx2 >= 0 else 0

        digit_sum = digit1 + digit2 + carry
        carry = 1 if digit_sum >= 10 else 0
        digit_sum = digit_sum % 10

        step_name = f"step{i+1}"
        steps[step_name] = {"carryString": "1"*carry, "sumString": f"{digit_sum:02d}"}

    return steps

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

steps = generate_steps(num1, num2)
output_json = json.dumps(steps, indent=2)
print(output_json)
