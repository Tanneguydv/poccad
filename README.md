![poccad_github](https://user-images.githubusercontent.com/81742654/116221635-15cd5d00-a74e-11eb-86e8-b058216ed3c8.png)

# poccad
a simple pyqt5 modelisation/visualization didactic tool for pythonocc

Edit your code and render your file on the same UI.

Use any of the pythonocc-core method as long as you import them.

I've started to implement method in `lib\Scripts` such as `make_box` , `bool_cut` or `export_step`

File are named `*.occ`

I guess the code need a lot clean-up as I'm new to all this, hope it would be useful to anybody. 
The Qt designer file is `poccad.ui` is converted in `poccad.py` thanks to the line in `cmd_qtGUI.txt` and all the functions are stored under `poccad_Method.py` 

# Launch

Requires : https://github.com/tpaviot/pythonocc-core and PyQt5

Execute `poccad_launcher.py` to get started



**Open a demo file :**

![open_demofile](https://user-images.githubusercontent.com/81742654/116223455-d142c100-a74f-11eb-9cbd-a9ddde39b921.gif)


**Boolean cut and export result as filename.step :**

![box_translate](https://user-images.githubusercontent.com/81742654/116221251-ba9b6a80-a74d-11eb-9f03-617ff6b7eb32.gif)


**Translate a box and change view to Top :**

![bool](https://user-images.githubusercontent.com/81742654/116221241-b707e380-a74d-11eb-99eb-52c486927c29.gif)
