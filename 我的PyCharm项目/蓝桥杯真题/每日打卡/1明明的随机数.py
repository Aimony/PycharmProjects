while True:
    try:
        n = int(input())
        num_set = set()
        for i in range(n):
            num_set.add(int(input()))

        nums = list(num_set)
        nums.sort()
        for i in nums:
            print(i)
    except:
        break