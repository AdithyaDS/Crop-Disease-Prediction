from disease import DiseaseManager
from predictor import DiseasePredictor
from reports import ReportManager


disease_manager = DiseaseManager()

predictor = DiseasePredictor()

report_manager = ReportManager()

# DISEASE MANAGEMENT

def disease_menu():

    while True:

        print("\n========== DISEASE MANAGEMENT ==========")

        print("1. Add Disease")
        print("2. View Diseases")
        print("3. Search Disease")
        print("4. Delete Disease")
        print("5. Back")


        choice = input(
            "Enter your choice: "
        )


        if choice == "1":

            name = input("Disease Name: ")

            crop = input("Crop: ")

            symptoms = input(
                "Symptoms: "
            )

            disease_type = input(
                "Disease Type: "
            )

            temp_min = input(
                "Minimum Favorable Temperature: "
            )

            temp_max = input(
                "Maximum Favorable Temperature: "
            )

            humidity = input(
                "Favorable Humidity: "
            )

            treatment = input(
                "Treatment: "
            )

            severity = input(
                "Severity: "
            )


            disease_manager.add_disease(

                name,
                crop,
                symptoms,
                disease_type,
                temp_min,
                temp_max,
                humidity,
                treatment,
                severity
            )


        elif choice == "2":

            disease_manager.view_diseases()


        elif choice == "3":

            name = input(
                "Enter disease name: "
            )

            disease_manager.search_disease(
                name
            )


        elif choice == "4":

            name = input(
                "Enter disease name: "
            )

            disease_manager.delete_disease(
                name
            )


        elif choice == "5":

            break


        else:

            print("Invalid choice.")

# DISEASE PREDICTION
def prediction_menu():

    print("\n========== CROP DISEASE PREDICTION ==========")

    # Get available crops
    crops = predictor.get_crops()

    print("\nAvailable Crops:")

    for i, crop in enumerate(crops, start=1):
        print(f"{i}. {crop}")


    # Select crop
    try:
        choice = int(input("\nSelect crop number: "))

        if choice < 1 or choice > len(crops):
            print("Invalid crop selection.")
            return

    except ValueError:
        print("Please enter a number.")
        return


    crop = crops[choice - 1]

    print("\nSelected Crop:", crop)


    # Get symptoms for selected crop
    available_symptoms = predictor.get_symptoms_for_crop(crop)

    print("\nAvailable Symptoms:")

    for i, symptom in enumerate(available_symptoms, start=1):
        print(f"{i}. {symptom}")


    # Select symptoms using numbers
    try:

        symptom_input = input(
            "\nSelect symptoms (example: 1,3): "
        )

        symptom_numbers = [
            int(number.strip())
            for number in symptom_input.split(",")
        ]


        # Validate symptom numbers
        for number in symptom_numbers:

            if number < 1 or number > len(available_symptoms):

                print("Invalid symptom number.")
                return


        # Convert numbers into symptom names
        user_symptoms = [
            available_symptoms[number - 1]
            for number in symptom_numbers
        ]


    except ValueError:

        print("Please enter symptom numbers only.")
        return


    print("\nSelected Symptoms:")

    for symptom in user_symptoms:
        print("-", symptom)


    # Predict disease
    disease, match_count = predictor.predict_disease(
        crop,
        user_symptoms
    )


    # Display result
    if disease is not None:

        print("\n========== PREDICTION RESULT ==========")

        print("Crop         :", disease["crop"])
        print("Disease      :", disease["name"])
        print("Disease Type :", disease["disease_type"])
        print("Matched      :", match_count, "symptom(s)")
        print("Severity     :", disease["severity"])
        print("Treatment    :", disease["treatment"])

    else:

        print("\nNo matching disease found.")

# REPORT MENU


def report_menu():

    while True:

        print("\n========== REPORTS ==========")

        print("1. Disease Summary")
        print("2. Crop Report")
        print("3. Disease Type Report")
        print("4. Severity Report")
        print("5. Back")


        choice = input(
            "Enter your choice: "
        )


        if choice == "1":

            report_manager.disease_summary()


        elif choice == "2":

            report_manager.crop_report()


        elif choice == "3":

            report_manager.disease_type_report()


        elif choice == "4":

            report_manager.severity_report()


        elif choice == "5":

            break


        else:

            print("Invalid choice.")


# MAIN MENU
def main():

    while True:

        print("\n")
        print("=" * 50)

        print(
            "       CROP DISEASE PREDICTION SYSTEM"
        )

        print("=" * 50)
        print("1. Disease Management")
        print("2. Predict Disease")
        print("3. Reports")
        print("4. Exit")


        choice = input(
            "Enter your choice: "
        )


        if choice == "1":

            disease_menu()


        elif choice == "2":

            prediction_menu()


        elif choice == "3":

            report_menu()


        elif choice == "4":

            print(
                "Thank you for using the system."
            )

            break


        else:

            print(
                "Invalid choice. Please try again."
            )


if __name__ == "__main__":

    main()