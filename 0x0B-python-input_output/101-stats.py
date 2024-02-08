#!/usr/bin/python3
"""Module comment"""
import sys


def get_stdin_data():
    """Entry point, this function reads a std in"""
    inputs = []
    i = 0
    try:
        for line in sys.stdin:
            i += 1
            inputs.append(line.split())
            if i == 10 or line is None:
                print_metrics(compute_metrics(inputs))
                i = 0
        else:
            if i != 0:
                print_metrics(compute_metrics(inputs))
            elif i == 0 and not inputs:
                print("File size: 0")

    except KeyboardInterrupt:
        print_metrics(compute_metrics(inputs))
        raise


def compute_metrics(list_of_inputs):
    """This function is called to compute values read from stdin"""
    metrics = {}
    for line in list_of_inputs:
        if len(line) < 7:
            continue
        metrics['file_size'] = metrics.get('file_size', 0) + int(line[-1])
        metrics[line[-2]] = metrics.get(line[-2], 0) + 1
    return metrics


def print_metrics(metrics):
    valid_keys = ['200', '301', '400', '401', '403', '404', '405', '500']
    """This function prints metrics to stdout"""
    if metrics.get('file_size'):
        print("{:s}: {:d}".format('File size', metrics.pop('file_size')))
        for key in sorted(metrics.keys()):
            if key in valid_keys:
                print("{:s}: {:d}".format(key, metrics.get(key)))


get_stdin_data()
