import urllib.request
def csv_file_download(csv_url):
    response = urllib.request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    print(csv_str)
    lines = csv_str.split("\\n")
    dest_url = "goog.csv"
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + '\n')