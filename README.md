![poccad_github](https://user-images.githubusercontent.com/81742654/116783820-36b8e980-aa91-11eb-8137-e7502adc98ee.png)


# poccad
a pyqt5 modelisation/visualization didactic tool for pythonocc

Edit your code and render your file on the same UI.

Use any of the pythonocc-core method as long as you import them.

I guess the code needs a lot clean-up (several ui/dialog bugs remain)  and hope it would be useful to anybody. I've started to implement method in `lib\Scripts` such as `make_box` , `draw_point` or `export_step`, as I'm new to all this any help is welcome! :)

Generated files are named `*.pocc`

The Qt designer file is `poccad.ui` is converted in `poccad.py` thanks to the line in `cmd_qtGUI.txt` and all the functions are stored under `poccad_Method.py` 

# Launch

Requires : https://github.com/tpaviot/pythonocc-core and PyQt5

Execute `poccad_launcher.py` to get started

**new ui design and functions, readme update coming soon**

![20210430_new-ui](https://user-images.githubusercontent.com/81742654/116717430-29402880-a9d9-11eb-8fe0-323d050dfb1e.jpg)

# ex ui example :

**Open a demo file :**

![open_demofile](https://user-images.githubusercontent.com/81742654/116223455-d142c100-a74f-11eb-9cbd-a9ddde39b921.gif)


**Boolean cut and export result as filename.step :**

![box_translate](https://user-images.githubusercontent.com/81742654/116221251-ba9b6a80-a74d-11eb-9f03-617ff6b7eb32.gif)


**Translate a box and change view to Top :**

![bool](https://user-images.githubusercontent.com/81742654/116221241-b707e380-a74d-11eb-99eb-52c486927c29.gif)
