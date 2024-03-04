from PIL import Image
import os

# Get script location (assuming script is in the same folder as JPEGs)
script_dir = os.path.dirname(os.path.realpath(__file__))

def compress_jpeg_folder(folder_path, target_size=500 * 1024):
  """
  Compresses all JPEG images in a folder to approximately the target size while maintaining quality.

  Args:
    folder_path: Path to the folder containing JPEG images.
    target_size: Target file size in bytes (default: 500kB).
  """
  # Create compressed folder if it doesn't exist
  compressed_folder = os.path.join(folder_path, "compressed")
  if not os.path.exists(compressed_folder):
    os.makedirs(compressed_folder)

  for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
      input_file = os.path.join(folder_path, filename)
      output_file = os.path.join(compressed_folder, filename)
      compress_jpeg(input_file, target_size, output_file)

def compress_jpeg(input_file, target_size, output_file):
  """
  Compresses a single JPEG image to approximately the target size while maintaining quality.

  Args:
    input_file: Path to the input JPEG file.
    target_size: Target file size in bytes.
    output_file: Path to the output compressed JPEG file.
  """
  quality = 99
  
  # Open and compress image with current quality
  img = Image.open(input_file)
  compressed_size = os.path.getsize(input_file)
  
  while True:
    if compressed_size > target_size:
      img.save(output_file, "JPEG", quality=quality)
      compressed_size = os.path.getsize(output_file)
      quality -= 1
    else:
      break
  
  # Resize if size is still above target
  if compressed_size > target_size:
    print("Quality compression not enough, resizing...")
    width, height = img.size
    new_width = int(width * (target_size / compressed_size))
    new_height = int(height * (target_size / compressed_size))
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    img.save(output_file, "JPEG", quality=quality)
  
  print(f"Image '{input_file}' compressed to {compressed_size / 1024:.2f}kB with quality {quality}")

# Example usage
# Replace with your actual folder path
folder_path = script_dir

size = input("Enter the target size in kB: ")

if size.isdigit():
  size = int(size)
else:
  size = 500
  
compress_jpeg_folder(folder_path, size * 1024)
