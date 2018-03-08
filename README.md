# cfd
## This project is for code.fun.do ShowCase 2018

This is a platform for Smart Health and Cognition Monitoring.
When a person is in front of a computer and the webcam is not in use, we use computer vision techniques to monitor the person's mood,
pulse rate and track his/her gaze direction to check if he/she is distracted.

All the features are modular and can be activated according to the need.

A web-based GUI displays pulse rate and emotion in realtime. These data can also be saved, viewed continuously or sent to a doctor for diagnosis.

Also, interactive prompts with content(videos, thoughts etc)  suggessions depending on the current mood is displayed. 

More modules can be added depending on the application.

The estimation of non-contact pulse rate has lot of uses. Pulse rate has to be monitored
frequently all the time to understand any symptom at an early stage. People don’t like
wearing something all the time. So, there is a need for some non-contact device that
could monitor the pulse all the time. So, we tried to make a device that detects pulse rate
using head motion by trying to implement one and integrated them here [1] .

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
```
Python 2.7
openCV
flask
azure.storage.blob
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

### Realtime emotion display 
![alt text](https://image.ibb.co/fhgqiS/happy.png)
### Realtime pulse display
![alt text](https://image.ibb.co/gxbCxn/withp.png)
### Suggessions of contents depending on your current mood
![alt text](https://image.ibb.co/bFhKcn/happy1.png)
### Real-time statistics 
![alt text](https://image.ibb.co/ei2Kcn/rtp.png)

## Authors

* **Muhammedh Ajwahir** 
* **Abdul Hafeez** 
* **Hamdan N Ridwan** 

## Reference 

[1] Balakrishnan, G., Durand, F., and Guttag, J. (2013). Detecting pulse from head motions in
video.  In
Proceedings of the 2013 IEEE Conference on Computer Vision and Pattern
Recognition
, CVPR ’13, pages 3430–3437, Washington, DC, USA. IEEE Computer
Society.
