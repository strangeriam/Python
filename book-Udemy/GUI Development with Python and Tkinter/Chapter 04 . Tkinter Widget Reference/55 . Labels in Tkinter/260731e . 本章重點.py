Change a label's font:
--> font=("Font name", 20)

Add an image by first opening it.
--> image = Image.open("image.png")
Then creating a ImageTk.
--> ImageTk.photoImage(image)
Add applying it to the label with
--> image=photo

Adjust text and image positioning with
--> compound="right"
