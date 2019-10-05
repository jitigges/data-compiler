import json
import os
import os.path
#https://stackoverflow.com/questions/12994442/how-to-append-data-to-a-json-file
#Link above tells you what the function below does in more detail...
def append_to_json(_dict,path): 
    with open(path, 'ab+') as f:
        f.seek(0,2)                                #Go to the end of file    
        if f.tell() == 0 :                         #Check if file is empty
            f.write(json.dumps([_dict],indent = 4).encode())  #If empty, write an array
        else :
            f.seek(-1,2)
            f.truncate()
            f.seek(-1,2)         
            f.truncate()                           #Remove the last character, open the array
            f.write(' , '.encode())                #Write the separator
            f.write(json.dumps(_dict,indent = 4).encode())    #Dump the dictionary
            f.write(']}'.encode())                  #Close the array
def append(_dict,path): 
    with open(path, 'ab+') as f:
        f.seek(0,2)                                #Go to the end of file    
        if f.tell() == 0 :                         #Check if file is empty
           f.write(json.dumps([_dict],indent = 4).encode())  #If empty, write an array
        else :   
           f.seek(-1,2)         
           f.truncate()                           #Remove the last character, open the array
           f.write('},'.encode())                #Write the separator
           f.write(json.dumps(_dict,indent = 4).encode())    #Dump the dictionary
while True:
  if os.path.exists("C:\Program Files\PC\compile.json"):
    os.remove("C:\Program Files\PC\compile.json")
  else:
    pass
  with open("C:\Program Files\PC\JSONFiles\\ase.json",'r') as infile:
    first = json.load(infile)
    append(first,"C:\Program Files\PC\compile.json")
    with open("C:\Program Files\PC\compile.json",'ab+') as f:
     f.seek(-1,2)
     f.truncate()
     f.seek(-1,2)
     f.truncate()
  with open("C:\Program Files\PC\JSONFiles\wifi.json",'r') as infile:
    load = json.load(infile)
    append(load,"C:\Program Files\PC\compile.json")
  with open("C:\Program Files\PC\JSONFiles\solid.json",'r') as infile:
    load = json.load(infile)
    append(load,"C:\Program Files\PC\compile.json")
  with open("C:\Program Files\PC\JSONFiles\RAM.json",'r') as infile:
    load = json.load(infile)
    append(load,"C:\Program Files\PC\compile.json")
  with open("C:\Program Files\PC\JSONFiles\processor.json",'r') as infile:
    load = json.load(infile)
    append(load,"C:\Program Files\PC\compile.json")
  with open("C:\Program Files\PC\JSONFiles\powersupply.json",'r') as infile:
    load = json.load(infile)
    append(load,"C:\Program Files\PC\compile.json")
  with open("C:\Program Files\PC\JSONFiles\motherboard.json",'r') as infile:
    load = json.load(infile)
    append(load,"C:\Program Files\PC\compile.json")
  with open("C:\Program Files\PC\JSONFiles\HDD.json",'r') as infile:
    load = json.load(infile)
    append(load,"C:\Program Files\PC\compile.json")
  with open("C:\Program Files\PC\JSONFiles\GPU.json",'r') as infile:
    load = json.load(infile)
    append(load,"C:\Program Files\PC\compile.json")
  with open("C:\Program Files\PC\compile.json", 'ab+') as outfile:
    outfile.seek(0,2)
    outfile.truncate()
    outfile.seek(0,2)
    outfile.write(']'.encode())    
  component_ask = raw_input("What component do you want added? PSU/MOBO/CPU/RAM/CASE/WIFI/GPU/HDD/SDD: ").upper()
  if component_ask == "CPU":
    maker = raw_input("Manufacturer: ").lower()
    model = raw_input("Model: ").lower()
    clockspeed = raw_input("Clockspeed: ").lower()
    cores = raw_input("Cores: ").lower()
    price = raw_input("Price: ").lovwer()
    graphics = raw_input("Integrated GPU? If none then leave blank: ").lower()

    CPU = {
    "maker":maker, 
    "model":model,
    "clockspeed":clockspeed,
    "cores":cores,
    "price":price,
    "graphics":graphics
    }
    processor_path = "C:\Program Files\PC\JSONFiles\processor.json"
    append_to_json(CPU,processor_path)
  elif component_ask == "PSU":
    maker = raw_input("Manufacturer: ").lower()
    model = raw_input("Model: ").lower()
    wattage = raw_input("Wattage: ").lower()
    type_ = raw_input("Type: ").lower()
    certificate = raw_input("Certification: ").lower()
    price = raw_input("Price: ").lower()

    PSU = {
    "maker":maker, 
    "model":model,
    "wattage":wattage,
    "Type":type_,
    "certificate":certificate,
    "price":price,
    }
    processor_path = "C:\Program Files\PC\JSONFiles\powersupply.json"
    append_to_json(PSU,processor_path)
  elif component_ask == "MOBO":
    maker = raw_input("Manufacturer: ").lower()
    model = raw_input("Model: ").lower()
    size = raw_input("Form Factor: ").lower()
    socket = raw_input("socket: ").lower()
    chipset = raw_input("Chipset: ").lower()
    wifi = raw_input("Wi-Fi: ").lower()
    RAM = raw_input("RAM Slots: ").lower()
    price = raw_input("Price: ").lower()
    memorytype = raw_input("Memory Type: ").lower()
    m2slots = raw_input("M.2 Slots: ").lower()
    RAID = raw_input("RAID Support? True/False: ").lower()

    MOBO = {
       "price":price,
       "model":model,
       "maker":maker,
       "formfactor":size,
       "socket":socket,
       "chipset":chipset,
       "wifi":wifi,
       "RAM_slots":RAM,
       "MemoryType":memorytype,
       "m2slots":m2slots,
       "RAID-support":RAID,
     }
    processor_path = "C:\Program Files\PC\JSONFiles\motherboard.json"
    append_to_json(MOBO,processor_path)
  elif component_ask == "RAM":
    maker = raw_input("Manufacturer: ").lower()
    model = raw_input("Model: ").lower()
    speed = raw_input("Speed: ").lower()
    modules = raw_input("Modules: ").lower()
    color = raw_input("Color: ").lower()
    size = raw_input("Size: ").lower()
    price = raw_input("Price: ").lower()
    RAM = {
       "price":price,
       "model":model,
       "maker":maker,
       "speed":speed,
       "size":size,
       "modules":modules,
       "color":color,
     }
    processor_path = "C:\Program Files\PC\JSONFiles\RAM.json"
    append_to_json(RAM,processor_path)
  elif component_ask == "CASE":
    maker = raw_input("Manufacturer: ").lower()
    model = raw_input("Model: ").lower()
    RGB = raw_input("RGB: ").lower()
    glass = raw_input("Tempered Glass (T/F): ")
    watercooling = raw_input("Water Cooling Support (T/F): ").lower()
    gpumax = raw_input("GPU Max Size: ").lower()
    psu = raw_input("Comes with PSU (T/F): ").lower()
    usb = raw_input("Supports what type of USB: ").lower()
    internal25 = raw_input('Internal 2.5" Bays: ').lower()
    internal35 = raw_input('Internal 3.5" Bays: ').lower()
    psushroud = raw_input("Power Supply Shroud: ").lower()
    color = raw_input("Color: ").lower()
    size = raw_input("Case supports what MOBO Sizes: ").lower()
    price = raw_input("Price: ").lower()
    case = {
       "price":price,
       "model":model,
       "maker":maker,
       "RGB":RGB,
       "size":size,
       "tempglass":glass,
       "color":color,
       "watercooling":watercooling,
       "gpumax":gpumax,
       "psu":psu,
       "usb":usb,
       "internal25":internal25,
       "internal35":internal35,
       "PSUshroud":psushroud,
     }
    processor_path = "C:\Program Files\PC\JSONFiles\ase.json"
    append_to_json(case,processor_path)
  elif component_ask == "WIFI":
    maker = raw_input("Manufacturer: ").lower()
    model = raw_input("Model: ").lower()
    protocol = raw_input("Protocol: ").lower()
    interface = raw_input("Interface: ").lower()
    price = raw_input("Price: ").lower()
    WIFI = {
       "price":price,
       "model":model,
       "maker":maker,
       "protocol":protocol,
       "interface":interface,
     }
    processor_path = "C:\Program Files\PC\JSONFiles\wifi.json"
    append_to_json(WIFI,processor_path)
  elif component_ask == "GPU":
    maker = raw_input("Manufacturer: ").lower()
    model = raw_input("Model: ").lower()
    chipset = raw_input("Chipset: ").lower()
    coreclock = raw_input("Core Clock: ").lower()
    boostclock = raw_input("Boost Clock: ").lower()
    color = raw_input("Color: ").lower()
    length = raw_input("Length: ").lower()
    dviports = raw_input("DVI Ports: ").lower()
    hdmiports = raw_input("HDMI Ports: ").lower()
    displayports = raw_input("DisplayPort Ports: ").lower()
    cooling = raw_input ("Cooling: ").lower()
    externalpower = raw_input ("External Power: ").lower()
    slicrossfire = raw_input("SLI/Crossfire: ").lower()
    tdp = raw_input("Thermal Design Power: ").lower()
    framesync = raw_input("Frame Sync: ").lower()
    memoryclock = raw_input("Effective Memory Clock: ").lower()
    interface = raw_input("Interface: ").lower()
    memorytype = raw_input("Memory Type: ").lower()
    price = raw_input("Price: ").lower()
    GPU = {
       "price":price,
       "model":model,
       "maker":maker,
       "chipset":chipset,
       "coreclock":coreclock,
       "boostclock":boostclock,
       "color":color,
       "length":length,
       "dviports":dviports,
       "hdmiports":hdmiports,
       "displayports":displayports,
       "cooling":cooling,
       "externalpower":externalpower,
       "slicrossfire":slicrossfire,
       "tdp":tdp,
       "framesync":framesync,
       "memoryclock":memoryclock,
       "interface":interface,
       "memorytype":memorytype,
     }
    processor_path = "C:\Program Files\PC\JSONFiles\GPU.json"
    append_to_json(GPU,processor_path)
  elif component_ask == "HDD":
    maker = raw_input("Manufacturer: ").lower()
    model = raw_input("Model: ").lower()
    capacity = raw_input("Capacity: ").lower()
    type_ = raw_input("Type: ").lower()
    cache = raw_input("Cache: ").lower()
    formfactor = raw_input("Form Factor: ").lower()
    interface = raw_input("Interface: ").lower()
    price = raw_input("Price: ").lower()
    HDD = {
       "price":price,
       "model":model,
       "maker":maker,
       "interface":interface,
       "capacity":capacity,
       "type":type_,
       "cache":cache,
       "formfactor":formfactor,
     }
    processor_path = "C:\Program Files\PC\JSONFiles\HDD.json"
    append_to_json(HDD,processor_path)
  elif component_ask == "SSD":
    maker = raw_input("Manufacturer: ").lower()
    model = raw_input("Model: ").lower()
    capacity = raw_input("Capacity: ").lower()
    cache = raw_input("Cache: ").lower()
    formfactor = raw_input("Form Factor: ").lower()
    interface = raw_input("Interface: ").lower()
    nvme = raw_input("NVMe (T/F): ").lower()
    price = raw_input("Price: ").lower()
    ssd = {
       "price":price,
       "model":model,
       "maker":maker,
       "interface":interface,
       "capacity":capacity,
       "cache":cache,
       "formfactor":formfactor,
       "NVME":nvme
    }
    processor_path = "C:\Program Files\PC\JSONFiles\solid.json"
    append_to_json(ssd,processor_path)
  else:
    print("Component not Found... Try again...")