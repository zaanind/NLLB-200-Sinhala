import pysrt
import re

# Load the subtitle file
subs = pysrt.open('The.Exorcism.2024.1080p.AMZN.WEB-DL.DDP5.1.H.264-XEBEC-HI.srt')

# Define a regular expression pattern to match contents within square brackets
pattern = re.compile(r'\[.*?\]', re.DOTALL)  # Use re.DOTALL to match across multiple lines

# Iterate over each subtitle and remove the matched content
for sub in subs:
    sub.text = re.sub(pattern, '', sub.text).strip()

# Save the modified subtitles to a new file
subs.save('cleaned_subtitle_file.srt')
