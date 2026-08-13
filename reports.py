import pandas as pd

from disease import DISEASE_FILE


class ReportManager:

    def disease_summary(self):

        data = pd.read_csv(DISEASE_FILE)

        print("\n========== DISEASE SUMMARY ==========")

        print(
            "Total Diseases :",
            len(data)
        )

        print(
            "Total Crops    :",
            data["crop"].nunique()
        )

        print(
            "Disease Types  :",
            data["disease_type"].nunique()
        )


    def crop_report(self):

        data = pd.read_csv(DISEASE_FILE)

        print("\n========== CROP REPORT ==========")

        crop_counts = data["crop"].value_counts()

        for crop, count in crop_counts.items():

            print(
                crop,
                ":",
                count,
                "disease(s)"
            )


    def disease_type_report(self):

        data = pd.read_csv(DISEASE_FILE)

        print("\n========== DISEASE TYPE REPORT ==========")

        type_counts = data["disease_type"].value_counts()

        for disease_type, count in type_counts.items():

            print(
                disease_type,
                ":",
                count
            )


    def severity_report(self):

        data = pd.read_csv(DISEASE_FILE)

        print("\n========== SEVERITY REPORT ==========")

        severity_counts = data["severity"].value_counts()

        for severity, count in severity_counts.items():

            print(
                severity,
                ":",
                count
            )