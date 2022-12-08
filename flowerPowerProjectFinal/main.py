import glob
import os
from tkinter import *
from tkinter import Tk, Button, Label, Frame, filedialog, messagebox
import tkinter.font as TkFont
from PIL import Image, ImageTk
import botany

root = Tk()
root.title("Flower Identification")
root.geometry("800x500")
root['background']='#5A5A5A'

Cal12Norm = TkFont.Font(family="Calibri",size=12, slant="italic")
Cal12Bold = TkFont.Font(family="Calibri",size=12,weight="bold")
orangeColor='#FBBE81'

C = Canvas(root, bg="blue", height=0, width=0)
imageFileBG= ImageTk.PhotoImage(Image.open("./backdrop/flowerBackdrop.jpg").resize((800,800)))
background_label = Label(root, image=imageFileBG)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

# create labels
uploadButtonsFrame = Frame(root, bg='#FBBE81')
topLabelsFrame = Frame(root, bg='#FBBE81')
insertImageLbl = Label(uploadButtonsFrame, text="Insert image here:", font=Cal12Norm, bg=orangeColor, fg='white')
flowerDeterminedLbl = Label(topLabelsFrame, text="Upload a flower", font=Cal12Bold, bg=orangeColor, fg='white')
percentMatchLbl = Label(topLabelsFrame, text="See your match!", font=Cal12Bold, bg=orangeColor, fg='white')

topLabelsFrame.pack()
uploadButtonsFrame.pack(anchor="w", side=BOTTOM)
insertImageLbl.grid(row=1, column=1)
flowerDeterminedLbl.grid(row=1, column=3)
percentMatchLbl.grid(row=3, column=3)

#################################################################################################################
# ////////GUI SETUP ABOVE////////////////////////////////////////////////////////////////////////////////////////#
#################################################################################################################

flowerGuess = ""
datasetPath = './Sample_Images/'
# add frames for images
imageOutFrames = [Frame(topLabelsFrame) for i in range(6)]
# array for sample image import
sampleImages = []
# array for all sample image labels placed into frame
sampleLabels = [Label(imageOutFrames[i], image='',bg='#FBBE81') for i in range(6)]


#################################################################################################################
# ////////DEFINITIONS////////////////////////////////////////////////////////////////////////////////////////////#
#################################################################################################################

# upload file
def upload_img(upload_buttons_frame):
    file_name = filedialog.askopenfilename(filetypes=[('Image Files', '*jpg')])
    user_image = Image.open(file_name)
    user_image.save('./User_Input/UserImage.jpg')
    user_image = ImageTk.PhotoImage(Image.open(file_name).resize((125, 125)))
    input_image = Label(upload_buttons_frame,
                        image=user_image)  # interesting that this alone doesn't work, but removing it breaks the
    # program
    input_image.image = user_image
    input_image.grid(row=0, column=1, sticky=N)

    if file_name is not None:
        pass


def displaySampleImages():
    [flower_type, confidence] = botany.flower_prediction(
        './User_Input/UserImage.jpg')
    getFlowersFromFile(flower_type)
    confidenceUpdate(str(confidence))
    flowerNameUpdate(flower_type)
    updateSampleImages()


def confidenceUpdate(confidence):
    percentMatchLbl.config(text='It is a ' + confidence + '% match')


def flowerNameUpdate(match):  
    temp=""
    
    if match=="daisy":
        temp = "Daisy"
    elif match=="dandelion":
        temp="Dandelion"
    elif match=="roses":
        temp="Rose"
    elif match=="sunflowers":
        temp="Sunflower"
    elif match=="tulips":
        temp="Tulip"
        
        
    flowerDeterminedLbl.config(text='I think it is a: ' + temp)


def getFlowersFromFile(flowerName):
    sampleImages.clear()
    for file in glob.glob(os.path.join(datasetPath, flowerName, '*.jpg')):
        sampleImages.append(ImageTk.PhotoImage(Image.open(file).resize((100, 100))))


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
imageOutFrames[0].grid(row=4, column=2, padx=1)
imageOutFrames[1].grid(row=4, column=3, padx=1)
imageOutFrames[2].grid(row=4, column=4, padx=1)
imageOutFrames[3].grid(row=5, column=2, padx=1)
imageOutFrames[4].grid(row=5, column=3, padx=1)
imageOutFrames[5].grid(row=5, column=4, padx=1)

root.mainloop()
