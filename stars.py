import sys
import os
import logging
from github import Github
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Get the GitHub token from the environment variable
    github_token = os.getenv('GITHUB_TOKEN')
    
    if not github_token:
        logger.error("GITHUB_TOKEN not found in .env file")
        sys.exit(1)

    g = Github(github_token, per_page=1000)

    # Get the list of repositories from command-line arguments
    repositories = sys.argv[1:]

    if not repositories:
        logger.warning("No repositories provided. Usage: python stars.py repo1 repo2 ...")
        sys.exit(1)

    # Set to store unique usernames
    unique_stargazers = set()

    # Iterate through each repository
    for repo in repositories:
        logger.info(f"Processing repository: {repo}")
        try:
            # Get the repository object
            repository = g.get_repo(repo)
            
            # Get stargazers and add their usernames to the set
            stargazers = repository.get_stargazers()
            for stargazer in stargazers:
                if stargazer.login not in unique_stargazers:
                    unique_stargazers.add(stargazer.login)
                    logger.info(f"Added new stargazer: {stargazer.login}")
                else:
                    logger.debug(f"Skipped duplicate stargazer: {stargazer.login}")
            
            logger.info(f"Found {len(unique_stargazers)} unique stargazers so far")
        except Exception as e:
            logger.error(f"Error processing repository {repo}: {str(e)}")

    # Print unique usernames
    logger.info(f"Total unique stargazers: {len(unique_stargazers)}")
    for username in unique_stargazers:
        print(username)

if __name__ == "__main__":
    main()

