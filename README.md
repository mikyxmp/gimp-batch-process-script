# GIMP Batch Process Script

This Python script is designed to automate the batch processing of PNG images using GIMP. It applies a series of image manipulations—such as Gaussian Blur, Thresholding, Despeckling, and Erosion—to enhance the images. The script also crops each image to a specified size with custom positioning, making it ideal for repetitive image processing tasks.

## Features
- **Batch Processing**: Automatically processes all PNG images in a selected input folder.
- **Image Enhancements**: Applies Gaussian Blur, Threshold, Despeckling, and Erosion filters to improve image quality.
- **Custom Cropping**: Crops each image to 1700x1400 pixels with a specified vertical offset.
- **Flexible Output**: Saves the processed images in a user-defined output folder with a `_gimp.png` suffix.

## Prerequisites
Before using this script, ensure you have the following installed:

- **GIMP 2.10 or later**: The script relies on GIMP’s Python-Fu plug-in.
- **Python 2.x or 3.x**: GIMP’s Python-Fu requires Python to execute scripts.

## Installation
1. **Download the Script**: Clone or download the script to your local machine.
   ```bash
   git clone https://github.com/mikyxmp/gimp-batch-process-script.git

### Move to GIMP Plug-ins Folder:
Copy the `batch_process_images.py` script to your GIMP plug-ins directory:

- **On Windows**: `C:\Users\<YourUsername>\AppData\Roaming\GIMP\2.10\plug-ins\`
- **On macOS**: `~/Library/Application Support/GIMP/2.10/plug-ins/`
- **On Linux**: `~/.config/GIMP/2.10/plug-ins/`

### Restart GIMP:
If GIMP is already running, restart it to load the new script.

## Usage

### Run the Script:
- Open GIMP and go to `Filters > MyScripts > Batch Process Images`.

### Select Folders:
- You will be prompted to select the input folder containing the PNG images you want to process.
- After selecting the input folder, you’ll be prompted to select an output folder where the processed images will be saved.

### Processing:
- The script will process each PNG image in the input folder and save the modified images with a `_gimp.png` suffix in the output folder.
- A message will be displayed if no input or output folder is selected.

## Example Workflow
1. Prepare a folder of PNG images you wish to enhance.
2. Run the script from GIMP and select the prepared folder as the input.
3. Choose a destination folder for the processed images.
4. Let the script run, and the processed images will appear in the output folder.

## Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to create an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
Special thanks to the GIMP development community for providing an open platform that enables such powerful customizations.


   ### Key Changes:
- **Headings**: I added `#` symbols to create headings for each section.
- **Lists**: Features and prerequisites are now properly formatted as bulleted lists.
- **Code Blocks**: The installation command is placed inside a code block using triple backticks (\`\`\`) with the `bash` language specifier.
- **Bold Text**: Important terms like "Batch Processing" and "GIMP 2.10 or later" are bolded for emphasis.

This formatting ensures that the text will be displayed correctly on GitHub, with proper styling and structure.

