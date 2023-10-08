# coding: utf-8
import time
# Serviceimports
from services.datagrenerater import generate_random_points, load_data_csv
from services.performancemeasure import performance_measure
from services.visualization import visualize
from services.dialog import set_values
# Klassenimports
from classes.giftwrapping import GiftWrapping
from classes.quickhull import QuickHull

if __name__ == "__main__":
    # Konsolendialog und das setzen von Punkten:
    perf_mode, number, generate_random_data, file_path = set_values()
    coord_tresh = 20

    if generate_random_data:
        lst_point = generate_random_points(number, coord_tresh, "circle")
    else:
        _ , lst_point = load_data_csv("Punkte.CSV")
 ############################################################################################################

# Verschiedene Modi
    if perf_mode:
        # Testet den Algos auf die Performanz
        total_calls, hull, dauer = performance_measure(QuickHull(lst_point))
        print("Der Qickhull Algorithmus benoetigt: ", total_calls, " Schritte, bei einer Zeit von: ", dauer,
              " Sekunden. Die Huelle hat die Laenge:", len(hull), " und die folgende Punkte", hull, '\n')

        total_calls, hull, dauer = performance_measure(GiftWrapping(lst_point))
        print("Der Giftwrapping Algorithmus benoetigt: ", total_calls, " Schritte, bei einer Zeit von: ", dauer,
              " Sekunden. Die Huelle hat hat die Laenge", len(hull), "und die folgende Punkte", hull)
        ende = time.time()
    else:
        # Returns für die Visualisierung
        print('Start Visualization')
        giftwrapping_hull, giftwr_steps = GiftWrapping(lst_point).visualisation()
        # Quickhull
        quick_hull, quickhull_steps = QuickHull(lst_point).visualisation()

        visualize(lst_point, coord_tresh, giftwrapping_hull, giftwr_steps, quickhull_steps)
##################################################################################################
# Performance Test für Protokoll (DEPRICATED)

        # shapes = ["uniform"]
        # exponents = [1,2,3,4,5,6,7]
        # coord_tresh = 500
        # quick_calls =[]
        # gift_calls = []
        # quick_time =[]
        # gift_time = []
        #
        # for shape in shapes:
        #     print("\n******Distribution:", shape,"********")
        #     quick_calls_exp = []
        #     gift_calls_exp = []
        #     quick_time_exp = []
        #     gift_time_exp = []
        #     for exponent in exponents:
        #         lst_point = generate_random_points(10**exponent, coord_tresh, type= shape)
        #
        #
        #         print(f"N-Points: 10^{exponent}")
        #         total_calls, hull, dauer = performance_measure(QuickHull(lst_point))
        #         quick_calls_exp.append(total_calls)
        #         quick_time_exp.append(dauer)
        #
        #         print("\tQuickhull")
        #         print("Total Calls:\t\t", total_calls),
        #         print("Time:\t", dauer,)
        #         print("N-Points Hull:\t", len(hull))
        #         if (shape == "circle") & (exponent > 4):
        #             total_calls, hull, dauer=0,0,0
        #         else:
        #             total_calls, hull, dauer = performance_measure(GiftWrapping(lst_point))
        #             print("\tGiftwrapping")
        #             print("Total Calls:\t", total_calls),
        #             print("Time:\t", dauer,)
        #             print("N-Points Hull:\t", len(hull),"\n")
        #         gift_calls_exp.append(total_calls)
        #         gift_time_exp.append(dauer)
        #
        #     quick_calls.append(quick_calls_exp)
        #     gift_calls.append(gift_calls_exp)
        #     quick_time.append(quick_time_exp)
        #     gift_time.append(gift_time_exp)
        # print(shapes)
        # print(exponents)
        # print(quick_calls)
        # print(gift_calls)
        # print(quick_time)
        # print(gift_time)
