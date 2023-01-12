def isAnagram(s: str, t: str) -> bool:
    # 哈希表法
    record = [0] * 26
    for i in range(len(s)):
        # 不用记住字符的ASCII值 只需要记录差值
        record[ord(s[i]) - ord("a")] += 1
    print(record)
    for i in range(len(t)):
        record[ord(t[i]) - ord("a")] -= 1
    for i in range(26):
        if record[i] != 0:
            return False
    return True


s = input("Please input your first word:")
t = input("Please input your first word:")
if(isAnagram(s,t)):
    print("Yes,they are!")
