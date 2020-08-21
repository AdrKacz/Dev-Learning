with open("log.txt","r") as file:
    all_text = file.readlines()

parsed_line = list()
for text in all_text:
    parsed_line.append(dict([item.split('":"') for item in text[2:-2].split('","')]))

    