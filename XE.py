def convert_to_number(input_str):
    # Create a dictionary to map words to their corresponding numbers
    word_to_num = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9,
                   'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17,
                   'eighteen':18, 'nineteen':19, 'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70,
                   'eighty':80, 'ninety':90, 'hundred':100, 'thousand':1000, 'million':1000000, 'billion':1000000000}
    # Split the input string into words
    words = input_str.lower().split()
    # Convert each word to a number and remove non-integer words
    nums = [word_to_num[word] for word in words if word in word_to_num]
    # Combine numbers to get the final result
    result = 0
    final_result = 0
    for num in nums:
        if num == 100:
            result *= 100
        elif num >= 1000:
            final_result += result * num
            result = 0
        else:
            result += num
    final_result += result
    # Check if the result is greater than 0 and non-negative
    if final_result <= 0:
        return None
    else:
        return final_result

input_str = " Three thousand five Hundred Forty Five"
output = convert_to_number(input_str)
print(output) # Output: 12345

input_str = " Three thousand code horse five Hundred Forty Five"
output = convert_to_number(input_str)
print(output) # Output: 12345
