from DataPreparation_3min.txt_to_csv import text_to_csv
from DataPreparation_3min.auto_markup import auto_markup
from DataPreparation_3min.to_txt import convert_to_txt
from DataPreparation_3min.hex_to_dec import hex_to_dec
import config as cf
import os
directory = "../prepared_data_3min"

def data_processing(raw_data: str, num_new=None, out_dir=directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

    print('Data processing started')
    # Function txt_to_csv returns '../converted_data/{0}CSV.csv'.format(num)
    csv = text_to_csv(raw_data, num_new)


    # Function auto_markup returns "../converted_data/markup_class{0}.csv".format(num)
    marked_up = auto_markup(csv)


    # Function convert_to_txt returns '../converted_data/full_prepared{0}.txt'.format(num)
    txt = convert_to_txt(marked_up)


    # Function hex_to_dec returns 'decimal{0}.csv'.format(num)
    hex_to_dec(txt, directory)
    print('Data processing ended')

# Merging to one
data_processing(raw_data=cf.raw_data_3min, num_new='2B', out_dir=directory)