import os
from datetime import datetime

class Logger:
    def __init__(self, log_dir='logs'):
        self.log_dir =  os.path.join(os.getcwd(), log_dir)
        self.log_file = None

        # Ensure log directory exists
        os.makedirs(self.log_dir, exist_ok=True)

    def start_run(self, log_task):
        # make sure log task is lower case and has no spaces
        log_task = log_task.lower().replace(' ', '_')

        timestamp = datetime.now().strftime("%m_%d_%Y_%H%M%S")
        log_filename = f"{self.log_dir}/{log_task}_run_{timestamp}.txt"

        self.log_file = open(log_filename, 'w')
        self.write_log(f"Run started at {timestamp}")

    def write_log(self, message):
        if self.log_file:
            self.log_file.write(message + '\n')
            print(message)

    def end_run(self):
        if self.log_file:
            self.write_log(f"Run ended at {datetime.now()}")
            self.log_file.close()