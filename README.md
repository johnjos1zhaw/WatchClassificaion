# Watch Image Classification Project README

## Project Overview

The project's goal is to develop a machine learning model that accurately classifies watch brands based on images. The idea was initiated from an original intent to distinguish real from fake luxury watches, which later shifted to a broader scope of identifying watch brands. The model could be a valuable tool for e-commerce platforms, enhancing the shopping experience and inventory management by streamlining the process of watch categorization and recommendation.

The project involves data collection, model training and fine-tuning, result interpretation, and model performance validation. It leverages visual supervised learning methods, with a main focus on image classification.

## Motivation

The watch industry is diverse and complex, with numerous brands, models, and designs. It can be a daunting task for consumers, particularly those new to watches, to navigate this vast landscape. This project aims to simplify the categorization and recommendation process for online platforms, thereby enhancing the customer shopping experience.

## Data Collection

Two methods were used for data collection: web scraping and Kaggle datasets. Initial attempts at web scraping directly from chrono24.com proved challenging due to my novice experience in web scraping and the site's lazy-loading feature. Instead, I opted to use a dataset available on Kaggle, which had well-structured and balanced data for ten watch brands.

In parallel, I explored the use of a more user-friendly web scraping tool (Web Scraper for Google Chrome) and found watchbase.com more amenable to web scraping. After a meticulous process that involved scraping, downloading images, and organizing them into directories based on brands and models, a comprehensive dataset was created. 

Challenges encountered during data collection included handling different image file types, addressing special characters in French watch brand names, and ensuring no duplicate images were downloaded.

## Model Training and Performance

Two main models were used in this project: a custom-built model and the Xception pre-trained model.

**Custom Model Evaluation:**
The custom-built model achieved a respectable accuracy of 69%. To balance complexity and performance, modifications were made to the architecture, including increasing the dropout rate to prevent overfitting, reducing the learning rate for more precise convergence, and adding extra convolutional and dense layers to capture more complex patterns.

**Xception Model Evaluation:**
The Xception pre-trained model, after initial underperformance (3% accuracy), showed significant improvement through transfer learning (43.1% accuracy). Further fine-tuning of the model led to a substantial increase in performance, achieving validation and test accuracies of around 75% and 76%, respectively. Key adjustments included increasing the number of units in the dense layers and adjusting the dropout rate to handle overfitting.

The best-performing model, which isn't mentioned in the notebook, achieved an accuracy of 80%.

## Reproduction of Results

The project can be reproduced using Google Colab, and all datasets and models utilized in the project are publicly available on Google Drive and GitHub. The scripts used in the project are also available in the project's GitHub repository.

## Future Work and Improvements

Despite the considerable success in this project, there is still room for improvement. One potential area for enhancement is the model's ability to handle variations within a brand. Currently, the model is only designed to classify watches by brand, without considering the model variations within a brand.

Moreover, future work could involve additional fine-tuning and experimenting with other pre-trained models to further boost performance. Additionally, expanding the scope of the project to include more brands or watch characteristics could increase the utility of the model.

Overall, this project has laid a solid foundation for using machine learning in the context of watch image classification, and there is much potential for future research and development in this area.

---

For any further questions or discussions, feel free to contact me

 through [email details] or open an issue in the GitHub repository.
