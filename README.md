
# SMART BIKE USING DEEP LEARNING AND IOT ON RASPBERRY PI4

In this project, we'll create a smart bike that guarantees the rider's safety.

## Detailed Overview

We've added 3 elements to a bike to make it smart. They are

### A. Helmet Detection and Bike ignition

Here, we'll create a deep learning model to categorise whether or not the rider is wearing a helmet. We must generate our own image dataset consisting of two folders of images—one with a helmet and the other without—in order to train this model. 

The CNN algorithm will be used to train our model. To detect helmets in real time, we used opencv. 

The model detects the helmet when the rider puts it on and uses a relay to close the internal circuit of the bike so that the rider can start the bike if necessary. The internal circuit of the motorcycle will open when the rider takes off his or her helmet, which will cause the engine to shut off.

### B. Driver Drowsiness Detection

This model, which we will create using the Inception V3 algorithm, will keep track of the drivers' state.
Use the dataset provided in the link to train this model. 
@http://mrl.cs.vsb.cz/data/eyedataset/

This model will keep an eye on the driver's condition, and if the driver becomes drowsy, a buzzer will sound to wake up the rider.

### C. GPS Locator

To update the website with the bike's real-time location, we will use a Neo 6M GPS module.




## Deployment

To deploy this project follow the steps:

    1. Clone this repository
    2. Create a dataset for helmet detection
    3. Modify the dataset's path in the training files
    4. Train the models, give this models to the python files named driver_drow_exe.py and helmet_det_exe.py
    5. When equipment is fully connected, run python files named driver_drow_rasp_pi_final.py, gps_send_rasp_pi_final.py and helmet_det_rasp_pi_final.py
## Author

[Sudhan Jee](https://github.com/sudhanRacharla)

