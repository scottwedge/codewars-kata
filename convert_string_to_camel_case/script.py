#!/usr/bin/env python3

text = "a_cat-Was_kawaii"

def split_and_cap(text, sepr):
    # Split on character ("-") into list of strings
    text_list = text.split(sep = sepr)

    # Capitalize first letter of all except first word in list
    # cannot use 'capitalize' method since it converts upper case inside word to lower case
    for j in range(1,len(text_list)):
        text_list[j] = text_list[j][0].upper() + text_list[j][1:]
         
    # Add all words together into a new string
    new_text = text_list[0]  # Init string 
    for j in range(1, len(text_list)):
        new_text = new_text + text_list[j]
    return new_text
    

def to_camel_case(text):
    # Split on character ("-") and capitalize all but first word
    print(text)
    t = split_and_cap(text, "-")
    print(t)
    t = split_and_cap(t, "_")
    print(t)
    return t
    

t = to_camel_case(text)
