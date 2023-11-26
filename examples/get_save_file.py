import sys
import mrequests

buf = bytearray(1024)

if len(sys.argv) > 1:
    url = sys.argv[1]

    if len(sys.argv) > 2:
        filename = sys.argv[2]
    else:
        filename = url.rsplit("/", 1)[1]
else:
    host = 'http://httpbin.org/'
    #host = "http://localhost/"
    url = host + "image"
    filename = "image.png"

r = mrequests.get(url, headers={b"accept": b"image/png"})

if r.status_code == 200:
    r.save(filename, buf=buf)
    print("Image saved to '{}'.".format(filename))
else:
    print("Request failed. Status: {}".format(r.status_code))

r.close()
