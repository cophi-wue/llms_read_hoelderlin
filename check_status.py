"""
reads the configuration file and outputs info, if value changed from UNCHANGED to CHANGED
"""

import configparser


def read_config():
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Read the configuration file
    config.read('config.ini')

    # Access values from the configuration file
    n00_intro = config.get('General', '00_intro')
    n01_metrics = config.get('General', '01_metrics')
    n02_rhyme = config.get('General', '02_rhyme')
    n03_assonances = config.get('General', '03_assonances')
    n04_lexis = config.get('General', '04_lexis')
    n05_phrases = config.get('General', '05_phrases')
    n06_syntax = config.get('General', '06_syntax')
    n07_metaphors = config.get('General', '07_metaphors')
    n08_titles = config.get('General', '08_titles')
    n09_textmeaning = config.get('General', '09_textmeaning')
    n10_style = config.get('General', '10_style')
    
    return config




if __name__ == "__main__":
    config = read_config()

    TODO = False

    for key in config['General']:
        if config['General'][key] != "UNCHANGED":
            print(f"{key}: {config['General'][key]}")
            TODO = True

    if TODO == False:
        print("Nothing to do.")
