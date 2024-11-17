
a,b,c,d,e,f = 2,3,4,5,6,6




def myfunc(a,b, *args, **kwargs):
   for ar in args:
      print ar
myfunc(a,b,c,d,e,f)
