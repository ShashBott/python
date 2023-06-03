dic=dict()

file1=open(r'E:\dir\rhyme.txt','r')

f1=file1.read()

f1=f1.lower()

words=f1.split()

for word in words:

  if word in dic:

    dic[word] = dic[word] + 1

  else:

    dic[word] = 1



file2= open(r'E:\dir\words.txt','w')

file2.write(str(dic))

file2=open(r'E:\dir\words.txt','r')

print(file2.read())

file1.close()

file2.close()
