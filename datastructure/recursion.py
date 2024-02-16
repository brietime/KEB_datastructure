def decimal_to_octal(number:int) -> str:
    """
    decimal_to_octal 
    param:
        number (int): base dec

    return:
        str: base octal
    """
    if number < 8:
        return str(number)
    else:
        return decimal_to_octal(n//8) + str(n % 8)
    
    
    # octal = ''
    # while number >0:
    #     octal = str(number %8) + octal
    #     number = number // 8
    # return octal

n = int(input("Enter decimal number: "))
print(decimal_to_octal(n))