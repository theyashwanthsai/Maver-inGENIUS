
import cv2
from pyzbar.pyzbar import decode



def BarcodeReader(image):

    img = cv2.imread(image)


    detectedBarcodes = decode(img)


    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:


        for barcode in detectedBarcodes:


            (x, y, w, h) = barcode.rect


            cv2.rectangle(img, (x - 10, y - 10),
                          (x + w + 10, y + h + 10),
                          (255, 0, 0), 2)

            if barcode.data != "":

                print(barcode.data)
                print(barcode.type)


    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    
    image = "Img.jpg"
    BarcodeReader(image)

