from . import project_dir

projects_markdown_dir = project_dir.joinpath("static/md/projects")


def get_projects_markdown():
    projects = []
    for project_file in projects_markdown_dir.glob("*.md"):
        projects.append(project_file.read_text())
    return projects


def parse_markdown(markdown: str):
    raise NotImplementedError
