n=int(input())
list1 = []
list2 = []
for i in range(n):
        user_input = int(input())
        list1.append(user_input)
for i in range(n):
        user_input = int(input())
        list2.append(user_input)
summarize = []
def summation(n):
  for i in range(n):
      summarize.append(list1[i]+list2[i])
  return summarize
def find_min_max():
      min= summarize[0]
      max= summarize[0]
      for i in range(len(summarize)):
            if summarize[i] > max:
                  max = summarize[i] 
            if summarize[i] < min:
                  min = summarize[i] 
      return min,max
print(summation(n))
print(find_min_max())
