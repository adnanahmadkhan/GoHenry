1) XML to CSV processor

In Python and only using Python's standard library, create a program to convert the XML file `accountbalance20210101.xml` into a CSV.

Account balances for user's are being sent by a third party finacial via the XML file. A row for a user begins with a `<ACCOUNT>` tag and ends with a `<ACCOUNT>`.

The file is expected to eventually have millions of rows and given the nature of XML it will not be possible to load the entire file in memory. In the processor, create a way of iterating over the file without loading it all into memory.

2) Python API Client

There are three JSON files in this directory which contain response data from an API:
- `campaign_statistics.json`
- `campaigns.json`
- `creatives.json`

Build a Python client to call the different endpoints for this API.
The client must be able to:
- Authenticate using an API key
- Paginate

To test the client there is a Flask app in `app.py`.
To run the Flask app do the following:
```
pip install -r requirements.txt
```

``
flask run
``# GoHenry
