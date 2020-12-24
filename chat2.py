#讀取檔案
def read_file(filename):
	lines = []
	with open (filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

#轉換檔案
def convert(lines):
	ella_count = 0
	ella_sticker_count = 0
	ella_img_count = 0
	wei_count = 0
	wei_sticker_count = 0
	wei_img_count = 0
	for line in lines:
		s = line.split('	')
		time = s[0]
		name = s[1]
		if name == '憶慧':
			if s[2] == '貼圖':
				ella_sticker_count += 1
			elif s[2] == '圖片':
					ella_img_count += 1
			else:
				for m in s[2:]:
					ella_count += len(m)
		elif name == '薇羽':
			if s[2] =='貼圖':
				wei_sticker_count += 1
			elif s[2] == '圖片':
					wei_img_count += 1
			else:
				for m in s[2:]:
					wei_count += len(m)
	print('憶慧字數: ', ella_count, '字', ella_sticker_count ,'個貼圖', ella_img_count ,'個圖片')
	print('薇羽字數: ', wei_count, '字', wei_sticker_count, '個貼圖' , wei_img_count, '個圖片')

#輸出轉換的檔案
# def write_file(filename, lines):
# 	with open (filename,'w', encoding = 'utf-8-sig') as f:
# 		for line in lines:
# 			f.write(line + '\n')
def main():
	lines = read_file('[LINE].txt')
	#print(lines)
	convert(lines)
	# write_file('output.txt',lines)

#主程式進入點
main()