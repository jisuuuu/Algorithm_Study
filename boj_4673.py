#셀프 넘버

all_num = set(range(1, 10001))
generate_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generate_num.add(i)

self_num = sorted(all_num - generate_num)
for n in self_num:
    print(n)