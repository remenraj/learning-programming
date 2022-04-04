# Internet speed twitter complaint bot
# Tweets at the internet service provider when the internet speed dips below the promised speed

from internet_speed_twitter_bot import InternetSpeedTwitterBot


def main():
    """Main function"""
    
    # promised speed
    PROMISED_DOWN = 150
    PROMISED_UP = 100
    
    # creating the object and initializing the driver/browser
    bot = InternetSpeedTwitterBot()
    
    # getting the internet speed
    bot.get_internet_speed()
    
    # tweet if the internet speed is below the promised speed
    if float(bot.down) < PROMISED_DOWN or float(bot.up) < PROMISED_UP:
        print("Internet speed is low")
        bot.tweet_at_provider()

    
if __name__ == "__main__":
    main()