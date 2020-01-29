def func():
  print("mini=5rs/perkm   micro= 3rs/perkm   premium=10rs/perkm")
  a=int(input("enter source point:"))
  if (a < 0):
      a = a * -1
  b=int(input("enter destination point"))
  if (b < 0):
    b = b * -1
  r=b-a
  if(r<0):
    r=r*-1
  print("1.mini    2.micro    3.premium ")
  d=(int(input("Enter your option")))
  mini=5
  micro=3
  premium=10
  if(d==1):
    print("your fare is",r*mini)
  if(d==2):
    print("your fare is", r*micro)
  if(d==3):
    print("your fare is", r*premium)
  m = str(input("Do you want taxi? yes/no"))
m=str(input("Do you want taxi? yes/no"))
func()
while(m=='yes'):
    func()
