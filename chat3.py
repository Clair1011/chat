#取出檔案,存入清單
lines = []
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
	 for line in f:
	 	lines.append(line.strip())

#清單分割name, time
for line in lines:
	s = line.split('	')
	time = s[0][:7]
	name = s[0][7:]
	#print(time)
	print(name)