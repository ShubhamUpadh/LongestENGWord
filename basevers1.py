import csv

print("\t\t\t===== WORDOMINATOR ===== \n I will tell you the longest english word that doesn't contain the "
      "entered alphabets")

# x = [a for a in input("Enter the alphabets separated by comma(,) :: ").split(",")]
y = input("Enter the alphabets that the target word shouldn't contain ::")
z = list()
for alpha in y:
    if alpha.isalpha() and not alpha in z:
        z.append(alpha)

print(z)

# print(x)
lenWord = 0
longestWord = ""

with open("dictionaryedited.csv", mode='r') as file:
    fileF = csv.reader(file)
    for lines in fileF:

        flag = True

        for alphabet in z:
            if alphabet.lower() in str(lines) or alphabet.upper() in str(lines):
                flag = False
                break

        if flag and lenWord < len(str(lines)):
            longestWord = str(lines)
            lenWord = len(str(lines))

if longestWord == "":
    print("No such word exists")

else:
    print(longestWord)
