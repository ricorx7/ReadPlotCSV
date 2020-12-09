from rti_python.Utilities.read_plot_csv import ReadPlotCSV

to_csv = ReadPlotCSV()
to_csv.select_and_process(max_roll=160, max_vel=88, max_bt_vel=1.0, max_mag=3.0)
