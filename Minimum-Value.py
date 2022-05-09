print('''This calculator was designed to help identify a minimum polling value to input into the HACS Govee Integration for Home Assistant. \n\nPlease use at your own risk. \n\n\n''')
devices = input ("How many Govee devices do you have? \n")

#constants
limit = 10000
seconds_per_day = 86400

#calculations
polling = int(devices) * seconds_per_day / limit
buffer_value = .5
buffer = int(polling) + int(polling) * float(buffer_value)
used_hits = int(seconds_per_day) / int(buffer) * int(devices)
remaining_hits = int(limit)-int(used_hits)

#output
print(f'''\n\nBased on the quantity of devices you own, your MINIMUM recommended polling amount should be no less than a value of: \n\n\n{int(buffer)}''')      
print(f'''\n\nThis value should provide a remaining available hit quantity of {int(remaining_hits)} out of {limit}.''')
print('\n\n\nGovee API Documentation can be found at: https://govee-public.s3.amazonaws.com/developer-docs/GoveeDeveloperAPIReference.pdf')
print('\nPlease visit https://github.com/LaggAt/hacs-govee to learn more.')
