# activities.py
import os
import subprocess
import requests


def navigate_to_path(path: str):
    os.chdir(path)
    return "Navigated to " + path


def git_clone(repo_url: str):
    subprocess.run(["git", "clone", repo_url], check=True)
    return "Repository cloned"


def list_files_in_repo(repo_path: str):
    files = os.listdir(repo_path)
    return files


def http_get_request(url: str):
    response = requests.get(url)
    return response.text
