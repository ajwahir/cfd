# cfd
## This project is for code.fun.do ShowCase 2018

This is a platform for Smart Cognitive and Health Monitoring.
When, a person is front of the computer and webcam is not in use, we us computer vision techniques monioter a person's mood,
pulse rate and track his/her eye-gaze to check if he is distrcted.

All the features are modular and can be activated according to the need

Its web-based gui and have real time pulse rate monitoring system with real-time plot and can be accessible by the doctors
for continious monitoring of the emotions and pulse.

More modules can be added, depending on the application.

The estimation of non-contact pulse rate has lot of uses. Pulse rate has to be monitored
frequently all the time to understand any symptom at an early stage. People don’t like
wearing something all the time. So, there is a need for some non-contact device that
could monitor the pulse all the time. So, we tried to make a device that detects pulse rate
using head motion by trying to implement one and integrated them here.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Python 2.7
openCV
flask
azure.storage.blob

```
Give examples
```

### Installing

To get the framework running

```
git clone https://github.com/ajwahir/cfd
python pulse.py
```
That will start your pulse monitor with gaze tracking
Then, in a new terminal,
```
python home.py
```
This will run the web container and then in a new terminal
```
python emotions.py
```
which will start your congnitive monitor
```
firefox static/index.html

```
and you will have your gui up and running then.


## Running the tests


### Realtime pulse display

### Realtime emotion display 

### Suggessions of contents depending on your current mood

### Real-time statistics 


## Authors

* **Muhammedh Ajwahir** 
* **Muhammedh Ajwahir** 
* **Muhammedh Ajwahir** 

