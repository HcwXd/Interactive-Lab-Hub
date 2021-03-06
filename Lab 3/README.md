# You're a wizard, [Student Name Here]

<img src="https://pbs.twimg.com/media/Cen7qkHWIAAdKsB.jpg" height="400">

In this lab, we want you to practice wizarding an interactive device as discussed in class. We will focus on audio as the main modality for interaction but there is no reason these general techniques can't extend to video, haptics or other interactive mechanisms. In fact, you are welcome to add those to your project if they enhance your design.


## Text to Speech and Speech to Text

In the home directory of your Pi there is a folder called `text2speech` containing some shell scripts.

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav

```

you can run these examples by typing 
`./espeakdeom.sh`. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts

```

You can also play audio files directly with `aplay filename`.

After looking through this folder do the same for the `speech2text` folder. In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

## Serving Pages

In Lab 1 we served a webpage with flask. In this lab you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/$ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to [http://ixe00.local:5000]()


## Demo

In the [demo directory](./demo), you will find an example wizard of oz project you may use as a template. **You do not have to** feel free to get creative. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser. You can control what system says from the controller as well.

## Optional

There is an included [dspeech](./dspeech) demo that uses [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) for speech to text. If you're interested in trying it out we suggest you create a seperarate virutalenv. 



# Lab 3 Part 2

Create a system that runs on the Raspberry Pi that takes in one or more sensors and requires participants to speak to it. Document how the system works and include videos of both the system and the controller.

## Prep for Part 2

1. Sketch ideas for what you'll work on in lab on Wednesday.

![Sketch](Images/Sketch.png)

## Share your idea sketches with Zoom Room mates and get feedback

*what was the feedback? Who did it come from?*

Justin Liu:

It's pretty cool. But right now it sounds a little bit like what Alexa can do.

Kae-Jer Cho:

I think the most important part may be how Raspberry Pi decides which songs to play. Also, sometimes people may want to listen to upbeat song when they're upset, but not listen to emotional song. 

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

The device, which I call him Dude, can take user's sentence as an input and do sentimental analyze using NLP. When you say "What's up Dude", this Dude will start to listen to your input. After capturing the user's emotion, this Dude will play a music based on the analysis.

*Include videos or screencaptures of both the system and the controller.*

[Video demo](https://drive.google.com/file/d/1maaFhJyj9pTmV-ozX9VxDxmGM7z5mWBb/view?usp=sharing)

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Two people tested the system -  Justin Liu, Kae-Jer Cho

Answer the following:

### What worked well about the system and what didn't?
In general, the interaction between the user and this Dude worked well. Adding a Siri-like interaction technique like saying "What's up Dude" before the actual command not only made the interaction more smooth but also made the user like the device more.

Something that didn't work well is that sometimes the user didn't like the music this Dude played.

### What worked well about the controller and what didn't?

The controller is easy to use in general and worked well with no latency.

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

One of the main lessons I can take away from the WoZ interaction for designing a more autonomous version of the system is that making the interaction fun and natural is very important for improving the whole experience. Saying something playful like "What's up Dude" to the device actually made the user like the device and also made the overall experience more lovely.

The other lesson I learn it is also important for the user to have the ability to specify some songs the user wants to listen to since, sometimes, the user may have made up his/her mind for listening to certain songs 


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

I could use my system to track all the songs the device plays and the reaction of the user. In this way, we can analyze whether some songs are working well in certain emotions.

The other sensing modalities we may capture are the facial expression or the heart rate of a user. These two sensing modalities can help us determine the user's emotion better.

