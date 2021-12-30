import sys
import py7zr

class Callback():#尚未使用，先写在这里，参考：https://github.com/miurahr/py7zr/issues/74
    def init():
        pass
    def report_start(self, processing_file_path, processing_bytes):
        print("report_start",processing_file_path, processing_bytes)

    def report_end(self, processing_file_path, wrote_bytes):
        print("report_end",processing_file_path, wrote_bytes)

def makearchive(filelist,outfilename):
    print(outfilename)
    with py7zr.SevenZipFile(outfilename,"w") as archive:
        for file in filelist:
            print("\t",file)
            archive.write(file)

version=sys.argv[1]
filelist=[
    "Hitsuboku Kumi JPN {}.srdx".format(version),
    "A3.vsdx",
    "A3.vsdxindex",
    "A4.vsdx",
    "A4.vsdxindex",
    "D4.vsdx",
    "D4.vsdxindex",
    "D5.vsdx",
    "D5.vsdxindex",
    "main.lsd",
    "license.md",
    "readme.md",
    "readme_zh.md",
]
outfilename="bin/Hitsuboku Kumi JPN {}.7z".format(version)
makearchive(filelist,outfilename)
