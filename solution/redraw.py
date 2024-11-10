import pyshark
import matplotlib.pyplot as plt

fig_width = 24
fig_height = 1

x_values = []
y_values = []

capture = pyshark.FileCapture(
    'record.pcapng',
    display_filter='usb.src == "1.9.2" && usb.transfer_type == 0x01',
    use_json=True,
    include_raw=True
)

for packet in capture:
    raw_data = bytes.fromhex(packet.get_raw_packet().hex())

    if len(raw_data) >= 34:
        x_axis = int.from_bytes(raw_data[29:31], byteorder='little')
        y_axis = int.from_bytes(raw_data[31:33], byteorder='little')
        pressure = int.from_bytes(raw_data[33:35], byteorder='little')

        if pressure > 0:
            x_values.append(x_axis)
            y_values.append(y_axis)
    else:
        print("Packet too short to contain all required bytes.")

if x_values and y_values:
    plt.figure(figsize=(fig_width, fig_height))
    plt.scatter(x_values, y_values, marker='o')
    plt.gca().invert_yaxis()
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Drawing from Tablet Data')
    plt.show()
else:
    print("No data with pressure > 0 was collected.")
