import csv
import shutil
import sys
import time
import os
import logging

# http client configuration
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/63.0.3239.84 Chrome/63.0.3239.84 Safari/537.36'

# logging configuration
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

python_version = sys.version_info.major
logging.info("executed by python %d" % python_version)

# compatibility with python 2
if python_version == 3:
    import urllib.parse
    import urllib.request
    urljoin = urllib.parse.urljoin
    urlretrieve = urllib.request.urlretrieve
    quote = urllib.parse.quote

    # configure headers
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', user_agent)]
    urllib.request.install_opener(opener)
else:
    import urllib
    urljoin = urllib.urljoin
    urlretrieve = urllib.urlretrieve
    quote = urllib.quote

    # configure headers
    class AppURLopener(urllib.FancyURLopener):
        version = user_agent
    urllib._urlopener = AppURLopener()

def fix_url(url):
    url = quote(url, safe="%/:=&?~#+!$,;'@()*[]")
    return url

def create_brand_folder(brand_name):
    brand_dir = os.path.join(".", brand_name)
    if not os.path.exists(brand_dir):
        os.makedirs(brand_dir)
    return brand_dir

def create_model_folder(brand_dir, model_name):
    sanitized_model_name = "".join(c if c.isalnum() else "_" for c in model_name)
    model_dir = os.path.join(brand_dir, sanitized_model_name)
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    return model_dir

def download_csv_row_images(row, dest_dir):
    brand_name = row['brand_name']
    model_name = row['model_name']

    brand_dir = create_brand_folder(brand_name)
    model_dir = create_model_folder(brand_dir, model_name)

    for key in row:
        if key.endswith("-src"):
            image_url = row[key]
            image_url = urljoin(row['web-scraper-start-url'], image_url)

            image_filename = "%s-%s" % (row['web-scraper-order'], key[0:-4])
            download_image(image_url, model_dir, image_filename)

def download_image(image_url, dest_dir, image_filename):
    image_url = fix_url(image_url)

    try:
        logging.info("downloading image %s" % image_url)
        tmp_file_name, headers = urlretrieve(image_url)
        content_type = headers.get("Content-Type")

        if content_type == 'image/jpeg' or content_type == 'image/jpg':
            ext = 'jpg'
        elif content_type == 'image/png':
            ext = 'png'
        elif content_type == 'image/gif':
            ext = 'gif'
        elif content_type == 'image/webp':
            ext = 'webp'
        else:
            logging.warning("unknown image content type %s" % content_type)
            return

        image_path = os.path.join(dest_dir, image_filename + "." + ext)
        shutil.move(tmp_file_name, image_path)
    except Exception as e:
        logging.warning("Image download error. %s" % e)

def get_csv_image_dir(csv_filename):
    base = os.path.basename(csv_filename)
    dir = os.path.splitext(base)[0]

    if not os.path.exists(dir):
        os.makedirs(dir)

    return dir

def download_csv_file_images(filename):
    logging.info("importing data from %s" % filename)

    dest_dir = get_csv_image_dir(filename)

    # check whether csv file has utf-8 bom char at the beginning
    skip_utf8_seek = 0
    with open(filename, "rb") as csvfile:
        csv_start = csvfile.read(3)
        if csv_start == b'\xef\xbb\xbf':
            skip_utf8_seek = 3

    with open(filename, "r", encoding="utf8") as csvfile:
        # remove utf-8 bom sig
        csvfile.seek(skip_utf8_seek)

        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            download_csv_row_images(row, dest_dir)

def main(args):
    # filename passed through args
    if len(args) >= 2:
        csv_filename = args[1]
        download_csv_file_images(csv_filename)
        logging.info("image download completed")
    else:
        logging.warning("no input file found")

    time.sleep(10)

main(sys.argv)
