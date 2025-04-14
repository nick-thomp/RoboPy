from pyautogui import hotkey
from .base_task import BaseTask
import time

class PressKeysTask(BaseTask):

    def __init__(self, step_data):
        self.keys = step_data.get('keys', [])

    def run(self):
        if not isinstance(self.keys, list) or not all(isinstance(k, str) for k in self.keys):
            return {"status": "error", "message": "Keys must be a list of strings"}
        
        try:
            hotkey(*self.keys)
            time.sleep(1)
            return {"status": "success", "message": f"Pressed keys:  {', '.join(self.keys)}"}
        except Exception as e:
            return {"status": "error", "message": f"Erorr: {e}"}