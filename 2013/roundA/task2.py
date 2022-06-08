# use python as task involves heavy string processing and nothing else

nums = {0: "zero", 1 : "one", 2 : "two", 3 : "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
mults = {2: "double", 3: "triple", 4: "quadruple", 5: "quintuple", 6: "sextuple", 7: "septuple", 8: "octuple", 9: "nonuple", 10: "decuple"}

def read_out(str):
    res = ""
    i = 0
    while i != len(str):
        cur_dig = int(str[i])
        nrep = 0
        while (i != len(str)) and (int(str[i]) == cur_dig):
            nrep += 1
            i += 1  
        if nrep in range(2, 11):
            res += (mults[nrep] + " " + nums[cur_dig] + " ")
        else:
            res += (nums[cur_dig] + " ")*nrep
    return res

def solve(num, fmt):
    res = ""
    parts = fmt.split(sep='-')
    parts = [int(part) for part in parts]
    i = 0
    for part in parts:
        substr = num[i:i+part]
        res += read_out(substr)
        i += part
    # remove the trailing space
    return res[0:len(res)-1]

def main():
    ncase = int(input())
    for case in range(1, ncase+1):
        words = input().split()
        res = solve(words[0], words[1])
        print(f"Case #{case}: {res}")

main()