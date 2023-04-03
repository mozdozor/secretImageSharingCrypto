from secretsharing import PlaintextToHexSecretSharer
import pyqrcode
import matplotlib.image as image
import numpy as np

def main():
    
    global scale, threshold,min_threshold
    # QR code scale best practice is 4
    scale = 4
    # Min value must be 2. Because 1 QR Code would violate the sharing logic
    min_threshold = 2
    try:
        path = input("Please enter your secret image:")
        img = image.imread(path)
        imageArray = np.array(img)
        # print(imageArray)
        strImage = ' '.join([str(item) for item in imageArray])
    except:
        print("You entered wrong file path!")
    # Select number of Shared QR Codes
    numberOfSharedQRCode = int(input("How many QR codes do you want to store the secret in (At Least 2): "))
    if numberOfSharedQRCode > 2:
        max_threshold = numberOfSharedQRCode
        thresholds = [x for x in range(min_threshold, max_threshold+1)] #shows the choices
        print("Threshold Limit Options: -",end='')
        for x in thresholds:
            print(x,end='-')
        print()
        threshold = int(input("How many shares should be enough to decrypt? (Most secure is: " + str(max_threshold) + ")\n"))


    secretSharing = strImage;
    print("The password is embedded in QR codes...")
    shares = PlaintextToHexSecretSharer.split_secret(secretSharing, threshold, numberOfSharedQRCode)


    for sharedItem in shares: # Create png for each share
        img = pyqrcode.create(sharedItem)
        img.png(sharedItem[0]+'.png', scale=scale)

    print("The password was embedded in the QR codes and all desired QR codes were created.")
if __name__ == '__main__':
    main()
