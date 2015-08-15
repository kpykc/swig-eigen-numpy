import pyinverter
import numpy as np

inv = pyinverter.Inverter()
m = np.array([[2.0, 0.0],
              [0.0, 2.0]])
print inv.getInverse(m)
print inv.getInversePlus1(m)

try:
    inv.getInverse("foo")
except Exception as e:
    print "Caught an expected error:", e