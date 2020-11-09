# Importing module
import platform

# Initializing a dictionary
info = {}

# Fetching platform details
platform_details = platform.platform()
system_name = platform.system()
processor_name = platform.processor()
architecture_details = platform.architecture()

# Add and append to the dictionary
info["Platform Details"] = platform_details
info["System Name"] = system_name
info["Processor Name"] = processor_name
info["Architecture Details"] = architecture_details

# Printing out the result
for i, j in info.items():
    print(i, "\t-\t", j)
