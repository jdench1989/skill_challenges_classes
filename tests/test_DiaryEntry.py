from lib.DiaryEntry import DiaryEntry

def test_initialises_correctly():
    diary_entry = DiaryEntry("Day one", "Nothing much happened")
    assert isinstance(diary_entry, DiaryEntry)
    assert diary_entry.title == "Day one"
    assert diary_entry.contents == "Nothing much happened"

def test_format_method_returns_correctly_formatted_string():
    diary_entry = DiaryEntry("Day one", "Nothing much happened")
    assert diary_entry.format() == "Day one: Nothing much happened"

def test_count_words_method_returns_correct_number_of_words_of_contents():
    diary_entry = DiaryEntry("Day one", "Nothing much happened")
    assert diary_entry.count_words() == 3

def test_reading_time_returns_correct_estimate_value():
    diary_entry = DiaryEntry("Test title", " ".join(["word" for i in range(1000)]))
    assert diary_entry.reading_time(200) == 5
    assert diary_entry.reading_time(100) == 10
    assert diary_entry.reading_time(1000) == 1
    assert diary_entry.reading_time(333) == 3

def test_reading_chunk_returns_correct_chunk_of_contents():
    diary_entry = DiaryEntry("Test title", " ".join([str(i) for i in range(1, 1001)]))
    reading_chunk = diary_entry.reading_chunk(200, 2)
    assert isinstance(reading_chunk, str)
    assert len(reading_chunk.split()) == 400
    

def test_reading_chunk_correctly_returns_next_chunk_when_called_second_time():
    diary_entry = DiaryEntry("Test title", " ".join([str(i) for i in range(1, 1001)]))
    first_chunk = diary_entry.reading_chunk(200, 1)
    second_chunk = diary_entry.reading_chunk(200,1)
    assert first_chunk != second_chunk
    assert second_chunk.split()[0] == "201"
    assert second_chunk.split()[-1] == "400"

def test_reading_chunk_final_call_includes_all_unread_words_only():
    diary_entry = DiaryEntry("Test title", " ".join([str(i) for i in range(1, 501)]))
    first_chunk = diary_entry.reading_chunk(200, 1)
    second_chunk = diary_entry.reading_chunk(200, 1)
    third_chunk = diary_entry.reading_chunk(200, 1)
    assert len(third_chunk.split()) == 100
    assert third_chunk.split()[-1] == str(500)

def test_reading_chunk_final_call_resets_already_read_to_empty():
    diary_entry = DiaryEntry("Test title", " ".join([str(i) for i in range(1, 501)]))
    first_chunk = diary_entry.reading_chunk(200, 1)
    second_chunk = diary_entry.reading_chunk(200, 1)
    third_chunk = diary_entry.reading_chunk(200, 1)
    assert diary_entry.already_read == ""
