# worker.py
from temporalio.worker import Worker
import activities
import workflow


def main():
    with Worker.start("localhost:7233", task_queue="git_ops_workflow_queue") as worker:
        worker.register_workflow(workflow.GitOpsWorkflow)
        worker.register_activity(activities.navigate_to_path)
        worker.register_activity(activities.git_clone)
        worker.register_activity(activities.list_files_in_repo)
        worker.register_activity(activities.http_get_request)
        worker.run()


if __name__ == "__main__":
    main()
