# date
extension_csv = '.csv'
extension_ane = '.ane'

day_date_main = '07-09-67'
day_date_sub = '07.09'

# =================== input =================== #

n_door = 'Door_07-09-2024_180143'
n_window = 'Window_07-09-2024_180103'
n_center = 'Center_07-09-2024_180123'

n_dht = 'DHT22_07-09-2024_175921'

wind_door = 'door-backup-7.9.2'
wind_window = 'window-backup-7.9.2'

ips_door_path = f'{day_date_main}/{n_door}{extension_csv}'
ips_window_path = f'{day_date_main}/{n_window}{extension_csv}'
ips_center_path = f'{day_date_main}/{n_center}{extension_csv}'
dht22_path = f'{day_date_main}/{n_dht}{extension_csv}'

speed_wind_door = f'{day_date_main}/{day_date_sub}/{wind_door}{extension_ane}'
speed_wind_window = f'{day_date_main}/{day_date_sub}/{wind_window}{extension_ane}'

# ============================================= #

# =================== output =================== #

n_wind_door = '!door_wind_speed_'
n_wind_window = '!window_wind_speed_'

wind_door_path_out = f'{day_date_main}/{n_wind_door}{day_date_sub}{extension_csv}'
wind_window_path_out = f'{day_date_main}/{n_wind_window}{day_date_sub}{extension_csv}'

data_path_out = f'data_combine/{day_date_sub}/combine_data_{day_date_sub}{extension_csv}'
wind_path_out = f'data_combine/{day_date_sub}/combine_wind_{day_date_sub}{extension_csv}'
finish_path_out = f'data_combine/{day_date_sub}/!Finish_data_{day_date_sub}{extension_csv}'

# ============================================== #