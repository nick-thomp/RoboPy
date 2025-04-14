# 🤖 RoboPy

RoboPy is a Python-based automation tool inspired by platforms like UiPath — allowing you to build, manage, and run workflows using a customizable GUI and Python logic under the hood.

Built with **PySide6**, RoboPy aims to bring the power of desktop automation and scripting into a lightweight, extensible framework.

---

## 🛠 Features

- 🧱 Task-based modular system (clicking, typing, waiting, etc.)
- 🗂 Workflow builder to chain actions together
- 🖥 GUI interface built with PySide6
- 🧰 Utilities and logging to support debugging
- ⚙ Workflow runner for automation execution

---

## 📁 Project Structure

```bash
robopy/
├── gui/ # PySide6 GUI components 
├── logs/ # Workflow logs (gitignored) 
├── tasks/ # Atomic task definitions (click, type, etc.) 
├── utils/ # Helpers and shared utilities 
├── workflows/ # User-defined task sequences 
├── main.py # GUI launcher 
├── runner.py # Core engine for running workflows
```
---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/robopy.git
cd robopy
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python main.py
```

---
## Dependencies

### Key libraries:
- **PySide6** - For GUI
- **pyautogui** - For mouse click, keyboard, etc.

---
## Notes
- Logs for each workflow run are saved into ```logs/``` folder
- Workflows are defined in the ```workflows/``` directory
- Each workflow is a ```.yaml``` file
- Tasks are modular, making it easy to add new ones — just drop a new Python module into the ```tasks/``` folder.

---

## 🛣 Roadmap

Here are some planned features and ideas:

- [ ] 🧱 GUI workflow builder
- [ ] 🎯 Focus window by title/class
- [ ] 📸 Take screenshots
- [ ] 🖱️ Move mouse to position
- [ ] 🔃 Scroll, drag & drop
- [ ] 📝 Fill out forms (web or desktop)
- [ ] 📋 View logs in GUI
- [ ] 🔕 Toggle logs on/off per task
- [ ] 🎙️ Record mouse and keyboard actions
- [ ] 🔁 Looping and conditional logic
- [ ] 🌐 Support for environment variables

*Got an idea? Open an issue or fork the project!*
