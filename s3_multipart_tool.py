import argparse
import boto3
import sys

s3 = boto3.resource('s3')


hdd_units =["bytes", "KB", "MB", "GB", "TB", "PB"]


def convertDiskSizeToSI( bytes ):
    index = 0
    while bytes >= 1024:
        bytes /= 1024
        index += 1

    return str(bytes) + " " + hdd_units[index]


def output( string ):
    print(string)


def list_buckets():
    try:
        count = 1
        for bucket in s3.buckets.all():
            print(str(count) + ") " + bucket.name)
            count += 1
    except Exception as e:
        print(e)


def list_multiparts(bucket_names):
    try:
        for name in bucket_names:
            bucket = s3.Bucket(name)
            bucket_size = 0
            part_count = 0

            for upload in bucket.multipart_uploads.all():
                multipart_size = 0

                for part in upload.parts.all():
                    output("   " + str(part.last_modified) + " -- " + convertDiskSizeToSI(part.size) + " -- " + upload.key + " -- " + part.e_tag)
                    multipart_size += part.size
                    part_count += 1

                bucket_size += multipart_size

            output(bucket.name + " -- " + str(part_count) + " parts -- " + convertDiskSizeToSI(bucket_size))
    except Exception as e:
        print(e)


def delete_multiparts(bucket_names):
    try:
        for name in bucket_names:
            bucket = s3.Bucket(name)

            for upload in bucket.multipart_uploads.all():
                print("  Deleting " + upload.key)
                upload.abort()
    except Exception as e:
        print(e)


def addArguments():
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('-b', '--bucket', dest='buckets', action='store', nargs='+', help='Specify S3 bucket(s) to use')
    parser.add_argument('-d', '--delete', dest='delete', action='store_true', help='Delete the multiparts in the specified bucket(s)')
    parser.add_argument('-l', '--list', dest='list', action='store_true', help='List the multiparts in the specified bucket(s)')
    parser.add_argument('--list-buckets', dest='list_buckets', action='store_true', help='List all the buckets in the account')
    
    return parser.parse_args()


if __name__ == "__main__":
    args = addArguments()

    if args.list_buckets:
        list_buckets()

    if args.delete:
        delete_multiparts(args.buckets)

    if args.list:
        list_multiparts(args.buckets)
