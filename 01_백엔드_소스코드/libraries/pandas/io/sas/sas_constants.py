# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sas_constants.pyc (Python 3.11)

from __future__ import annotations
from typing import Final
magic: 'Final' = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc2\xea\x81`\xb3\x14\x11\xcf\xbd\x92\x08\x00\t\xc71\x8c\x18\x1f\x10\x11'
align_1_checker_value: 'Final' = b'3'
align_1_offset: 'Final' = 32
align_1_length: 'Final' = 1
align_1_value: 'Final' = 4
u64_byte_checker_value: 'Final' = b'3'
align_2_offset: 'Final' = 35
align_2_length: 'Final' = 1
align_2_value: 'Final' = 4
endianness_offset: 'Final' = 37
endianness_length: 'Final' = 1
platform_offset: 'Final' = 39
platform_length: 'Final' = 1
encoding_offset: 'Final' = 70
encoding_length: 'Final' = 1
dataset_offset: 'Final' = 92
dataset_length: 'Final' = 64
file_type_offset: 'Final' = 156
file_type_length: 'Final' = 8
date_created_offset: 'Final' = 164
date_created_length: 'Final' = 8
date_modified_offset: 'Final' = 172
date_modified_length: 'Final' = 8
header_size_offset: 'Final' = 196
header_size_length: 'Final' = 4
page_size_offset: 'Final' = 200
page_size_length: 'Final' = 4
page_count_offset: 'Final' = 204
page_count_length: 'Final' = 4
sas_release_offset: 'Final' = 216
sas_release_length: 'Final' = 8
sas_server_type_offset: 'Final' = 224
sas_server_type_length: 'Final' = 16
os_version_number_offset: 'Final' = 240
os_version_number_length: 'Final' = 16
os_maker_offset: 'Final' = 256
os_maker_length: 'Final' = 16
os_name_offset: 'Final' = 272
os_name_length: 'Final' = 16
page_bit_offset_x86: 'Final' = 16
page_bit_offset_x64: 'Final' = 32
subheader_pointer_length_x86: 'Final' = 12
subheader_pointer_length_x64: 'Final' = 24
page_type_offset: 'Final' = 0
page_type_length: 'Final' = 2
block_count_offset: 'Final' = 2
block_count_length: 'Final' = 2
subheader_count_offset: 'Final' = 4
subheader_count_length: 'Final' = 2
page_type_mask: 'Final' = 3840
page_type_mask2: 'Final' = 61440 | page_type_mask
page_meta_type: 'Final' = 0
page_data_type: 'Final' = 256
page_mix_type: 'Final' = 512
page_amd_type: 'Final' = 1024
page_meta2_type: 'Final' = 16384
page_comp_type: 'Final' = 36864
page_meta_types: 'Final' = [
    page_meta_type,
    page_meta2_type]
subheader_pointers_offset: 'Final' = 8
truncated_subheader_id: 'Final' = 1
compressed_subheader_id: 'Final' = 4
compressed_subheader_type: 'Final' = 1
text_block_size_length: 'Final' = 2
row_length_offset_multiplier: 'Final' = 5
row_count_offset_multiplier: 'Final' = 6
col_count_p1_multiplier: 'Final' = 9
col_count_p2_multiplier: 'Final' = 10
row_count_on_mix_page_offset_multiplier: 'Final' = 15
column_name_pointer_length: 'Final' = 8
column_name_text_subheader_offset: 'Final' = 0
column_name_text_subheader_length: 'Final' = 2
column_name_offset_offset: 'Final' = 2
column_name_offset_length: 'Final' = 2
column_name_length_offset: 'Final' = 4
column_name_length_length: 'Final' = 2
column_data_offset_offset: 'Final' = 8
column_data_length_offset: 'Final' = 8
column_data_length_length: 'Final' = 4
column_type_offset: 'Final' = 14
column_type_length: 'Final' = 1
column_format_text_subheader_index_offset: 'Final' = 22
column_format_text_subheader_index_length: 'Final' = 2
column_format_offset_offset: 'Final' = 24
column_format_offset_length: 'Final' = 2
column_format_length_offset: 'Final' = 26
column_format_length_length: 'Final' = 2
column_label_text_subheader_index_offset: 'Final' = 28
column_label_text_subheader_index_length: 'Final' = 2
column_label_offset_offset: 'Final' = 30
column_label_offset_length: 'Final' = 2
column_label_length_offset: 'Final' = 32
column_label_length_length: 'Final' = 2
rle_compression: 'Final' = b'SASYZCRL'
rdc_compression: 'Final' = b'SASYZCR2'
compression_literals: 'Final' = [
    rle_compression,
    rdc_compression]
# WARNING: Decompyle incomplete
