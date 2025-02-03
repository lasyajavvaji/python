def jump(h,s,w,m):
    count=0
    for i in m:
        if i==h or i<h:
            count=count+1
        else:
           jumps=0
           current_heigt=0
           while current_height<i:
               jumps+=1
               current_height+=h
               if current_height>=i:
                   break
                current_height-=y
            count+=jumps
    return count
            
   

            
            
            
hei=int(input())
slide=int(input())
wall=int(input())
len=int(input())
meters=[]
while len>0:
    ele=int(input())
    meters.append(ele)
    len=len-1

print(jump(hei,slide,wall,meters))

