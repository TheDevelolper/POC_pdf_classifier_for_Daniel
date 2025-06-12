import os
from pathlib import Path
from pdf2image import convert_from_path
from PIL import Image


from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import numpy as np

CONVERT_PDF = True


BASE_DIR = Path(__file__).resolve().parent  # folder containing this script
INPUT_PDF_DIR = BASE_DIR / "examples"
PROCESSED_IMAGES_DIR = BASE_DIR / "processed/images"


if CONVERT_PDF:

    def pdf_to_image(pdf_path, output_path=None, dpi=200):
        images = convert_from_path(pdf_path, dpi=dpi)
        first_page = images[0]

        if output_path:
            first_page.save(output_path, "PNG")
            print(f"Saved image to: {output_path}")

        return first_page

    for example_directory in os.listdir(INPUT_PDF_DIR):
        for file in os.listdir(INPUT_PDF_DIR / example_directory):
            if file.lower().endswith(".pdf"):
                pdf_path = INPUT_PDF_DIR / example_directory / file
                output_path = (
                    PROCESSED_IMAGES_DIR
                    / example_directory
                    / Path(file).with_suffix(".png")
                )
                pdf_to_image(pdf_path, output_path)


def images_to_vectors(image_dir, image_size=(64, 64)):
    """
    Load images from subfolders in image_dir.
    Each subfolder name is the label.
    Returns X (features) and y (labels).
    """
    X = []
    y = []
    labels = os.listdir(image_dir)
    for label in labels:
        label_dir = os.path.join(image_dir, label)
        if not os.path.isdir(label_dir):
            continue
        for filename in os.listdir(label_dir):
            filepath = os.path.join(label_dir, filename)
            try:
                img = Image.open(filepath).convert("L")  # grayscale
                img = img.resize(image_size)
                arr = np.array(img).flatten() / 255.0  # normalize
                X.append(arr)
                y.append(label)
            except Exception as e:
                print(f"Skipping {filepath}: {e}")
    return np.array(X), np.array(y)


classifier = SVC(kernel="linear")
X, y = images_to_vectors(PROCESSED_IMAGES_DIR)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

classifier.fit(X_train, y_train)

labelled_images = []

X, y_prediction = images_to_vectors(PROCESSED_IMAGES_DIR)

print(classification_report(y, y_prediction))
