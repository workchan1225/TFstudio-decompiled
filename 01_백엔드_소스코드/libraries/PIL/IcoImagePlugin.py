# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: IcoImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import warnings
from io import BytesIO
from math import ceil, log
from typing import IO, NamedTuple
from  import BmpImagePlugin, Image, ImageFile, PngImagePlugin
from _binary import i16le as i16
from _binary import i32le as i32
from _binary import o8
from _binary import o16le as o16
from _binary import o32le as o32
_MAGIC = b'\x00\x00\x01\x00'

def _save(im = None, fp = None, filename = None):
    fp.write(_MAGIC)
    bmp = im.encoderinfo.get('bitmap_format') == 'bmp'
    sizes = im.encoderinfo.get('sizes', [
        (16, 16),
        (24, 24),
        (32, 32),
        (48, 48),
        (64, 64),
        (128, 128),
        (256, 256)])
    frames = []
    provided_ims = [
        im] + im.encoderinfo.get('append_images', [])
    (width, height) = im.size
    for size in sorted(set(sizes)):
        if size[0] > width and size[1] > height and size[0] > 256 or size[1] > 256:
            continue
        for provided_im in provided_ims:
            if provided_im.size != size:
                continue
            frames.append(provided_im)
            if bmp:
                bits = BmpImagePlugin.SAVE[provided_im.mode][1]
                bits_used = [
                    bits]
                for other_im in provided_ims:
                    if other_im.size != size:
                        continue
                    bits = BmpImagePlugin.SAVE[other_im.mode][1]
                    if bits not in bits_used:
                        frames.append(other_im)
                        bits_used.append(bits)
                frame = provided_im.copy()
                frame.thumbnail(size, Image.Resampling.LANCZOS, reducing_gap = None)
                frames.append(frame)
                continue
                fp.write(o16(len(frames)))
                offset = fp.tell() + len(frames) * 16
                for frame in frames:
                    (width, height) = frame.size
                    fp.write(o8(width if width < 256 else 0))
                    fp.write(o8(height if height < 256 else 0))
                    (bits, colors) = BmpImagePlugin.SAVE[frame.mode][1:] if bmp else (32, 0)
                    fp.write(o8(colors))
                    fp.write(b'\x00')
                    fp.write(b'\x00\x00')
                    fp.write(o16(bits))
                    image_io = BytesIO()
                    if bmp:
                        frame.save(image_io, 'dib')
                        if bits != 32:
                            and_mask = Image.new('1', size)
                            ImageFile._save(and_mask, image_io, [
                                ImageFile._Tile('raw', (0, 0) + size, 0, ('1', 0, -1))])
                        else:
                            frame.save(image_io, 'png')
                    image_io.seek(0)
                    image_bytes = image_io.read()
                    if bmp:
                        image_bytes = image_bytes[:8] + o32(height * 2) + image_bytes[12:]
                    bytes_len = len(image_bytes)
                    fp.write(o32(bytes_len))
                    fp.write(o32(offset))
                    current = fp.tell()
                    fp.seek(offset)
                    fp.write(image_bytes)
                    offset = offset + bytes_len
                    fp.seek(current)
                    return None


def _accept(prefix = None):
    return prefix.startswith(_MAGIC)


class IconHeader(NamedTuple):
    color_depth: 'int' = 'IconHeader'


class IcoFile:
    
    def __init__(self = None, buf = None):
