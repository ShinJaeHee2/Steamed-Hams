import cv2
import os
import time
import playsound
import threading

class SteamedHams:
    
    def __init__(self):

        os.system('mode 130,50')
        
        self.videoPath = f'{os.path.dirname(__file__)}\\steamed_hams.mp4'
        self.audioPath = f'{os.path.dirname(__file__)}\\steamed_hams.mp3'
        self.capture = cv2.VideoCapture(self.videoPath)
        self.color = {'0':'\033[40m　', '255':'\033[47m　'}
        self._map = lambda x: self.color[str(x)]

        if self.capture.isOpened():

            self.t = threading.Thread(target=playsound.playsound, args=(self.audioPath,))
            self.t.start()

            while True:

                self.ret, self.image = self.capture.read()

                if self.ret:

                    self._resize = cv2.resize(self.image, dsize=(64, 48))
                    self._cvtColor = cv2.cvtColor(self._resize, cv2.COLOR_BGR2GRAY)
                    self._threshold = cv2.threshold(self._cvtColor, 128, 255, cv2.THRESH_BINARY)[1]
                    self.frameList = self._threshold.tolist()
                    self.visual = ''

                    for frame in self.frameList:

                        self.pixels = list(map(self._map, frame))
                        self.pixel = ''.join(self.pixels) + '\n'
                        self.visual += self.pixel

                    print(f'\033[%d;%dH{self.visual}' % (0,0))

                    time.sleep(0.0335)

                else:

                    break
        
        self.capture.release()
        cv2.destroyAllWindows()
        os.system('cls')

if __name__ == '__main__':

    SteamedHams()