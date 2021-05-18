# Final Project

Using the tools and techniques you learned in this class, design, prototype and test an interactive device.

Project Github page set up - May 3

Functional check-off - May 10

Final Project Presentations (video watch party) - May 12

Final Project Documentation due - May 19

## Project Description

Our project is a status dashboard that can connect with multiple devices from your friends. This device can be placed on the desk and you can set your own status for the moment right now, such as you're busy, you're available, or even like you have a short free time slot right now.

Besides status, our status dashboard also supports using Computer Vision to translate facial impressions to emojis. We will use the camera to detect the user's emotion and display the corresponding emoji on the screen of our device.

The status will sync with all your friends who also connected with your device, and you can chat with people with available status using the device just like you bump into them in a hallway and have a short small talk.

Special thanks to Angelica Kosasih (ak2725) for sharing the thoughts and inspiring me to have this idea at the beginning of the semester.

## Technical Implementation

To adjust the local status of the device, the users can press the button on the device to switch between three statuses: Free to talk, Free but don’t want to talk, Busy. As shown in figure (1). We used three different colors to indicate three different statuses: Free to talk (Green), Free but don’t want to talk (Blue), Busy (Red). After pressing the button, the user’s status board will change color accordingly.

![Figure(1)](imgs/Figure(1).png)

To connect different multiple devices, we used the similar structure we have learned and used in Lab 6. MQTT was used to send and sync states between different devices. Whenever a user presses the button to change the status, it will send the new status over MQTT under the specific topic `IDD/Illusinate/playerX_status`. The path here will be determined by which player is using the Raspberry Pi. As shown in figure (2).

![Figure(2)](imgs/Figure(2).png)

## Design

To make the device more usable, we use cardboards to let the user be able to put the device on their desk and adjust it to an angle that the user can easily see all the users’ statuses and press the button to update their own statuses.

Also, because our device is aiming to let the user be able to have a phone call with their available friends, we also designed the device the way that the user can put their phones on it, as shown in the video later.

![IMG_5343](imgs/Figure(3).png)

## Project Video

[Demo Video](https://drive.google.com/file/d/1Fq6qUFNlfVv9uQ__QDI-Z0VBWKINB6cy/view)











1. Documentation of design process
2. Archive of all code, design patterns, etc. used in the final design. (As with labs, the standard should be that the documentation would allow you to recreate your project if you woke up with amnesia.)
3. Video of someone using your project (or as safe a version of that as can be managed given social distancing)
4. Reflections on process (What have you learned or wish you knew at the start?)





