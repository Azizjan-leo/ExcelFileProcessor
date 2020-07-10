
# Importing needed libraries
# We need sys library to pass arguments into QApplication
import sys
# QtWidgets to work with widgets
from PyQt5 import QtWidgets
# QPixmap to work with images
from PyQt5.QtGui import QPixmap

# Importing designed GUI in Qt Designer as module
import design as design

# Importing YOLO v3 module to Detect Objects on image
from sorting import sort
from coloring import color
import re
import string

"""
Start of:
Main class to add functionality of designed GUI
"""
keywords_list = []

# Creating main class to connect objects in designed GUI with useful code
# Passing as arguments widgets of main window
# and main class of created design that includes all created objects in GUI
class MainApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    # Constructor of the class
    def __init__(self):
        # We use here super() that allows multiple inheritance of all variables,
        # methods, etc. from file design
        # And avoiding referring to the base class explicitly
        super().__init__()

        # Initializing created design that is inside file design
        self.setupUi(self)

        # Connecting event of clicking on the button with needed function
        self.pushButton.setCheckable(True)
        self.pushButton_2.setCheckable(True)
        self.pushButton_3.setCheckable(True)
        self.pushButton.clicked.connect(self.take_keywords)
        self.pushButton_2.clicked.connect(self.sort)
        self.pushButton_3.clicked.connect(self.color)

    # Defining function that will be implemented after button is pushed
    # noinspection PyArgumentList
    def take_keywords(self):

        # Showing text while image is loading and processing
        self.label_2.setText('Taking keywords from \n.txt file ...')

        # Opening dialog window to choose an image file
        # Giving name to the dialog window --> 'Choose Image to Open'
        # Specifying starting directory --> '.'
        # Showing only needed files to choose from --> '*.png *.jpg *.bmp'
        # noinspection PyCallByClass
        image_path = \
            QtWidgets.QFileDialog.getOpenFileName(self, 'Choose Image to Open',
                                                  '.',
                                                  '*.txt *.word')

        # Variable 'image_path' now is a tuple that consists of two elements
        # First one is a full path to the chosen image file
        # Second one is a string with possible extensions

        # Checkpoint
        print(type(image_path))  # <class 'tuple'>
        print(image_path[0])  # /home/my_name/Downloads/example.png
        print(image_path[1])  # *.png *.jpg *.bmp

        # Slicing only needed full path
        image_path = image_path[0]  # /home/my_name/Downloads/example.png


        # Passing full path to loaded image into YOLO v3 algorithm
        with open(image_path) as f:
            for line in f:
                line = line.strip()
                line = line.lower()
                # Remove the punctuation marks from the line
                line = line.translate(line.maketrans("", "", string.punctuation))
                # Split the line into words
                words = line.split(" ")
                keywords_list.append(words)
        print(keywords_list)


    # Defining function that will be implemented after button is pushed
    # noinspection PyArgumentList

    def sort(self):

        # Showing text while image is loading and processing
        self.label_2.setText('Processing ...')

        # Opening dialog window to choose an image file
        # Giving name to the dialog window --> 'Choose Image to Open'
        # Specifying starting directory --> '.'
        # Showing only needed files to choose from --> '*.png *.jpg *.bmp'
        # noinspection PyCallByClass
        image_path = \
            QtWidgets.QFileDialog.getOpenFileName(self, 'Choose Image to Open',
                                                  '.',
                                                  '*.xlsx')

        # Variable 'image_path' now is a tuple that consists of two elements
        # First one is a full path to the chosen image file
        # Second one is a string with possible extensions

        # Checkpoint
        print(type(image_path))  # <class 'tuple'>
        print(image_path[0])  # /home/my_name/Downloads/example.png
        print(image_path[1])  # *.png *.jpg *.bmp

        # Slicing only needed full path
        image_path = image_path[0]  # /home/my_name/Downloads/example.png

        # Passing full path to loaded image into YOLO v3 algorithm
        sort(image_path, keywords_list)


    # Defining function that will be implemented after button is pushed
    # noinspection PyArgumentList
    def color(self):


        # Showing text while image is loading and processing
        self.label_2.setText('Processing ...')


        # Opening dialog window to choose an image file
        # Giving name to the dialog window --> 'Choose Image to Open'
        # Specifying starting directory --> '.'
        # Showing only needed files to choose from --> '*.png *.jpg *.bmp'
        # noinspection PyCallByClass
        image_path = \
            QtWidgets.QFileDialog.getOpenFileName(self, 'Choose Image to Open',
                                                  '.',
                                                  '*.xlsx')

        # Variable 'image_path' now is a tuple that consists of two elements
        # First one is a full path to the chosen image file
        # Second one is a string with possible extensions

        # Slicing only needed full path
        image_path = image_path[0]  # /home/my_name/Downloads/example.png

        # Passing full path to loaded image into YOLO v3 algorithm
        color(image_path,keywords_list)


"""
End of:
Main class to add functionality of designed GUI
"""


"""
Start of:
Main function
"""


# Defining main function to be run
def main():
    # Initializing instance of Qt Application
    app = QtWidgets.QApplication(sys.argv)

    # Initializing object of designed GUI
    window = MainApp()

    # Showing designed GUI
    window.show()

    # Running application
    app.exec_()


"""
End of:
Main function
"""


# Checking if current namespace is main, that is file is not imported
if __name__ == '__main__':
    # Implementing main() function
    main()
