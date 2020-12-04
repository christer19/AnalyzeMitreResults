#!/usr/bin/env python
__author__ = "J. Carter Briggs"
__version__ = "1.0"

import InitializeMitre
import pandas as pd
import matplotlib.pyplot as plt

#    //TODO
#    - Functions to compare counts of Detections and misses by Company overall and by step
#    - Calculate mean and median for blocks and misses and be able to slice by category
#    - Bar chart of blocks and misses by company with ability to slice by category
#    - CLI
#    - GUI
#    - Debug switch
#    - refactor classes and methods
#    - Summary by company
#    - Summary by technique
#    - Exception handling
#    - Venv
#    - battle card comparisons
#    - Combine multiple APTs
#    - create separate git repository with readme, license
#    - compile as application

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    InitializeMitre.downloadFiles()
    InitializeMitre.createDictionary()
    df = InitializeMitre.createDataFrame()

    #Count missed Detections
    missed_detections_table = df[(df['MainDetectionType'] == "None")]
    missed_detections_by_company = missed_detections_table.groupby('Company')['MainDetectionType'].count()
    missed_detections_by_company = missed_detections_by_company.sort_values()
    #print(missed_detections_by_company)

    #count detections of all other types by company
    detections_table = df[(df['MainDetectionType'] != "None")]
    detections_by_company = detections_table.groupby('Company')['MainDetectionType'].count()
    detections_by_company = detections_by_company.sort_values()
    print(detections_by_company)
    plt.figure()
    detections_by_company.plot.bar()
    #plt.legend(loc='best')
    plt.show()


