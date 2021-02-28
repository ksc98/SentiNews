import httplib2
import sys
import os
import logging
from googleapiclient import discovery
from googleapiclient.errors import HttpError
from pprint import pprint


logger = logging.getLogger()

NLP_KEY = os.getenv('GCP_NLP_API_KEY')

if not NLP_KEY:
    logging.debug("No API key found. Export to GCP_NLP_API_KEY")
    return {}


def gcp_nlp(content):
    discovery_url = 'https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'
    service = discovery.build(
        'language', 'v1',
        http=httplib2.Http(),
        discoveryServiceUrl=discovery_url,
        developerKey=NLP_KEY,
        cache_discovery=False,
    )
    service_request = service.documents().annotateText(
        body={
            'document': {
                'type': 'PLAIN_TEXT',
                'content': content,
            },
            'features': {
                'extract_syntax': True,
                'extractEntities': True,
                'extractDocumentSentiment': True,
            },
            'encodingType': 'UTF16' if sys.maxunicode == 65535 else 'UTF32',
        })
    try:
        response = service_request.execute()
    except HttpError as e:
        response = {'error': e}
    return response
