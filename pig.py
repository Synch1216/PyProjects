#get sentence from user

original= input("Enter your sentence:").strip().lower()

# store each group of letters, separated by [" "] in iterable list. Here I will use the .split() on original.
sentence= original.split()



# For each item in WORD, IF it begins with a vowel- append 'yay' at the end of the word.
new_words=[]
for item in sentence:
    if item[0] in "aeiou":
        new_word= item + "ay"
        new_words.append(new_word)
    else:
        vowel_pos= 0
        for letter in item:
            if letter not in "aeiou":
                vowel_pos= vowel_pos +1
            else:
                break
        cons=item[:vowel_pos]
        the_rest= item[vowel_pos:]
        new_word= the_rest +cons +"ay"
        new_words.append(new_word)


    output= " ".join(new_words)

    print(output)

#   If item != "aeiou" , then cut first two letters of word and append to the end of the word.

#   append "yay" to the end of the word.

#output final string.