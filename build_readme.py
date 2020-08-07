import sys

import httpx

README_TEMPLATE = """
### Hi there 👋

My name is Timothée Mazzucotelli,
I learned computer science at a french university,
and now have a few years of experience in development,
particularly with Python.

I really enjoy sharing my code
and contributing to other projects!

You can see [a showcase of my projects on my website][showcase]
(sorry for the heavy GIFs and SVGs :sweat_smile:),
as well as [the list of my blog posts][blog].

Here are some [auto-updated][sw-post]
stats about my published Python projects:

Total downloads: {total_dl:,}<br>
Downloads/month: {total_dl_per_month:,}<br>
Stars count: {total_stars:,}

It ain't much (and it doesn't mean much either),
but I'm nonetheless proud to see
that what I created is used by others :heart_eyes:

You can see more about what I'm working on
on my [support page][support]!

[sw-post]: https://simonwillison.net/2020/Jul/10/self-updating-profile-readme/
[showcase]: https://pawamoy.github.io/showcase/
[blog]: https://pawamoy.github.io/
[support]: https://github.com/sponsors/pawamoy/
""".lstrip("\n")

GITHUB_ACCOUNTS = [
    "pawamoy",
    "shellm-org",
    "shenv"
]

PYTHON_PROJECTS = [
    "aria2p",
    "mkdocstrings",
    "shellman",
    "git-changelog",
    "keycut",
    "mvodb",
    "ansito",
    "django-app-settings",
    "unminder",
    "shellhistory",
    "pytkdocs",
    "pawabot",
    "privibot",
    "archan",
    "django-cs-models",
    "django-suit-dashboard",
    "failprint",
    "dependenpy",
    "neo4j-api",
    "django-zxcvbn-password",
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

    with open("README.md", "w") as fd:
        fd.write(README_TEMPLATE.format(
            total_dl=total_dl,
            total_dl_per_month=total_dl_per_month,
            total_stars=total_stars,
        ))

    return 0


if __name__ == "__main__":
    sys.exit(main())
