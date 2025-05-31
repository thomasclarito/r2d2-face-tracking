import cv2


class TestCapture:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.frame_queue = []
        self.prev_frame = None

    
    def run(self):
        if self.frame_queue.count < 10:
            self.frame_queue.append(self.capture_frame_gray)
            return
        
        
        frame_diffs = []
        for i in range(self.frame_queue.count() - 1):
            frame_diffs[i] = cv2.absdiff(self.frame_queue[i+1], self.frame_queue[i])

        print(frame_diffs[0])
        # curr_frame = self.capture_frame_gray()
        # diff = cv2.absdiff(self.prev_frame, curr_frame)
        # self.prev_frame = curr_frame
        # cv2.imshow('diff', diff)


    def capture_frame_gray(self):
        ret, frame = self.cap.read()
        frame = cv2.flip(frame, 1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return frame
    
    # def get_pixel_average()
    
    def cleanup(self):
        self.cap.release()
        cv2.destroyAllWindows()


if (__name__ == '__main__'):
    tc = TestCapture()
    while True:
        tc.run()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    tc.cleanup()