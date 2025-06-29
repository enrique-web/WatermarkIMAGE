# WatermarkIMAGE

A simple Python utility to add watermarks to images using the Pillow (PIL) library.

## Description

This project provides an easy way to watermark images by overlaying text or image watermarks on your pictures. It leverages the popular Python Imaging Library (Pillow) to manipulate images and apply visible watermarks, helping protect your images or add branding.

## Features

- Add text watermark with customizable font, size, opacity, and position
- Add image watermark overlay with transparency support
- Supports common image formats (JPEG, PNG, etc.)
- Lightweight and easy to use

## Installation

Make sure you have Python installed (3.x recommended).

Install Pillow:

```
pip install pillow
```

Clone this repository:

```
git clone https://github.com/enrique-web/WatermarkIMAGE.git
cd WatermarkIMAGE
```

## Usage

Example of adding a text watermark:

```
from PIL import Image, ImageDraw, ImageFont

def add_text_watermark(input_image_path, output_image_path, text, position=(0,0), opacity=128, font_path=None, font_size=36):
    base = Image.open(input_image_path).convert("RGBA")
    txt = Image.new("RGBA", base.size, (255,255,255,0))

    draw = ImageDraw.Draw(txt)
    font = ImageFont.truetype(font_path if font_path else "arial.ttf", font_size)

    draw.text(position, text, fill=(255,255,255,opacity), font=font)

    watermarked = Image.alpha_composite(base, txt)
    watermarked.convert("RGB").save(output_image_path, "JPEG")

if __name__ == "__main__":
    add_text_watermark("input.jpg", "watermarked.jpg", "Sample Watermark", position=(30,30), opacity=100)
```

You can modify the `position`, `opacity`, `font_path`, and `font_size` parameters as needed.

## Contributing

Contributions and suggestions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---
