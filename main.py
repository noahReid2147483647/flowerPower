from tkinter import *
from tkinter.filedialog import askopenfile

root = Tk()
root.title("Flower Identification")
# create labels
insertImageLbl = Label(root, text="Insert image here:")
flowerDeterminedLbl = Label(root, text="The flower you inserted is: ")
percentMatchLbl = Label(root, text="It is a x% match")
# create button
generateButton = Button(text="Generate Flower Name")


# add frames for images

def upload_img():
    file_path = askopenfile(mode='r', filetypes=[('Image Files', '*jpg', '*jpeg')])
    if file_path is not None: pass


insertImageLbl.grid(row=3, column=1)
flowerDeterminedLbl.grid(row=2, column=4)
percentMatchLbl.grid(row=3, column=4)
generateButton.grid(row=8, column=1)

root.mainloop()
