#get numbers
#get operation
#do operation
#return result

def get_nums():
    numbers = []
    numbers.append(int(input("Provide first number: ")))
    numbers.append(int(input("Provide second number: ")))
    return numbers


def get_operation():
    while True:
        options = ['1','2','3','4']
        selection = input("What operation would you like to perform?\n"
                          "1) Add \n"
                          "2) Subtract\n"
                          "3) Multiply\n"
                          "4) Divide\n")
        if selection in options:
            return selection
        else:
            print("-------------------------\n"
                  "Please select from the following options.")


def main():
    print("Welcome to Calculator!")
    numbers = get_nums()
    operation = get_operation()
    match operation:
        case '1':
            result = numbers[0] + numbers[1]
        case '2':
            result = numbers[0] - numbers[1]
        case '3':
            result = numbers[0] * numbers[1]
        case '4':
            result = round(numbers[0] / numbers[1],8)
    print(f"Result: {result}")

main()

