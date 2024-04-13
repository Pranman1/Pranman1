import qsharp
import azure.quantum


qsharp.init(project_root = r"C:\Users\prana\OneDrive\tess\tro")
a = qsharp.eval("Sample.RandomNBits(10)")

def bitstringtoint(a):
    total = 0
    n = 0
    for b in a:
        total = total + int(b) * 2^n
        n +=1
    return total

print(bitstringtoint(a))
