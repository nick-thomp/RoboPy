from .open_app import OpenAppTask
from .type_text import TypeTextTask
from .press_keys import PressKeysTask
from .wait import WaitTask
from .click import ClickTask
from .launch_webbrowser import LaunchWebsiteTask

TASK_REGISTRY = {
    "open_app": OpenAppTask,
    "type_text": TypeTextTask,
    "press_keys": PressKeysTask,
    "wait": WaitTask,
    "click": ClickTask,
    "launch_webbrowser": LaunchWebsiteTask
}
