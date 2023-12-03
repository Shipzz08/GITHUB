def find(arr):
    l = len(arr)
    if l == 1:
        print(*arr)
    else:
        thresh = int(l / 3)
        counts = {}  
        ans = []

        for num in arr:
            counts[num] = counts.get(num, 0) + 1

        for key, value in counts.items():
            if value > thresh:
                ans.append(key)

        print(*ans)
        

user_input=input()
array = list(map(int, user_input.split()))
find(array)