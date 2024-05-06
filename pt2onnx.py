from ultralytics import YOLO

model = YOLO("weights/bestx.pt")
success = model.export(format="onnx", simplify=True,device='cpu')  # export the model to onnx format
assert success
print("转换成功")