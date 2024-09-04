# Cleanlab Python take-home coding screen

# Summary

Write a Python script [`stars.py`](http://stars.py) that finds the set of people who have starred any of a collection of given repositories.

**Input**: the script should take a list of repositories as command-line arguments

**Output**: the script should print the set of usernames, one per line

**Example invocation**:

```
$ python stars.py cleanlab/cleanlab BurntSushi/ripgrep
anishathalye
lukemainwaring
...
axl1313

```

# Details

- The script can print usernames in any order
- Each username should appear only once, even if the person has starred multiple repositories in the given set
- You can use the [GitHub REST API](https://docs.github.com/en/rest) using a library like [requests](https://pypi.org/project/requests/) or a library like [PyGithub](https://pygithub.readthedocs.io/en/latest/introduction.html) (we recommend using PyGithub)
    - You can generate a GitHub API token by navigating to the [fine-grained access tokens page](https://github.com/settings/tokens?type=beta), clicking “generate”, giving the token a name, and leaving all the permissions at their default settings (public repositories, no access under account permissions).

# Notes

- This assignment is “open-book”: feel free to use GitHub, Stack Overflow, or any other online resource.
- We expect this assignment to take < 30 min (avg 15 min). Our reference solution is 8 lines of code.
- Don’t worry about performance, rate limiting, or error handling. As long as the logic is correct, and it works on repos with a small number of stars, you’re good.
- If you make any assumptions, write them down in a comment.
