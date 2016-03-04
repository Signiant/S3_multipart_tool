# S3 Multipart Tool
Provides quick access to list/remove unseen multipart objects, contained within a S3 bucket

## Installation

Install prerequisites

* sudo pip install --upgrade pip
* sudo pip install -U boto3


Create credentials file for S3
The default location for the credentials file is:

* ~/.aws/credentials (Linux/Mac)
* %USERPROFILE%\\.aws\\credentials  (Windows)

The basic format of the credentials file is:
[default]
aws\_access\_key\_id = ACCESS\_KEY
aws\_secret\_access\_key = SECRET\_KEY


## Usage
```
list buckets: python ./aws_multipart_tool.py --list-buckets

list parts: python ./aws_multipart_tool.py --list --bucket <bucket-names>

delete parts: python ./aws_multipart_tool.py --delete --bucket <bucket-names>
```
