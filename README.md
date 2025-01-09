## Handwritten Digit Recognition with Convolutional Neural Networks
![cnn-cover](https://github.com/user-attachments/assets/d2056e55-19e5-40e8-8f1b-1091cae97bcb)

# Update Jan 2025
## **Version 1.1.**
In this update:
- **Improved user input recognition:** Added some adjustments to match the MNIST image pre-processing so that the software achieves better recognition of user-drawn digits.
- **Error handling**: If no digit is drawn, an error message is shown instead of proceeding with attempting to recognise the digit.
__________________________

# Motivation for the project
This is my version of solving the MNIST Digit data set. As a complete beginner in the field of machine learning I decided that I should build one of the 'classics' for my first project: a handwritten digit recognizer. This project uses the MNIST dataset ( a well-known dataset of handwritten digits) to train a model that can accurately classify digits from 0 to 9. Through this project, I aimed to gain hands-on experience with ML concepts and learn how to implement them using Python and popular ML libraries.

# Project Overview
The goal of the project is to create a model that can recognize handwritten digits with high accuracy. I started by loading the MNIST dataset and preprocessing the data to normalise the pixel values and reshape the images to fit the model. This step was crucial to ensure that the data was in the right format for the neural network.

# Basic Neural Network (NN) vs. Convolutional Neural Network (CNN)
Initially, I considered using a **basic neural network** (fully connected network) for this project. A basic neural network consists of layers of neurons where each neuron in one layer is connected to every neuron in the next layer. These networks can be used for classification tasks, but they are not as effective for image data because they don't capture spatial hierarchies and local patterns very well.

On the other hand, **Convolutional Neural Networks** (CNNs) are designed specifically for processing grid-like data - such as images! They use convolutional layers to apply filters that can detect various features in the images such as edges, textures and patterns, which are crucial for image analysis. Moreover, CNNs require fewer parameters than fully connected networks, which helps prevent overfitting and makes training more efficient.

Given the advantages of CNNs for image data I decided to use one for this project. This decision allowed me to utilise the powerful feature extraction capabilities of convolutional layers and achieve higher accuracy in digit recognition.

Through the process of building this project I learned how to compile a model with an appropriate optimiser and loss function, how to fit the model to the training data and how to evaluate its performance on test data. The final model achieved very high accuracy (above 98%). Finally, I visualised the results using a confusion matrix and sample predictions shown in a grid to understand the model's strengths and weaknesses.

# Interactive Python program for real-time handwritten digit recognition
As an addition to this project I implemented a Python program that integrates the trained CNN model to allow for real-time prediction. This program provides a graphical interface where the user can draw a digit on the screen and the model will predict which digit was drawn. This interactive feature not only makes the application more engaging but also demonstrates the practical side of building the model.

# Future Plans
In the next version of this project I want to further refine the user interface and enhance the drawing accuracy by incorporating additional preprocessing steps. I'd also like to expand the model's capabilities to recognize handwritten letters.

# Conclusion
This project has been an excellent learning experience. It allowed me to gain practical knowledge of machine learning basics and also boosted my confidence in tackling more complex ML tasks, which I am looking forward to doing very soon!
