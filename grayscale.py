from PIL import Image
with Image.open(filename,'r') as im:
    pix_val = list(im.getdata())
    a= [x for sets in pix_val for x in sets]
   
count=0
m=[]
n=0
g=[]
for i in a:
    m.append(i)
    count+=1
    if count%3==0:      #if image is png use 4 everywhere inplace of 3 
        k=3
        g.append(m[n:n+k])
        n+=3


q=[]
for i in range(len(g)):
    p=max(g[i])

    i+=1
    q.append(p)


e=[y for x in q for y in 3*[x]]


b=[tuple(e[i:i+3]) for i in range(0, len(e), 3)]

list_of_pixels = list(b)

im2 = Image.new(im.mode, im.size)
im2.putdata(list_of_pixels)

im2.save(filename)
