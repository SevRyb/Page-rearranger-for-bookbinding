# Page-rearranger-for-bookbinding
Python script to rearrange page order of PDF file for bookbinding
# What is it?

![explanation](https://github.com/SevRyb/Page-rearranger-for-bookbinding/blob/main/what_is_it.png)

# Usage
Set the input PDF file as example.pdf:
```powershell
PS> python main.py example.pdf
```
Set preferred number of blocks in book:
```
[?] Number of blocks: 2
```
Set preferred number of sheets (not pages) in book block:
```
[?] Number of sheets in block: 3
```
The script counts total pages of input PDF file:
```
[INFO] Total pages: 24
```
# Output
Generated files are in "out/" directory. 
##### out/
  * example (side_A).pdf
  * example (side_B).pdf
  * example (side_by_side).pdf
# Printing
For printing I recommend you to use:\
`example (side_A).pdf`\
`example (side_B).pdf`\
Firstly, you have to print all pages of **_side A_**, then all pages of **_side B_** (2 pages on the sheet).
# Requirements
`PyPDF2`
