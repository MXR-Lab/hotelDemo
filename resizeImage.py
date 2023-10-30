import cv2

class Resize: 
    def __init__(self, image, width):
        self.image = image
        self.width = width

    def ResizeWithAspectRatio(self, inter=cv2.INTER_AREA):
        dim = None
        (h, w) = self.image.shape[:2]

        if self.width is None:
            return self.image
        else:
            r = self.width / float(w)
            dim = (self.width, int(h * r))

        return cv2.resize(self.image, dim, interpolation=inter)