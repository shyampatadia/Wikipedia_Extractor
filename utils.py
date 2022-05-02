import requests
from bs4 import BeautifulSoup
import wikipediaapi
from tqdm import tqdm
import json

#constants
WIKIPEDIA_URL_EXTENSION = "https://en.wikipedia.org"

# initializing wikipediaapi class
wikipedia_api_class = wikipediaapi.Wikipedia(
    language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)


def generate_output_dictionary(element):
    """Generates a dictionary object containing a URL of the related article and its content

    Args:
        a HTML element containing from which we want to extract the URL

    Returns:
        _dictionary_: contains 2 keys named "url" and "content"
    """
    if element.has_attr('data-serp-pos') == True:
        ouput_dict = {}
        ouput_dict['url'] = WIKIPEDIA_URL_EXTENSION + element['href'] #extracting article URL
        ouput_dict['content'] = wikipedia_api_class.page(element['title']).text #using wikipedia_api library to extract the content from the article 
        return ouput_dict

def generate_final_list(page_url):
    """Send a Get request to the URL and get the reponse back and then extract the required information from the response.

    Args:
        page_url (_type_): _description_

    Returns:
        _type_: _description_
    """
    response = requests.get(url=page_url) #sending a get request
    soup = BeautifulSoup(response.content, 'html.parser') #Parsing the response received in the request that we made
    link_info = soup.find('div', {"id": "mw-content-text"}).find('ul',
                                                                class_="mw-search-results").find_all('a') #getting all the elements required to extract information and stroring them in a list
    list_final_output = list(tqdm(map(generate_output_dictionary, link_info))) #using generate_output_dictionary function to generate content and extract url
    return list_final_output


def generate_json(final_list, output_file_name): 
    """This fucntions will generate a json file given a certain input

    Args:
        final_list (list): a list object that we want to store it in json format
        output_file_name (string): name of the output file
    """
    if ".json" in output_file_name:
        with open(output_file_name, 'w') as f:
            json.dump(final_list, f) 
    else:
        with open(output_file_name+".json", 'w') as f:
            json.dump(final_list, f)  