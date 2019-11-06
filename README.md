# Text To Image Documents script

Requirement: ImageMagick 

Instruction: 
> python3.7 txt2ImgDoc.py \<input folder\>

\<input folder\> is the directory containing all of text files as well as sub-directories (2 or more level of sub-folder may cause crashes. It's best to not have any sub-directory at all).

This will create 2 new folders: One containing the clean text file without any html tags, the other having all of the text files converted into images.

Note: Removing html tags currently only works with articles from DAniEL dataset. Just comment out line #82 if you already have a clean dataset
