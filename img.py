import requests
from PIL import Image
from io import BytesIO

r=requests.get("https://img.magnific.com/free-photo/beautiful-lake-mountains_395237-44.jpg?semt=ais_hybrid&w=740&q=80")
i=Image.open(BytesIO(r.content))
fp=open("img.jpg","wb")
i.save(fp)
fp.close()