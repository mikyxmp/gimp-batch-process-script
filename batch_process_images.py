import os
from gimpfu import *

def batch_process_images():  # No arguments needed
    # Prompt the user to select the input and output folders
    input_folder = pdb.gimp_file_select_folder("Select Input Folder", "")
    output_folder = pdb.gimp_file_select_folder("Select Output Folder", "")
    
    if not input_folder or not output_folder:
        pdb.gimp_message("Input or Output folder not selected. Aborting operation.")
        return

    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            # Construct the full file path
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + "_gimp.png"
            output_path = os.path.join(output_folder, output_filename)
            
            # Load the image
            image = pdb.gimp_file_load(input_path, input_path)
            drawable = pdb.gimp_image_get_active_layer(image)
            
            # Apply Despeckle
            pdb.plug_in_despeckle(image, drawable, 14, 10, 1, 248)
            # Apply Gaussian Blur
            pdb.plug_in_gauss(image, drawable, 1.0, 1.0, 0)
            # Apply Threshold
            pdb.gimp_threshold(drawable, 255, 255)
            # Apply Erode
            pdb.plug_in_erode(image, drawable, 1, 0, 1, 15, 0, 255)
            # Apply Despeckle again
            pdb.plug_in_despeckle(image, drawable, 14, 10, 1, 248)

            # Calculate the crop area (1700x1700 square)
            width = 1700
            height = 1400
            original_width = pdb.gimp_image_width(image)
            original_height = pdb.gimp_image_height(image)

            # Calculate the crop position (center with a vertical offset of 250px)
            offset_x = (original_width - width) // 2
            offset_y = (original_height - height) // 2 - 100

            # Crop the image to 1700x1700 pixels
            pdb.gimp_image_crop(image, width, height, offset_x, offset_y)

            # Save the modified image
            pdb.file_png_save(image, drawable, output_path, output_path, 0, 9, 1, 1, 1, 1, 1)
            
            # Clean up
            pdb.gimp_image_delete(image)

# Register the script in GIMP
register(
    "python_fu_batch_process_images",
    "Batch process PNG images with Gaussian Blur and Threshold",
    "Applies Gaussian Blur and Threshold to all PNG images in a folder and saves them with '_gimp' suffix.",
    "<Your first name>",
    "<Your last name>",
    "2024",
    "<Toolbox>/MyScripts/Batch Process Images",  # Adjusted the menu location
    "",
    [],
    [],
    batch_process_images)

# Main entry point for the script
main()
