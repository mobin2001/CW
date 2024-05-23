S1 = input()
S2 = input()

middle_S1 = len(S1) // 2

S3 = S1[0:middle_S1] + S2 + S1[middle_S1:]

print(S3)