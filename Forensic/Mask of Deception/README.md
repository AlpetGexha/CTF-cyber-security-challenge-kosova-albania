```python
from PIL import Image, ImageChops, ImageEnhance, ImageFilter
import numpy as np

def get_common_size(img1, img2):
    """Return smallest common width and height from two images."""
    common_width = min(img1.width, img2.width)
    common_height = min(img1.height, img2.height)
    return (common_width, common_height)

def xor_images(mask_path, result_path, output_path):
    """
    Perform bitwise XOR between two images.
    This may cancel the "mask" (cover.gif) from the result (results.gif)
    to reveal hidden differences.
    """
    try:
        # Open both images and force them to RGB
        img_mask = Image.open(mask_path).convert("RGB")
        img_result = Image.open(result_path).convert("RGB")
        
        # Resize to smallest common dimensions
        size = get_common_size(img_mask, img_result)
        img_mask = img_mask.resize(size)
        img_result = img_result.resize(size)
        
        # Convert to numpy arrays for pixel-wise XOR
        arr_mask = np.array(img_mask)
        arr_result = np.array(img_result)
        
        # XOR the images (this operation is applied on each channel)
        xor_arr = np.bitwise_xor(arr_mask, arr_result)
        
        # Create an image from the XOR result
        xor_img = Image.fromarray(xor_arr.astype(np.uint8))
        xor_img.save(output_path)
        print(f"[XOR] Output saved as: {output_path}")
    
    except Exception as e:
        print("Error during XOR operation:", e)


def bit_plane_slicing(image_path, output_prefix):
    """
    Extract and save each bit plane of the grayscale version of an image.
    The hidden flag might be embedded in a particular bit (e.g., LSB).
    """
    try:
        img = Image.open(image_path).convert("L")  # Convert to grayscale
        img_arr = np.array(img)

        # Loop through bit planes 0 (LSB) to 7 (MSB)
        for bit in range(8):
            bit_mask = 1 << bit
            # Isolate the specific bit-plane
            plane = (img_arr & bit_mask) // bit_mask  * 255
            plane_img = Image.fromarray(plane.astype(np.uint8))
            output_file = f"{output_prefix}_bit{bit}.png"
            plane_img.save(output_file)
            print(f"[Bit-Plane] Extracted bit {bit} saved as: {output_file}")
            
    except Exception as e:
        print("Error during bit-plane slicing:", e)


if __name__ == "__main__":
    # Paths (make sure these files are in your working directory)
    mask_image = "cover.gif"
    result_image = "results.gif"
    
    # 1. Try the XOR approach: use cover.gif as the mask and results.gif as the underlying image.
    xor_output = "xor_output.png"
    xor_images(mask_image, result_image, xor_output)
    
    # 2. Also try bit-plane slicing on the results image
    # The flag might be hidden in one of the bit planes
    bit_plane_slicing(result_image, "results")
```


```
```


```python
from PIL import Image
import numpy as np

def resize_images(image1, image2):
    # Resize both images to the smallest size
    min_width = min(image1.size[0], image2.size[0])
    min_height = min(image1.size[1], image2.size[1])
    return image1.resize((min_width, min_height)), image2.resize((min_width, min_height))

def compare_images(image1_path, image2_path, output_path):
    # Open the two images
    img1 = Image.open(image1_path).convert('RGB')
    img2 = Image.open(image2_path).convert('RGB')

    # Resize the images to the same dimensions
    img1_resized, img2_resized = resize_images(img1, img2)

    # Convert images to numpy arrays
    img1_array = np.array(img1_resized)
    img2_array = np.array(img2_resized)

    # Perform XOR or Subtraction (uncomment one option)
    # result_array = np.bitwise_xor(img1_array, img2_array)  # XOR comparison
    result_array = np.abs(img1_array - img2_array)          # Subtraction comparison

    # Convert result back to image and save
    result_img = Image.fromarray(result_array.astype('uint8'))
    result_img.save(output_path)
    print(f"Comparison image saved as {output_path}")

# Usage example
compare_images('cover.gif', 'results.gif', 'output.gif')
```