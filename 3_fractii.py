x=int(input('x='))
y=int(input('y='))
z=int(input('z='))
k=int(input('k='))
def adunare_fractii(a,b,c,d):
    return (((a*d)+(c*b))/(b*d))

def inmultire_fractii(a,b,c,d):
    return ((a*c)/(b*d))
print(adunare_fractii(x,y,z,k))
print(inmultire_fractii(x,y,z,k))
