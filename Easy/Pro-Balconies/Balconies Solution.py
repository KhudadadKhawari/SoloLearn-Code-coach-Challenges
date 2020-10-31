A = input().split(",")
B = input().split(",")

balconeyA = int(A[0]) * int(A[1])
balconeyB = int(B[0]) * int(B[1])

print("Apartment A") if balconeyA > balconeyB else print("Apartment B")