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

### Update local status 

To adjust the local status of the device, the users can press the button on the device to switch between three statuses: Free to talk, Free but don’t want to talk, Busy. As shown in figure (1). We used three different colors to indicate three different statuses: Free to talk (Green), Free but don’t want to talk (Blue), Busy (Red). After pressing the button, the user’s status board will change color accordingly.

![Figure(1)](imgs/Figure(1).png)

### Sync status across multiple devices

To connect different multiple devices, we used the similar structure we have learned and used in Lab 6. MQTT was used to send and sync states between different devices. Whenever a user presses the button to change the status, it will send the new status over MQTT under the specific topic `IDD/Illusinate/playerX_status`. The path here will be determined by which player is using the Raspberry Pi. As shown in figure (2).

![Figure(2)](imgs/Figure(2).png)

### Facial impression translation

To translate the facial impressions to emojis, we utilized what we have learned and used in Lab5. We used Teachable Machine service to help us train a Computer Vision model that can identify whether a user's facial impression is indicating a good mood or not. By doing so, we can adjust the emoji on the user's status board accordingly.

## Design

To make the device more usable, we use cardboards to let the user be able to put the device on their desk and adjust it to an angle that the user can easily see all the users’ statuses and press the button to update their own statuses.

Also, because our device is aiming to let the user be able to have a phone call with their available friends, we also designed the device the way that the user can put their phones on it, as shown in the video later.

![IMG_5343](imgs/Figure(3).png)

## Project Video

[Demo Video](https://drive.google.com/file/d/1Fq6qUFNlfVv9uQ__QDI-Z0VBWKINB6cy/view)

## Reflection

In the process of the final project, we learned to integrate what we have learned in the previous labs and made something that we think can be valuable and useful for people. 

The display technique we learned in lab 2 help us program the user interface of the status board. In lab 4, we also learned about leveraging cardboard to increase the device's usability and make it more enjoyable to use, which also contributed to the status board's final design. As we have mentioned above, in lab 5 we learned about how to use services like Teachable Machine to support Computer Vision functions like image recognition and classification, which enables us to add the features to translate facial impressions to emojis. Last but not least, in lab 6 we learned about MQTT and how to send and sync states between different devices. By adopting a similar structure, we make the status board able to connect to multiple devices, and therefore, multiple people.





