# prettify-html-tag-remover
This program is to remove the html from services like tl;dv and similar that transcribes conversations but returns it in an unreadable html mess.


# Usage

copy the html tag (I recommend you to just copy where the conversation you want is located. Do not copy the entire html file) from your browser and paste in the file.html

After pasting the file in file.html run the following in your terminal (you need python3 installed)

```bash
    python3 extract_text.py file.html 
```

This should extract the text from the html but still unorganized. For better reading, I recommend running:

```bash
    python3 format_speakers.py file.txt
```

This will populate the file_formatted.txt where you will have a much better reading.

# Improvements

This code was done in 5 minutes. I know it is still duplicating the name of the user (I am using mostly with tl;dv). But it is working for me. If you see a bug or wants a better software, you can open a pullrequest after forking. Thanks