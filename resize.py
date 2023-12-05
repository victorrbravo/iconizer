from PIL import Image

def resize_image(input_path, output_path):
    try:
        # Open the image file
        image = Image.open(input_path)

        # Get the original size
        original_size = image.size

        # Calculate the new size (50% reduction)
        new_size = (int(original_size[0] * 0.25), int(original_size[1] * 0.25))

        # Resize the image
        resized_image = image.resize(new_size)

        # Save the resized image
        resized_image.save(output_path)

        print(f"Image resized successfully and saved at {output_path}")

    except Exception as e:
        print(f"Error resizing image: {e}")
