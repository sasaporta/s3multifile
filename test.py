import boto
from boto.s3.key import Key

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    # If user has submitted the form...
    if request.method == 'POST':

        # Connect to Amazon S3
        s3 = boto.connect_s3()

        # Get a handle to the S3 bucket
        bucket_name = 'mybucket'
        bucket = s3.get_bucket(bucket_name)
        k = Key(bucket)

        # Loop over the list of files from the HTML input control
        data_files = request.files.getlist('file[]')
        for data_file in data_files:

            # Read the contents of the file
            file_contents = data_file.read()

            # Use Boto to upload the file to the S3 bucket
            k.key = data_file.filename
            print "Uploading some data to " + bucket_name + " with key: " + k.key
            k.set_contents_from_string(file_contents)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int('8080'),
        debug=True
    )
