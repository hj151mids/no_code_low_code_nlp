import boto3
from pathlib import Path
client = boto3.client("comprehend")
oms_text = Path('first_part_book.txt').read_text()
response = client.detect_sentiment(
    Text = oms_text,
    LanguageCode='en'
    )
print(response)

'''{'Sentiment': 'NEUTRAL', 'SentimentScore': {'Positive': 0.07813818007707596, 'Negative': 0.07705685496330261, 'Neutral': 0.5472100377082825, 'Mixed': 0.29759496450424194}, 'ResponseMetadata': {'RequestId': '935a0379-c87d-4fe7-9a46-6a8fc9191f8d', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '935a0379-c87d-4fe7-9a46-6a8fc9191f8d', 'content-type': 'application/x-amz-json-1.1', 'content-length': '161', 'date': 'Mon, 11 Oct 2021 06:16:36 GMT'}, 'RetryAttempts': 0}}'''
