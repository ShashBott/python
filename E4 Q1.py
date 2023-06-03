def count_substring(string, sub_string):
    c = 0
    for i in range(len(string)):
       if string[i:].startswith(sub_string):
          c = c + 1
    return c


string = input("Enter a string ").strip()
sub_string = input("Enter a sub string ").strip()
count = count_substring(string, sub_string)
print(count)
