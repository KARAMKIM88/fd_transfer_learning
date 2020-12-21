import cv2

class DataSetMaker:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.faces_list = []
        self.title = "image"
        cv2.namedWindow(self.title)        
        cv2.setMouseCallback(self.title, self.get_pose)
        self.drawing = False
     

        
    def get_pose(self, event, x, y, flags, param):

        if event == cv2.EVENT_LBUTTONDOWN:
            self.x = x
            self.y = y
            self.drawing = True

        if event == cv2.EVENT_MOUSEMOVE :
            if self.drawing is True:
                copy_img = self.img.copy()
                cv2.rectangle(copy_img, (x, y), (self.x, self.y), (0, 255, 255), 1)  
                cv2.imshow(self.title, copy_img)     

        if event == cv2.EVENT_LBUTTONUP:
            self.width = abs(self.x - x)
            self.height = abs(self.y - y)
            if x < self.x : 
                self.x = x
            if y < self.y :
                self.y = y
            self.drawing = False
            
            print("x:%d, y:%d, width:%d, height:%d \n" %(self.x, self.y, self.width, self.height))

    def get_image(self, path):
        self.img = cv2.imread(path)
        cv2.imshow(self.title, self.img)
        self.key = cv2.waitKey(0)
        if self.key == 'q':
            cv2.destoyWindows()











if __name__=="__main__":
    datasetmaker = DataSetMaker()
    datasetmaker.get_image("./20201101_115549.jpg")