s3multifile
By Steve Saporta
Apr 25 2014

Illustrates how to upload multiple files to Amazon S3 using:
- An HTML file input tag
- Python
- Flask
- Boto

To run this program, you'll need:
- Python 2.7 (Boto doesn't work with 3.3
- Flask (I used *pip install flask* to get the latest version)
- [Boto](https://github.com/boto/boto) (A Python interface to Amazon Web Services)
- An AWS account

You'll need an AWS bucket and AWS user with appropriate permissions.

1. In S3, create a bucket. We'll assume it's named *mybucket*.
2. Go to the bucket's properties and expand *Permissions*.
3. Add a new grantee, selecting *Authenticated Users* and checking the box for *Upload/Delete*.
4. In IAM, add a user. From the *Permissions* tab, attach a User Policy, similar to this one (your Sid will be different):
                                            
```javascript
"Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1396533377000",
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket",
        "s3:DeleteObject",
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:s3:::mybucket"
      ]
    }
  ]
}
```
From the *Security Credentials" tab, create an Access Key. Take note of the Access Key ID and Secret Access Key. Set the following environment variables:
- AWS_ACCESS_KEY_ID=[your Access Key ID]
- AWS_SECRET_ACCESS_KEY=[your Secret Access Key]

Now use Python 2.7 to launch test.py. In your web browser, visit http://localhost:8080. Select some files and click *Submit. The files should appear in your S3 bucket!