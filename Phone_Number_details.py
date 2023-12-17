# import phonenumbers
# from phonenumbers import timezone,geocoder,carrier
# Phone_Number = input("Enter Your Number With +__::")
# Phone = phonenumbers.parse(Phone_Number)
# time_1 = timezone.time_zones_for_number(Phone_Number)
# carrier__1 = carrier.name_for_number(Phone_Number,"en")
# # Pass en Because we got  a Output in english Language 
# reg = geocoder.description_for_number(Phone_Number,"en")
# print(f"The Phone Number is :: {Phone}")
# print(f" Time  :: {time_1}")
# print(f"The Phone Number is :: {carrier__1}")
# print(f"The Phone Number is :: {reg}")

import phonenumbers
from phonenumbers import timezone, geocoder, carrier

Phone_Number = input("Enter Your Number With +__::")
Phone = phonenumbers.parse(Phone_Number)
time_1 = timezone.time_zones_for_number(Phone)
carrier__1 = carrier.name_for_number(Phone, "en")
# Pass en Because we got an Output in the English Language
reg = geocoder.description_for_number(Phone, "en")

print(f"The Phone Number is :: {Phone}")
print(f" Time  :: {time_1}")
print(f"The Phone Number is :: {carrier__1}")
print(f"The Phone Number is :: {reg}")
