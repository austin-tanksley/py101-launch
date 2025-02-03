import pdb

def prompt(message):
    print(f"==> {message}")

def invalid_amount(amount):
    try:
        float(amount)
    except ValueError:
        return True
    if float(amount) <= 0:
        return True
    
    return False

def invalid_apr(apr):
    try:
        float(apr)
    except ValueError:
        return True
    apr = float(apr)
    if apr < 0:
        return True
    elif apr > 100:
        return True
    
    return False

def get_info():
    invalid_response = ("Input invalid. Please enter a valid")
    prompt("Enter borrowed amount:")
    loan_amount = input()

    while invalid_amount(loan_amount):
        prompt(f"{invalid_response} amount:")
        loan_amount = input()
    loan_amount = round(float(loan_amount), 2)

    prompt("Enter APR(--%):")
    apr = input()

    while invalid_apr(apr):
        prompt(f"{invalid_response} APR:")
        apr = input()
    apr = float(apr) / 100

    prompt("Enter duration of loan in months:")
    duration = input()

    while invalid_amount(duration):
        prompt(f"{invalid_response} duration:")
        duration = input()
    duration = int(duration)

    return [loan_amount, apr, duration,]

def calculate_payment(loan_amount, apr, duration):
    monthly_interest = apr / 12
    payment = loan_amount * (monthly_interest / ( 1 - ((1 + monthly_interest) ** (-duration))))
    return payment

def main():
    prompt("Welcome to Loan Calculator!")
    info = get_info()
    monthly_payment = calculate_payment(info[0], info[1], info[2])
    print(f"${monthly_payment:.2f}")
main()