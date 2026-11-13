from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "title": "Face Detection",
        "description": "Detects faces in images and in real-time webcam video using OpenCV Haar Cascade classifiers, with bounding boxes and the option to save detected faces.",
        "tech_stack": ["Python", "OpenCV"],
        "github_url": "https://github.com/remy1777/Face-Detection-using-OpenCV-in-Python-main",
        "image": "",
    },
    {
        "title": "Hand Gesture Volume Control",
        "description": "Adjusts the Windows system volume in real time from the distance between thumb and index finger, using MediaPipe hand tracking. Based on an open-source project by Pushtogithub23.",
        "tech_stack": ["Python", "OpenCV", "MediaPipe", "pycaw"],
        "github_url": "https://github.com/remy1777/Gesture-Volume-Control-using-MediaPipe-and-OpenCV-master",
        "image": "",
    },
    {
        "title": "Speech Recognition App",
        "description": "A desktop app that captures speech from the microphone and transcribes it to text, with a simple graphical interface.",
        "tech_stack": ["Python", "Tkinter", "SpeechRecognition"],
        "github_url": "https://github.com/remy1777/Speech-Recognition-main",
        "image": "",
    },
    {
        "title": "News Article Summarizer",
        "description": "Fetches a news article from a URL and selects its key sentences to build an extractive summary, with named entities and article statistics.",
        "tech_stack": ["Python", "NLP", "Streamlit"],
        "github_url": "https://github.com/remy1777/News-Article-Summarizer-main",
        "image": "",
    },
    {
        "title": "Titanic Survival Analysis",
        "description": "Statistical analysis and visualization of the Titanic dataset, exploring how gender, class, age and family size influenced survival.",
        "tech_stack": ["Python", "Pandas", "Jupyter Notebook"],
        "github_url": "https://github.com/remy1777/titanic-survival-analysis-main",
        "image": "",
    },
    {
        "title": "YT-DLP GUI",
        "description": "A graphical interface for downloading videos with yt-dlp, built with pure Python and Tkinter.",
        "tech_stack": ["Python", "Tkinter", "yt-dlp"],
        "github_url": "https://github.com/remy1777/ytdlp-gui-master",
        "image": "",
    },
]

@app.route("/")
def home():
    return render_template("index.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True)