def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	new = []
	person = None #跟NULL一樣意思，無值
	allen_word_count = 0
	viki_word_count= 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0
	viki_image_count = 0
	
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for ss in s[2:]:
					allen_word_count += len(ss)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count +=1
			else:
				for ss in s[2:]:
					viki_word_count += len(ss)
		print('allen說',allen_word_count, '字', '並且傳了', allen_sticker_count, '張貼圖', '及', allen_image_count,'張圖片')
		print('viki說',viki_word_count, '字', '並且傳了', viki_sticker_count, '張貼圖', '及', viki_image_count, '張圖片' )
	return new


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('LINE-Viki.txt')
	convert(lines)
	lines = convert(lines)
	#write_file('output.txt',lines)
main()