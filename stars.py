import sys
import os
import logging
import argparse
from github import Github
from dotenv import load_dotenv
from datetime import datetime

def setup_logging(log_file):
    # Ensure the logs directory exists
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Configure file logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=log_file,
        filemode='w'
    )

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Find stargazers of GitHub repositories")
    parser.add_argument('repositories', nargs='+', help='List of repositories to process')
    parser.add_argument('-o', '--output', help='Output file to write results')
    args = parser.parse_args()

    # Set up logging
    log_file = os.path.join('logs', f"stargazers_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    setup_logging(log_file)
    logger = logging.getLogger(__name__)

    # Load environment variables from .env file
    load_dotenv()

    # Get the GitHub token from the environment variable
    github_token = os.getenv('GITHUB_TOKEN')
    
    if not github_token:
        logger.error("GITHUB_TOKEN not found in .env file")
        sys.exit(1)

    g = Github(github_token, per_page=100)

    # Set to store unique usernames across all repositories
    all_unique_stargazers = set()

    # Iterate through each repository
    for repo in args.repositories:
        logger.info(f"Processing repository: {repo}")
        try:
            # Get the repository object
            repository = g.get_repo(repo)
            
            # Log the total number of stargazers for this repository
            total_stargazers = repository.stargazers_count
            logger.info(f"Total stargazers for {repo}: {total_stargazers}")
            
            # Set to store unique usernames for this repository
            repo_unique_stargazers = set()
            
            # Get stargazers and add their usernames to the sets
            stargazers = repository.get_stargazers()
            page_count = 0
            while True:
                page_count += 1
                page = stargazers.get_page(page_count - 1)
                if not page:
                    break
                new_stargazers = set(stargazer.login for stargazer in page)
                repo_unique_stargazers.update(new_stargazers)
                all_unique_stargazers.update(new_stargazers)
                logger.info(f"Downloaded page {page_count} of stargazers. Total unique stargazers across all repos: {len(all_unique_stargazers)}")
            
            logger.info(f"Finished processing {repo}. Unique stargazers for this repo: {len(repo_unique_stargazers)}")
            logger.info(f"Total stargazers: {total_stargazers}, Unique stargazers: {len(repo_unique_stargazers)}")
            logger.info(f"Total unique stargazers across all repos so far: {len(all_unique_stargazers)}")
        except Exception as e:
            logger.error(f"Error processing repository {repo}: {str(e)}")

    # Log final count of unique stargazers across all repositories
    logger.info(f"Total unique stargazers across all repositories: {len(all_unique_stargazers)}")

    # Write or print unique usernames
    if args.output:
        with open(args.output, 'w') as f:
            for username in all_unique_stargazers:
                f.write(f"{username}\n")
        logger.info(f"Results written to {args.output}")
    else:
        for username in all_unique_stargazers:
            print(username)

if __name__ == "__main__":
    main()

