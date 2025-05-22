import os
import geopandas as gdf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def calc_percentage_category(shapefile, corine_shapefile):

    intersection = gdf.overlay(shapefile, corine_shapefile, how='intersection')

    intersection['intersection_area_ha'] = intersection.geometry.area / 10_000

    inter_grouped = intersection.groupby(by=['Code_18'])['intersection_area_ha'].sum().reset_index()

    total_area = inter_grouped['intersection_area_ha'].sum()
    print(f'total area: {total_area}')

    inter_grouped['percentage'] = (inter_grouped['intersection_area_ha'] / total_area) * 100

    return inter_grouped




def combine_small_percentages(predicted_clc, corine_legend):

    corine_legend['Code_18'] = pd.to_numeric(corine_legend['Code_18'], errors='coerce').astype('Int64')
    predicted_clc['Code_18'] = pd.to_numeric(predicted_clc['Code_18'], errors='coerce').astype('Int64')

    predicted_clc = predicted_clc.merge(corine_legend[['Code_18', 'LABEL3']], on='Code_18', how='left')
    #print(predicted_clc)
    predicted_clc_grouped = predicted_clc[predicted_clc['percentage'] < 1].copy()
    predicted_clc_grouped['percentage'] = predicted_clc_grouped['percentage'].sum()
    predicted_clc_grouped['Code_18'] = '000'
    predicted_clc_grouped['LABEL3'] = 'Other'
    predicted_clc_grouped = predicted_clc_grouped.iloc[:1]


    predicted_clc = predicted_clc[predicted_clc['percentage'] > 1]

    predicted_clc = predicted_clc.append(predicted_clc_grouped[['Code_18', 'percentage', 'LABEL3']], ignore_index=True)
    predicted_clc = predicted_clc.drop('intersection_area_ha', axis=1)

    return predicted_clc




if __name__ == "__main__":
    os.system('clear')

    ground_truth = gdf.read_file('output/UNet3D_10days/ground_truth_combined/ground_truth_combined.shp')
    predicted = gdf.read_file('output/UNet3D_10days/predicted_combined/predicted_combined.shp')

    corine_cropped = gdf.read_file('corine_cropped/test_CLC.shp')
    corine_legend = pd.read_csv('corine_cropped/clc_legend.csv')
    corine_legend = corine_legend.rename(columns={'CLC_CODE': 'Code_18'})
    print(corine_cropped.columns)
    corine_legend = corine_legend.drop(44)
    #print(corine_legend)
    #exit()

    # update Area of every polygon (gia na eimaste sigouroi)
    corine_cropped['Area_Ha'] = corine_cropped.geometry.area / 10_000 # in ha

    # chnage crs of corine to match predicted and ground_truth
    corine_cropped = corine_cropped.to_crs('EPSG:3035')

    ground_truth = ground_truth.to_crs('EPSG:3035')

    predicted = predicted.to_crs('EPSG:3035')

    # clipped predicted to ground_truth to get only True Positives
    predicted = predicted.clip(ground_truth)

    
    print('Predicted')
    predicted_clc = calc_percentage_category(predicted, corine_cropped)
    print('Ground Truth')
    ground_truth_clc = calc_percentage_category(ground_truth, corine_cropped)

    #print(ground_truth_clc)
    #print(predicted_clc['percentage'].round(2))


    #print(corine_legend)
    predicted_clc = combine_small_percentages(predicted_clc, corine_legend)
    ground_truth_clc = combine_small_percentages(ground_truth_clc, corine_legend)
    
    predicted_clc['LABEL3'] = predicted_clc['LABEL3'].replace('Land principally occupied by agriculture, with significant areas of natural vegetation', 'Natural Vegetation')
    ground_truth_clc['LABEL3'] = ground_truth_clc['LABEL3'].replace('Land principally occupied by agriculture, with significant areas of natural vegetation', 'Natural Vegetation')
    print(predicted_clc)
    print(ground_truth_clc)
    predicted_clc['Code_18'] = predicted_clc['Code_18'].astype(str)
    ground_truth_clc['Code_18'] = ground_truth_clc['Code_18'].astype(str)

    predicted_clc = predicted_clc.sort_values(by='percentage', ascending=True)
    ground_truth_clc = ground_truth_clc.sort_values(by='percentage', ascending=True)

    labels = predicted_clc['LABEL3'].astype(str).unique()
    y_positions = np.arange(len(labels))

    predicted_clc['y_pos'] = predicted_clc['LABEL3'].map({label: i for i, label in enumerate(labels)})
    ground_truth_clc['y_pos'] = ground_truth_clc['LABEL3'].map({label: i for i, label in enumerate(labels)})

    bar_height = 0.4

    plt.barh(predicted_clc['y_pos'] - bar_height/2, predicted_clc['percentage'], height=bar_height, color='#0bb4ff', label='Categories in Predicted Polygons', zorder=1)
    plt.barh(ground_truth_clc['y_pos'] + bar_height/2, ground_truth_clc['percentage'], height=bar_height, color='#e60049', label='Categories in Ground Truth Polygons', zorder=1)
    
    plt.yticks(y_positions, labels, fontsize=9)
    plt.xticks(fontsize=9)
    plt.xlabel('Percentage (%)', fontsize=10)
     
    #plt.xticks(np.linspace(0, 21, num=5))  
    plt.ylabel('Corine Land Cover Categories', fontsize=10)
    plt.grid(axis='x', linestyle=':', linewidth=0.5, color='gray', zorder=0)

    plt.title('Land Cover Predicted and Ground Truth', fontsize=12)
    plt.legend(fontsize=9)

    plt.tight_layout()
    os.makedirs('output/evaluation_extra/plots', exist_ok=True)
    plt.savefig('output/evaluation_extra/plots/Land_Cover_Predicted_Ground_Truth.png', dpi=300)

    


