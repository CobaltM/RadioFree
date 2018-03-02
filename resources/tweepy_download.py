# To run this code, first edit config.py with your configuration, then:
#
# mkdir data
# python twitter_stream_download.py -q apple -d data
#
# It will produce the list of tweets for the query "apple"
# in the file data/stream_apple.json

import tweepy
from tweepy import OAuthHandler
import sys
import time
import argparse
import string
import config
import snowflake
import json
import datetime

def get_parser():
    currenttime = time.asctime()
    currenttime = currenttime[:20] + "+0000 " + currenttime[20:]
    """Get parser for command line arguments."""
    parser = argparse.ArgumentParser(description="Twitter Downloader")
    parser.add_argument("-q",
                        "--query",
                        dest="query",
                        help="Query/Filter",
                        default='-')
    parser.add_argument("-d",
                        "--data-dir",
                        dest="data_dir",
                        help="Output/Data Directory")
    parser.add_argument("-t1",
                        "--time-start-query",
                        dest="time_start_query",
                        help="Time Start Query",
                        default="Sat Jan 1 00:00:00 +0000 2000")
    parser.add_argument("-t2",
                        "--time-end-query",
                        dest="time_end_query",
                        help="Time End Query",
                        default=currenttime)
    return parser


def format_filename(fname):
    """Convert file name into a safe string.

    Arguments:
        fname -- the file name to convert
    Return:
        String -- converted file name
    """
    return ''.join(convert_valid(one_char) for one_char in fname)


def convert_valid(one_char):
    """Convert a character into '_' if invalid.

    Arguments:
        one_char -- the char to convert
    Return:
        Character -- converted char
    """
    valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
    if one_char in valid_chars:
        return one_char
    else:
        return '_'



def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)
@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_secret)
    api = tweepy.API(auth)

    starttime = snowflake.utc2snowflake(snowflake.str2utc(args.time_start_query))
    endtime = snowflake.utc2snowflake(snowflake.str2utc(args.time_end_query))

    name = args.query + "_" + args.time_start_query + "_" + args.time_end_query
    query_fname = format_filename(name)
    outFile=open("SERVERDIRECTORY/server/resources/data/"+query_fname+".json",'w')
    done=0;
    count=0;
    while (done == 0):
        for status in limit_handled(tweepy.Cursor(api.search, q=args.query,since_id=starttime,max_id=endtime).items(200)):
            try:
                json.dump(status._json,outFile)
                outFile.write('\n')
                count+=1
            except BaseException as e:
                print("Error on_data: %s" % str(e))
                time.sleep(5)
        latest = status.id
        if(endtime==latest):
            break
        endtime=latest
        sys.stdout.write("crawled %d tweets\n" % count)
        sys.stdout.flush()

