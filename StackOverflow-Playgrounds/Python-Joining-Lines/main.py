new_log = str()

with open("input-test.txt", 'r') as input_file:
	lines = [line[37:-1] for line in input_file.readlines()]
	lines = [l for (i,l) in enumerate(lines) if i%4!=3]

	remastered = list()
	i = 0
	while i < len(lines):
		remastered.append(f"{lines[i]} | {lines[i+2]} | {lines[i+1]}")
		i += 3

	new_log = '\n'.join(remastered)

with open("new_log.txt", 'a') as input_file:
	input_file.write(new_log+'\n')