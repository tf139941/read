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

print('檔案讀取完成, 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)

print('留言的平均長度為', sum_len / len(data))
