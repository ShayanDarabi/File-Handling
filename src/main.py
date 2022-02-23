import shutil
from collections import Counter
from pathlib import Path
import matplotlib.pyplot as plt
from typing import Union
class OrgenizedDirectory:
    """
    This class is used to orgnize files in a directory by creating and moving
    files into directories based on their file's extension.
    """
    def __init__(self, directory:Union[str,Path]):
        self.directory = Path(directory)
        if not self.directory.exists():
            raise FileNotFoundError(f"{self.directory} doesn't exist.")
        self.extention_destinations = {
            ".png": "image",
            ".csv": "data",
            ".pdf": "document",
            ".xlsx": "excel",
            ".exe": "executable",
            ".zip": "compressed",
            ".jpg": "image",
            ".docx": "document",
            ".pptx": "presentation",
            ".txt": "document",
            ".rar": "compressed",
            ".json": "data",
            ".mpp": "project",
            ".py": "python",
            ".mp3": "audio",
            ".mp4": "video"
        }

    def __call__(self):
        """
        this method creats correspondent directories for each file format
        and moves those files into their specific directory.
        """
        for file in self.directory.iterdir():
            #exclude other directories and hidden files
            if file.is_dir() or file.name.startswith("."):
                continue
            #process excluded file formats
            if file.suffix not in self.extention_destinations:
                if Path(self.directory / "other").is_dir():
                    shutil.move(str(file), str(self.directory / "other"))
                    continue
                else:
                    Path(self.directory / "other").mkdir()
                    shutil.move(str(file), str(self.directory / "other"))
                    continue
            #process included file formats
            DEST_DIR = self.directory / self.extention_destinations[file.suffix]
            if Path(DEST_DIR).is_dir():
                shutil.move(str(file), str(DEST_DIR))
            else:
                Path(DEST_DIR).mkdir()
                shutil.move(str(file), str(DEST_DIR))

    def dirstat(self):
        """
        this method plots a pie chart and saves it into the given directory
        as a png file based on the files' extentions.
        """
        #Get all files' types
        file_extension = []
        for file in self.directory.iterdir():
            if file.is_dir():
                continue
            file_extension.append(file.suffix)

        #files statistics
        file_stat = Counter(file_extension).most_common()
        label = []
        number_of_file = []
        for element in file_stat:
            label.append(element[0])
            number_of_file.append(element[1])

        # plot a pie chart of directory contents and save it in the directory which was gien to the class
        plt.figure(figsize=(15, 15), dpi=80)
        plt.pie(x=number_of_file, labels=label, shadow=True, autopct='%1.1f%%')
        plt.savefig(Path(self.directory) / "chatstat.png")

#the lines below were for testing the script and it didn't fail:)
if __name__ == "__main__":
    directory = OrgenizedDirectory("/mnt/c/users/shayan/downloads")
    directory.dirstat()
    directory()
