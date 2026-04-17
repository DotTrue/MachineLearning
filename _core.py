#libs
import cv2
import torch
from ultralytics import YOLO
from tests import CameraYolo
# Загрузка модели

# mod =  YOLO("yolo26l.pt", task="detect")
mod =  YOLO("yolov5s.pt", task="detect")


class RECOGNITION:
    def __init__(self):
        self.camera = CameraYolo()
        self.model = model = YOLO("yolo26l.pt", task="detect")
        if torch.cuda.is_available():
            self.model.to("cuda")
    def start(self):
        for frame in self.camera.start_flow():
            res = self.model(frame)
            cv2.imshow("frame4",res[0].plot())
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
onj = RECOGNITION()
onj.start()