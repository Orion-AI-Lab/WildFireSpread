<div align="center">
  <img src="https://raw.githubusercontent.com/nikos230/WildFireSpread/main/logos/fire.png" alt="Fire Logo" />
</div>
<br /> 

<p align="center">
  <a href="https://www.google.com" target="_blank"><img alt="IEEEAccess Paper" src="https://img.shields.io/badge/IEEE𝘈𝘤𝘤𝘦𝘴𝘴 Paper-View|Download(Coming Soon)-ff0066" /></a>
</p>


<p align="center">
  <a href="https://mega.nz/file/dTBX1QrQ#2INiS8LK4fB3oLxWKAOS6cRUaHiKG1m-sJx-W9i41T0"><img alt="Dataset" src="https://img.shields.io/badge/Dataset-Download-blue" /></a>
  <a href="https://mega.nz/file/RTZWlCZY#H9u2s6rSAfJlgLNZLIkVvZSnJRkCGrMhWS_wnIY_aUk"><img alt="Pre-trained model" src="https://img.shields.io/badge/Pre%20Trained%20Model-Download-blue" /></a>
  <a href="https://drive.google.com/drive/folders/1cw7qrxHi9VEAlh9IMnz4xCRiPZbUDBIH?usp=sharing"><img alt="Results" src="https://img.shields.io/badge/Results-View|Download-blue" /></a>
</p>




# About The Project
A Machine Learning ready Dataset and Model to predict final burned area from a Wildfire. <br /> <br /> 
This project is part of my Thesis and makes use of [mesogeos](https://github.com/Orion-AI-Lab/mesogeos) Dataset and Convolutional Neural Networks models to predict final burned area from 27 remote sensing variables using spatial and temporal data.<br /> <br /> 
**This project includes** :
- Deep Learning Models 
- Dataset with ≈ 9500 samples (fire events)
- Tools for model evalution and visualization of results in shapefile form
- Tools for Dataset statistics extraction
- Showcase of results


## Table of Contents
- [About the Project](#about-the-project)
  - [Dataset](#dataset)
  - [Deep Learning Models](#deep-learning-models)
  - [Models Evaluation and Metrics (latest results Feb 2025)](#models-evaluation-and-metrics-latest-results-feb-2025)
  - [Visualiasion of Test Results](#visualiasion-of-test-results)
  - [Download Best Models and Dataset](#download-best-models-and-dataset)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [How to Use](#how-to-use)
    - [Training the Models](#training-the-models)
      - [Train UNet2D](#train-unet2d)
      - [Train UNet3D](#train-unet3d)
      - [Train UNet2D Baseline](#train-unet2d-baseline)
  - [Tesing the pre-trained Models](#tesing-the-pre-trained-models)
 - [Contributing / Contact](#contact)
 - [Variables, Spatial and Temporal Resolution and Sources](#dataset-variables-spatial-resolution-and-sources)



## Dataset
Training and Testing of the Models have been done with [mesogeos](https://github.com/Orion-AI-Lab/mesogeos) Dataset. Training data (and validation) are 27 variables in 64 x 64 km paches and a Spatial Resolution of 1 pixel = 1km x 1km in netCDF format. The mesogeos DataCube has 1km x 1km x 1day Spatial and Temporal resolution of 1 day. <br /> <br />
The Samples from the DataCube have 64km x 64km x 1day resoltuion, for every fire event there is a 64 x 64km patch around the fire with a random offset so the burned area is not always in the middle of the patch, and for every sample there are 10 days in total, 5 before the fire started and 5 days after. Samples are from the mesogeos region and includes ≈9500 samples from 31 countries and from years 2006 to 2022. <br /><br />
![Alt text](https://raw.githubusercontent.com/nikos230/WildFireSpread/main/screenshots/dynamic_variables.gif)

<br />


## Deep Learning Models
This project makes use of UNet2D and UNet3D models, the main difference in UNet3D is the 3D convolution which takes into account the temporal information of the samples as the 3D convolution can get info from 3 or more days at once, the 2D convolution is good for spartial feature extraction but not for temporal feature extraction. <br />
In Feature work the Dataset will be tested on a Vision Transformer (ViT) and results will be published. <br /><br />
<br />

## Models Evaluation and Metrics
The main evaluation metric is the Dice Coefficient, presented below, which shows how much 2 shapes are similar, in this Segmatation Task along with Intersection Over Union (IoU) are the most important metrics.
A baseline UNet2D is trained on only the fire day and then with all samples meaning using all 10 days each sample has. 


| Metrics (%)         | UNet2D<br /> Baseline (1 day) | UNet2D<br /> 10days  | UNet3D <br /> 10days  | ViT <br /> 10days 
|:------------------:|:------------------------------:|:--------------------:|:---------------------:|:--------------------------:|
| F1 Score / Dice    | 48.3                           | 51.7                 | **53.6**              | 43.7                  
| IoU                | 31.9                           | 34.8                 | **36.6**              | 28.0
| Precision          | 50.2                           | 58.6                 | **59.6**              | 59.4
| Recall             | 46.6                           | 46.2                 | **48.8**              | 34.6

<br />

| Metrics (%)      | UNet3D <br /> 9days  | UNet3D <br /> 8days | UNet3D <br /> 7days | UNet3D <br /> 6days
|:----------------:|:-------------------:|:-------------------:|:-------------------:|:------------------:|
| F1 Score / Dice  | 51.2                | 49.4                | 48.7                | 47.5
| IoU              | 34.4                | 32.8                | 32.2                | 31.1
| Precision        | 56.6                | 55.0                | 53.6                | 53.6
| Recall           | 46.7                | 44.9                | 44.6                | 42.5

<br />

- Baseline Model is trained using only the fire day with 27 variables <br />
- UNet2D is trained using all spatial and temporal data using 117 variables which are the 10 days <br />
- UNet3D is trained using all data like UNet2D <br />

## Download Best Models and Dataset
Dataset used is in .netCDF format and separated by year and by country for every sample. For every Model Metric that is reported the checkpoint is made available which can be used with the provided test.py scripts to run the experiments.

| Dataset / Best Models Checkpoints |                    Link 1 (MEGA Drive)                                                  | 
|:-------|:------------------------------------------------------------------------------------------------------------------:|
| Dataset (.zip)**                  | [Download](https://mega.nz/file/dTBX1QrQ#2INiS8LK4fB3oLxWKAOS6cRUaHiKG1m-sJx-W9i41T0)   | 
| UNet3D (10days)                   | [Download](https://mega.nz/file/RTZWlCZY#H9u2s6rSAfJlgLNZLIkVvZSnJRkCGrMhWS_wnIY_aUk)   | 
| Unet3D (5 days after)             | [Download](https://mega.nz/file/ZSZyAIQZ#Lr7pttkFV7Dc3GtEN7MMJV4dVJO18GSG3LiihAnhQYI)   | 
| Unet2D (10days)                   | [Download](https://mega.nz/file/AXZigRKa#p3P-4bwaj9VGuo65RuRtQj2rT0Tz6SDZ2a3XOF3jTGU)   | 
| Unet2D (1day) Baseline            | [Download](https://mega.nz/file/YGoVVahS#CrOCSd6pcXqrzKrQZlDf6YGxbIvQt8Zu1JLYiir6_70)   | 
 
** Dataset size is 10.34gb in .zip format when unzipped size will be 30.2gb

<br />



## Visualiasion of Test Results
![Image 1](https://github.com/nikos230/WildFireSpread/blob/main/screenshots/test.png)
![Image 1e](https://github.com/nikos230/WildFireSpread/blob/main/screenshots/readme_map1.png)
![Image 1](https://github.com/nikos230/WildFireSpread/blob/main/screenshots/readme_map2.png)

More to come soon...


# Getting Started
To run the experiments you can either train the model from scratch or use the trained models. Training the best model (UNet3D) takes some time...

## Prerequisites
Install requirements.txt, which has all required frameworks for the project. It is recommended to make a conda enviroment and install all files there

1. First Download the Dataset of the project from this [link](https://mega.nz/file/MDggRLxQ#XXeLnpCo2bsMugxs85NiS_HGjBuZLNVfsmPmxKdjF_Q), then extract it and place the folder named `dataset_64_64_all_10days_final` inside dataset folder on the project or
anywhere in you PC like a SSD or NVME. Then specify the path to the folder inside configs/dataset.yaml in the `corrected_dataset_path:` variable.

2. First create a new Conda Enviroment
```
conda create -n Wildfire_env python=3.8
```
3. then install requirements.txt
```
pip install requiremets.txt
```
4. you will need Pytorch CUDA Enbaled to train the models on Nvidia GPU you can install it with this command
```
pip install torch==1.13.1+cu117 torchvision>=0.13.1+cu117 torchaudio>=0.13.1+cu117 --extra-index-url https://download.pytorch.org/whl/cu117 --no-cache-dir
```
5. Done! if you find something wrong contact me to fix it

## How to Use
With this repo you can train the models, test the trained models, extract dataset statistics and visualize results of model predictions in shapefiles

### Training the Models
This project has 3 Models, a baseline model, a UNet2D model and a UNet3D model. By default the Models are trained on all 10 days of each sample, only baseline model is using 1 day for training (and testing)

#### Train UNet2D
- First open `configs/train_test_unet2d.yaml` and chnage the `checkpoints:` path to somewhere is your pc.
- Run `train_unet2d.py` and wait to finish.
- Done!, now go back to `configs/train_test_unet2d.yaml` and chnage the `checkpoint_path:` to the path of your best checkpoint <br /><br />
To test the model Run `test_unet2d.py` and this withh return metrics, first 100 binary results in png and all 1101 tesing samples in form of Shapefiles inside output/UNet2D folder (by default, you can chnage location of output files as will from `configs/train_test_unet2d.yaml`)

#### Train UNet3D
- First open `configs/train_test_unet3d.yaml` and chnage the `checkpoints:` path to somewhere is your pc.
- Run `train_unet3d.py` and wait to finish.
- Done!, now go back to `configs/train_test_unet3d.yaml` and chnage the `checkpoint_path:` to the path of your best checkpoint <br /><br />
To test the model Run `test_unet3d.py` and this withh return metrics, first 100 binary results in png and all 1101 tesing samples in form of Shapefiles inside output/UNet3D folder (by default, you can chnage location of output files as will from `configs/train_test_unet3d.yaml`)

#### Train UNet2D Baseline
- First open `configs/train_test_unet2d.yaml` and chnage the `checkpoints:` path to somewhere is your pc. And `change save_results_path:` to somewhere different so not to overwrite the UNet2D from above.
- Open `dataset_unet2d.py` and uncomment line 17 to `sample = sample.isel(time=slice(4, 5))` this will load only day 4 of the 10 days of each sample which is the fire day
- Comment lines 57, 60, 61, 63
- Chnage `.values[4]` in line 125 to `.values[0]`
- Run `train_unet2d.py` and wait to finish.
- Done!, now go back to `configs/train_test_unet2d.yaml` and chnage the `checkpoint_path:` to the path of your best checkpoint <br /><br />
To test the model Run `test_unet2d.py` and this withh return metrics, first 100 binary results in png and all 1101 tesing samples in form of Shapefiles inside output/UNet2D folder (by default, you can chnage location of output files as will from `configs/train_test_unet2d.yaml`)
- Roll back chnages to `dataset_unet2d.py` if you want to keep expirementing with all days

### Testing the pre-trained Models
If you do not train the models you can use the saved checkpoints from my work. You can download them from the links above.
- For UNet3D, download the best model from this [link](https://mega.nz/folder/8O5RDBZQ#y3olJJq7_4IksUF5zDcV2g) and go to `configs/train_test_unet3d.yaml` and specify path to checkpoint in `checkpoint_path:` variable, then Run test_unet3d.py
- For UNet2D, download the best model from this [link](https://mega.nz/folder/MOJlnADD#0KJSwgMoBSEN-TOGZTSyPw) and go to `configs/train_test_unet2d.yaml` and specify path to checkpoint in `checkpoint_path:` variable, then Run test_unet2d.py


## Contact
For more info contact : nikolas619065@gmail.com <br /><br />


## Dataset Variables, Spatial resolution and Sources

| Variables (Dynamic)                          | Spatial Resolution | Temportal Resolution | Source |  
|----------------------------------------------|:------------------:|:----------:|:-----------:|
|Max Temperature                               | 9km                |     1day    | ERA5-Land  |  
|Max Wind Speed                                | 9km                |     1day    | ERA5-Land  |
|Max Wind Direction                            | 9km                |     1day    | ERA5-Land  |
|Max Surface Pressure                          | 9km                |     1day    | ERA5-Land  |
|Min Relative Humidity                         | 9km                |     1day    | ERA5-Land  |
|Total Precipitation                           | 9km                |     1day    | ERA5-Land  |
|Mean Surface Solar Radiation Downwards        | 9km                |     1day    | ERA5-Land  |
|Day Land Surface Temperature                  | 1km                |     1day    | MODIS      |
|Night Land Surface Temperature                | 1km                |     1day    | MODIS      |
|Normalized Difference Vegetation Index (NDVI) | 500m               |     16days  | MODIS      |
|Leaf Area Index (LAI)                         | 500m               |     16days  | MODIS      |
|Soil moisture                                 | 5km                |     5days   | EDO        |
|Burned Areas                                  | 1km                |     1day    | EFFIS      |
|Ignition Points                               | 1km                |     1day    | MODIS      |

| Variables (Static)                           | Spatial Resolution | Source     |
|----------------------------------------------|:------------------:|:----------:|
|Slope                                         |30m                 | COP-DEM     
|Aspect                                        |30m                 | COP-DEM
|Curvature                                     |30m                 | COP-DEM
|Population                                    |1km                 | Worldpop
|Fraction of agriculture                       |300m                | Copernicus CCS
|Fraction of forest                            |300m                | Copernicus CCS
|Fraction of grassland                         |300m                | Copernicus CCS
|Fraction of settlements                       |300m                | Copernicus CCS
|Fraction of shrubland                         |300m                | Copernicus CCS
|Fraction of sparse vegetation                 |300m                | Copernicus CCS
|Fraction of water bodies                      |300m                | Copernicus CCS
|Fraction of wetland                           |300m                | Copernicus CCS
|Roads distance                                |1km                 | Worldpop




