import os
from nicegui import ui, app
import subprocess

# Print current directory and list files
print("Current Directory:", os.getcwd())
print("Files in Directory:", os.listdir('.'))

ui.add_head_html("""
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css">
    <title>ShapeShift Prosthetics HackNC2024</title>
""")

# Include Bulma CSS and your local style.css
ui.add_css('''
.top-nav {
    background-color: #0B1932;
    overflow: hidden;
}

.nav-image {
    width: 300px;
}

.large {
    font-size: 4rem;
}

#banner {
    position: relative;
    width: 100%;
    overflow: hidden;
    color: black;
    /* Text color for better contrast */
}

.img-background {
    position: absolute;
    top: 0;
    left: 0;
    min-width: 100%;
    min-height: 100%;
    height: auto;
    width: auto;
    object-fit: cover;
    z-index: -1;
}

#banner .column {
    position: relative;
    /* Required to overlay the image */
    z-index: 1;
    /* Ensures text is above the background image */
}

label {
    display: block;
    margin: 0.4rem 0; /* Optional margin for spacing */
}

input[type="file"] {
    display: block; /* Ensures the input is block-level */
    margin-top: 0.4rem; /* Optional space between label and input */
}

.background-color {
    background-color: #0B1932;
}
''')

with ui.header(elevated=True).style('background-color: #0B1932').classes('top-nav'):
        ui.image('images/logo.png').classes('nav-image')

# Title and Introduction
with ui.column().classes('pt-4'):
    ui.label('Making prosthetics accessible, customizable, and affordable through the power of 3D printing technology').style('color: #000000; font-size: 3rem; font-weight: 300')
    ui.label('By streamlining the design and fabrication process, ShapeShift enables users to create tailored prosthetic limbs that meet specific needs, fit comfortably, and enhance mobility. Whether for individuals, clinics, or support organizations, ShapeShift provides an intuitive platform where anyone can generate high-quality, lightweight prosthetics in a fraction of the traditional time and cost. Our mission is to empower users with tools that transform lives, combining digital design and physical production to reshape prosthetics for a modern age.').style('color: #000000; font-size: 1rem; font-weight: 300')

# Transradial Generator Section
with ui.column().classes('pt-4 has-text-centered'):
    ui.label('Transradial Generator').style('color: #000000;').classes('has-text-centered is-size-3')

# Input section
with ui.row().classes('pt-4'):
    with ui.column().classes('px-6'):
        ui.label('Please upload your STL file')
        uploaded_file = ui.upload(on_upload=lambda e: handle_file_upload(e), auto_upload=True).props('accept=.stl')
        
        # Regular input fields for numeric values
        socket_length = ui.input(label='Socket Length (mm)', placeholder='Enter length in mm')
        amputation_length = ui.input(label='Amputation Length (mm)', placeholder='Enter length in mm')
        limb_length = ui.input(label='Ideal Limb Length (mm)', placeholder='Enter length in mm')
        wrist_diameter = ui.input(label='Wrist Diameter (mm)', placeholder='Enter diameter in mm')

        # ui.button('Generate', on_click=lambda: test(socket_length.value, amputation_length.value, limb_length.value, wrist_diameter.value)).classes('is-link')
        
        ui.button('Generate', on_click=lambda: openscadtest())

    with ui.column().classes('px-6'):
        socket_label = ui.label()
        amputation_label = ui.label()
        limb_label = ui.label()
        wrist_label = ui.label()
        file_label = ui.label()

# Handle file upload
def handle_file_upload(event):
    # Access the single uploaded file directly
    file_name = event.name  # Get the uploaded file name
    file_extension = os.path.splitext(file_name)  # Get the file extension
    
    # Copy the uploaded file to a new file
    copy_uploaded_file(file_extension['data'], file_name)
    
# Function to copy the uploaded STL file to a new file
def copy_uploaded_file(data, original_file_name):
    new_file_name = f"{original_file_name}"  # Specify the new file name
    with open(new_file_name, 'wb') as new_file:  # Open new file in write-binary mode
        new_file.write(data)  # Write the uploaded file data to the new file
    print(f'Copied file to {new_file_name}')  # Print a message to confirm the copy

# Define the function for the button click
def test(socket_length_value, amputation_length_value, limb_length_value, wrist_diameter_value):
    try:
        # Convert input values to float and update labels
        lengthSocket = float(socket_length_value)
        lengthAmputation = float(amputation_length_value)
        lengthFullLimb = float(limb_length_value)
        wristDiam = float(wrist_diameter_value)

        socket_label.set_text(f'Socket Length: {lengthSocket} mm')
        amputation_label.set_text(f'Amputation Length: {lengthAmputation} mm')
        limb_label.set_text(f'Full Limb Length: {lengthFullLimb} mm')
        wrist_label.set_text(f'Wrist Diameter: {wristDiam} mm')
    except ValueError:
        socket_label.set_text('Please enter valid numeric values.')
        
def openscadtest():
    try:
            result = subprocess.run(
                ["openscad", "--enable","all", "-o", "output.stl", "ReneeGardnerBaseScan.scad"],
                check=True,
                capture_output=True,
                text=True
            )
            print("OpenSCAD Output:", result.stdout)
            print("OpenSCAD Errors:", result.stderr)
    except subprocess.CalledProcessError as e:
            print("An error occurred:", e)
            print("Return code:", e.returncode)
            print("Output:", e.output)
            print("Error output:", e.stderr)


# Start the NiceGUI app
ui.run()