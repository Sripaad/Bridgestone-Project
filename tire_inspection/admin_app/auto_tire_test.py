from cv2 import cv2
import numpy as np

class tire_testing:
    """
    Class containing all the tire testing function.
    """
    def ink_test(self,location):
        """
        Function checks the ink spillage in tire. 
        Returns 0 or 1, 1 for defective.
        """
        frame = cv2.imread(location)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray,150,200,0)
        contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.fillPoly(frame,pts=[contours[17]],color=(0,0,0))
        cv2.fillPoly(frame,pts=[contours[34]],color=(0,0,0))
        cv2.fillPoly(frame,pts=[contours[44]],color=(0,0,0))
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray,165,165,0)
        _, contours = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        count = 0
        for _ in contours:
            count = count + 1
        if count > 0:
            flag = 1
        else:
            flag = 0
        return flag
    def twi_test(self,location,template_of_twi):
        """
        Function checks the scorch in tire. 
        Returns 0 or 1, 1 for defective
        """
        img_rgb = cv2.imread(location)  
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(template_of_twi,0)
        w, h = template.shape[::-1]  
        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)  
        threshold = 0.8
        loc = np.where( res >= threshold)  
        flag = 0
        for pt in zip(*loc[::-1]): 
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2) 
            flag = 1
        return flag
    
    def wobbling_test(self,location):
        """
        Test checking the wobbling shape of the tire.
        Return 0 or 1, 1 for defective.
        """
        frame = cv2.imread(location)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray,150,200,0)
        contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame,contours,-1,(0,255,0),3)
        height = np.size(frame, 0)
        width = np.size(frame, 1)
        img_area = height * width
        i=0
        for contour in contours:
            if i > 0:
                area = cv2.contourArea(contour)
                img_area = area
            elif i > 1:
                area = cv2.contourArea(contour)
                img_area = img_area - area
            i = i + 1
        height = np.size(frame, 0)
        width = np.size(frame, 1)
        if img_area > 60000 and img_area < 50000:
            flag = 0
        else:
            flag = 1
        return flag
    def seperation_test(self,location):
        """
        Seperation test on the tire sides.
        Return 0 or 1, 1 for defective.
        """
        frame = cv2.imread(location)
        edges = cv2.Canny(frame,300,150)
        count = 0
        flag = 0
        for ls in edges:
            if 255 in ls:
                count = count + 1
        if count == 80:
            flag = 1
        return flag
