import torch

a = torch.randn(3,3)
b = torch.randn(1,3)

b = torch.transpose(b,0,1)


print(torch.matmul(a,b))