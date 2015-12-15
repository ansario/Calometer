from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.images import ImageFile
from PIL import Image
import pytesseract
import os


def index(req):
    return HttpResponse("Hello world.")

@csrf_exempt
def decode(req):
    # print req.FILES


    file_key=None
    for file_key in sorted(req.FILES):


        wrapped_file = ImageFile(req.FILES[file_key])
        filename = wrapped_file.name

    # new photo table-row
        # print wrapped_file

        Image.open(wrapped_file).rotate(270).save("test-phone.jpg")
        os.system("./textcleaner -g -e none -f 10 -u -s 1 -T -o 5 test-phone.jpg out.jpg")
        print pytesseract.image_to_string(Image.open(wrapped_file).rotate(270))
    return HttpResponse(status=200)

# Create your views here.
