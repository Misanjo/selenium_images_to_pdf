import csv
import re
import os
import argparse
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch

def convert_to_jpeg(img: Image.Image, quality: int = 85) -> Image.Image:
    if img.mode in ('RGBA', 'LA'):
        img = img.convert('RGB')
    return img

def sort_files(files: list[str]) -> list[str]:
    def extract_number(file: str) -> int:
        match = re.search(r'\d+', file)
        return int(match.group()) if match else 0

    return sorted(files, key=extract_number)

def images_to_pdf(folder_path: str, output_pdf_path: str) -> None:
    file_list = os.listdir(folder_path)
    image_files = sort_files([file for file in file_list if file.lower().endswith(('jpg', 'jpeg'))])

    c = canvas.Canvas(output_pdf_path, pagesize=A4)
    width, height = A4  # Tamaño A4 en puntos

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        try:
            img = Image.open(image_path)
            img = convert_to_jpeg(img)
            img_width, img_height = img.size
            aspect_ratio = img_height / img_width

            new_img_width = width
            new_img_height = new_img_width * aspect_ratio

            if new_img_height > height:
                new_img_height = height
                new_img_width = new_img_height / aspect_ratio

            x = (width - new_img_width) / 2
            y = (height - new_img_height) / 2

            c.drawImage(image_path, x, y, new_img_width, new_img_height, preserveAspectRatio=True)
            c.showPage()
        except Exception as e:
            print(f"No se pudo procesar la imagen {image_path}: {e}")

    c.save()

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convierte imágenes en un directorio a un PDF.")
    parser.add_argument('--folder_path', type=str, help='Carpeta que contiene las imágenes a incluir en el PDF')
    parser.add_argument('--pdf_name', type=str, help='Nombre del PDF resultante')
    parser.add_argument('--csv_file', type=str, help='Archivo CSV que contiene las rutas de las carpetas y nombres de PDF')
    return parser.parse_args()

def main() -> None:
    args = parse_arguments()

    if args.csv_file:
        if not os.path.isfile(args.csv_file):
            print(f"El archivo CSV {args.csv_file} no existe.")
            return

        with open(args.csv_file, newline='') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                folder_path, pdf_name = row
                if not os.path.isdir(folder_path):
                    print(f"La carpeta {folder_path} no existe.")
                    continue
                images_to_pdf(folder_path, pdf_name)
    elif args.folder_path and args.pdf_name:
        if not os.path.isdir(args.folder_path):
            print(f"La carpeta {args.folder_path} no existe.")
            return
        images_to_pdf(args.folder_path, args.pdf_name)
    else:
        print("Error: Debe proporcionar o bien el CSV o los parámetros individuales --folder_path y --pdf_name.")

if __name__ == "__main__":
    main()
