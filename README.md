# ai_face_detection
This is a project i decided to do out of pure curiosity and interest i have in artificial intelligence and its capabilities. This project detects human faces in real-time using the **OpenCV Haar Cascade Classifier**.  
It uses a pre-trained XML model provided by the official OpenCV project.

# Dependancies
1. Python 3.8 or newer  
2. Webcam (built-in or USB)
3. `haarcascade_frontalface_default.xml` file (from OpenCV repository)
5. The following Python packages(In the requirements.txt):
  `opencv-python`
  `numpy`

# Setup Steps
1. Clone my repository
git clone https://github.com/YOUR_USERNAME/ai_face_detection.git
cd ai_face_detection/face_detect 

2. A For macOS / Linux:
python3 -m venv venv
source venv/bin/activate

2. B For Windows(CMD or PowerShell)
python -m venv venv
venv\Scripts\activate

3. Install Dependancies
pip install -r requirements.txt

4. Download the pretrained classifier from OpenCV’s GitHub and place it in your project folder(make sure its in the same folder as main.py)

5. Run your programme

# Acknowledgments
This project uses the `haarcascade_frontalface_default.xml` file from the OpenCV project,  
licensed under the [Apache 2.0 License](https://github.com/opencv/opencv/blob/4.x/LICENSE).

This project also takes inspiration from multiple youtube sources,
Tiff in Tech: https://www.youtube.com/watch?v=i3sLv1sus0I
Nicholas Renotte: https://www.youtube.com/watch?v=bK_k7eebGgc 