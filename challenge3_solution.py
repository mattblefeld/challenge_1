import csv
import time


def jmeter_log_parser(file):
    """
    Purpose: To parse a jmeter log file and print out any unsuccessful responses.
            This method prints out the label, response code, response message, failure message,
            and the time of non-200 response in human-readable format in PST timezone
            (e.g. 2021-02-09 06:02:55 PST).
    :param file: this is the jmeter file you want to parse
    """

    with open(file, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            timestamp       = int(row['timeStamp'])
            label           = row['label']
            response_code   = row['responseCode']
            response_msg    = row['responseMessage']
            failure_msg     = row['failureMessage']

            if response_code != "200":
                x_time = time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime((timestamp/1000)))

                print(label + "," + response_code + "," + response_msg + "," + failure_msg + "," + x_time)


if __name__ == "__main__":
    jmeter_log_parser("Jmeter_log1.jtl")
    jmeter_log_parser("Jmeter_log2.jtl")

