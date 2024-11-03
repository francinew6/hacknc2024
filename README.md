# ShapeShift Prosthetics HackNC2024

## **Inspiration**

## **What it does**
Users seeking an arm prosthesis can easily upload a scan of their arm and provide key measurements of their current and desired limb dimensions. Based on these inputs, the platform will design and generate a customized arm and hand prosthetic file, ready for the user to 3D print.

## **How we built it**
ShapeShift was developed using a robust technology stack, including Python, NiceGUI, and OpenSCAD. The frontend leverages NiceGUI's Python-based UI framework, enabling seamless integration of Python functions directly into the user interface, creating a responsive and intuitive web experience. The backend is powered by Python, which orchestrates the generation of 3D models by interfacing with OpenSCAD. This architecture allows for efficient processing of user inputs to create customized prosthetic designs that are readily accessible for 3D printing.

## **Challenges we ran into**
We encountered several challenges during the development of ShapeShift:

- **Technical Limitations of PyScript and Pyodide:** Our initial approach involved building the website with HTML, CSS, JavaScript, and PyScript to facilitate Python integration. However, we soon discovered that PyScript and Pyodide could not support OpenSCAD or other essential modules required for our backend 3D model generator. This limitation led us to pivot our approach and explore alternative methods to meet our project’s requirements.
- **Complexity of 3D Modeling:** Generating an accurate and functional 3D model of an arm from the uploaded scan was a detailed and intricate task. It required meticulous work to analyze and plot the various data points from the scan, and then construct a solid, anatomically appropriate arm model around them. This step was both time-consuming and technically demanding, as we aimed to create a prosthetic that was both accurate and customizable.
- **Rapid Learning and Implementation of NiceGUI:** Integrating NiceGUI into our project involved a steep learning curve, as we had to familiarize ourselves with the framework while simultaneously building the application. Due to limited and sometimes unclear documentation, we often found ourselves embarking on extensive research efforts to uncover critical details about NiceGUI’s capabilities. Despite these challenges, we were able to effectively leverage the framework for a seamless user interface.
Each of these challenges required adaptability, problem-solving, and perseverance, and overcoming them was essential to successfully bringing ShapeShift to life.

## **Accomplishments that we're proud of**
We're thrilled to have brought ShapeShift to life with just two people, 24 hours, and a whole lot of determination! From the ground up, we built the entire frontend and backend of the website, tackling each line of code from scratch. We’re especially proud of mastering NiceGUI in record time—even when the documentation left a lot to be desired! This project has been an exciting, fast-paced journey, and we're proud of what we accomplished in such a short period.

## **What we learned**
Along the way, we picked up some valuable lessons (and a few battle scars):

- **Mastering Collaboration with Git:** We honed our skills in collaborative coding, learning the ins and outs of Git to keep our work synchronized. Nothing says teamwork like navigating branch merges together!
- **Becoming Merge Conflict Pros 😬:** Merge conflicts became an inevitable (and often unexpected) part of our journey. We quickly learned how to resolve them—sometimes gracefully, sometimes through sheer perseverance—but each one brought us closer as collaborators!
- **Delving into the World of NiceGUI, Three.js, and Quasar:** NiceGUI came with its own set of quirks and hidden treasures. We uncovered its use of three.js for 3D rendering and Quasar components for UI, gaining a whole new appreciation for the intricate layers powering our interface.
- **Getting Up Close and Personal with OpenSCAD and Python:** By working with OpenSCAD and Python, we developed a deeper, almost “behind-the-scenes” understanding of these tools. From generating precise 3D models to tweaking tiny details in code, we now know them like old friends.
Every lesson, from Git mastery to NiceGUI’s hidden gems, has left us better equipped, more skilled, and with a few new tricks up our sleeves for future projects!

## **What's next for ShapeShift Prosthetics**
Future developments will include a comprehensive resources section, where users can browse and download a variety of specialized hand attachment files tailored to their specific needs. This feature will offer free access to attachments designed to enhance functionality in various activities—whether it's a grip designed for cycling, a bow holder for playing the violin, or other customized tools to support daily tasks and hobbies. By expanding the range of available attachments, we aim to empower users to further personalize their prosthetic experience, enabling greater independence and engagement in diverse activities.
