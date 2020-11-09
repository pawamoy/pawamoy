import sys

import httpx

README_TEMPLATE = """
Total downloads: {total_dl:,}<br>
Downloads/month: {total_dl_per_month:,}<br>
Stars count: {total_stars:,}
""".strip("\n")

GITHUB_ACCOUNTS = [
    "pawamoy",
    "shellm-org",
    "shenv"
]

PYTHON_PROJECTS = [
    "ansito",
    "archan",
    "aria2p",
    "django-app-settings",
    "django-cs-models",
    "django-suit-dashboard",
    "django-zxcvbn-password",
    "dependenpy",
    "duty",
    "failprint",
    "git-changelog",
    "keycut",
    "mkdocstrings",
    "moving-stars",
    "mvodb",
    "neo4j-api",
    "pawabot",
    "privibot",
    "pytkdocs",
    "shellhistory",
    "shellman",
    "unminder",
]

PEPYTECH_API_URL = "https://api.pepy.tech/api/projects/"
GITHUB_API_URL = "https://api.github.com/"

def main():
    total_stars = total_dl = total_dl_per_month = 0
    with httpx.Client() as client:
        for project in PYTHON_PROJECTS:
            data = client.get(PEPYTECH_API_URL + project).json()
            total_dl += data["total_downloads"]
            total_dl_per_month += sum(data["downloads"].values())

        for account in GITHUB_ACCOUNTS:
            repos = client.get(GITHUB_API_URL + f"users/{account}/repos?per_page=100").json()
            total_stars += sum(repo["stargazers_count"] for repo in repos)

    text = README_TEMPLATE.format(
        total_dl=total_dl,
        total_dl_per_month=total_dl_per_month,
        total_stars=total_stars,
    )

    with open("README.md") as fd:
        lines = fd.read().splitlines(keepends=False)

    marker_start = lines.index("<!--marker-->")
    marker_end = lines.index("<!--end-->")
    lines = lines[:marker_start+1] + [text] + lines[marker_end:]

    with open("README.md", "w") as fd:
        fd.write("\n".join(lines))

    return 0


if __name__ == "__main__":
    sys.exit(main())
