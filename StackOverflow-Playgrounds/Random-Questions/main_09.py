firstText = 'I LoVe LOVE You'

secondText = 'Love is a cool feeling love you too'

words_list = []

i = 0
for word in firstText.upper().split():
    if word in secondText.upper().split():
        if word not in " ".join(words_list).upper():
            words_list.append(firstText.split()[i])
    i += 1

print(words_list)
