from secretsharing import PlaintextToHexSecretSharer

import numpy as np
from PIL import Image
from pyzbar.pyzbar import decode


def main():
    sharedImages=[]
    while True:
        try:      # Enter shares QR code images from the user
            pngShareImage = decode(Image.open(input("Enter your share image file name :")))
            dataStringOfImage = pngShareImage[0].data.decode("utf-8")
            sharedImages.append(dataStringOfImage)  # append the sharedImages array
        except:
            print("Wrong file path! Please try again")
        answerUser = input("Do you have more secret images?\tYes (Y)\tNO (N)\n").upper()
        if answerUser == "Y": # if the user doesn't press the N key program will be accept to last file number
            pass
        elif answerUser == "N":
            break
        else:
            print("You haven't answered correctly, try again\n")

    # Recover
    try:
        message = PlaintextToHexSecretSharer.recover_secret(sharedImages)  # send the data string array of images to library and take the returning value
        print("Image is constructing...")
        message = message.replace("[", "").replace("]", "").replace("\n", "").replace("  ", " ")
        message = message.replace("  ", " ")
        messageArray = message.split(" ")
        messageArray = [int(numeric_string) for numeric_string in messageArray]    #convert data string to int
        array1 = np.array(messageArray, dtype=np.uint8).reshape(6, 6, 3)    # reshape operations
        # print(array1)
        img = Image.fromarray(array1, mode="RGB")
        img.show()  # show images in the end
    except:
        print("Message cant reveal")


if __name__ == '__main__':
    main()
