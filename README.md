#  Eye Gaze Controlled Virtual Keyboard with Predictive Text and Emergency Alert

A real-time assistive technology system that enables users with motor or speech impairments to type using **eye gaze** and **blinks**. The system includes a predictive text feature for faster typing and an integrated **emergency alert module** that sends SMS notifications via **Twilio API**.

---

##  Features

-  **Real-time eye and blink detection** using webcam input.
-  **Predictive text suggestions** based on typed characters.
-  **Emergency alert system** triggered by long blink over "Emergency" key.
-  **Virtual keyboard GUI** controlled using gaze direction and blinks.
-  **Audio feedback** for key selection.
-  Lightweight and non-intrusive (no special hardware required).

---

##  Tools & Technologies

- **Python 3.12.5**
- **OpenCV** – Image and video processing
- **dlib** – 68-point facial landmark detection
- **imutils** – Facial landmark utilities and image handling
- **PyQt5** – GUI development for virtual keyboard
- **Twilio API** – SMS alert functionality
- **NumPy**, **math** – Supportive numerical operations

 ---
 ##  System Requirements

###  Hardware Requirements
- **Camera**: Standard webcam (minimum 720p resolution)
- **Processor**: Intel Core i3 or equivalent
- **Memory**: 4 GB RAM or higher
- **Operating System**: Windows 10 / Linux (Tested on Windows)

###  Software Requirements
- **Python**: Version 3.12.5
- **PyQt5**: Version 5.15 or higher
- **OpenCV**: Version 4.5 or higher
- **Dlib**: Pre-trained model for facial landmarks
- **Twilio API**: For sending SMS alerts (internet required)

  ---
  ##  Future Enhancements

-  **Text-to-Speech (TTS) Integration**  
  Add voice output for typed messages to enhance communication for users with visual impairments.

-  **Multilingual Support**  
  Include multiple language dictionaries for predictive text to serve a diverse user base.

-  **Mobile and Web App Development**  
  Extend the system to Android/iOS platforms and browsers using lightweight ML models.

-  **Adaptive Blink Detection**  
  Implement dynamic calibration for blink thresholds based on individual user patterns.

-  **ML-Based Gaze Estimation**  
  Integrate deep learning models for more precise and robust gaze tracking, even in low light or varying head poses.

-  **Customizable Interface**  
  Let users personalize keyboard layout, font size, and color contrast for better accessibility.

-  **Voice-Activated Emergency Commands**  
  Add voice backup for emergency triggers, improving reliability for multi-disability scenarios.

---
##  Authors

| Name                     | Roll Number   | Contribution                                |
|--------------------------|---------------|----------------------------------------------|
| **Jahnavi Katta**        | 21261A3231    | Implementation: Eye tracking, GUI, Testing   |
| **Nishitha Kanakanapuri**| 21261A3228    | Research: Predictive text, Emergency system  |

- **Department**: Computer Science and Business Systems  
- **Institution**: Mahatma Gandhi Institute of Technology (MGIT)    
- **Project Title**: *Eye Gaze Controlled Virtual Keyboard with Predictive Text and Emergency Alert System*  
- **Supervisor**: Dr. N. Sree Divya, Assistant Professor, MGIT
  
