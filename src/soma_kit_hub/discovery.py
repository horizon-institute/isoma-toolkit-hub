from bleak import BleakScanner

SK_SERVICE_UUID = "aa4a4abe-1bf2-45c2-bb97-08eaa6afbcb7"

async def discover_devices():
    results = []
    for d in await BleakScanner.discover(service_uuids=[SK_SERVICE_UUID], return_adv=True):
        results.append(str(d))
    return results
