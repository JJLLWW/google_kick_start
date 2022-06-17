# have /* */ comments, unlike C can nest. Comments can appear anywhere.

# must remove all comments from 1 "file" read from stdin. < 100K bytes (too big to store entire file)

# can we read line by line? how do we know when we're at the end of the file? get EOFError

def find_first(s, sub1, sub2, i):
    j, k = s.find(sub1, i), s.find(sub2, i)
    if j == -1 and k == -1:
        return -1
    else:
        if j == -1:
            return k
        if k == -1:
            return j
        return min(j,k)

# you can get a /*/ split across two lines, but still part of a comment.
def main():
    print("Case #1:")
    try:
        cur_lvl = 0
        while True:
            line = input()
            level = [None]*len(line)
            i_last = 0
            i = find_first(line, "/*", "*/", 0)
            while i != -1:
                for j in range(i_last, i):
                    level[j] = cur_lvl
                if line[i] == "/":
                    cur_lvl += 1
                    level[i], level[i+1] = cur_lvl, cur_lvl
                    i += 1
                # we may get leading */ outside of any comment, if we are outside this may be the start of a /*
                elif line[i] == "*":
                    if cur_lvl > 0:
                        level[i], level[i+1] = cur_lvl, cur_lvl
                        cur_lvl -= 1
                        i += 1
                    else:
                        level[i] = cur_lvl
                i_last = i + 1
                i = find_first(line, "/*", "*/", i_last)
            # fill in remaining levels in the line (if necessary)
            for j in range(i_last, len(line)):
                level[j] = cur_lvl
            out_line = ""
            for i in range(len(line)):
                if level[i] == 0:
                    out_line += line[i]
            # if we end still in a comment skip the newline as well, watch out for "\n" lines.
            if len(line) == 0:
                # (!) if we are inside a comment we don't want the newline (!) - now passes both test cases.
                if not cur_lvl > 0:
                    print("")
            elif cur_lvl > 0:
                print(out_line, end='')
            else:
                print(out_line)
    except EOFError as e:
        pass

main()