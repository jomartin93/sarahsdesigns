from PIL import Image, ImageOps
import os

input_folder  = "assets/gallery"
output_folder = "assets/gallery"
max_width  = 1000
max_height = 1000

for fname in os.listdir(input_folder):
    ext = os.path.splitext(fname)[1].lower()
    if not (ext.endswith(".png") or ext.endswith(".jpg") or ext.endswith(".jpeg")):
        continue
    in_path  = os.path.join(input_folder, fname)
    base     = os.path.splitext(fname)[0]
    out_path = os.path.join(output_folder, base + ".jpg")

    img = Image.open(in_path)

    # Honor EXIF orientation (prevents unexpected rotation)
    img = ImageOps.exif_transpose(img)

    # If image has an alpha channel (transparency), convert to RGB with white background
    if img.mode in ("RGBA", "LA") or (img.mode=="P" and "transparency" in img.info):
        background = Image.new("RGB", img.size, (255,255,255))
        background.paste(img, mask=img.split()[3])  # 3 is the alpha channel
        img = background
    else:
        img = img.convert("RGB")

    # Resize while preserving aspect ratio
    img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)

    # ---- STRIP ALL METADATA ----
    # Ensure no EXIF or profiles survive
    if "exif" in img.info:
        del img.info["exif"]
    if "icc_profile" in img.info:
        del img.info["icc_profile"]

    # Save as JPG with quality
    try:
        img.save(out_path, "JPEG", quality=85, optimize=True, progressive=True)
    except Exception as e:
        print(f"Error saving {out_path}: {e}")
        continue

    # delete the original PNG file
    if ext.endswith(".png") or ext.endswith(".jpeg"):
        os.remove(in_path)

    print(f"Saved: {out_path}")
