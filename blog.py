import os
import openai
from git import Repo

from pathlib import Path

PATH_TO_BLOG_REPO = Path("/Users/admin/Desktop/test/py/GitHub/openai/.git")

PATH_TO_BLOG = PATH_TO_BLOG_REPO.parent

PATH_TO_CONTENT = PATH_TO_BLOG/"content"

PATH_TO_CONTENT.mkdir(exist_ok=True, parents=True)


def update_blog(commit_message='Updated blog'):
    repo = Repo(PATH_TO_BLOG_REPO)
    # git add .
    repo.git.add(all=True)
    # git commit -m "update blog"
    repo.index.commit(commit_message)
    # git push
    origin = repo.remote(name='origin')
    print(origin.push())


random_string = "hello"

with open(PATH_TO_BLOG/"index.html", "w") as f:
    f.write(random_string)

update_blog()
