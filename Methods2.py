def reverse_string(text):
    result = ""
    for i in range(len(text)-1, -1, -1):
        result += text[i]
    return result

text = input("Enter a string and I will reverse it: ")
print(f"{text} reversed is: {reverse_string(text)}")