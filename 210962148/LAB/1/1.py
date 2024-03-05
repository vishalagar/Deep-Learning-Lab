import torch

a = torch.tensor([[1,2],
                 [4,6],
                 [7,8]])

print(a.reshape([6,1]))
# print(a.resize_([1,6]))


print(a.view([2,3]))

x = torch.tensor([8])
z = torch.tensor([9])

d = torch.stack([x,z])
print(d)

print(torch.squeeze(a).shape)

print(torch.unsqueeze(a, dim=1).shape)