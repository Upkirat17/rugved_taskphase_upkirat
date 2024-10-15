
n=input("Enter your number: ")

def check_hill_number(n):
    
    digits=[int(d) for d in str(n)]
    if len(digits)<3:
        return False
    
    increasing=True

    for i in range(1,len(digits)):
        if increasing:
            if digits[i] < digits[i-1]:
                increasing=False
            elif digits[i]==digits[i-1]:
                return False
        
        else:
            if digits[i]>=digits[i-1]:
                return False

    return not increasing

print(check_hill_number(n))