# have /* */ comments, unlike C can nest. Comments can appear anywhere.

# must remove all comments from 1 "file" read from stdin. < 100K bytes (too big to store entire file)

# can we read line by line? how do we know when we're at the end of the file? get EOFError

# you can get a /*/ split across two lines, but still part of a comment.
def main():
    print("Case #1:")
    try:
        level = 0
        while True:
            # use python string manipulation
            line = input()
            keep = [True]*len(line)
            i_last = 0
            level = 0
            i = min(line.find("/*"), line.find("*/"))
            while i != -1:
                print(i)
                for j in range(i_last,i):
                    if level > 0:
                        keep[j] = False
                if line[i] == "/":
                    keep[i] = False
                    level += 1
                if line[i] == "*":
                    # avoid file starting with */ before a /*, and /*/
                    if level > 0 and i != i_last + 1:
                        level -= 1
                i_last = i
                i = min(line.find("/*", i_last+1), line.find("*/", i_last+1))
            out_line = ""
            for i in range(len(line)):
                if keep[i]:
                    out_line += line[i]
            if keep[len(line)-1]:
                print(out_line)
            else:
                print(out_line, end='')

    except EOFError as e:
        pass

main()