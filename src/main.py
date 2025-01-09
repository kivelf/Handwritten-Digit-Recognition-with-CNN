import numpy as np
import tkinter as tk
from PIL import Image, ImageDraw, ImageOps, ImageFilter
import tensorflow as tf
from tkinter import messagebox

# loading the trained model
model = tf.keras.models.load_model('../models/my_model.keras')


# creating a drawing canvas for the user using Tkinter
class DrawApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Draw a Digit")

        self.canvas = tk.Canvas(self.root, width=200, height=200, bg='white')
        self.canvas.grid(row=0, column=0, pady=2, sticky="W", columnspan=2)

        self.image = Image.new("L", (200, 200), 255)  # greyscale image
        self.draw = ImageDraw.Draw(self.image)

        self.canvas.bind("<B1-Motion>", self.paint)

        self.predict_button = tk.Button(self.root, text="Predict", command=self.predict_digit)
        self.predict_button.grid(row=1, column=0, pady=2, padx=2)

        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_canvas)
        self.clear_button.grid(row=1, column=1, pady=2, padx=2)

    def paint(self, event):
        x1, y1 = (event.x - 5), (event.y - 5)
        x2, y2 = (event.x + 5), (event.y + 5)
        self.canvas.create_oval(x1, y1, x2, y2, fill="black", width=5)
        self.draw.line([x1, y1, x2, y2], fill="black", width=5)

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (200, 200), 255)
        self.draw = ImageDraw.Draw(self.image)

    def predict_digit(self):
        # crop the image to the bounding box of the digit
        image = self.image
        bbox = ImageOps.invert(image).getbbox()  # find bounding box of the drawn content
        if bbox:
            image = image.crop(bbox)
        else:
            tk.messagebox.showinfo("Error", "No digit drawn!")
            return

        # resize to 20x20 while keeping the aspect ratio
        image = image.resize((20, 20), Image.Resampling.LANCZOS)

        # create a new 28x28 image with the digit centered
        new_image = Image.new("L", (28, 28), 255)  # start with white background
        new_image.paste(image, (4, 4))  # paste the 20x20 image in the center

        # invert colours for white digit on black background
        new_image = ImageOps.invert(new_image)

        # apply Gaussian blur to simulate MNIST-like smoothing
        new_image = new_image.filter(ImageFilter.GaussianBlur(radius=1))

        # normalise the image
        image_array = np.array(new_image).astype('float32')
        image_array = image_array / 255.0  # scale pixel values to [0, 1]
        image_array = image_array.reshape(1, 28, 28, 1)

        # predict the digit using the model
        prediction = model.predict([image_array])
        digit = np.argmax(prediction)

        # display the prediction
        print(f"Predicted Digit: {digit}")
        tk.messagebox.showinfo("Prediction", f"Predicted Digit: {digit}")


# running the application
root = tk.Tk()
app = DrawApp(root)
root.mainloop()
