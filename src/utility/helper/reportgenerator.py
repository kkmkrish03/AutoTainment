import pandas as pd

def write_to_csv(resultList, reportName, columnList, file_name_suffix):
    df = pd.DataFrame(resultList, columns=columnList)
    df.to_csv("output/{}_{}.csv".format(reportName, file_name_suffix))
    return "{}_{}.csv".format(reportName, file_name_suffix)

