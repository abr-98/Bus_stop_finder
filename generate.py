import os

def assign(i_s):
    i=int(i_s)

    trails=['trails/up_azone','trails/up_ukhra','trails/up_54feet','trails/up_8B']
    ground= ['ground_truth/azone.txt','ground_truth/ukhra.txt','ground_truth/54feet.txt','ground_truth/8B.txt']
    trail_range=[50,28,60,43]
    input_file_path=trails[i]
    output_folder = '2018_Results_54feet_TC_10'
    ground_truth_file_path = ground[i]
    distance_threshold = 30
    starting_time = '05:00:00'
    ending_time = '22:00:00'
    min_points_threshold = 10
    trail_id_range = trail_range[i]
    ground_truth_threshold = 50
    false_positive_distance = 100

    return input_file_path,output_folder,ground_truth_file_path,distance_threshold,starting_time,ending_time,min_points_threshold,trail_id_range,ground_truth_threshold,false_positive_distance

    