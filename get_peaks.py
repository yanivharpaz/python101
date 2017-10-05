from __future__ import print_function
from bs4 import BeautifulSoup as bs
import bs4
import json
import csv
import sys
import datetime
import requests
from multiprocessing.dummy import Pool as ThreadPool
# from multiprocessing import Pool as ThreadPool


reload(sys)
sys.setdefaultencoding('utf8')

import pandas as pd
import traceback

# settings
URLS = {
    "peaks_main_url": "https://www.peakware.com/peaks.php",
    "continent_url": "https://www.peakware.com/peaks.php?choice=",
    "peak_url": "https://www.peakware.com/peaks.php?pk=",
}

NUMERIC_PROPERTIES_LIST = [
                            "Year first climbed",
                            "Elevation (meters)",
                            "Elevation (feet)",
                            "Latitude",
                            "Longitude",
                            ]

CONTINENT_PEAKS_SUFFIX_FOR_SORT_BY_NAME = "A"
PARALLEL_FACTOR = 10
# SAMPLE_DATA = True
SAMPLE_DATA = False


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


class RunningTimer(object):
    # Class for basic timer management
    def __init__(self, remove_micro_seconds=False):
        self.end_timer = None
        if remove_micro_seconds:
            self.timer = datetime.datetime.now().replace(microsecond=0)
            self.remove_micro_seconds = remove_micro_seconds
        else:
            self.timer = datetime.datetime.now()
            self.remove_micro_seconds = remove_micro_seconds

    def restart(self, remove_micro_seconds=False):
        if remove_micro_seconds:
            self.timer = datetime.datetime.now().replace(microsecond=0)
        else:
            self.timer = datetime.datetime.now()

    def stop(self):
        if self.remove_micro_seconds:
            self.end_timer = datetime.datetime.now().replace(microsecond=0)
        else:
            self.end_timer = datetime.datetime.now()

    def display(self):
        if self.end_timer is None:
            return "The timer did not stop"
        result = str(self.end_timer - self.timer)
        return result


def get_numeric_value(raw_value):
    if isinstance(raw_value, str):
        try:    # string - remove "," first
            result = float(raw_value.replace(",", "").strip())
        except:
            result = None
    else:       # not a string, convert to float only
        try:
            result = float(raw_value)
        except:
            result = None
    return result


def get_continents():
    continents = dict()
    url = URLS["peaks_main_url"]
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


def get_peaks_list(continents):
    peaks = dict()
    for continent_name, continent_code in continents.items():
        url = URLS["continent_url"] + continent_code + CONTINENT_PEAKS_SUFFIX_FOR_SORT_BY_NAME
        response = requests.get(url)

        # parse the unordered list (UL) from the HTML
        soup = bs(response.text, "html.parser")
        ul_list = soup.find("ul", {"id": "peakList"})

        # loop through the list items (LI)
        print("Processing peaks list of {}, so far got {} peaks.".format(continent_name, str(len(peaks))))
        for list_item in ul_list:

            if isinstance(list_item, bs4.element.Tag):
                # break the line into data items
                row_items = str(list_item).split('>')

                peak_id = row_items[1][row_items[1].index("pk=") + 3: -1]
                peak_name = row_items[2][:-3]
                peak_heights = row_items[4][:-4]

                # save the data into the peaks_list dictionary
                peaks[peak_id] = {
                    'Name': peak_name,
                    'Continent': continent_name,
                    'Heights': peak_heights,
                }

    return peaks


def peak_response_to_dictionary(response, peak_properties):
    peak_info = dict()

    # parse the unordered list (UL) from the HTML
    soup = bs(response.text, "html.parser")

    overview_div = soup.find("div", {"id": "overview"})
    headers = overview_div.findAll("th")
    values = overview_div.findAll("td")

    for header, value in zip(headers, values):
        peak_info[header.text[:-1]] = value.text
        peak_properties.add_property(header.text[:-1])

    return peak_info


def build_peak_raw_data(peak_id, peak_info, peaks_list):
    peak_raw_data = {'Id': peak_id,
                     'Name': peaks_list[peak_id]['Name'],
                     'Continent': peaks_list[peak_id]['Continent'],
                     'Heights': peaks_list[peak_id]['Heights'],
                     }
    for key, value in peak_info.items():
        peak_raw_data[key] = value
    return peak_raw_data


def get_peaks_response_list(peaks_url_list):
    pool = ThreadPool(PARALLEL_FACTOR)
    result_response_list = pool.map(requests.get, peaks_url_list)
    return result_response_list


def get_peaks_info(peak_properties, peaks_list):
    peaks_counter = 0
    peaks_info_raw = dict()

    website_timer = RunningTimer()
    # build a URL list and process it
    peaks_url_list = [URLS["peak_url"] + peak_id for peak_id in peaks_list]     # list comprehension for URLs
    response_list = get_peaks_response_list(peaks_url_list)                     # launch a parallel process for requests
    # print stats: how many and how long
    print("response_list", len(response_list))
    website_timer.stop()
    print("Time for website parallel access:", website_timer.display())

    # process the HTML response list into a dict
    for response in response_list:
        peaks_counter += 1
        peak_info = peak_response_to_dictionary(response, peak_properties)
        peak_id = response.url[response.url.index("pk=") + 3:]
        peak_raw_data = build_peak_raw_data(peak_id, peak_info, peaks_list)

        peaks_info_raw[peak_id] = peak_raw_data
    return peaks_info_raw


def complete_peaks_info(peaks_info_raw, properties_list):
    result_peaks_info = dict()
    for peak_id in peaks_info_raw:
        # generate keys for all the data items found
        new_peak_dict = {property_name: None for property_name in properties_list}

        for key, value in peaks_info_raw[peak_id].items():
            # in Country use only the first country if more than one found
            if key == "Country":
                new_value = value.split("/")[0]
            else:
                # convert numbers to float or encode strings to UTF-8
                new_value = get_numeric_value(value) if key in NUMERIC_PROPERTIES_LIST else value.lower().encode("utf-8")
            new_peak_dict[key] = new_value

        # fill data with the heights info
        elevation_m = new_peak_dict["Elevation (meters)"]
        elevation_ft = new_peak_dict["Elevation (feet)"]

        # heights field on (from the peaks list) contains feet and meters separated by /
        heights = new_peak_dict["Heights"].split("/")

        # fill the meters info from the height
        if elevation_m is None and heights is not None:
            for height in heights:
                if height.endswith("m"):
                    elevation_m = float(height.strip().replace(" ", "").replace("m", ""))

        # fill the feet info from the height
        if elevation_ft is None and heights is not None:
            for height in heights:
                if height.endswith("ft"):
                    elevation_ft = float(height.strip().replace(" ", "").replace("ft", ""))

        # if count not find height info in either meters or feet, skip saving the peak in my dictionary
        if elevation_m is None and elevation_ft is None:
            continue

        # fill meters and feet info if one is missing
        if elevation_m is None:
            elevation_m = get_numeric_value(elevation_ft) / 3.28

        if elevation_ft is None:
            elevation_ft = get_numeric_value(elevation_m) * 3.28

        # save it back, fixed
        new_peak_dict["Elevation (meters)"] = elevation_m
        new_peak_dict["Elevation (feet)"] = elevation_ft

        # save the peak info in the result dictionary
        result_peaks_info[peak_id] = new_peak_dict

    return result_peaks_info


def get_headers(dict_to_examine):
    headers = list()
    for outer_key in dict_to_examine:
        headers = dict_to_examine[outer_key].keys()
        break

    return headers


def write_dict_to_csv(csv_file, csv_columns, dict_data):
    try:
        with open(csv_file, 'wb') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError as (errno, strerror):
            print("I/O error({0}): {1}".format(errno, strerror))
    return


def main():
    my_timer = RunningTimer()
    # load applications properties
    peak_properties = PeakProperties()
    print("Starting web scraping of www.peakware.com ")
    print("Getting initial continents list.")

    # work on Antarctica for the development phase (SAMPLE_DATA is True)
    # continents = {"Antarctica": "An", "South America": "So"} if SAMPLE_DATA else get_continents()
    # continents = {"Asia": "As", "North America": "No"} if SAMPLE_DATA else get_continents()
    continents = {"North America": "No"} if SAMPLE_DATA else get_continents()
    # continents = {"Asia": "As"} if SAMPLE_DATA else get_continents()
    # continents = {"Antarctica": "An"} if SAMPLE_DATA else get_continents()

    print("Initial continents list retrieval complete.")
    print("Getting peaks list.")
    peaks_list = get_peaks_list(continents)

    # Get and process peaks info
    print("Got {} peaks to process info".format(str(len(peaks_list))))
    peaks_info_raw = get_peaks_info(peak_properties, peaks_list)            # get a basic dict for peaks info
    properties_list = peak_properties.get_properties_list()                 # manage a set for all the properties
    peaks_info = complete_peaks_info(peaks_info_raw, properties_list)       # complete the peaks info

    # write the data into a json file (more accurate for knowing what we got from the website)
    with open('peaks_info.json', 'wb') as outfile:
        json.dump(peaks_info, outfile, indent=4)

    # write the data to the result CSV file
    headers = get_headers(peaks_info)
    write_dict_to_csv("peaks.csv", headers, peaks_info.values())

    print("")
    my_timer.stop()
    print(my_timer.display())
    print("Web scraping of www.peakware.com is complete.")


if __name__ == "__main__":
    main()
