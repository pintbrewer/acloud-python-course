new_bucket = s3.create_bucket(Bucket='guru-ahalfnother-4243', CreateBucketConfiguration={'LocationConstraint': session.region_name})

new_bucket = s3.create_bucket(Bucket='guru-ahalfnother-2222')

new_bucket.upload_file('index.html', 'index.html', ExtraArgs={'ContentType': 'text/html'})

policy = """
    ...: {
    ...:   "Version":"2012-10-17",
    ...:   "Statement":[{
    ...:       "Sid":"PublicReadGetObject",
    ...:       "Effect":"Allow",
    ...:       "Principal": "*",
    ...:       "Action":["s3:GetObject"],
    ...:       "Resource":["arn:aws:s3:::%s/*"
    ...:       ]
    ...:     }
    ...:   ]
    ...: }
    ...: """ % new_bucket.name

    pol.put(Policy=policy)