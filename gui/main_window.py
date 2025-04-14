import sys
from PySide6.QtWidgets import QListWidget, QMainWindow, QHBoxLayout, QTextEdit, QVBoxLayout, QPushButton, QWidget, QScrollArea, QLabel
import os
from runner import run_workflow
import yaml
from functools import partial

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RoboPy Assistant")
        self.setGeometry(200, 200, 600, 400)

        self.workflow_list = self.get_workflow_files()
        self.parsed_workflow = None
        self.workflow_dir = os.path.join(os.getcwd(), 'workflows')
        self.init_ui()

    def get_workflow_files(self):
        workflows_dir = 'workflows'
        return [f for f in os.listdir(workflows_dir) if f.endswith('.yaml')]

    def init_ui(self):
        central_widget = QWidget()
        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        # Workflow button list
        self.workflow_btn_list = QListWidget()
        self.workflow_btn_list.itemClicked.connect(self.update_workflow_steps)
        left_layout.addWidget(self.workflow_btn_list)

        # Step preview and run btn
        self.step_preview = QTextEdit()
        self.step_preview.setReadOnly(True)
        self.workflow_run_button = QPushButton("Run Workflow")
        self.workflow_run_button.clicked.connect(self.start_workflow)

        right_layout.addWidget(self.step_preview)
        right_layout.addWidget(self.workflow_run_button)

        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        # Set the layout
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        for workflow in self.workflow_list:
            self.workflow_btn_list.addItem(workflow)

    def update_workflow_steps(self, item):
        with open(f"{self.workflow_dir}/{item.text()}", "r") as f:
            self.parsed_workflow = yaml.safe_load(f)
        str_steps = yaml.dump(self.parsed_workflow, default_flow_style=False)

        self.step_preview.setText(str_steps)

    def start_workflow(self):
        # Trigger the runner to run the selected workflow
        result = run_workflow(self.parsed_workflow)
        if result == True:
            print(f"Workflow {self.parsed_workflow['name']} executed successfully!")
        else:
            print(f"Error running {self.parsed_workflow['name']} please check logs")