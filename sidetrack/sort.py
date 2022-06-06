import matplotlib.pyplot as plt
import statistics as stat

def main():
    with open("./prog1_scores.txt") as sfile:
        lines = sfile.readlines()
        scores = []
        for line in lines:
            words = line.split()
            scores.append(int(words[-1]))
        scores.sort()
        print(f"Mean was {stat.mean(scores)}")
        nless40 = 0
        for score in scores:
            if score < 40 and score != 0:
                nless40 += 1
        print(f"{nless40} out of 347 failed")
        plt.hist(scores, bins=20)
        plt.show()  

main()