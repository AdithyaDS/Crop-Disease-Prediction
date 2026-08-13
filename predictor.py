import pandas as pd

from disease import DISEASE_FILE


class DiseasePredictor:

    def __init__(self):

        self.data = pd.read_csv(DISEASE_FILE)
    def get_symptoms_for_crop(self, crop):

        crop_data = self.data[
        self.data["crop"].str.lower() == crop.lower()
        ]
        symptoms = set()
        for symptom_list in crop_data["symptoms"]:
            for symptom in symptom_list.split(";"):
                symptoms.add(symptom.strip())

        return sorted(symptoms)

    def get_crops(self):

        crops = self.data["crop"].unique()

        return sorted(crops)
    def get_symptoms_for_crop(self, crop):

        crop_data = self.data[
        self.data["crop"].str.lower() == crop.lower()
        ]
        symptoms = set()
        for symptom_list in crop_data["symptoms"]:
            for symptom in symptom_list.split(";"):
                symptoms.add(symptom.strip())

        return sorted(symptoms)
    def predict_disease(self, crop, user_symptoms):

        crop_data = self.data[
            self.data["crop"].str.lower() == crop.lower()
        ]


        best_disease = None
        best_match = 0


        for _, row in crop_data.iterrows():

            disease_symptoms = [

                symptom.strip().lower()

                for symptom in row["symptoms"].split(";")
            ]


            match_count = 0


            for symptom in user_symptoms:

                if symptom.strip().lower() in disease_symptoms:

                    match_count += 1


            if match_count > best_match:

                best_match = match_count
                best_disease = row


        return best_disease, best_match