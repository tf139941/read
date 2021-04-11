# 讀取檔案
# strip() 除掉換行符號 \n

data = []
count = 0
with open('reviews.txt', 'r') as f: # 將檔案當成f 'r' = read讀取模式, 'w' = write寫入模式
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

print(len(data))

print(data[0])
print('-----------------')
print(data[1])