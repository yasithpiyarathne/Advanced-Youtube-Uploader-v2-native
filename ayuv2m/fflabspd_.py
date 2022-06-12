from ffprobe import FFProbe

def get_eng_subtitles_from_file(media_file):
    metadata = FFProbe(media_file)
    streams = 