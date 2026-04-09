def remove_duplicates(string) :
    result = ""
    for char in string :
        if char not in result :
            result += char

    return result 
string = input()
print(remove_duplicates(string))