import fiftyone as fo

# A name for the dataset
name = "treeAI"


dataset_dir_12 = "/run/media/simone/Extreme SSD/data/TreeAI/12_RGB_FullyLabeled_640/coco"

dataset_12_train = fo.Dataset.from_dir(
    dataset_dir=dataset_dir_12,
    dataset_type=fo.types.YOLOv5Dataset,
    name="TreeAI_12_train",
    split="train"
)

dataset_12_val = fo.Dataset.from_dir(
    dataset_dir=dataset_dir_12,
    dataset_type=fo.types.YOLOv5Dataset,
    name="TreeAI_12_val",
    split="val"
)



dataset_dir_0 = "/run/media/simone/Extreme SSD/data/TreeAI/0_RGB_FullyLabeled/coco"

dataset_0_train = fo.Dataset.from_dir(
    dataset_dir=dataset_dir_0,
    dataset_type=fo.types.YOLOv5Dataset,
    name="TreeAI_0",
    split="train"
)

dataset_0_val = fo.Dataset.from_dir(
    dataset_dir=dataset_dir_0,
    dataset_type=fo.types.YOLOv5Dataset,
    name="TreeAI_0_val",
    split="val"
)


dataset = dataset_0_train #only of at the time at the start

session = fo.launch_app(dataset)
session.wait()