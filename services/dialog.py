# coding: utf-8

# def set_values():
#     bool_val_input = raw_input("\nMöchten Sie den Performance Modus oder den Visualisierungs Modus für die Alogrithmen Quickhull und Giftwrapping? (p/v): ").lower()
#     if bool_val_input == "p":
#         bool_val = True
#         print("\nSie haben sich für den Performance Modus entschieden.\n")
#     elif bool_val_input == "v":
#         bool_val = False
#         print("\nSie haben sich für den Visualisierungs Modus entschieden.\n")
#     else:
#         print("\nUngültige Eingabe. Bitte geben Sie 'p' oder 'v' für einen Modus ein.\n")
#         return set_values()
#     num_val = raw_input("\nBitte geben Sie eine Nummer ein, für die Anzahl an zufälligen Punkten, für die Sie die Convexe-Hülle berechnen wollen: ")
#     try:
#         num_val = int(num_val)
#         if num_val <= 0:
#             print("\nBitte geben Sie eine positive Nummer ein.\n")
#             return set_values()
#     except ValueError:
#         print("\nBitte geben Sie eine positive Nummer ein.\n")
#         return set_values()
#     return bool_val, num_val
# coding: utf-8

def set_values():
    # Abfrage für den Modus
    bool_val_input = raw_input(
        "\nMöchten Sie den Performance Modus oder den Visualisierungs Modus für die Algorithmen Quickhull und Giftwrapping? (p/v): ").lower()

    if bool_val_input == "p":
        bool_val = True
        print("\nSie haben sich für den Performance Modus entschieden.\n")
    elif bool_val_input == "v":
        bool_val = False
        print("\nSie haben sich für den Visualisierungs Modus entschieden.\n")
    else:
        print("\nUngültige Eingabe. Bitte geben Sie 'p' oder 'v' für einen Modus ein.\n")
        return set_values()

    # Abfrage für Datenquelle
    data_source_input = raw_input("\nMöchten Sie zufällige Daten generieren oder eine Datei einlesen? (z/d): ").lower()
    file_path = None
    num_val = None

    if data_source_input == "z":
        generate_random_data = True
        num_val_input = raw_input(
            "\nBitte geben Sie eine Nummer ein, für die Anzahl an zufälligen Punkten, für die Sie die Convexe-Hülle berechnen wollen: ")
        try:
            num_val = int(num_val_input)
            if num_val <= 0:
                print("\nBitte geben Sie eine positive Nummer ein.\n")
                return set_values()
        except ValueError:
            print("\nBitte geben Sie eine positive Nummer ein.\n")
            return set_values()
    elif data_source_input == "d":
        generate_random_data = False
        file_path = raw_input("\nBitte geben Sie den Pfad zur Datei an: ")
    else:
        print("\nUngültige Eingabe. Bitte geben Sie 'z' für zufällige Daten oder 'd' für Datei ein.\n")
        return set_values()

    return bool_val, num_val, generate_random_data, file_path

# Beim Aufrufen der Funktion wird entsprechend:
# bool_val: True oder False (je nach Modus)
# generate_random_data: True (zufällige Daten) oder False (Datei)
# file_path: Pfad zur Datei oder None (falls zufällige Daten gewählt wurden)



