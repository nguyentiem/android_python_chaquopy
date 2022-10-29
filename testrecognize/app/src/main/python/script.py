import numpy as np
def main(a,b):
   out = np.arange(5)
   a = np.int64(a)
   b = np.int64(b)
   out = out.astype(np.int64)
   out +=a
   out -=b
   return out