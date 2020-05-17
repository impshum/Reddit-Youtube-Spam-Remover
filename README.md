## Reddit Youtube Spam Remover

Removes Youtube spam from a chosen subreddit.

### How Does It Work?

1. Streams submissions from subreddit
2. Checks N user submissions for youtube links
3. Counts duplicate titles over N submissions
4. If spam count is high the submission is removed

### Instructions

-   Install requirements `pip install -r requirements.txt`
-   Create Reddit (script) app at https://www.reddit.com/prefs/apps/ and get keys
-   Edit conf.ini with your details
-   Run it `python run.py`

### General Info

- Bot account needs to be admin of the subreddit
- Written in about 15 minutes on a Sunday
- Not tested to a great degree at all

#### Settings Info

-   `reddit_target_subreddit` - Subreddit to remove spam
-   `submission_user_max` - Max user submissions to check for youtube spam
-   `test_mode` - Runs the bot without any actions

#### Tip

BTC - 1AYSiE7mhR9XshtS4mU2rRoAGxN8wSo4tK
