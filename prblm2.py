'''
AUTHOR:INDHU SUBASH
DATE=19-11-24
'''
limit=int(input("Enter the limit:"))
i=0
s="*"
while i<limit:
  for i in range(limit,0,-1):
    print(s*i,end="\n")
  i=i+1
  break