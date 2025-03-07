from abc import ABC,abstractmethod

class FileCompressor(ABC):

    @abstractmethod
    def  compress(self,file_path):
        pass
    @abstractmethod
    def decompress(self,file_path):
        pass

class ZipCompressor(FileCompressor):

    def compress(self,file_path):
        print("Compressing file using ZIP format" )
    def decompress(self,file_path):
        print("decompressing file using ZIP format" )

class RarCompressor(FileCompressor):

    def compress(self,file_path):
        print("Compressing file using RAR format")
    def decompress(self,file_path):
        print("decompressing file using RAR format")

z=ZipCompressor()
z.compress("abc")
z.decompress("def")

r=RarCompressor()
r.compress("rac")
r.decompress("radec")
