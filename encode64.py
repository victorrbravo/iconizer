from PIL import Image
import base64

def encode_image_to_base64(image_path):
    try:
        # Open the image file
        with open(image_path, "rb") as image_file:
            # Read the image data
            image_data = image_file.read()

            # Encode the image data in Base64
            encoded_data = base64.b64encode(image_data)

            # Convert bytes to a UTF-8 string
            base64_string = encoded_data.decode("utf-8")

            return base64_string

    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage:
image_path = "lancha.jpg"
encoded_image = encode_image_to_base64(image_path)

if encoded_image:
    print("Base64 encoded image:\n", encoded_image)
else:
    print("Failed to encode the image.")

