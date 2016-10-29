#import matplotlib.pyplot as plt
from PIL import Image

def fractals(c=0, d=0, ax=0.0, ay=0.0, zx=1.0, zy=1.0, res=100.0):
    points = [[0]*(int(res+1.1)) for j in range(int(res+1.1))]
    for i in range(int(res+1.1)):
        for j in range(int(res+1.1)):
            z = ax+(zx-ax)*i/res + 1j*(ay+(zy-ay)*j/res)
            sid = 2
            for n in range(128):
                z = f(z, c, d)
                if abs(z) > 10:
                    points[i][j]=(sid, n)
                    break
                elif abs(z) < 0.5:
                    sid = 0
                elif abs(z-1) < 0.5:
                    sid = 1
            else:
                points[i][j] = (-1, z)
    return points

E1 = 1.02
E2 = 1.001
c1 = 2**(-0.5) *E1
c2 = 2**(-0.5) *E1
d1 = 0.8 *E2
d2 = 0.6 *E2

res = 5000
c=complex(c1,c2)
d=complex(d1,d2)
def f(z, c, d):
    return (c+d-2)*z*z*z + (3-2*c-d)*z*z + c*z

#clinfo=([0,10,25,60,99],[(0,0,0), (255,0,0), (128,128,0), (128,255,128), (0,0,0)])
#def colouring(n):
#    for i in range(len(clinfo[0])):
#        if n<=clinfo[0][i]: return tuple([(k*(n-clinfo[0][i-1]) + j*(clinfo[0][i]-n))//(clinfo[0][i]-clinfo[0][i-1]) for j,k in zip(clinfo[1][i-1],clinfo[1][i])])
#    return clinfo[1][-1]
clinfo = {-2:(0,0,0), -1:(255,0,0), 0:(0,255,0), 1:(0,0,255)}
def colouring(n):
    typ, dep = n
    if typ == -1:
        sid = (abs(dep-1) - abs(dep))/(abs(dep-1) + abs(dep))
        return (0, max(0, int(-sid*50)), max(0, int(sid*100)))
    
    if dep < 16:sh = 255 - 8*dep
    else: sh = 144 - dep
    
    ret = [0,0,0]
    ret[0] = sh ;ret[1] = sh//2
    if typ == 1:ret[1] += dep//2
    if typ == 0: ret[2] += dep//2
    return tuple(ret)

points = fractals(c, d, -1., -1.5, 2., 1.5, res)

im = Image.new('RGB',(res+1,res+1))
ip = im.load()
r=range(res+1)
for i in r:
    for j in r:
        ip[i,j]=colouring(points[i][res-j])

im.save("Julia_d3_c={0:6.4f}, {1:6.4f}, {2:6.4f}, {3:6.4f}.png".format(c1, c2, d1, d2))
im.show()

