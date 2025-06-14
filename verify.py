import torch
print("CUDA available:", torch.cuda.is_available())           # Should be True
print("CUDA device name:", torch.cuda.get_device_name(0))     # Should show your GPU name
