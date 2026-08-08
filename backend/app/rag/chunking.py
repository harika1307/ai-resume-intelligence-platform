from typing import List

class Chunker:
    def __init__(self,chunk_size:int=500,overlap:int=100):
        """initializes the chunker.
        Args: 
        chunk_size:Maximum size of each chunk.
        overlap:Number of overlapping charcaters between consecutive chunks.
        """
        if chunk_size<=0:
            raise ValueError("chunk size must be greater than 0")
        if overlap<0:
            raise ValueError("Overlap cannot be negative")
        if overlap>=chunk_size:
            raise ValueError("overlap must be smaller than chunk size")
        self.chunk_size=chunk_size
        self.overlap=overlap
    def chunk_text(self,text:str)->List[str]:
        """Splits input text into fixed size chunks.
        Args: text:the input text to be chunked.
        returns: A list of text chunks.
        """
        if not text.strip():
            return []
        chunks=[]
        step=self.chunk_size-self.overlap
        for i in range(0,len(text),step):
            chunk=text[i:i+self.chunk_size]
            chunks.append(chunk)
        return chunks
    def recursive_chunk(self):
        pass
    def sentence_chunk(self):
        pass
    def token_chunk(self):
        pass

# chunker = Chunker(chunk_size=5,overlap=2)
# text = "ABCDEFGHIJKLMNO"
# chunks = chunker.chunk_text(text)

# print(chunks)