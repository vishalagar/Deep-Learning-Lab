
import torch

input_var = torch.randn(2,4)

print(input_var.size())

print(input_var)


input_var = input_var.permute(1, 0)


print(input_var.size())

print(input_var)
