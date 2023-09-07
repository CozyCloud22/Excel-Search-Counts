# Excel-Search-Counts

## Installation Steps
I'll do my best to detail everything here but feel free to reach out to me if you have any questions. I have only done this on windows so I have no idea how this might operate on Mac.

1. Firstly since this is Python code, your computer will need to have Python and a Python sublibrary called Pandas installed.
2. You can check if Python is installed by typing "python --version" in your command line app.
3. If Python is NOT installed, you can go to https://www.python.org/downloads/ and follow the instructions there to install it.
4. When Python is installed, go to your command line app and type "pip install pandas". This should install pandas on your computer.

## Usage Steps
1. To get started, clone this repository. In file explorer, click where you want this file to be located then copy the path. (right click location and click "copy path").
2. Next, you will take the copied path and take it to your command line app. You will type "cd" then copy and paste the path (make sure its cd *space* path) and press enter.
3. Then, you will write "git clone https://github.com/CozyCloud22/Excel-Search-Counts".
4. This repository's code should now be in that folder. All that's left is opening the program and running it. (I use VScode to run it but other code editors work as well).

## Running the Program
Running the program is pretty simple and most of what you need is already detailed in the comments but I'll rewrite them here:
1. The first file location should be switched to the location of the excel sheet you are trying to analyze (find the search results).
2. You can get the file location by finding where this excel sheet is and right clicking on it then clicking "copy path".
3. Once you replace the example file location with the actual location of your excel sheet, replace all the backword slashes with double backword slashes.
4. The second file location should be an empty excel sheet but one that's already saved and named. You will repeat steps #2-3 with this as well.
5. After replacing both file locations, the program should run. You will need to make sure neither excel sheet is open when running the program or it will not work.

## Possible Questions
**Q.** What happens if I edited some data in the first excel sheet (the one you want analyzed) but already ran the program so the second excel sheet (the initially empty one) is already full?

**A.** Since the program will not work if there is already content in the supposedly "empty" excel sheet, you have two options. You can create a new blank spreadsheet, name it, and replace the file location with this new one OR you can just ctrl + A (select all) and right click. There should be an option to clear content. Once you have cleared all content and saved/closed the sheet, the program should work.

**Q.** Is this completed?

**A.** No, this a rough draft of what I have planned. There are a few useful functions I want to add but am unsure as of now and am currently looking at how I would approach them. This is a usable program but is a WIP.
