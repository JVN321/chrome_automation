# Chrome Automation for NASSCOM FutureskillsPrime

A Python + Selenium + PyAutoGUI project that automates course completion and quiz taking on the NASSCOM FutureSkills Prime platform.
It launches Chrome with remote debugging, logs in, navigates through course content, marks modules as complete, launches quizzes, and auto‑answers them using injected JavaScript and image‑based UI clicks.

## Features

- Headless‑style automation via Selenium and Chrome remote debugging
- In‑browser helper scripts (`nasscom_auto.js`, `nasscom_quiz.js`) for DOM interaction
- Screenshot‑driven clicks (start buttons, DevTools panels, submit buttons) using PyAutoGUI
- Clipboard injection of quiz‐solving script via Pyperclip
- Parallel process orchestration with `run.py`

## Prerequisites

- Python 3.8+
- Google Chrome
- Windows OS (tested on 10/11)
- Screen resolution & DPI consistent with reference images

## Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/JVN321/chrome_automation.git
   cd chrome_automation
   ```
2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
3. Copy or capture reference screenshots into the project root:

   - `start.png`
   - `inspect_icon.png`
   - `submit.png`
   - `console.png`
   - `final_submit.png`
4. Create a `.env` file in the project root with your login credentials:

   ```env
   USERNAME=your_username
   PASSWORD=your_password
   ```

## Usage

Simply run the orchestrator script:

```bash
python run.py
```

- `launch.py` opens Chrome on port 9222 and logs in.
- After a short wait, `main.py` attaches to that Chrome instance, injects the JS helpers, marks all modules complete, launches quizzes, and auto‑submits answers.

### Tips

- Adjust `time.sleep()` delays in `run.py`, `launch.py`, and `main.py` if your network or machine is slower/faster.
- Ensure DevTools shortcuts (`F12`) and UI element screenshots match your locale/theme.
- If an element isn’t found, update selectors in `nasscom_auto.js` or replace the reference image for PyAutoGUI.

## File Structure

```
chrome_automation/
├── launch.py           # Launches Chrome & logs in via Selenium
├── main.py             # Attaches to Chrome, injects JS, automates content & quizzes
├── nasscom_auto.js     # In‑page helper: findCurrentCourse, markAsComplete, launch_quiz
├── nasscom_quiz.js     # In‑page quiz solver: find_answers()
├── run.py              # Orchestrates concurrent launch.py & main.py
├── requirements.txt    # Python dependencies
├── .env                # (not checked in) USERNAME & PASSWORD
├── *.png               # Reference screenshots for PyAutoGUI
└── README.md           # This documentation
```

## License

MIT © Your Name
