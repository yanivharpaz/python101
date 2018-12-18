import csv
import sys
import json


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


def complete_peaks_info(orig_peaks_info):
    result_peaks_info = dict()
    for peak_id in orig_peaks_info:
        new_peak_dict = dict()
        for key, value in orig_peaks_info[peak_id].items():
            # in Country use only the first country if more than one found
            if key == "Country":
                new_value = value.split("/")[0]
            else:
                new_value = value
            new_peak_dict[key] = new_value

        # fill data with the heights info
        elevation_m = orig_peaks_info[peak_id]["Elevation (meters)"]
        elevation_ft = orig_peaks_info[peak_id]["Elevation (feet)"]

        # heights field on (from the peaks list) contains feet and meters separated by /
        heights = orig_peaks_info[peak_id]["Heights"].split("/")

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
            elevation_m = elevation_ft / 3.28

        if elevation_ft is None:
            elevation_ft = elevation_m * 3.28

        # save the peak info in the result dictionary
        result_peaks_info[peak_id] = new_peak_dict

    return result_peaks_info


def main():
    # take care of the encoding issues
    reload(sys)
    sys.setdefaultencoding('utf8')

    # file name of full data to load from
    full_peaks_file_name = "peaks_info_full.json"

    print("Loading peak info from {}".format(full_peaks_file_name))
    with open(full_peaks_file_name, "r") as in_file:
        orig_peaks_info = json.load(in_file)

    peaks_info = complete_peaks_info(orig_peaks_info)
    headers = get_headers(peaks_info)
    write_dict_to_csv("peaks_all.csv", headers, peaks_info.values())

    # print(len(peaks_info))
    print("Execution complete.")


if __name__ == "__main__":
    main()
