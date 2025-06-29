from PIL import Image

def add_image_watermark(input_image_path: str, watermark_image_path: str,
                        output_image_path: str, position: tuple = None, opacity: float = 0.5):
    """
    Add an image watermark over an input image and save the result.

    Parameters:
    - input_image_path: str - path to the original image.
    - watermark_image_path: str - path to the watermark image (should support transparency, e.g., PNG).
    - output_image_path: str - path to save the watermarked image.
    - position: tuple (x, y) - position to place the watermark. Defaults to bottom-right corner.
    - opacity: float (0 to 1) - opacity level of the watermark.
    """
    base_image = Image.open(input_image_path).convert("RGBA")
    watermark = Image.open(watermark_image_path).convert("RGBA")

    # Resize watermark if larger than base image
    if watermark.size[0] > base_image.size[0] or watermark.size[1] > base_image.size[1]:
        ratio = min(base_image.size[0] / watermark.size[0], base_image.size[1] / watermark.size[1])
        new_size = (int(watermark.size[0] * ratio), int(watermark.size[1] * ratio))
        watermark = watermark.resize(new_size, Image.ANTIALIAS)

    # Adjust watermark opacity
    if opacity < 1:
        # Split watermark into channels
        r, g, b, a = watermark.split()
        # Apply opacity to alpha channel
        a = a.point(lambda i: int(i * opacity))
        watermark = Image.merge("RGBA", (r, g, b, a))

    # Default position: bottom-right corner with 10px padding
    if position is None:
        x = base_image.width - watermark.width - 10
        y = base_image.height - watermark.height - 10
        position = (x, y)

    # Create a transparent layer the size of base image
    transparent = Image.new('RGBA', base_image.size, (0,0,0,0))
    # Paste watermark onto transparent layer at the given position
    transparent.paste(watermark, position, mask=watermark)

    # Composite the watermark with the base image
    watermarked = Image.alpha_composite(base_image, transparent)

    # Convert back to RGB and save (PNG preserves transparency, JPG does not)
    watermarked.convert("RGB").save(output_image_path, "PNG")

    print(f"Watermarked image saved to: {output_image_path}")

# Example usage
if __name__ == "__main__":
    add_image_watermark(
        input_image_path="input.jpg",
        watermark_image_path="watermark.png",
        output_image_path="output_watermarked.png",
        opacity=0.4
    )
