# Computer Vision Model

## Fashion MNIST Dataset

Created a simple deep neural network for computer vision. Trained to recognize a piece of clothing from the Fashion MNIST Dataset. 
Note: In this model, the clothing item has to be the only thing on the picture and it has to be centered.
Accuracy:
Test Data: 83% ; Training Data: 87%

## Convolutions And Pooling

* Created a feature map of an image from the from misc in SciPy.

     <img src="./assets/proj3ActualImage.png" width="256" height="256">

* The first filter gives emphasis to the vertical lines of the picture.

     <img src="./assets/proj3SharpenVerticalLines.png" width="256" height="256">


* The second filter provides emphasis to the horizontal lines of the picture.

     <img src="./assets/proj3SharpenHorizontalLines.png" width="256" height="256">

* Pooling is done using Maximum Pooling. Information from the picture is reduced (in terms of pixels) while maintaining the features that are detected.

     <img src="./assets/proj3PoolingHorizontal.png" width="256" height="256">


## Enhance Computer Vision Using Convolutions

Enhanced Computer Vision for the MNIST Fashion Dataset using a Convolution Matrix.
Accuracy:
Test Data: 91% ; Training Data: 99%
