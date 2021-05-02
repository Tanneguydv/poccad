![poccad_github](https://user-images.githubusercontent.com/81742654/116783820-36b8e980-aa91-11eb-8137-e7502adc98ee.png)


# poccad
poccad is a Python parametric CAD application using pyqt5 and keeping original pythonocc scripts syntax.

The idea is modeling in an user friendly framework with a didactic way to learn and use pythonocc. You can edit your code and render your file on the same UI, use any of the pythonocc-core method that are not yet implement as long as you import them, export your project as `.py` files or 3d exchange format such as `.stp`, .`iges` or `.stl`.

Example of use :
- Modeling part and export
- Developp functions in a friendly user framework before implement in your code
- Discover and learn pythonocc by trying and consult files

I guess the code needs a lot clean-up and hope it would be useful to anybody. I've started to implement method in `lib\Scripts` such as `make_box` , `draw_point` or `export_step`, a contribute instructions file will follow.

Generated files are named `*.pocc` or `*.py`

The Qt designer file is `poccad.ui` then converted in `poccad.py` thanks to the line stored in `cmd_qtGUI.txt` and all the functions are stored under `poccad_Method.py` 

# Launch

Requires : pythonocc-core and PyQt5. Installation guide will be add soon, but you can refer to https://github.com/tpaviot/pythonocc-core with for example conda installing  https://anaconda.org/conda-forge/pythonocc-core 

Execute `poccad_launcher.py` to get started

**New ui design and functions, readme update coming soon**

![20210430_new-ui](https://user-images.githubusercontent.com/81742654/116717430-29402880-a9d9-11eb-8fe0-323d050dfb1e.jpg)

# Examples from the previous UI :

**Open a demo file :**

![open_demofile](https://user-images.githubusercontent.com/81742654/116223455-d142c100-a74f-11eb-9cbd-a9ddde39b921.gif)


**Boolean cut and export result as filename.step :**

![box_translate](https://user-images.githubusercontent.com/81742654/116221251-ba9b6a80-a74d-11eb-9f03-617ff6b7eb32.gif)


**Translate a box and change view to Top :**

![bool](https://user-images.githubusercontent.com/81742654/116221241-b707e380-a74d-11eb-99eb-52c486927c29.gif)
