a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=int(input('d='))
def adunare_fractii(x,y,z,q):
    return (((x*d)+(y*z))/(y*q))

def inmultire_fractii(x,y,z,q):
    return ((x*z)/(y*q))
print(adunare_fractii(a,b,c,d))
print(inmultire_fractii(a,b,c,d))
