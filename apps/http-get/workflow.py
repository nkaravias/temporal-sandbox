# workflow.py
from temporalio import workflow
import activities


@workflow.defn
class GitOpsWorkflow:
    @workflow.run
    async def run(self, path: str, repo_url: str, repo_path: str, api_url: str):
        await workflow.execute_activity(activities.navigate_to_path, path)
        await workflow.execute_activity(activities.git_clone, repo_url)
        files = await workflow.execute_activity(activities.list_files_in_repo, repo_path)
        print("Files in repository:", files)
        api_response = await workflow.execute_activity(activities.http_get_request, api_url)
        print("API response:", api_response)
