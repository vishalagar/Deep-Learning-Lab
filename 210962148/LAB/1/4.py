import numpy as np

import torch

a = np.arange(0,10,2)
print(a)

t = torch.from_numpy(a)
print(t)

b = t.numpy()
print(b)