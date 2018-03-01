import time
import argparse

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


if __name__ == '__main__':
    parser = get_parser()

    args = parser.parse_args()
    print(args.query)