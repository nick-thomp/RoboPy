from pyautogui import typewrite
from .base_task import BaseTask
import time

class TypeTextTask(BaseTask):
    
    def __init__(self, step_data):
        self.text = step_data.get('text')

    def run(self):
        if not self.text:
            return {"status": "error", "message": f"No text provided"}
        
        try:
            typewrite(self.text)
            time.sleep(1)
            return {"status": "success", "message": f"Finished typeing {self.text}"}
        except Exception as e:
            return {"status": "error", "message": f"Error: {e}"}