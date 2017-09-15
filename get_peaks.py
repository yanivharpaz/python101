from bs4 import BeautifulSoup as bs
import bs4
import sys
import requests
import json
import traceback
from pprint import pprint as pp

# settings
urls = {
    "peaks_main_url": "https://www.peakware.com/peaks.php",
    "continent_url": "https://www.peakware.com/peaks.php?choice=",
    "peak_url": "https://www.peakware.com/peaks.php?pk=",
}

CONTINENT_PEAKS_SUFFIX_FOR_SORT_BY_NAME = "A"
SAMPLE_DATA = True
# SAMPLE_DATA = False


class PeakProperties(object):
    """
    Class for all the peak info properties
    """
    def __init__(self):
        self.properties_set = set()

    def add_property(self, property_name):
        self.properties_set.add(property_name)

    def get_properties_list(self):
        return list(self.properties_set)


def get_continents():
    continents = dict()
    url = urls["peaks_main_url"]
    response = requests.get(url)

    # parse the unordered list (UL) from the HTML
    soup = bs(response.text, "html.parser")
    ul_list = soup.find("ul", {"id": "contList"})

    # loop through the list items (LI)
    for list_item in ul_list:
        if isinstance(list_item, bs4.element.Tag):
            # Get the continent name
            continent_name = list_item.text[:list_item.text.index('(')].strip()

            continent_url = str(list_item.find("a"))
            continent_code_index = continent_url.index(">by Name</a>") - 4
            # Get the continent code
            continent_code = continent_url[continent_code_index: continent_code_index + 2]
            # Save new data to the continents dictionary
            continents[continent_name] = continent_code
    return continents


def analyze_continent_peaks():
    pass


def get_peaks_list(continents):
    peaks = dict()
    for continent_name, continent_code in continents.items():
        url = urls["continent_url"] + continent_code + CONTINENT_PEAKS_SUFFIX_FOR_SORT_BY_NAME
        response = requests.get(url)

        # parse the unordered list (UL) from the HTML
        soup = bs(response.text, "html.parser")
        ul_list = soup.find("ul", {"id": "peakList"})

        # loop through the list items (LI)
        for list_item in ul_list:

            if isinstance(list_item, bs4.element.Tag):
                # break the line into data items
                row_items = str(list_item).split('>')

                peak_id = row_items[1][row_items[1].index("pk=") + 3: -1]
                peak_name = row_items[2][:-3]
                peak_heights = row_items[4][:-4]

                # save the data into the peaks_list dictionary
                peaks[peak_id] = {
                    'name': peak_name,
                    'heights': peak_heights,
                }

    return peaks


def get_peak_info_by_id(peak_id, peak_properties):
    peak_info = dict()

    url = urls["peak_url"] + peak_id
    response = requests.get(url)

    # parse the unordered list (UL) from the HTML
    soup = bs(response.text, "html.parser")

    overview_div = soup.find("div", {"id": "overview"})
    headers = overview_div.findAll("th")
    values = overview_div.findAll("td")

    for header, value in zip(headers, values):
        peak_info[header.text[:-1]] = value.text
        peak_properties.add_property(header.text[:-1])

    return peak_info


def main():
    peak_properties = PeakProperties()
    print("Starting web scraping of www.peakware.com ")
    print("Getting initial continents list.")

    # work on Antarctica for the development phase (SAMPLE_DATA is True)
    continents = {"Antarctica": "An"} if SAMPLE_DATA else get_continents()

    # print(json.dumps(continents, indent=4))
    print("Initial continents list retrieval complete.")
    # print("Amount of continents found:", len(continents))

    print("Getting peaks list.")
    peaks_list = get_peaks_list(continents)
    # print(json.dumps(peaks_list, indent=4))

    peaks_counter = 0
    for peak_id in peaks_list:
        peaks_counter += 1
        peak_info = get_peak_info_by_id(peak_id, peak_properties)
        print json.dumps(peak_info, indent=4)
        if peaks_counter > 2:
            break

    properties_list = peak_properties.get_properties_list()
    print(properties_list)
    # print("Amount of peaks found:", len(peaks))
    print("Web scraping of www.peakware.com is complete.")


if __name__ == "__main__":
    main()
