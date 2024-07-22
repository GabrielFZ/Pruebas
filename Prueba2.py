import os

def last_number_before_sleep(N):
    if N == 0:
        return "INSOMNIA"
    
    multiple = 0
    seen_digits = set()
    while len(seen_digits) < 10:
        multiple += N
        seen_digits.update(str(multiple))

    return str(multiple)

def process_file():
    dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(dir, 'c-input.in')

    input = [int(w.rstrip()) for w in open(file)]
    
    if input[0] > 100 or input[0] < 1:
        print("The number of test cases T must be 1 ≤ T ≤ 100")   
    if len(input)-1 != input[0]:
        print("Error: T does not match")
    
    for i, case in enumerate(input[1:]):
        lastn = last_number_before_sleep(case)        
        print(f"Case #{i+1}: {lastn}")


if __name__ == "__main__":
    process_file()