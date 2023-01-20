# `TimeScriber`, a textual user interface (TUI) app
A note taking app that timestamps your notes! Built off of TUI (https://textual.textualize.io/) to create a simple platform for recording meeting minutes and taking notes during usability testing.

`TimeScriber` is a ✨Work in Progress✨

## Basic run instructions:

1. Create an anaconda environment with `python==3.10.8`
2. `pip install textual` -> see https://textual.textualize.io/getting_started/ for more details
3. Manually add any packages in the `requirements.txt` folder, **OR** 
4. ... navigate to the folder containing `requirements.txt` and run 
    
    `pip install -r requirements.txt`

5. In a terminal set to your `TimeScriber` conda environment, set the current directory (`cd`) to the folder containing `timescriber.py`
6. Type `textual run timescriber.py` and hit enter :)

`TimeScriber` should be running!

On Windows, you should have something that looks like this:
![timescriber_windows](https://user-images.githubusercontent.com/62706609/209975501-70a47ab9-b925-4171-bb23-4e0307b57fc8.png)

On Mac, it will look something like this (note, I removed the darkmode toggle):
![timescriber_mac](https://user-images.githubusercontent.com/62706609/209975523-69663171-4e7c-4163-b26f-413e227b74e6.png)

Note: These instructions are "quick and dirty". I hope to have an `.exe` of TimeScriber soon!
