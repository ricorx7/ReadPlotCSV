from rti_python.Utilities.read_plot_csv import ReadPlotCSV

rpc = ReadPlotCSV()

max_roll = 160.0
max_vel = 2.0
max_bt_vel = 1.0
max_mag = 3.0

# Select the file and process the data to a DB file
rpc.select_and_process()

filter_data = "WHERE ensembles.roll > " + str(max_roll) + " OR ensembles.roll < -" + str(max_roll)

# Beam Velocity
rpc.beam_0_vel(filter_data, max_vel=max_vel, display_text=False, display_stats=False, display_plot=False)
rpc.beam_0_vel_remove_ship(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
rpc.beam_1_vel(filter_data, max_vel=max_vel, display_text=False, display_stats=False, display_plot=False)
rpc.beam_1_vel_remove_ship(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
rpc.beam_2_vel(filter_data, max_vel=max_vel, display_text=False, display_stats=False, display_plot=False)
rpc.beam_2_vel_remove_ship(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
rpc.beam_3_vel(filter_data, max_vel=max_vel, display_text=False, display_stats=False, display_plot=False)
rpc.beam_3_vel_remove_ship(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
rpc.display_beam_vel_plots()

# Instrument Velocity
rpc.intr_x_vel_remove_ship(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
rpc.intr_y_vel_remove_ship(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
rpc.intr_z_vel_remove_ship(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
rpc.intr_err_vel_remove_ship(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
rpc.display_instr_vel_plots()

# Earth Velocity
rpc.earth_east_vel(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
rpc.earth_north_vel(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
rpc.earth_vert_vel(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
rpc.earth_east_vel_remove_ship(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
rpc.earth_north_vel_remove_ship(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
rpc.earth_vert_vel_remove_ship(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
rpc.display_earth_vel_plots()
rpc.display_earth_vel_raw_vsr_plots()

# Magnitude and Direction
rpc.mag_plot(filter_data, max_mag=max_mag, max_bt_vel=max_bt_vel, display_text=True, display_stats=True, display_plot=False)
rpc.dir_plot(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=True, display_stats=True, display_plot=False)
rpc.mag_vsr_plot(filter_data, max_mag=max_mag, max_bt_vel=max_bt_vel, display_text=True, display_stats=True, display_plot=False)
rpc.dir_vsr_plot(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=True, display_stats=True, display_plot=False)
rpc.display_mag_dir_plots()

# Amplitude
rpc.amp_b0(filter_data, display_text=False, display_stats=True, display_plot=False)
rpc.amp_b1(filter_data, display_text=False, display_stats=True, display_plot=False)
rpc.amp_b2(filter_data, display_text=False, display_stats=True, display_plot=False)
rpc.amp_b3(filter_data, display_text=False, display_stats=True, display_plot=False)
rpc.display_amp_plots()

# Correlation
rpc.corr_b0(filter_data, display_text=False, display_stats=True, display_plot=False)
rpc.corr_b1(filter_data, display_text=False, display_stats=True, display_plot=False)
rpc.corr_b2(filter_data, display_text=False, display_stats=True, display_plot=False)
rpc.corr_b3(filter_data, display_text=False, display_stats=True, display_plot=False)
rpc.display_corr_plots()

# Display all the plots in a single HTML
rpc.display_all_plots()
rpc.display_mag_dir_earth_corr_amp()

# Export the data to CSV
rpc.export_beam_to_csv(max_roll=max_roll)
rpc.export_instr_to_csv(max_roll=max_roll)
rpc.export_earth_to_csv(max_roll=max_roll)
rpc.export_mag_dir_to_csv(max_roll=max_roll)

