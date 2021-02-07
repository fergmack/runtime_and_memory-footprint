!pip install memory_profiler

# The get_publisher_heroes() function and get_publisher_heroes_np() function should be saved within a file titled hero_funcs.py
# (i.e., you can import both functions from hero_funcs). 

%load_ext memory_profiler

%mprun -f convert_units convert_units(heroes, hts, wts)
