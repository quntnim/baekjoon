word = input().upper();wordlist = list(set(word));arr = []
for i in wordlist:
  arr.append(word.count(i))
if (arr.count(max(arr))>1):print("?")
else:print(wordlist[(arr.index(max(arr)))])