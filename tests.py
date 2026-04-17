import cv2

class CameraYolo:
    def __init__(self):

        self.FrameCount = 0
        self.FrameSlide = 2
        self.cap = cv2.VideoCapture(0)
    def start_flow(self):
        while True:
            ret, frame = self.cap.read()

            if not ret:
                print("Не удалось получить кадр")
                break


            self.FrameCount += 1
            if self.FrameCount % self.FrameSlide == 0:
                yield frame

            # Выход по клавише 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.cap.release()
                cv2.destroyAllWindows()
                break
            if self.FrameCount >= 60:
                self.FrameCount = 0
