from tkinter import *
from tkinter.filedialog import askopenfile

root = Tk()
root.title("Flower Identification")
root.geometry("750x300")
# create labels
uploadButtonsFrame = Frame(root)
topLabelsFrame = Frame(root)
insertImageLbl = Label(uploadButtonsFrame, text="Insert image here:")
flowerDeterminedLbl = Label(topLabelsFrame, text="The flower you inserted is: ")
percentMatchLbl = Label(topLabelsFrame, text="It is a x% match")

# add frames for images
imageOutFrame1 = Frame(topLabelsFrame)
imageOutFrame2 = Frame(topLabelsFrame)
imageOutFrame3 = Frame(topLabelsFrame)
imageOutFrame4 = Frame(topLabelsFrame)
imageOutFrame5 = Frame(topLabelsFrame)
imageOutFrame6 = Frame(topLabelsFrame)
# upload file


def upload_img():
    file_path = askopenfile(mode='r', filetypes=[('Image Files', '*jpg')])
    if file_path is not None:
        pass


generateButton = Button(uploadButtonsFrame, text="Generate Flower Name")
chooseImage = Button(uploadButtonsFrame, text="Choose image", command=lambda: upload_img())

topLabelsFrame.pack()
uploadButtonsFrame.pack(anchor="w", side=BOTTOM)
insertImageLbl.grid(row=1, column=1)
flowerDeterminedLbl.grid(row=1, column=4)
percentMatchLbl.grid(row=3, column=4)
generateButton.grid(row=3, column=1)
chooseImage.grid(row=2, column=1)

imageOutFrame1.grid(row=5, column=4)
imageOutFrame2.grid(row=5, column=5)
imageOutFrame3.grid(row=5, column=6)
imageOutFrame4.grid(row=6, column=4)
imageOutFrame5.grid(row=6, column=5)
imageOutFrame6.grid(row=6, column=6)

root.mainloop()
