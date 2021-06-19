import requests
import configparser
import pandas as pd


def main():
    search_tag, url = get_search_url()

    response = requests.get(url, headers=get_request_headers())

    if response.status_code != 200:
        print("Call to instagram unsuccessful, response status =", response.status_code)
        exit()

    if response.headers.get("content-type") != "application/json; charset=utf-8":
        print("Invalid response type, received type =", response.headers.get("content-type"))
        exit()

    print_response(response, search_tag)


def get_search_url():
    """
    Reads user input from console and returns search url and search_tag
    """
    base_url = 'https://www.instagram.com/web/search/topsearch/?context=blended&query=%23'
    search_tag = str(input('Enter the hashtag you would like to search: '))
    if '#' in search_tag:
        search_tag = search_tag.strip('#')
    url = base_url + search_tag
    return search_tag, url


def get_request_headers():
    """
    Create request headers from application.properties
    """
    config = configparser.ConfigParser()
    config.read('../configuration/application.properties')
    request_headers = {
        "Accept": config.get("instagram-request-headers", "accept"),
        "Cookie": config.get("instagram-request-headers", "cookie"),
        "User-Agent": config.get("instagram-request-headers", "user-agent")}
    return request_headers


def print_response(response, search_tag):
    """
    Writes output to CSV
    """
    hashtag_list = response.json()['hashtags']
    hashtag_name = []
    hashtag_count = []
    for row_data in hashtag_list:
        hashtag_name.append(row_data['hashtag']['name'])
        hashtag_count.append(row_data['hashtag']['media_count'])
    df = pd.DataFrame({'hashtag': hashtag_name, 'count': hashtag_count})
    df.to_csv('../output/' + search_tag + '_list.csv')


main()
