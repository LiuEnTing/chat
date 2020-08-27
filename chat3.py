#清單分割(時間與名字黏在一起成為一個[]處理方式)
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	time = s[0][:5]
	name = s[0][5:]
	print('聊天時間:', time, '名字:', name)
