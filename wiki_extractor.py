import argparse
import sys

from utils import *

# initializing the arg_parser which will take the input from the command line
parser = argparse.ArgumentParser()
parser.add_argument("--keyword", type=str,
                    help="Enter the Keyword you want to search on Wikipedia")
parser.add_argument("--num_urls", type=int,
                    help="Enter the number of urls that you want to scrape")
parser.add_argument("--output", type=str,
                    help="Please input the filename in which you want the output to be in, it should be json!")
args = parser.parse_args()

# formatting input data according to api call format
args.keyword = str(args.keyword).replace(" ", "+")

#constants
WIKIPEDIA_API = "https://en.wikipedia.org/w/index.php?title=Special:Search&limit={0}&offset={1}&profile=default&search={2}&ns0=1"
OFF_SET = 0


if (args.num_urls > 10000):
    sys.exit("An error has occurred while searching: Could not retrieve results. Up to 10000 search results are supported, but results starting at 10000 were requested.")
elif (args.num_urls <= 5000):
    page_url = WIKIPEDIA_API.format(args.num_urls, OFF_SET, args.keyword)
    listOfContent = generate_final_list(page_url)
    generate_json(listOfContent, args.output)
else:
    page_url = WIKIPEDIA_API.format(args.num_urls, OFF_SET, args.keyword)
    listPart1 = generate_final_list(page_url)
    OFF_SET = 5000
    rmaining_number_of_urls = args.num_urls - OFF_SET
    page_url_offset_changed = WIKIPEDIA_API.format(rmaining_number_of_urls, OFF_SET, args.keyword)
    listPart2 = generate_final_list(page_url_offset_changed)
    finalList = listPart1 + listPart2 #concatenating both the list
    generate_json(finalList, args.output)
