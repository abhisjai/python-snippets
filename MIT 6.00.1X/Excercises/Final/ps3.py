# Problem
# Numbers in Mandarin follow 3 simple rules.

#     There are words for each of the digits from 0 to 10.
#     For numbers 11-19, the number is pronounced as "ten digit", so for example, 16 would be pronounced (using Mandarin) as "ten six".
#     For numbers between 20 and 99, the number is pronounced as “digit ten digit”, so for example, 37 would be pronounced (using Mandarin) as "three ten seven". If the digit is a zero, it is not included.

# Here is a simple Python dictionary that captures the numbers between 0 and 10.

# trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
#           '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

# We want to write a procedure that converts an American number (between 0 and 99), written as a string, into the equivalent Mandarin.



def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    # FILL IN YOUR CODE HERE
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si','5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

    us_num_int = int(us_num)
    us_num_one = str(us_num_int % 10)
    us_num_tens = str(us_num_int // 10)
    
    mandarinStr = ''

    if us_num_int >= 0 and us_num_int <=10:
        mandarinStr = trans[us_num]
    elif us_num_int >= 11 and us_num_int < 20:
        mandarinStr = trans['10'] + ' ' + trans[us_num_one]      
    elif us_num_int >= 20 and us_num_int <= 99:
        if us_num_one == '0': 
            mandarinStr = trans[us_num_tens] + ' ' + trans['10']
        else:
            mandarinStr = trans[us_num_tens] + ' ' + trans['10'] + ' ' + trans[us_num_one]
    
    return mandarinStr


    
convert_to_mandarin('0')
convert_to_mandarin('1')
convert_to_mandarin('10')
convert_to_mandarin('11')
convert_to_mandarin('20') # will return er shi
convert_to_mandarin('21')
convert_to_mandarin('99')
convert_to_mandarin('36') # will return san shi liu
convert_to_mandarin('20')# will return er shi
convert_to_mandarin('16') # will return shi liu

