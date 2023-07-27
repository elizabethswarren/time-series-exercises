import pandas as pd
from datetime import timedelta, datetime
import numpy as np

import matplotlib.pyplot as plt

def prep_sales_data(df):
    '''This function takes in the sale_item df from TSA Item Demand db.
        1. Changes the sale_date column to datetime type.
        
        2.  Sets the index to the sale_date column.
        
        3. Creates a new column titled 'month'.
            a. The month as January = 1, December = 12.
            
        4. Creates a new column titled 'day_of_week
            a. The day as Monday = 0, Sunday = 6.
        
        5. Creates a new column 'sales_total'.
            a. Product of sale_amount and item_price.
             
        6. Plots the distribution of sale_amount and item_price.'''
    
    # 1
    df.sale_date = df.sale_date.astype('datetime64')

    #2
    df = df.set_index('sale_date')

    #3
    df['month'] = df.index.month

    #4
    df['day_of_week'] = df.index.day_of_week

    #5
    df['sales_total'] = df.sale_amount * df.item_price

    #6
    cols = ['sale_amount', 'item_price']

    for col in cols:
        df[col].hist()
        plt.title([col])
        plt.show()

    return df