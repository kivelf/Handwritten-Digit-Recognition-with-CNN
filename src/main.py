import numpy as np
import tkinter as tk
from PIL import Image, ImageDraw, ImageOps
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
        # convert the image to a 28x28 image as expected by the CNN model
        image = self.image.resize((28, 28))
        image = ImageOps.invert(image)
        image = np.array(image)
        image = image.reshape(1, 28, 28, 1)
        image = image.astype('float32')
        image /= 255.0

        # predict the digit
        prediction = model.predict([image])
        digit = np.argmax(prediction)

        # display the prediction
        print(f"Predicted Digit: {digit}")
        tk.messagebox.showinfo("Prediction", f"Predicted Digit: {digit}")


# running the application
root = tk.Tk()
app = DrawApp(root)
root.mainloop()
