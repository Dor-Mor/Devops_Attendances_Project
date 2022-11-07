#!/usr/bin/env python3
import os
import glob
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


def fix_csv():
    # creating an empty DF
    all_meetings = pd.DataFrame()
    counter = 0
    num_of_classes = 0
    # if file exists, remove it and creating a new one
    if os.path.exists(os.getenv('LOCAL_ALL_MEETINGS')):
        os.remove(os.getenv('LOCAL_ALL_MEETINGS'))
    # running on all CSV file in dir
    for f in glob.glob(os.getenv('LOCAL_PATH')+'/*csv'):

        num_of_classes += 1
        name = counter

        counter += 1
        # read+encode the csv file
        df = pd.read_csv(f, encoding='utf-16', sep='\t')
        # mins to int
        df[name] = df['Attendance Duration'].apply(lambda time: int(time.split()[0]))
        df = df.groupby('Name')[name].sum()
        # adding to the empty DF
        if all_meetings.empty:
            all_meetings = df.copy()
        else:
            all_meetings = pd.merge(left=all_meetings, right=df, on='Name', how='outer')
    # table cosmetics
    all_meetings = pd.DataFrame(all_meetings.sum(axis=1))
    all_meetings.rename(columns={0: 'mins'}, inplace=True)
    all_meetings = all_meetings.sort_values(by='mins', ascending=False)
    # mins calculations
    all_meetings['percentage'] = (all_meetings['mins'] / (num_of_classes * 240))
    all_meetings['percentage'] = all_meetings['percentage'].map(lambda n: '{:,.2%}'.format(n))
    all_meetings.sort_values(by='mins', ascending=False, inplace=True)

    # saving new file
    all_meetings.to_csv(os.getenv('LOCAL_ALL_MEETINGS'))




