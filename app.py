import sys
import os

from flask import Flask
from flask_s3_viewer import FlaskS3Viewer
from flask_s3_viewer.aws.ref import Region

app = Flask(__name__)

# For test, disable template caching
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
app.config['TEMPLATES_AUTO_RELOAD'] = True

# FlaskS3Viewer Init
s3viewer = FlaskS3Viewer(
    app, # Flask app
    namespace='flask-s3-viewer', # namespace be unique
    template_namespace='mdl', # set template
    object_hostname='http://127.0.0.1:3000', # file's hostname
    allowed_extensions={}, # allowed extension
    config={ # Bucket configs and else
    'profile_name': None,
        'access_key': os.getenv("AWS_ACCESS_KEY_ID"),
        'secret_key': os.getenv("AWS_SECRET_ACCESS_KEY"),
        'region_name': os.getenv("AWS_DEFAULT_REGION"),
        'endpoint_url': None,
        'bucket_name': os.getenv("BUCKET_NAME"),
        'cache_dir': '/tmp/flask_s3_viewer',
        'use_cache': True,
        'ttl': 86400,
    }
)

s3viewer.register()

@app.route('/index')
def index ():
    return 'Your app index page'

# Usage: python example.py test (run debug mode)
if __name__ == '__main__':
    debug = False
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            debug = True
    app.run(debug=debug, port=3000)

