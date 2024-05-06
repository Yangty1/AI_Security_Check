from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
# Use the model
model.train(data="ultralytics/cfg/datasets/mydata.yaml",batch_size=4,epochs=200,resume=True)  # train the model
metrics = model.val()  # evaluate model performance on the validation set
# results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image