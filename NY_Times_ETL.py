from pynytimes import NYTAPI
import pandas as pd
import s3fs


def my_function():

    # API KEY
    API_KEY = "100yeFqevmiZAZtjvx3IsIuiaGJqqiWi"

    # secert: TqclkUVoOWL0iXeS

    # creating an instance of the class (object)
    nyt = NYTAPI(API_KEY, parse_dates=True)

    # Get all the top stories from a sports category
    top_sports_stories = nyt.top_stories(section="sports")

    extracted_data = []

    # list compherension to extract required information
    extracted_data = [
        {
            "abstract": story.get("abstract", ""),
            "created_date": pd.to_datetime(story.get("created_date", "")).date(),
            "title": story.get("title", ""),
            "url": story.get("url", ""),
        }
        for story in top_sports_stories
    ]

    # convert to dataframe
    df = pd.DataFrame(extracted_data)
    df.to_csv("s3://data-engineering-datasets/AIRFLOW_DATASETS/Sport_Stories.csv")
