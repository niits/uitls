def convert_message_to_number(message):
        number = 0
        for charater in message.upper():
            number = number * 26 + ord(charater) - 65
        
        return number
    
def convert_number_to_message(number):
    
    arr = []
    while number > 0:
        arr.append(chr(number % 26 + 65))
        number = number // 26
    
    return ''.join(arr[::-1])