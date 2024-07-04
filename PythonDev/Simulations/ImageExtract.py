from PIL import Image
import io

def extract_embedded_image(image_path):
    with open(image_path, 'rb') as file:
        data = file.read()

        # JPEG header and footer
        jpeg_header = b'\xFF\xD8'
        jpeg_footer = b'\xFF\xD9'

        start = data.find(jpeg_header, 1)  # Find second JPEG header
        end = data.find(jpeg_footer, start) + 2  # Find the corresponding JPEG footer

        if start != -1 and end != -1:
            embedded_data = data[start:end]
            embedded_image = Image.open(io.BytesIO(embedded_data))
            embedded_image.save("extracted_image.jpg")

# Use the function to extract the embedded image
extract_embedded_image('/Users/mechkarov/Desktop/ThermalFiles/20150810_0051.JPG')
