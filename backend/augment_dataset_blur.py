import os
import glob
import cv2
import random
import shutil
from pathlib import Path

# Paths
DATASET_PATH = Path("backend/Automatic Plate Number Recognition.v4i.yolov8/train")
IMAGES_DIR = DATASET_PATH / "images"
LABELS_DIR = DATASET_PATH / "labels"

def augment_with_blur():
    """
    Augments the training dataset by applying Gaussian and Motion Blur
    to the images. This creates new training examples that teach the model
    how to recognize blurry plates.
    """
    if not IMAGES_DIR.exists() or not LABELS_DIR.exists():
        print(f"Dataset directories not found: {IMAGES_DIR} or {LABELS_DIR}")
        return

    images = list(IMAGES_DIR.glob("*.jpg")) + list(IMAGES_DIR.glob("*.png")) + list(IMAGES_DIR.glob("*.jpeg"))
    
    print(f"Found {len(images)} images in the training set.")
    print("Applying blur augmentation to 50% of the dataset to improve robustness...")

    augmented_count = 0
    for img_path in images:
        # Skip if it's already an augmented image to avoid recursive augmentation
        if "_blur" in img_path.stem:
            continue

        # Only augment 50% of the dataset to keep a balance
        if random.random() > 0.5:
            continue

        # Load image
        img = cv2.imread(str(img_path))
        if img is None:
            continue

        # Randomly choose between Gaussian Blur and Motion Blur
        blur_type = random.choice(["gaussian", "motion"])

        if blur_type == "gaussian":
            # Apply Gaussian Blur (kernel size 5x5 or 7x7)
            ksize = random.choice([5, 7])
            blurred_img = cv2.GaussianBlur(img, (ksize, ksize), 0)
        else:
            # Apply Motion Blur (kernel size 7 or 9)
            ksize = random.choice([7, 9])
            kernel = cv2.getGaussianKernel(ksize, 0)
            blurred_img = cv2.filter2D(img, -1, kernel)

        # Save blurred image
        new_img_name = f"{img_path.stem}_blur{img_path.suffix}"
        new_img_path = IMAGES_DIR / new_img_name
        cv2.imwrite(str(new_img_path), blurred_img)

        # Copy the corresponding label file
        label_path = LABELS_DIR / f"{img_path.stem}.txt"
        if label_path.exists():
            new_label_path = LABELS_DIR / f"{new_img_name.replace(img_path.suffix, '.txt')}"
            shutil.copy2(label_path, new_label_path)
            augmented_count += 1
            
    print(f"Successfully generated {augmented_count} new blurry training images/labels.")
    print("The dataset is now ready for retraining with blur robustness!")

if __name__ == "__main__":
    augment_with_blur()
