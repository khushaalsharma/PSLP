import random

def cointoss():
  return random.choice(["Heads","Tails"])

n = int(input("Enter no. of events:"))
headcnt = 0
for i in range(n):
  ans = cointoss()
  if(ans == "Heads"):
    headcnt = headcnt + 1

probhead = headcnt/n
probtail = (n-headcnt)/cnt

print("Heads probability: ",probhead)
print("Tails probability: ",probtail)
