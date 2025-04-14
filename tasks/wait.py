import time
from .base_task import BaseTask

class WaitTask(BaseTask):

    def __init__(self, step_data):
        self.seconds = step_data.get('seconds')

    def run(self):
        try:
            time.sleep(float(self.seconds))
            return {"status": "success", "message": f"Waited for {self.seconds} seconds"}
        except Exception as e:
            return {"status": "error", "message": f"Error: {e}"}