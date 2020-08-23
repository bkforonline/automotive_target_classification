This is a object classification project based on radar spectrogram image.

## About the dataset

This dataset is based on matlab simulation. See [here](https://www.mathworks.com/help/phased/examples/pedestrian-and-bicyclist-classification-using-deep-learning.html?s_eid=PEP_16543) to know about the scene description and simulation process.

## Usage

The project is able to:
1. Visualization of data. User can use cursor to browse spectrogram images of training/test dataset.
2. Object classification and show misclassified results. User needs to prepare classfication configuration file. After classification, the misclassified spectrograms can be shown with true label and misclassified label. At the end of classification a txt log file will be generated, which includes classification algorithm configuration parameter and classification performance evaluation.

### Environment

* Ubuntu 18.04
* Python 3.7.7
* Tensorflow 2.0.0
* Keras 2.2.4-tf
* Sklearn 0.22.1

### Data preparation

1. Download data from [link](https://www.mathworks.com/supportfiles/SPT/data/PedBicCarData.zip).
2. Convert data and label files to `HDF5` format with *.m and *.m respectively.

### Configurations



### How to run







