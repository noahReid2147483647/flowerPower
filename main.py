from tkinter import *

root = Tk()
insertImageLbl = Label(root, text="Insert image here:")
flowerDeterminedLbl = Label(root, text="The flower you inserted is: ")
percentMatchLbl = Label(root, text="It is a x% match")
generateButton = Button(text="Generate Flower Name")

#add frames for images?

insertImageLbl.grid(row=3, column=1)
flowerDeterminedLbl.grid(row=2, column=4)
percentMatchLbl.grid(row=3, column=4)
generateButton.grid(row=8, column=1)

root.mainloop()
