def merge_the_tools(string, k):
    # your code goes here
    l = len(string)//k
    for i in range(l):
        t = ''
        for c in string[i*k:i*k+k]:
            if c not in t:
                t += c
        print(t)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
