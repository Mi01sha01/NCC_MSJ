h,m=map(int,input().split())
mins=h*60+m
if mins>=45:
    mins=mins-45
    h=mins//60
    m=mins%60
    print(h,m)
if mins<45:
    mins=24*60+m
    mins=mins-45
    h=mins//60
    m=mins%60
    print(h,m)    