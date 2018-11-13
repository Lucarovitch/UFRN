name = []
i = 0
name.append('1')
name.append('2')
name.append('3')
name.append('4')
name.append('5')
name.append('6')
name.append('7')
for index, c in enumerate(name):
	if name[index] == '3':
		name[index] = 'teste'
	print(c)
print(name)

