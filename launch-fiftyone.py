import fiftyone as fo

# A name for the dataset
name = "treeAI"

dataset_dir_12 = "/run/media/simone/Extreme SSD/data/TreeAI/12_RGB_FullyLabeled_640/coco"

dataset_12 = fo.Dataset.from_dir(
    dataset_dir=dataset_dir_12,
    dataset_type=fo.types.YOLOv5Dataset,
    name="TreeAI_12"
)



dataset_dir_0 = "/run/media/simone/Extreme SSD/data/TreeAI/0_RGB_FullyLabeled/coco"

dataset_0 = fo.Dataset.from_dir(
    dataset_dir=dataset_dir_0,
    dataset_type=fo.types.YOLOv5Dataset,
    name="TreeAI_0"
)

dataset = dataset_0 #only of at the time

session = fo.launch_app(dataset)
session.wait()