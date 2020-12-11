from tqdm import tqdm
from rti_python.Utilities.read_plot_csv import ReadPlotCSV


# ***********************************
# Take the absolute value of the value and compare to the absolute value of this filter.
# If it is greater, then set the value to NaN

max_roll = 160.0                        # Roll is +/-180 for downward and 0 for upward
max_vel = 2.0                           # Maximum velocity +/- for beam, instrument and earth.
max_bt_vel = 1.0                        # Maximum bottom track velocity +/-
max_mag = 3.0                           # Maximum magnitude value +/-

# Filter directly from the data query from the sqlite file
# These ensembles will not be included in the dataset at all
filter_data = "WHERE ensembles.roll > " + str(max_roll) + " OR ensembles.roll < -" + str(max_roll)
# ************************************

# Progress Bar
pbar = tqdm(total=45)

# Create the object to read, process, plot and export to csv
rpc = ReadPlotCSV()
pbar.update(1)

# Select the file and process the data to a DB file
# If raw binary files are selectecd, they will be converted to a SQLite DB file
rpc.select_and_process()
pbar.update(1)

"""
# Beam Velocity
rpc.beam_0_vel(filter_data, max_vel=max_vel, display_text=False, display_stats=False, display_plot=False)
pbar.update(1)
rpc.beam_0_vel_remove_ship(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
pbar.update(1)
rpc.beam_1_vel(filter_data, max_vel=max_vel, display_text=False, display_stats=False, display_plot=False)
pbar.update(1)
rpc.beam_1_vel_remove_ship(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
pbar.update(1)
rpc.beam_2_vel(filter_data, max_vel=max_vel, display_text=False, display_stats=False, display_plot=False)
pbar.update(1)
rpc.beam_2_vel_remove_ship(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
pbar.update(1)
rpc.beam_3_vel(filter_data, max_vel=max_vel, display_text=False, display_stats=False, display_plot=False)
pbar.update(1)
rpc.beam_3_vel_remove_ship(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
pbar.update(1)
rpc.display_beam_vel_plots()
pbar.update(1)

# Instrument Velocity
rpc.intr_x_vel_remove_ship(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
pbar.update(1)
rpc.intr_y_vel_remove_ship(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
pbar.update(1)
rpc.intr_z_vel_remove_ship(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
pbar.update(1)
rpc.intr_err_vel_remove_ship(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
pbar.update(1)
rpc.display_instr_vel_plots()
pbar.update(1)

# Earth Velocity
rpc.earth_east_vel(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
pbar.update(1)
rpc.earth_north_vel(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
pbar.update(1)
rpc.earth_vert_vel(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
pbar.update(1)
rpc.earth_east_vel_remove_ship(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
pbar.update(1)
rpc.earth_north_vel_remove_ship(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
pbar.update(1)
rpc.earth_vert_vel_remove_ship(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=False, display_stats=True, display_plot=False)
pbar.update(1)
rpc.display_earth_vel_plots()
pbar.update(1)
rpc.display_earth_vel_raw_vsr_plots()
pbar.update(1)

# Magnitude and Direction
rpc.mag_plot(filter_data, max_mag=max_mag, max_bt_vel=max_bt_vel, display_text=True, display_stats=True, display_plot=False)
pbar.update(1)
rpc.dir_plot(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=True, display_stats=True, display_plot=False)
pbar.update(1)
rpc.mag_vsr_plot(filter_data, max_mag=max_mag, max_bt_vel=max_bt_vel, display_text=True, display_stats=True, display_plot=False)
pbar.update(1)
rpc.dir_vsr_plot(filter_data, max_vel=max_vel, max_bt_vel=max_bt_vel, display_text=True, display_stats=True, display_plot=False)
pbar.update(1)
rpc.display_mag_dir_plots()
pbar.update(1)

# Amplitude
rpc.amp_b0(filter_data, display_text=False, display_stats=True, display_plot=False)
pbar.update(1)
rpc.amp_b1(filter_data, display_text=False, display_stats=True, display_plot=False)
pbar.update(1)
rpc.amp_b2(filter_data, display_text=False, display_stats=True, display_plot=False)
pbar.update(1)
rpc.amp_b3(filter_data, display_text=False, display_stats=True, display_plot=False)
pbar.update(1)
rpc.display_amp_plots()
pbar.update(1)

# Correlation
rpc.corr_b0(filter_data, display_text=False, display_stats=True, display_plot=False)
pbar.update(1)
rpc.corr_b1(filter_data, display_text=False, display_stats=True, display_plot=False)
pbar.update(1)
rpc.corr_b2(filter_data, display_text=False, display_stats=True, display_plot=False)
pbar.update(1)
rpc.corr_b3(filter_data, display_text=False, display_stats=True, display_plot=False)
pbar.update(1)
rpc.display_corr_plots()
pbar.update(1)

# Display all the plots in a single HTML
rpc.display_all_plots()
pbar.update(1)
rpc.display_mag_dir_earth_corr_amp()
pbar.update(1)


# Export the data to CSV
rpc.export_beam_to_csv(max_roll=max_roll)
pbar.update(1)
rpc.export_instr_to_csv(max_roll=max_roll)
pbar.update(1)
rpc.export_earth_to_csv(max_roll=max_roll)
pbar.update(1)
rpc.export_mag_dir_to_csv(max_roll=max_roll)
pbar.update(1)
"""
rpc.export_avg_depth_vel_dist_travel_to_csv(max_roll=max_roll)
pbar.update(1)

pbar.close()
