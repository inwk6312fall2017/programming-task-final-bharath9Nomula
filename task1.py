yf1=open('Book1.txt')
f2=open('Book2.txt')
f3=open('Book3.txt')

def longest_word():

 l1=""
 l2=""
 l3=""

 for line in f1:
  for word in line.split():

   if len(word)>len(l1):
    l1=word
 print('longest word in book1 is :',l1) 

 for line in f2:
  for word1 in line.split():
  
   if len(word1)>len(l2):
    l2=word1
 print('longest word in book2 is :',l2)


 for line in f3:
  for word2 in line.split():

   if len(word2)>len(l3):
    l3=word2
 print('longest word in book3 is :',l3)


longest_word()
