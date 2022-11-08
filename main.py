import glob
import os
from tkinter import *
from tkinter import Tk, Button, Label, Frame, filedialog
from PIL import Image, ImageTk
import botany

root = Tk()
root.title("Flower Identification")
root.geometry("800x400")

# create labels
uploadButtonsFrame = Frame(root)
topLabelsFrame = Frame(root)
insertImageLbl = Label(uploadButtonsFrame, text="Insert image here:")
flowerDeterminedLbl = Label(topLabelsFrame, text="Upload a flower")
percentMatchLbl = Label(topLabelsFrame, text="See your match!")

topLabelsFrame.pack()
uploadButtonsFrame.pack(anchor="w", side=BOTTOM)
insertImageLbl.grid(row=1, column=1)
flowerDeterminedLbl.grid(row=1, column=4)
percentMatchLbl.grid(row=3, column=4)

#################################################################################################################
# ////////GUI SETUP ABOVE////////////////////////////////////////////////////////////////////////////////////////#
#################################################################################################################

flowerGuess = ""
datasetPath = 'C:/Users/visha/Flower_Image_Recognition_Project/pythonProject/flower_photos'
# add frames for images
imageOutFrames = [Frame(topLabelsFrame) for i in range(6)]
# array for sample image import
sampleImages = []
# array for all sample image labels placed into frame
sampleLabels = [Label(imageOutFrames[i], image='') for i in range(6)]


#################################################################################################################
# ////////DEFINITIONS////////////////////////////////////////////////////////////////////////////////////////////#
#################################################################################################################

# upload file
def upload_img(upload_buttons_frame):
    file_name = filedialog.askopenfilename(filetypes=[('Image Files', '*jpg')])
    user_image = Image.open(file_name)
    user_image.save('C:/Users/visha/Flower_Image_Recognition_Project/pythonProject/User_Input/UserImage.jpg')
    user_image = ImageTk.PhotoImage(Image.open(file_name).resize((244, 244)))
    input_image = Label(upload_buttons_frame,
                        image=user_image)  # interesting that this alone doesn't work, but removing it breaks the
    # program
    input_image.image = user_image
    input_image.grid(row=1, column=1)

    if file_name is not None:
        pass


def displaySampleImages():
    [flower_type, confidence] = botany.flower_prediction(
        'C:/Users/visha/Flower_Image_Recognition_Project/pythonProject/User_Input/UserImage.jpg')
    getFlowersFromFile(flower_type)
    confidenceUpdate(str(confidence))
    flowerNameUpdate(flower_type)
    updateSampleImages()


def confidenceUpdate(confidence):
    percentMatchLbl.config(text='It is a ' + confidence + '% match')


def flowerNameUpdate(match):
    flowerDeterminedLbl.config(text='Your flower is a:' + match)


def getFlowersFromFile(flowerName):
    sampleImages.clear()
    for file in glob.glob(os.path.join(datasetPath, flowerName, '*.jpg')):
        sampleImages.append(ImageTk.PhotoImage(Image.open(file).resize((125, 125))))


def updateSampleImages():
    for i in range(6):
        sampleLabels[i].config(image=sampleImages[i])
        sampleLabels[i].pack()


#################################################################################################################
# ////////GUI SETUP BELOW////////////////////////////////////////////////////////////////////////////////////////#
#################################################################################################################

generateButton = Button(uploadButtonsFrame, text="Generate Flower Name", command=lambda: displaySampleImages())
chooseImage = Button(uploadButtonsFrame, text="Choose image", command=lambda: upload_img(uploadButtonsFrame))

generateButton.grid(row=3, column=1)
chooseImage.grid(row=2, column=1)
imageOutFrames[0].grid(row=5, column=4)
imageOutFrames[1].grid(row=5, column=5)
imageOutFrames[2].grid(row=5, column=6)
imageOutFrames[3].grid(row=6, column=4)
imageOutFrames[4].grid(row=6, column=5)
imageOutFrames[5].grid(row=6, column=6)

root.mainloop()
