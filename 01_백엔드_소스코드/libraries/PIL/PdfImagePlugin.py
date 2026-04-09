# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: PdfImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import io
import math
import os
import time
from typing import IO, Any
from  import Image, ImageFile, ImageSequence, PdfParser, features

def _save_all(im = None, fp = None, filename = None):
    _save(im, fp, filename, save_all = True)


def _write_image(im = None, filename = None, existing_pdf = None, image_refs = ('im', 'Image.Image', 'filename', 'str | bytes', 'existing_pdf', 'PdfParser.PdfParser', 'image_refs', 'list[PdfParser.IndirectReference]', 'return', 'tuple[PdfParser.IndirectReference, str]')):
    params = None
    decode = None
    (width, height) = im.size
    dict_obj = {
        'BitsPerComponent': 8 }
    if im.mode == '1':
        if features.check('libtiff'):
            decode_filter = 'CCITTFaxDecode'
            dict_obj['BitsPerComponent'] = 1
            params = PdfParser.PdfArray([
                PdfParser.PdfDict({
                    'K': -1,
                    'BlackIs1': True,
                    'Columns': width,
                    'Rows': height })])
        else:
            decode_filter = 'DCTDecode'
        dict_obj['ColorSpace'] = PdfParser.PdfName('DeviceGray')
        procset = 'ImageB'
    elif im.mode == 'L':
        decode_filter = 'DCTDecode'
        dict_obj['ColorSpace'] = PdfParser.PdfName('DeviceGray')
        procset = 'ImageB'
    elif im.mode == 'LA':
        decode_filter = 'JPXDecode'
        procset = 'ImageB'
        dict_obj['SMaskInData'] = 1
# WARNING: Decompyle incomplete


def _save(im = None, fp = None, filename = None, save_all = (False,)):
    is_appending = im.encoderinfo.get('append', False)
    filename_str = filename.decode() if isinstance(filename, bytes) else filename
    if is_appending:
        existing_pdf = PdfParser.PdfParser(f = fp, filename = filename_str, mode = 'r+b')
    else:
        existing_pdf = PdfParser.PdfParser(f = fp, filename = filename_str, mode = 'w+b')
    dpi = im.encoderinfo.get('dpi')
    if dpi:
        x_resolution = dpi[0]
        y_resolution = dpi[1]
    else:
        x_resolution = im.encoderinfo.get('resolution', 72)
        y_resolution = im.encoderinfo.get('resolution', 72)
    info = {
        'title': None if is_appending else os.path.splitext(os.path.basename(filename))[0],
        'author': None,
        'subject': None,
        'keywords': None,
        'creator': None,
        'producer': None,
        'creationDate': None if is_appending else time.gmtime(),
        'modDate': None if is_appending else time.gmtime() }
    for k, default in info.items():
        v = im.encoderinfo.get(k) if k in im.encoderinfo else default
        if v:
            existing_pdf.info[k[0].upper() + k[1:]] = v
        im.load()
        existing_pdf.start_writing()
        existing_pdf.write_header()
        existing_pdf.write_comment('created by Pillow PDF driver')
        ims = [
            im]
        if save_all:
            append_images = im.encoderinfo.get('append_images', [])
            for append_im in append_images:
                append_im.encoderinfo = im.encoderinfo.copy()
                ims.append(append_im)
                number_of_pages = 0
                image_refs = []
                page_refs = []
                contents_refs = []
                for im in ims:
                    im_number_of_pages = 1
                    if save_all:
                        im_number_of_pages = getattr(im, 'n_frames', 1)
                    number_of_pages += im_number_of_pages
                    for i in range(im_number_of_pages):
                        image_refs.append(existing_pdf.next_object_id(0))
                        if im.mode == 'P' and 'transparency' in im.info:
                            image_refs.append(existing_pdf.next_object_id(0))
                        page_refs.append(existing_pdf.next_object_id(0))
                        contents_refs.append(existing_pdf.next_object_id(0))
                        existing_pdf.pages.append(page_refs[-1])
                        existing_pdf.write_catalog()
                        page_number = 0
                        for im_sequence in ims:
                            im_pages = ImageSequence.Iterator(im_sequence) if save_all else [
                                im_sequence]
                            for im in im_pages:
                                (image_ref, procset) = _write_image(im, filename, existing_pdf, image_refs)
                                existing_pdf.write_page(page_refs[page_number], Resources = PdfParser.PdfDict(ProcSet = [
                                    PdfParser.PdfName('PDF'),
                                    PdfParser.PdfName(procset)], XObject = PdfParser.PdfDict(image = image_ref)), MediaBox = [
                                    0,
                                    0,
                                    im.width * 72 / x_resolution,
                                    im.height * 72 / y_resolution], Contents = contents_refs[page_number])
                                page_contents = b'q %f 0 0 %f 0 0 cm /image Do Q\n' % (im.width * 72 / x_resolution, im.height * 72 / y_resolution)
                                existing_pdf.write_obj(contents_refs[page_number], stream = page_contents)
                                page_number += 1
                                existing_pdf.write_xref_and_trailer()
                                if hasattr(fp, 'flush'):
                                    fp.flush()
    existing_pdf.close()

Image.register_save('PDF', _save)
Image.register_save_all('PDF', _save_all)
Image.register_extension('PDF', '.pdf')
Image.register_mime('PDF', 'application/pdf')
