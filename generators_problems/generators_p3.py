# Chunk File Reader
# Problem Statement:
#
# Write a generator function read_file_in_chunks(file_path, chunk_size) that:
#
# Reads a large text file line by line in chunks.
#
# Yields chunk_size lines at a time to prevent memory overload.
#
# Stops when the file has been completely read.
#
# This is useful for processing large files efficiently.
#

def read_file_in_chunks(file_path, chunk_size):
    with open (file_path,'r') as f:
        chunk=[]  # Temporary storage for lines
        for lines in f:
            chunk.append(lines.strip()) # Store line after stripping newline '\n'
            if len(chunk)== chunk_size:
                yield  chunk
                chunk=[]



c=read_file_in_chunks("../Text.txt", 5)
print(c.__next__())

