import sys
import os
from nicegui import ui, app
import subprocess
# Add the backend folder to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '../backend'))
import generatorLite  # Now you can import it

# Global variable to store uploaded filename and labels
uploaded_filename = None
socket_label = None
amputation_label = None
limb_label = None
wrist_label = None
file_label = None

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
ui.label('Transradial Prosthetic Generator').style('color: #000000; font-size: 2rem; font-weight: bold; text-align: center; width: 100%;')

app.add_static_files('/backend', 'backend')

# Input section
# Create a row that centers its contents and fills the screen width
with ui.row().style('width: 100%; justify-content: center; margin: 0;'):
    with ui.row().style('width: 100%; max-width: 1200px; display: flex; gap: 1rem; align-items: start;'):
        with ui.column().style('flex: 1; max-width: 50%; padding: 20px; border: 1px solid #ddd; box-sizing: border-box; align-items: center;'):
            ui.label('Please upload your STL file').classes('title is-4').style('text-align: center; width: 100%;')
            uploaded_file = ui.upload(on_upload=lambda e: handle_file_upload(e), auto_upload=True).props('accept=.stl').style('width: 100%; max-width: 400px;')
            
            # Regular input fields for numeric values
            socket_length = ui.input(label='Socket Length (mm)', placeholder='Enter length in mm').style('width: 100%; max-width: 400px;')
            amputation_length = ui.input(label='Amputation Length (mm)', placeholder='Enter length in mm').style('width: 100%; max-width: 400px;')
            limb_length = ui.input(label='Ideal Limb Length (mm)', placeholder='Enter length in mm').style('width: 100%; max-width: 400px;')
            wrist_diameter = ui.input(label='Wrist Diameter (mm)', placeholder='Enter diameter in mm').style('width: 100%; max-width: 400px;')

            # ui.button('Generate', on_click=lambda: test(socket_length.value, amputation_length.value, limb_length.value, wrist_diameter.value)).classes('is-link')
            
            ui.button('Generate', on_click=lambda: openscadtest(socket_length.value, amputation_length.value, limb_length.value, wrist_diameter.value))

        with ui.column().style('flex: 1; max-width: 50%; padding: 20px; border: 1px solid #ddd; box-sizing: border-box; align-items: center;'):
            socket_label = ui.label().style('text-align: center; width: 100%;')
            amputation_label = ui.label().style('text-align: center; width: 100%;')
            limb_label = ui.label().style('text-align: center; width: 100%;')
            wrist_label = ui.label().style('text-align: center; width: 100%;')
            file_label = ui.label().style('text-align: center; width: 100%;')
            with ui.column().style('text-align: center; width: 100%; max-width: 400px; height: 300px;'):
                with ui.scene().classes('w-full h-64') as scene:
                    prosthetic = '/backend/result.stl'
                    scene.stl(prosthetic)

# Global variable to store uploaded filename
uploaded_filename = None

# Handle file upload
def handle_file_upload(event):
    global uploaded_filename
    # Access the single uploaded file directly
    file_name = event.name  # Get the uploaded file name
    file_extension = os.path.splitext(file_name)[1]  # Get the file extension
    
    # Copy the uploaded file to a new file
    new_file_name=copy_uploaded_file(event.content, file_name)
    uploaded_filename = new_file_name  # Store the full path
    
# Function to copy the uploaded STL file to a new file
def copy_uploaded_file(temp_file, original_file_name):
    new_file_name = os.path.join('backend', original_file_name)
    os.makedirs('backend', exist_ok=True)  # Ensure the backend directory exists
    with open(new_file_name, 'wb') as new_file:
        temp_file.seek(0)
        new_file.write(temp_file.read())
    print(f'Copied file to {new_file_name}')
    return new_file_name  # Return the full path

# # Define the function for the button click
# def process_inputs_and_display(arm_file_element, lengthSocket, lengthAmputation, lengthFullLimb, wristDiam):
#     global socket_label, amputation_label, limb_label, wrist_label, file_label
#     try:
#         socket_label.set_text(f'Socket Length: {lengthSocket} mm')
#         amputation_label.set_text(f'Amputation Length: {lengthAmputation} mm')
#         limb_label.set_text(f'Full Limb Length: {lengthFullLimb} mm')
#         wrist_label.set_text(f'Wrist Diameter: {wristDiam} mm')
#         file_label.set_text(f"Generated output based on {os.path.basename(arm_file_element)}")
#     except ValueError:
#         socket_label.set_text('Please enter valid numeric values.')
        
def openscadtest(socket_length_value, amputation_length_value, limb_length_value, wrist_diameter_value):
    try:
        # Get user input values
        socket_length = float(socket_length_value)
        amputation_length = float(amputation_length_value)
        limb_length = float(limb_length_value)
        wrist_diameter = float(wrist_diameter_value)

        if uploaded_filename is None:
            print("No STL file uploaded.")
            return

        # Run the test function from generatorLite
        lengthSocket, lengthAmputation, lengthFullLimb, wristDiam, arm_file_element = generatorLite.test(
            uploaded_filename, socket_length, amputation_length, limb_length, wrist_diameter
        )
    
        # Update UI labels
        socket_label.set_text(f'Socket Length: {lengthSocket} mm')
        amputation_label.set_text(f'Amputation Length: {lengthAmputation} mm')
        limb_label.set_text(f'Full Limb Length: {lengthFullLimb} mm')
        wrist_label.set_text(f'Wrist Diameter: {wristDiam} mm')
        file_label.set_text(f"Generated output based on {os.path.basename(arm_file_element)}")

    except ValueError:
        socket_label.set_text('Please enter valid numeric values.')
    except Exception as e:
        print(f"An error occurred: {e}")


# Start the NiceGUI app
ui.run()