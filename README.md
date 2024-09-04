Just for fun, I added logging, an -o flag, and used a .env file for the token.

To set up, add the GitHub API token to a .env file:
GITHUB_TOKEN=<your_token_here>

To print the results to the console:
python stars.py cleanlab/cleanlab BurntSushi/ripgrep

To write the results to a file:
python stars.py cleanlab/cleanlab BurntSushi/ripgrep -o results.txt

While running the script, you can also see the detailed logs in the logs folder. I suggest tailing them:

tail -f logs/stargazers_log_20240724_123456.log

A log entry is emitted after each repository is processed. Final statistics are
displayed at the end for spot-checking.
