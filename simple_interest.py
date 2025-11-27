import sys
if len(sys.argv) == 4:
    script_name=sys.argv[0]
    principal=float(sys.argv[1])
    rate=float(sys.argv[2])
    time=float(sys.argv[3])
else:
    principal=1000.0
    rate=5.0
    time=10
simple_interest=(principal * rate * time) / 100
print("principal Amount is",principal)
print("rate of interest is",rate)
print("time period is",time)
print("simple interest is",simple_interst)
