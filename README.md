# File-Handling
A mini python project that handle your files in a given directory. If your file type is in one of the formats below, it will move them in a suitable directory. If 
there are some file types which are not supported, it will move them into **other** directory.
I tried to handle the most conventional file types.
| Supported File Format| Destination Directory |
| ---------------------| --------------------- |
| .png                 | image                 |
| .csv                 | data                  |
| .pdf                 | document              |
| .xlsx                | excel                 |
| .exe                 | executable            |
| .zip                 | compressed            |
| .jpg                 | image                 | 
| .docx                | document              |
| .pptx                | presentation          |
| .txt                 | document              |
| .rar                 | compressed            |
| .json                | data                  |
| .mpp                 | project               |
| .py                  | python                |
| .mp3                 | audio                 |
| .mp4                 | video                 |

## How To Run
First add the `src` to `PYTHONPATH`. If you don't know how to do it, write this command in your terminal:

```
export PYTHONPATH=${PWD}
```

Then run:

```
python src/main.py
```

## An example of the detail of my own messy directory
You can see the pie chart of one of my directories:
![alt text for screen readers](./dirstat.png "The directory stat")
