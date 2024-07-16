def count_substring(string, sub_string):
    for i in count_substring:
        if string[i] == sub_string[i]:
    return string.count(string)+sub_string.count(sub_string)

string = input().strip()
sub_string = input().strip()
    
count = count_substring(string, sub_string)
print(count)
