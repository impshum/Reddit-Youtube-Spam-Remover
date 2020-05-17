import praw
import configparser
import re
from collections import Counter


def main():
    config = configparser.ConfigParser()
    config.read('conf.ini')
    reddit_user = config['REDDIT']['reddit_user']
    reddit_pass = config['REDDIT']['reddit_pass']
    reddit_client_id = config['REDDIT']['reddit_client_id']
    reddit_client_secret = config['REDDIT']['reddit_client_secret']
    reddit_target_subreddit = config['SETTINGS']['reddit_target_subreddit']
    submission_user_max = int(config['SETTINGS']['submission_user_max'])
    test_mode = config['SETTINGS'].getboolean('test_mode')

    reddit = praw.Reddit(
        username=reddit_user,
        password=reddit_pass,
        client_id=reddit_client_id,
        client_secret=reddit_client_secret,
        user_agent='Reddit Youtube Spam Remover (by u/impshum)'
    )

    regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})')

    for submission in reddit.subreddit(reddit_target_subreddit).stream.submissions(skip_existing=True):
        user = submission.author.name
        title = submission.title
        youtube_count = 0
        spammer_score = 0
        titles = []

        try:
            for user_submission in reddit.redditor(user).submissions.new(limit=submission_user_max):
                title = user_submission.title

                if regex.match(user_submission.url):
                    youtube_count += 1
                    titles.append(title)

            if youtube_count:
                for k, v in Counter(titles).items():
                    if v >= 2:
                        spammer_score += v

            if spammer_score:
                if not test_mode:
                    submission.mod.remove()

                print(f'{user}: {youtube_count}/{submission_user_max} | {spammer_score}')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
