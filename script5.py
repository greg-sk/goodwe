#!/usr/bin/python 

import asyncio
import goodwe
from goodwe.et import ET


async def get_runtime_data():
    ip_address = '10.10.100.253'

    comm_addr = 0
    timeout = 1
    retries = 3

    inverter = ET(ip_address, comm_addr, timeout, retries)
    #inverter = await goodwe.connect(ip_address)
    runtime_data = await inverter.read_runtime_data()

    for sensor in inverter.sensors():
        if sensor.id_ in runtime_data:
            #print(f"{sensor.id_}: {sensor.name} = {runtime_data[sensor.id_]} {sensor.unit}")
            print("%-30s%6s %-5s%s"%(sensor.id_+':', runtime_data[sensor.id_], sensor.unit, sensor.name))


asyncio.run(get_runtime_data())

