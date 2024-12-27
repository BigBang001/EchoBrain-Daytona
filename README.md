This repository contains a README file sample for Daytona Samples and the MIT License.

It can be used as a template to create sample repositories that can be added into [Daytona](https://github.com/daytonaio/daytona).

Once you finish your sample and it gets merged, you can open a PR in the Daytona repo and submit the sample into the [index file](https://github.com/daytonaio/daytona/blob/main/hack/samples/index.json).


# EchoBrain: Intelligent Voice-Controlled Virtual Assistant

EchoBrain is a cutting-edge voice-controlled assistant powered by AI, capable of understanding and executing complex commands on both desktop and mobile devices. With features like facial recognition and seamless phone integration, EchoBrain automates tasks and offers a secure, efficient user experience.

❓ EchoBrain isn’t just a name; it’s a concept that merges cutting-edge artificial intelligence with natural human interaction. Imagine speaking to a smart assistant that not only listens but understands and responds as if it were a conversation with your own brain. The *Echo* symbolizes how your voice reverberates into action, and the *Brain* signifies the deep computational intelligence behind it. This unique combination creates an experience where commands are processed and executed, turning your voice into a powerful tool for automation and smart interaction.

---

## 🚀 Getting Started  

### Open Using Daytona  

1. **Install Daytona**: Follow the [Daytona installation guide](https://www.daytona.io/docs/installation/installation/).  
2. **Create the Workspace**:  
   ```bash  
   daytona create <SAMPLE_REPO_URL> 
   ```  
3. **Set Up Development Container**:  
   The project includes a `devcontainer.json` for a fully configured environment.  
4. **Run the Application**:  
   Launch the assistant with:  
   ```bash  
   python rum.py
   ```  

---

## ✨ Key Features  

- **Voice Command Processor**: Uses advanced NLP techniques for interpreting commands.  
- **Desktop & Phone Automation**: Control your computer and mobile device from a single interface.  
- **Facial Authentication**: Enhances security with real-time face recognition.  
- **Cross-Platform Communication**: Synchronize tasks between your desktop and phone effortlessly.  
- **Seamless Phone Integration**: Make calls, send texts, and open apps on your phone via ADB.  
- **Modular Architecture**: Easily extendable to add new functionalities as required.

---

## 🛠️ Technology Stack  

- **Python**: Core language for building and running the assistant.  
- **TensorFlow**: For integrating machine learning models.  
- **OpenCV**: Used for facial recognition and computer vision tasks.  
- **SQLite**: Lightweight database for storing preferences and session data.  
- **pyttsx3**, **SpeechRecognition**: To enable speech input and output for seamless interaction.  
- **Eel**, **PyAutoGUI**, **Pyaudio**: For creating the GUI and automating desktop tasks.  
- **HugChat API**: For intelligent chatbot capabilities.  
- **HTML**, **CSS**, **JavaScript**, **Bootstrap**: Frontend for smooth user interaction.

---

## 💡 How EchoBrain Works  

EchoBrain listens to voice commands, processes them using natural language understanding, and automates a range of tasks, including desktop controls, phone integration, and user feedback mechanisms. Whether it’s managing your calendar, sending messages, or controlling your PC’s apps, EchoBrain makes your tasks more efficient.

---

## 📸 Project Screenshots  
<p align="center">  
  <img src="https://github.com/user-attachments/assets/f178e89a-a85f-453c-a0c3-88478b44560e" alt="Starting Window" width="400">  
  <br>  
  Fig 1. EchoBrain Starting Window - Initial screen on launch
</p>  <br>

<p align="center">  
  <img src="https://github.com/user-attachments/assets/2a82211b-3702-45fa-8c25-66cd23f5fbb6" alt="Starting Window" width="400">  
  <br>  
  Fig 2. Facial Authentication - Secure login through face recognition 
</p> 
<br>

<p align="center">  
  <img src="https://github.com/user-attachments/assets/123561f8-cff8-4d14-b227-2e7d752bdad6" alt="App Launch" width="400">  
  <br>  
    <img src="https://github.com/user-attachments/assets/916d8178-02cd-4d31-8ee4-219361aaf31f" alt="App Launch" width="400"> 
   <br>
  Fig 3. Desktop Automation - Opening Canva via voice command  
</p>  
<br>

<p align="center">  
  <img src="https://github.com/user-attachments/assets/e9f7a70a-090b-424e-9a16-148a5174fdf1"
 alt="YouTube Opened" width="400">  
  <br>  
  <img src="https://github.com/user-attachments/assets/a5d801d9-d405-4d90-815f-24d50f442839"
 alt="YouTube Opened" width="400">
   <br>
  Fig 4. Phone Automation - Opening YouTube on mobile  
</p>  
<br>

<p align="center">  
    <img src = "https://github.com/user-attachments/assets/1e0ca829-4b5a-44fb-8615-ca2e8dee37ba" alt="Answering with Examples" width="400" >
  <br> 
  <img src="https://github.com/user-attachments/assets/1aff61b8-c5f8-486e-b6e2-99c7bbad8d4c"
  alt="Answering with Examples" width="400">  
   <br>
  Fig 5. Intelligent Q&A - Answering user queries with examples 
</p>  
 

---


## 🔧 Setup Instructions  

1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/BigBang001/EchoBrain.git
   cd EchoBrain
   ```  
2. **Install Dependencies**:  
   ```bash  
   pip install -r requirements.txt
   ```  
3. **Launch the Application**:  
   ```bash  
   python run.py
   ```  


---

With EchoBrain, you're not just getting a virtual assistant — you’re getting a smart, customizable assistant that learns and adapts to your needs, all while making your day-to-day tasks more efficient and secure.
