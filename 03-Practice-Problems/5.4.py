def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        return is_an_ip_number(word)
            
    return True

def is_an_ip_number(string):
    try:
        if int(string) in range(0,256):
            return True
        else:
            return False
    except ValueError:
        print("Invalid Entry")