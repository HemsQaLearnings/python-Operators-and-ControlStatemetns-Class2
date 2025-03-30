a = 10
b = 10
print ('Line 1','a=',a ,':',id(a), 'b=',b ,':',id(b))
if ( a is b ):
  print ("Line 2 - a and b have same identity")
else:
  print ("Line 2 - a and b do not have same identity")
# --------------------case 2---------------------------------
print("------------------------------------------------")
x = 10
y = 20
print ('Line 1','x=',x ,':',id(x), 'y=',y ,':',id(y))
if ( x is y ):
  print ("Line 2 - x and y have same identity")
else:
  print ("Line 2 - x and y do not have same identity")
  print("------------------------------------------------")
  print("Happy Learnings @hemsqalearnings")