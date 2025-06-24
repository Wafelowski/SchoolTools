from PIL import Image
import os

# Get script location (assuming script is in the same folder as JPEGs)
script_dir = os.path.dirname(os.path.realpath(__file__))

def compress_jpeg_folder(folder_path, target_size=500 * 1024):
  """
  Compresses all JPEG and PNG images in a folder to approximately the target size while maintaining quality.
  PNGs are converted to JPEG.
  Args:
    folder_path: Path to the folder containing images.
    target_size: Target file size in bytes (default: 500kB).
  """
  # Create compressed folder if it doesn't exist
  compressed_folder = os.path.join(folder_path, "compressed")
  if not os.path.exists(compressed_folder):
    os.makedirs(compressed_folder)

  for filename in os.listdir(folder_path):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
      input_file = os.path.join(folder_path, filename)
      # For PNGs, change extension to .jpg in output
      if filename.lower().endswith(".png"):
        output_filename = os.path.splitext(filename)[0] + ".jpg"
      else:
        output_filename = filename
      output_file = os.path.join(compressed_folder, output_filename)
      compress_jpeg(input_file, target_size, output_file)

def compress_jpeg(input_file, target_size, output_file):
  """
  Compresses a single JPEG or PNG image to approximately the target size while maintaining quality.
  PNGs are converted to JPEG.
  Args:
    input_file: Path to the input image file.
    target_size: Target file size in bytes.
    output_file: Path to the output compressed JPEG file.
  """
  quality = 99

  # Open image
  img = Image.open(input_file)
  # Convert PNG to RGB (JPEG doesn't support alpha)
  if img.mode in ("RGBA", "P"):
    img = img.convert("RGB")

  # Save a temporary file to measure size
  temp_file = output_file + ".tmp"
  img.save(temp_file, "JPEG", quality=quality)
  compressed_size = os.path.getsize(temp_file)

  while compressed_size > target_size and quality > 10:
    img.save(temp_file, "JPEG", quality=quality)
    compressed_size = os.path.getsize(temp_file)
    quality -= 1

  # Resize if size is still above target
  if compressed_size > target_size:
    print("Quality compression not enough, resizing...")
    width, height = img.size
    scale = (target_size / compressed_size) ** 0.5
    new_width = max(1, int(width * scale))
    new_height = max(1, int(height * scale))
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    img.save(temp_file, "JPEG", quality=quality)

  # Move temp file to output
  os.replace(temp_file, output_file)
  print(f"Image '{input_file}' compressed to {os.path.getsize(output_file) / 1024:.2f}kB with quality {quality}")

# Example usage
# Replace with your actual folder path
folder_path = script_dir

size = input("Enter the target size in kB: ")

if size.isdigit():
  size = int(size)
else:
  size = 500

compress_jpeg_folder(folder_path, size * 1024)
