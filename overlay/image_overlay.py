from PIL import Image, ImageOps
import sys
from pathlib import Path

def overlay_images(input_path, output_path, overlay_path="overlay_picture_name.extension"): # to be edited by user
    """Overlays an image onto a background image and saves the result.

    Args:
        input_path: Path to the background image.
        output_path: Path to save the result.
        overlay_path: Path to the overlay image (optional).
    """

    try:
        background = Image.open(input_path)
        overlay = Image.open(overlay_path).convert("RGBA")  # Preserve transparency

        # Ensure consistent file extensions
        output_path = Path(output_path).with_suffix(Path(input_path).suffix)

        # Resize both images efficiently
        size = overlay.size
        background_fit = ImageOps.fit(background, size, Image.LANCZOS)  # High-quality resizing
        overlay_fit = overlay

        # Overlay and save
        background_fit.paste(overlay_fit, overlay_fit)  # Paste at (0, 0)
        background_fit.save(output_path)

    except OSError as e:
        sys.exit(f"Error opening or saving files: {e}")
    except ValueError as e:
        sys.exit(f"Invalid image data: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        input_path = Path(sys.argv[1])
        output_path = Path(sys.argv[2])
        overlay_images(input_path, output_path)
    else:
        sys.exit("Usage: python overlay_images.py input_image.jpg output_image.jpg")
