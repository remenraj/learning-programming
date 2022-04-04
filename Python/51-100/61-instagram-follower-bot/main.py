# Instagram follower bot using selenium

from instagram_follower_bot import InstagramFollowerBot
import os


def main() -> None:
    """Main function"""

    # get the username and password from the environment variables
    INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
    INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

    # account username whose followers you want to follow
    similar_account_username = "indian_wild_dog"

    # create an instance of the InstagramFollowerBot class
    bot = InstagramFollowerBot(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)

    # logging into instagram
    bot.login()
    
    # find the followers of the target username
    bot.find_followers(target_username=similar_account_username)
    
    # follow the followers
    bot.follow()


if __name__ == "__main__":
    main()
