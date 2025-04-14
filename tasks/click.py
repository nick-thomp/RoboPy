from pyautogui import click
from .base_task import BaseTask

class ClickTask(BaseTask):

    def __init__(self, step_data):
        self.button = step_data.get('button', 'left')
        self.x = step_data.get('x')
        self.y = step_data.get('y')

    def run(self):
        if self.x is None or self.y is None:
            return {"status": "error", "message": "Missing coordinates for click"}

        try:
            x = int(self.x)
            y = int(self.y)
            click(x=x, y=y, button=self.button)
            return {"status": "success", "message": f"{self.button} click at ({x}, {y})"}
        except Exception as e:
            return {"status": "error", "message": f"Error: {e}"}
