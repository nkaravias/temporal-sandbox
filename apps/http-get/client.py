# client.py
from temporalio.client import Client
import workflow
import asyncio


async def start_workflow():
    client = await Client.connect("localhost:7233")
    workflow_client = client.workflow_client
    handle = await workflow_client.start(
        workflow.GitOpsWorkflow.run,
        args=["/desired/path", "http://repository.git", "/desired/path/repository", "http://localhost:8449"],
        task_queue="git_ops_workflow_queue",
        id="git_ops_workflow_run"
    )
    print("Workflow started, ID:", handle.id)

asyncio.run(start_workflow())
