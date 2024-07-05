from PIL import Image
import numpy as np

def load_image(image_path):
    """
    Load an image from disk using PIL (Python Imaging Library).

    Args:
    - image_path (str): Path to the image file.

    Returns:
    - PIL.Image.Image: Loaded image object.
    """
    return Image.open(image_path)

def save_image(image, image_path):
    """
    Save an image object to disk using PIL.

    Args:
    - image (PIL.Image.Image): Image object to be saved.
    - image_path (str): Path to save the image file.
    """
    image.save(image_path)

def encrypt_image(image, key):
    """
    Encrypt an image using a simple technique (pixel swapping and XOR).

    Args:
    - image (PIL.Image.Image): Image object to be encrypted.
    - key (int): Encryption key (used for XOR operation).

    Returns:
    - PIL.Image.Image: Encrypted image object.
    """
    # Convert image to numpy array for faster pixel manipulation
    pixels = np.array(image)
    height, width, channels = pixels.shape
    encrypted_pixels = np.copy(pixels)
    
    # Example of pixel swapping (swap adjacent pixels)
    for i in range(height):
        for j in range(0, width, 2):
            if j + 1 < width:
                encrypted_pixels[i, j], encrypted_pixels[i, j + 1] = pixels[i, j + 1], pixels[i, j]
    
    # Example of XOR operation with the key
    encrypted_pixels = encrypted_pixels ^ key

    # Convert encrypted pixels back to PIL image
    encrypted_image = Image.fromarray(encrypted_pixels)
    return encrypted_image

def decrypt_image(encrypted_image, key):
    """
    Decrypt an encrypted image to retrieve the original image.

    Args:
    - encrypted_image (PIL.Image.Image): Encrypted image object.
    - key (int): Decryption key (used to reverse encryption operations).

    Returns:
    - PIL.Image.Image: Decrypted image object.
    """
    # Convert encrypted image to numpy array
    encrypted_pixels = np.array(encrypted_image)
    height, width, channels = encrypted_pixels.shape
    
    # Reverse XOR operation with the same key to retrieve original pixels
    decrypted_pixels = encrypted_pixels ^ key
    
    # Reverse the pixel swapping operation
    for i in range(height):
        for j in range(0, width, 2):
            if j + 1 < width:
                decrypted_pixels[i, j], decrypted_pixels[i, j + 1] = decrypted_pixels[i, j + 1], decrypted_pixels[i, j]
    
    # Convert decrypted pixels back to PIL image
    decrypted_image = Image.fromarray(decrypted_pixels)
    return decrypted_image

# Input paths from user
image_path = input("Enter the path to the image you want to encrypt: ").strip()
encrypted_image_path = input("Enter the path where you want to save the encrypted image: ").strip()
decrypted_image_path = input("Enter the path where you want to save the decrypted image: ").strip()

# Validate paths or handle errors as needed (omitted for brevity)

# Load the original image
try:
    image = load_image(image_path)
except FileNotFoundError:
    print(f"Error: The image file '{image_path}' was not found.")
    exit()

# Input encryption key from user
try:
    key = int(input("Enter the encryption key (an integer): ").strip())
except ValueError:
    print("Error: The encryption key must be an integer.")
    exit()

# Encrypt the image
encrypted_image = encrypt_image(image, key)
save_image(encrypted_image, encrypted_image_path)
print(f"Image encrypted and saved to {encrypted_image_path}")

# Decrypt the image
decrypted_image = decrypt_image(encrypted_image, key)
save_image(decrypted_image, decrypted_image_path)
print(f"Image decrypted and saved to {decrypted_image_path}")
