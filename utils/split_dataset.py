import os
import shutil
import random

# Paths
raw_dataset = "../dataset/raw_images"
processed_dataset = "../dataset/processed_images"

train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

# Create folders
for split in ["train", "validation", "test"]:
    for category in os.listdir(raw_dataset):
        os.makedirs(os.path.join(processed_dataset, split, category), exist_ok=True)

# Split images
for category in os.listdir(raw_dataset):
    category_path = os.path.join(raw_dataset, category)
    images = os.listdir(category_path)
    random.shuffle(images)

    total = len(images)
    train_end = int(train_ratio * total)
    val_end = int((train_ratio + val_ratio) * total)

    train_images = images[:train_end]
    val_images = images[train_end:val_end]
    test_images = images[val_end:]

    for img in train_images:
        shutil.copy(os.path.join(category_path, img),
                    os.path.join(processed_dataset, "train", category, img))

    for img in val_images:
        shutil.copy(os.path.join(category_path, img),
                    os.path.join(processed_dataset, "validation", category, img))

    for img in test_images:
        shutil.copy(os.path.join(category_path, img),
                    os.path.join(processed_dataset, "test", category, img))

print("Dataset split completed successfully.")