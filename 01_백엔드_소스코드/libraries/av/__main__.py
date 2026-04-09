# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __main__.pyc (Python 3.11)

from __future__ import annotations
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--codecs', action = 'store_true')
    parser.add_argument('--hwdevices', action = 'store_true')
    parser.add_argument('--hwconfigs', action = 'store_true')
    parser.add_argument('--version', action = 'store_true')
    args = parser.parse_args()
    if args.version:
        import av
        import av._core as av
        print(f'''PyAV v{av.__version__}''')
        by_config = { }
        for libname, config in sorted(av._core.library_meta.items()):
            version = config['version']
            if version[0] >= 0:
                by_config.setdefault((config['configuration'], config['license']), []).append((libname, config))
            for config, license in sorted(by_config.items()):
                libs = None
                print('library configuration:', config)
                print('library license:', license)
                for libname, config in libs:
                    version = config['version']
                    print(f'''{libname:<13} {version[0]:3d}.{version[1]:3d}.{version[2]:3d}''')
                    if args.hwdevices:
                        hwdevices_available = hwdevices_available
                        import av.codec.hwaccel
                        print('Hardware device types:')
                        for x in hwdevices_available():
                            print('   ', x)
                            if args.hwconfigs:
                                dump_hwconfigs = dump_hwconfigs
                                import av.codec.codec
                                dump_hwconfigs()
    if args.codecs:
        dump_codecs = dump_codecs
        import av.codec.codec
        dump_codecs()
        return None

if __name__ == '__main__':
    main()
    return None
