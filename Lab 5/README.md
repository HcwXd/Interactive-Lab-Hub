# Observant Systems

For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture.
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms need to be aware of.

In Lab 5 part 1, we focus on detecting and sense-making.

In Lab 5 part 2, we'll incorporate interactive responses.

## Prep

1.  Pull the new Github Repo.
2.  Read about [OpenCV](https://opencv.org/about/).
3.  Read Belloti, et al's [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf)

### For the lab, you will need:

1. Raspberry Pi
1. Raspberry Pi Camera (2.1)
1. Microphone (if you want speech or sound input)
1. Webcam (if you want to be able to locate the camera more flexibly than the Pi Camera)

### Deliverables for this lab are:

1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview

Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A

### Play with different sense-making algorithms.

Befor you get started connect the RaspberryPi Camera V2. [The Pi hut has a great explanation on how to do that](https://thepihut.com/blogs/raspberry-pi-tutorials/16021420-how-to-install-use-the-raspberry-pi-camera).

#### OpenCV

A more traditional to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python.

Additionally, we also included 4 standard OpenCV examples. These examples include contour(blob) detection, face detection with the `Haarcascade`, flow detection(a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (I.e. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a `HowToUse.md` file, which explains how to run the python example.

```shell
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```

#### Filtering, FFTs, and Time Series data. (beta, optional)

Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU data stream could create a simple activity classifier between walking, running, and standing.

Using the set up from the [Lab 3 demo](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Spring2021/Lab%203/demo) and the accelerometer, try the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up averaging** Can you average your signal in N-sample blocks? N-sample running average?

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

Include links to your code here, and put the code for these in your repo--they will come in handy later.

#### Teachable Machines (beta, optional)

Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple. However, its simplicity is very useful for experimenting with the capabilities of this technology.

You can train a Model on your browser, experiment with its performance, and then port it to the Raspberry Pi to do even its task on the device.

Here is Adafruit's directions on using Raspberry Pi and the Pi camera with Teachable Machines:

1. [Setup](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/raspberry-pi-setup)
2. Install Tensorflow: Like [this](https://learn.adafruit.com/running-tensorflow-lite-on-the-raspberry-pi-4/tensorflow-lite-2-setup), but use this [pre-built binary](https://github.com/bitsy-ai/tensorflow-arm-bin/) [the file](https://github.com/bitsy-ai/tensorflow-arm-bin/releases/download/v2.4.0/tensorflow-2.4.0-cp37-none-linux_armv7l.whl) for Tensorflow, it will speed things up a lot.
3. [Collect data and train models using the PiCam](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/training)
4. [Export and run trained models on the Pi](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/transferring-to-the-pi)

Alternative less steps option is [here](https://github.com/FAR-Lab/TensorflowonThePi).

#### PyTorch

As a note, the global Python install contains also a PyTorch installation. That can be experimented with as well if you are so inclined.

### Part B

### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interactions outputs and inputs.
**Describe and detail the interaction, as well as your experimentation.**

The models I have tried is a system that can detect users hand gesture that represent a number from zero to three. Such a gesture detection system can be used in many application and scenarios. For example, in a virtual classroom using webcam like zoom, this system can help the student in the classroom easily answer teacher's multi-choice by just use hand gesture to represent the number that is the correct option. It can also be used to quick give feedback to a Likert scale question given by someone who need to be graded.

![0](images/0.png)

![1](images/1.png)

![2](images/2.png)

![3](images/3.png)

### Part C

### Test the interaction prototype

Now flight test your interactive prototype and **note your observations**:
For example:

1. When does it what it is supposed to do?

   The model works well for most cases when testing only hand is in the image due to the large data set that is used in training.

1. When does it fail?

   The model failed in two major cases: when the hand gesture for one is not super clear and when there's face in the image. 
   ![f2](images/f2.png) 

   ![f1](images/f1.png)

1. When it fails, why does it fail?

   For one is not super clear, it failed because the gesture of the one in hand may look a little bit like two for machine. For the face in the image, it failed because I failed to take this into consideration.

1. Based on the behavior you have seen, what other scenarios could cause problems?
   Based on the aforementioned observation, if may cause problem when we used it in scenario like zoom since it in zoom, people usually have their face included in the video.

**Think about someone using the system. Describe how you think this will work.**

To fix the problem I mentioned before, I add more training dataset with human face involved and do the training again. Right now, the model can work fine with human face in the video.

![00](images/00.png)

![11](images/11.png)

![22](images/22.png)

![33](images/33.png)


1. Are they aware of the uncertainties in the system?

   They should not be aware of the uncertainties in the system if such system is implemented in the product like Zoom. People will expect this system work without error.

1. How bad would they be impacted by a miss classification?

   If there's a miss classification, user may be affected much if the consequence of the result is pretty significant. For example, if the user is using it for some graded question, then they may be impacted badly. Otherwise, they may not be affected much. 

1. How could change your interactive system to address this?
   We can have the some soft of disclaimer such as buttons or other input in the system. In this way, we can always fallback to a simpler method of answering the question or ranking.

1. Are there optimizations you can try to do on your sense-making algorithm.

   An optimization has been done to address the issue of having human face in the system. For make it robust, we can have user report the error and put those image who gets error back to our model and train the model again.

https://teachablemachine.withgoogle.com/models/SyN511r9t/

### Part D

### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:

- What can you use X for?
- What is a good environment for X?
- What is a bad environment for X?
- When will X break?
- When it breaks how will X break?
- What are other properties/behaviors of X?
- How does X feel?

**Include a short video demonstrating the answers to these questions.**

What can you use X for?

Gesture detection system like this one can be used for classifying real-time reaction. Like mention before, this can be used in a virtual classroom using webcam like zoom. This system can help the student in the classroom easily answer teacher's multi-choice by just use hand gesture to represent the number that is the correct option. It can also be used to quick give feedback to a Likert scale question given by someone who need to be graded.

What is a good environment for X?

An environment with great video resolution, proper lighting conditions and simple background will be a good environment for the gesture detection system.

- What is a bad environment for X?

A bad environment where the video resolution is bad, lighting conditions is not good or background is messy will be bad environment for the gesture detection system.

- When will X break?

In any of the aforementioned bad environments the gesture detection system may break.

- When it breaks how will X break?

The gesture detection system will break either by not detecting a gesture or doing a miss classification.

- What are other properties/behaviors of X?

There's no other properties of the gesture detection system.

- How does X feel?

It feels like a modern technology that should be used in every video call meeting. This kind of technology can make user more engaged in the video call since they then don't have to use the keyboard or mouse to answer the question or give feedback.

Video: [Google Drive Link](https://drive.google.com/file/d/1BvGbEzLEJ4WUNvoHpWaht6FN_x2vlvaM/view?usp=sharing)

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**Include a short video demonstrating the finished result.**