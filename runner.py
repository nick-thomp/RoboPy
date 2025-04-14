from tasks import TASK_REGISTRY
from utils.logger import Logger

logger = Logger()

def run_workflow(workflow):
    is_successful = True  
    workflow_name = workflow.get('name', 'Unnamed')
    print(f"Running workflow: {workflow_name}")
    logger.start_run(workflow_name)
    for step in workflow.get("steps", []):
        task_type = step.get("type")
        task_cls = TASK_REGISTRY.get(task_type)
        
        if not task_cls:
            print(f"Unknown task: {task_type}")
            continue
        
        task = task_cls(step)
        result = task.run()
        if result['status'] == False:
            is_successful == False
        logger.write_log(f"{step} - {result['status']}: {result['message']}")
    logger.end_run()

    return is_successful
