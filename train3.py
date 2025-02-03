late=int(input())
grace=int(input())
fee=int(input())
charged=int(input())
days=0
total=0
if late>grace:
    days=late-grace
    total=days*fee
    if total>charged:
        print(charged)
    else:
        print(total)
