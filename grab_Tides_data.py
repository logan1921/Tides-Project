# Python script - Logan Ashall
# Latest update : 10/24/2022
# Commands: 
# chmod +x script.py - to give permission
# python script.py - to run the scsript
# pip install module - install missing modules

from dateutil import rrule
from datetime import datetime, timedelta
import easygui
from easygui import *
import numpy as np
import pandas as pd
import pyproj as proj
import requests

#load up gui
text = "Please enter in StationID, Start Year and End Year for data download. StationID can be found in csv in folder (Point Atkinson StationID is given as reference)."
title = "DFO Station Download"
input_list = ["StationID","Start Date","End Date"]
default_list = ["5cebf1de3d0f4a073c4bb94c","2000","2022"]
output = easygui.multenterbox(text, title, input_list, default_list)
print (f'{output[0]}, {output[1]}, {output[2]}')

#provide stationID
stationID =output[0]


# retrieve all station metadata
response = requests.get(f'https://api-iwls.dfo-mpo.gc.ca/api/v1/stations')
dic = response.json()
ndf = pd.DataFrame(dic)
ndf.iloc[:,3] = ndf.iloc[:,3].astype(bool) 
result_df= ndf.loc[ndf['operating']==True]
result_df.to_csv('StationList_Operating.csv', index=False)
ndf.to_csv('StationList.csv', index=False)



#retrieve all metadata regarding the stationID
response = requests.get(f'https://api-iwls.dfo-mpo.gc.ca/api/v1/stations/{stationID}/metadata')
dic = response.json()
mdf = pd.json_normalize(dic)
mdf.to_csv('Station_metadata.csv', index=False)
timeseriesdf = mdf['timeSeries']
timeseriesdf = pd.json_normalize(timeseriesdf)
frames =[]
for column in timeseriesdf:
    timeseries_id_df = timeseriesdf[column]
    timeseries_id_df = pd.json_normalize(timeseries_id_df)
    frames.append(timeseries_id_df)
tdf = pd.concat(frames)
tdf.to_csv(f'{stationID}-timeseries_metadata.csv', index=False)

#retrieve all benchmark metadata regarding the stationID
response = requests.get(f'https://api-iwls.dfo-mpo.gc.ca/api/v1/benchmarks?stationId={stationID}')
print(f'https://api-iwls.dfo-mpo.gc.ca/api/v1/benchmarks/{stationID}')
dic = response.json()
bdf = pd.json_normalize(dic)
bdf.to_csv(f'{stationID}-benchmark_metadata.csv', index=False)

# download all water level observations from station ID
frames =[]
for year in range(int(output[1]),int(output[2])+1):
    for month in range(1,13):
        print(f'{year:04}-{month:02}')
        response = requests.get(f'https://api-iwls.dfo-mpo.gc.ca/api/v1/stations/{stationID}/data?time-series-code=wlo&from={year:04}-{month:02}-01T00%3A00%3A00Z&to={year:04}-{month:02}-01T12%3A00%3A00Z')
        response.raise_for_status()  # raises exception when not a 2xx response
        if (
            response.status_code != 204 and
            response.headers["content-type"].strip().startswith("application/json")
        ):
            try:
                dic = response.json()
            except ValueError:
                pass
        df = pd.DataFrame(dic)
        frames.append(df)
df = pd.concat(frames)
df.to_csv(f'{stationID}-{output[1]}-{output[2]}.csv', index=False) 


""" tdf= tdf.loc[tdf['code']=='wlo']
timeSeriesWLOID = (tdf['id'].iloc[:1]).to_string(index=False)
print(f'Now requesting Time Series ID: {timeSeriesWLOID}') """

