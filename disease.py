from file_handler import (
    read_records,
    add_record,
    write_records
)


DISEASE_FILE = "data/disease_dataset.csv"

DISEASE_HEADERS = [
    "name",
    "crop",
    "symptoms",
    "disease_type",
    "favorable_temp_min",
    "favorable_temp_max",
    "favorable_humidity",
    "treatment",
    "severity"
]


class DiseaseManager:

    def add_disease(
        self,
        name,
        crop,
        symptoms,
        disease_type,
        temp_min,
        temp_max,
        humidity,
        treatment,
        severity
    ):

        records = read_records(DISEASE_FILE)

        for record in records:

            if record["name"].lower() == name.lower():

                print("Disease already exists.")
                return

        add_record(
            DISEASE_FILE,
            [
                name,
                crop,
                symptoms,
                disease_type,
                temp_min,
                temp_max,
                humidity,
                treatment,
                severity
            ]
        )

        print("Disease added successfully.")


    def view_diseases(self):

        records = read_records(DISEASE_FILE)

        if not records:

            print("No diseases found.")
            return

        print("\n========== DISEASE LIST ==========")

        for record in records:

            print(
                f"{record['name']} | "
                f"{record['crop']} | "
                f"{record['disease_type']} | "
                f"{record['severity']}"
            )


    def search_disease(self, disease_name):

        records = read_records(DISEASE_FILE)

        for record in records:

            if record["name"].lower() == disease_name.lower():

                print("\n========== DISEASE DETAILS ==========")

                print("Disease Type :", record["disease_type"])
                print("Disease      :", record["name"])
                print("Crop         :", record["crop"])
                print("Symptoms     :", record["symptoms"])
                print("Severity     :", record["severity"])
                print("Treatment    :", record["treatment"])

                return

        print("Disease not found.")


    def delete_disease(self, disease_name):

        records = read_records(DISEASE_FILE)

        new_records = []
        found = False

        for record in records:

            if record["name"].lower() == disease_name.lower():

                found = True

            else:

                new_records.append(record)


        if found:

            write_records(
                DISEASE_FILE,
                new_records,
                DISEASE_HEADERS
            )

            print("Disease deleted successfully.")

        else:

            print("Disease not found.")


    def get_all_diseases(self):

        return read_records(DISEASE_FILE)