import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from numpy import uint8
class mouseParam:
    def __init__(self, input_img_name):
        #マウス入力用のパラメータ
        self.mouseEvent = {"w":None, "h":None, "event":None, "flags":None}
        #マウス入力の設定
        cv2.setMouseCallback(input_img_name, self.__CallBackFunc, None)
    
    #コールバック関数
    def __CallBackFunc(self, eventType, w, h, flags, userdata):
        
        self.mouseEvent["w"] = w
        self.mouseEvent["h"] = h
        self.mouseEvent["event"] = eventType    
        self.mouseEvent["flags"] = flags    

    #マウス入力用のパラメータを返すための関数
    def getData(self):
        return self.mouseEvent
    
    #マウスイベントを返す関数
    def getEvent(self):
        return self.mouseEvent["event"]                

    #マウスフラグを返す関数
    def getFlags(self):
        return self.mouseEvent["flags"]                

    #xの座標を返す関数
    def getX(self):
        return self.mouseEvent["w"]  

    #yの座標を返す関数
    def getY(self):
        return self.mouseEvent["h"]  

    #xとyの座標を返す関数
    def getPos(self):
        return (self.mouseEvent["h"], self.mouseEvent["w"])
        

if __name__ == "__main__":
    plt.ion()
    #入力画像
    image = cv2.imread("gray.jpg", cv2.IMREAD_GRAYSCALE)
    #表示するWindow名
    window_name = "input window"
    #ゼロの配列
    h,w = image.shape
    S1= np.zeros(shape=(h,w))
    S2= np.zeros(shape=(h,w))
    S3= np.zeros(shape=(h,w))
    #フーリエ変換
    ff = np.fft.fft2(image)
    fshift = np.fft.fftshift(ff)
    mag = 20*np.log(np.abs(fshift))
    magmin = np.min(mag)
    magmax = np.max(mag)
    mag2 = (mag - magmin) * 255/(magmax - magmin)
    newma = np.uint8(mag2)
    cv2.imshow("fft",newma)
    #コールバックの設定
    cv2.imshow("click",S2)
    mouseData = mouseParam("click")
    #表示用の配列
    S14= np.zeros(shape=(h,w))
    S34= np.zeros(shape=(h,w))
    cv2.imshow(window_name, image)
    #cv2.imshow("click",S2)
    while 1:
        cv2.waitKey(20)
        #3つのウィンドウ
        cv2.imshow(window_name, image)
        
        #左クリックがあったら表示
        if mouseData.getEvent() == cv2.EVENT_LBUTTONDOWN:
            h1,w1 = mouseData.getPos()
            S2[h1:h1+10,w1:w1+10]=255
            S1[h1:h1+10,w1:w1+10]=1.0
            S3[:,:]=0
            S3[mouseData.getPos()]=1
            #今までの足したフーリエ
            S12 = fshift*S1
            S13 = np.fft.fftshift(S12)
            S1_iff= np.fft.ifft2(S13)
            S1_abs =np.abs(S1_iff) 
            S1max = np.max(S1_abs)
            S1min = np.min(S1_abs)
            S14 = (S1_abs - S1min )* 255/(S1max - S1min)
            #それぞれのフーリエ
            S3 = S3*ff
            S3 = np.fft.fftshift(S3)
            S3 = np.fft.ifft2(S3)
            S3 = np.abs(S3)
            S3max = S3.max()
            S3min = S3.min()
            S3 = (S3 - S3min) * 255/(S3max - S3min)
            #print(S3)
        cv2.imshow("ifft",S14.astype(uint8))
        cv2.imshow("ifft_single",S3.astype(uint8))
        cv2.imshow("click",S2)

        #右クリックがあったら終了
        if mouseData.getEvent() == cv2.EVENT_RBUTTONDOWN:
            break
            
    plt.close()      
    cv2.destroyAllWindows()            
    print("Finished")
