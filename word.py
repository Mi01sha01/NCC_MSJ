s = input().strip()
upper_case = sum(1 for c in s if c.isupper())
lower_case = len(s) - upper_case

if upper_case > lower_case:
    print(s.upper())
else:
    print(s.lower())