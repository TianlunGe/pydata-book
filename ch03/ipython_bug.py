def works_fine():
    a = 5
    b = 6
    assert(a + b == 11)

def throws_an_exception():
    a = 5
    b = 6
    assert(a + b == 10)

def calling_things():
    works_fine()
    throws_an_exception()

# calling_things()

print(str.title('asd'))

import numpy as np
import pandas as pd
from pandas import DataFrame
np.random.seed(12345)
data = DataFrame(np.random.randn(1000,4))
b3 = np.abs(data)>3
print(type(b3))
print(b3.any(0))

