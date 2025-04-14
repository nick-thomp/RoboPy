import webbrowser
from .base_task import BaseTask

class LaunchWebsiteTask(BaseTask):
    
    def __init__(self, step_data):
        self.url = step_data.get('url')

    def run(self):
        if not self.url:
            return {"status": "error", "message": "No url provided"}
        
        if not self.url.startswith(('http://', 'https://')):
            return {"status": "error", "message": "Invalid URL format"}

        try:
            webbrowser.open(self.url)
            return {"status": "success", "message": f"{self.url} opened"}
        except Exception as e:
            return {"status": "error", "message": f"Error: {e}"}
            