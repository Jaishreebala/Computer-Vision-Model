# Computer Vision Model

## Fashion MNIST Dataset

Created a simple deep neural network for computer vision. Trained to recognize a piece of clothing from the Fashion MNIST Dataset. 
Note: In this model, the clothing item has to be the only thing on the picture and it has to be centered.
Accuracy:
Test Data: 83% ; Training Data: 87%

## Convolutions And Pooling

* Created a feature map of an image from the from misc in SciPy.
    ![Actual image](./assets/proj3ActualImage.png)
* The first filter gives emphasis to the vertical lines of the picture.
    ![Sharpen Vertical lines](./assets/proj3SharpenVerticalLines.png)

* The second filter provides emphasis to the horizontal lines of the picture.
    ![Sharpen Horizontal lines](./assets/proj3SharpenHorizontalLines.png)

* Pooling is done using Maximum Pooling. Information from the picture is reduced (in terms of pixels) while maintaining the features that are detected.
    ![Max Pooling](./assets/proj3PoolingHorizontal.png)


## Enhance Computer Vision Using Convolutions

Enhanced Computer Vision for the MNIST Fashion Dataset using a Convolution Matrix.
Accuracy:
Test Data: 91% ; Training Data: 99%
