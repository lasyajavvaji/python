from math import sqrt
def per_sqr(n):
    sr=int(sqrt(n))
    if sr*sr==n:
        return True
    return False
    
print(per_sqr(63))