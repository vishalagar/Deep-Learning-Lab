import torch

a = torch.rand(2,3)
b = torch.rand(2,3)
# a = a.to(device='cpu')

b = b.permute(1,0)

mul = torch.matmul(a,b)
print(mul)

print("MAX: :",torch.max(mul))
print("MIN: ",torch.min(mul))


print("Position of max: ", torch.argmax(mul))
print("Position of min: ", torch.argmin(mul))
