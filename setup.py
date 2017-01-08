import cx_Freeze

executable = [cx_Freeze.Executable('main.py')]

cx_Freeze.setup(
    name = 'RPG',
    options = {'build_exe': {'packages': ['pygame'],
                             'include_files':["OldLondon.ttf", "Deutsch.ttf", "questdone.wav", "select.wav", "newdevil.png"],}},
    executables = executable
    )
