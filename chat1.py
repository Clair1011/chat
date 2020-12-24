#讀取檔案
def read_file(filename):
	lines = []
	with open (filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

#轉換檔案
def convert(lines):
	new = []
	for line in lines:
		if line == '程沖':
			person = '程沖'
			continue
		elif line == '林秀珍':
			person = '林秀珍'
			continue
		elif line == '林秀鴻':
			person = '林秀鴻'
			continue
		elif line == '江慧婷':
			person = '江慧婷'
			continue
		new.append(person + ': ' + line)
	return new

#輸出轉換的檔案
def write_file(filename, lines):
	with open (filename,'w', encoding = 'utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')
def main():
	lines = read_file('chat.txt')
	#print(lines)
	lines = convert(lines)
	write_file('output.txt',lines)

#主程式進入點
main()