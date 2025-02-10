class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        self.title = title
        self.contents = contents
        self.already_read = ""

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return f"{self.title}: {self.contents}"

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        contents_words = self.contents.split()
        return len(contents_words)

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        words_list = self.contents.split()
        return int(len(words_list)/wpm)

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        calculated_chunk_word_count = wpm * minutes
        chunk_starting_index = len(self.already_read.split())
        contents_total_word_count = len(self.contents.split())
        chunk_ending_index = chunk_starting_index + calculated_chunk_word_count

        if chunk_ending_index > contents_total_word_count:
            chunk_ending_index = contents_total_word_count
        
        chunk_word_list = self.contents.split()[chunk_starting_index:chunk_ending_index]
        reading_chunk = " ".join(chunk_word_list)

        if chunk_ending_index == contents_total_word_count:
            self.already_read = ""
        else:
            self.already_read += f" {reading_chunk}"
        return reading_chunk
