import subprocess
from .base_task import BaseTask

class OpenAppTask(BaseTask):
    
    def __init__(self, step_data):
        self.path = step_data.get('path')

    def run(self):
        if not self.path:
            return {"status": "error", "message": "No path provided"}
        
        try:
            subprocess.Popen(self.path)
            return {"status": "success", "message": f"{self.path} opened"}
        except Exception as e:
            return {"status": "error", "message": f"Error: {e}"}