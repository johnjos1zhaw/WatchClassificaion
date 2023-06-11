# Watch Image Classification Project

## Project Overview

The project's goal is to develop a machine learning model that accurately classifies watch brands based on images. The idea was initiated from an original intent to distinguish real from fake luxury watches, which later shifted to a broader scope of identifying watch brands. The model could be a valuable tool for e-commerce platforms, enhancing the shopping experience and inventory management by streamlining the process of watch categorization and recommendation.

The project involves data collection, model training and fine-tuning, result interpretation, and model performance validation. It leverages visual supervised learning methods, with a main focus on image classification.

## Motivation

The watch industry is diverse and complex, with numerous brands, models, and designs. It can be a daunting task for consumers, particularly those new to watches, to navigate this vast landscape. This project aims to simplify the categorization and recommendation process for online platforms, thereby enhancing the customer shopping experience.

## Data Collection

Two methods were used for data collection: web scraping and Kaggle datasets. Initial attempts at web scraping directly from chrono24.com proved challenging due to my novice experience in web scraping and the site's lazy-loading feature. Instead, I opted to use a [dataset available on Kaggle](https://www.kaggle.com/datasets/ahedjneed/fancy-watche-images), which had well-structured and balanced data for ten watch brands.

In parallel, I explored the use of a more user-friendly web scraping tool (Web Scraper for Google Chrome) and found watchbase.com more amenable to web scraping. After web scraping, downloading the images, and organizing them into directories based on brands and models, a comprehensive dataset was created. 

Challenges encountered during data collection included handling different image file types, addressing special characters in French watch brand names, and ensuring no duplicate images were downloaded.

## Model Training and Performance

Two main models were used in this project: a custom-built model and the Xception pre-trained model.

**Custom Model Evaluation:**
The custom-built model achieved a respectable accuracy of 69%. To balance complexity and performance, modifications were made to the architecture, including increasing the dropout rate to prevent overfitting, reducing the learning rate for more precise convergence, and adding extra convolutional and dense layers to capture more complex patterns.

The best-performing model, which isn't mentioned in the notebook, achieved an accuracy of 80%. *(find a few of my trained models in watch_models.zip)*

**Xception Model Evaluation:**
The Xception pre-trained model, after initial underperformance (3% accuracy), showed significant improvement through transfer learning (43.1% accuracy). Further fine-tuning of the model led to a substantial increase in performance, achieving validation and test accuracies of around 75% and 76%, respectively. Key adjustments included increasing the number of units in the dense layers and adjusting the dropout rate to handle overfitting.

## Reproduction of Results

The project can be reproduced using Google Colab Pro, as well as the better GPU (A100 or V100) that came with the Pro version. All datasets and models utilized in the project are here in the GitHub repository *(the Kaggle dataset, which I made my first steps with is available on the link above)*. The scripts used in the project are also available in the project's GitHub repository.

To run the code you need to download the datasets.zip (included & augmented) and upload them to your google drive.
On Google Colab, the you can run the cell, that mounts the google drive in your Colab environment and then update the paths to your location on the drive.

**Please note** the training took a long time eventhough I had the GPU from Colab Pro, the resources were very inconsistently (sometimes slow & sometimes faster, eventough I paid).

The scripts you don't need to run (*takes very long time anyway*), they are just here as evidence, what I did as well as the csv and the docx-file.
The watch_models.zip you can use also in combination with your drive, to make predictions whith the model files, in the prediction cells.

## Future Work and Improvements

Despite the considerable success in this project, there is still room for improvement. One potential area for enhancement is the model's ability to handle variations within a brand. Currently, the model is only designed to classify watches by brand, without considering the model variations within a brand.

But for the future (also considering training the classification on certain models) I would try to include multiple pictures of the same watch from different angles and with less variation. For example take this watch, the [Patek Philippe Nautilus](https://watchbase.com/patek-philippe/nautilus). This pictures are all from the same model, but there is too much variation once, it is gold, silver, roségold, green, brown, blue leather or a steel strap, special editions, once with and without diamonds but are all the same models. I think in the future I would try to get more images of just one or two specific model variations but from all angles and try to see if the model would generalize better, eventhough I have trained my model on the watch brands and not on the watch models, I'm sure it still had an impact.

Moreover, future work could involve additional fine-tuning and experimenting with other pre-trained models to further boost performance. Additionally, expanding the scope of the project to include more brands or watch characteristics could increase the utility of the model.

Overall, this project has laid a solid foundation for using machine learning in the context of watch image classification, and there is much potential for future research and development in this area.

---

For any further questions or discussions, feel free to contact me

 through email: *johnjos1@students.zhaw.ch* or open an issue in the GitHub repository.
