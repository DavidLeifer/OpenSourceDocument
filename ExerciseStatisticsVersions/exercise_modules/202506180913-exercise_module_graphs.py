'''
##############################################################################
# Part Z: Run the functions                                                  #
##############################################################################

# These functions are example usage for exercise_module.py
# Testing is in GraphsExerciseStatistics.ipynb.

# Part A: The path of the CSV to be parsed
def CSV_running(path,unflipped_col):
  # Create the CSV_Parser class object and open the files
  parser = eu.CSV_Parser(path)
  read = parser.file_opener()
  # Index the comma position from the CSV and split the characters into their values
  comma_indexed = parser.comma_index(read, path, 0)
  # Get the width of columns of the commas
  comma_width = parser.comma_index(read, path, 1)
  # Sort the list into verticle columns
  # The P0 csv gets flipped, except for the Stm column
  # Divide by two - the list of comma places is doubled for the start/end value
  col_width = int(((comma_width - 1 ) / 2) - 1)
  vert = []
  for i in range(0,comma_width-1,2):
    value_list = parser.csv_value_list(comma_indexed, read, col_width, i)
    if unflipped_col == 0:
      vert.append(value_list)
    else:
      if value_list[0] in unflipped_col:
        vert.append(value_list)
      else:
        flip = parser.csv_flipper(value_list, col_width)
        vert.append(flip)
  return vert

# One month of May, 2024 observations
P0_path = "/content/P0.csv"
B0_path = "/content/B0.csv"
# A0 is a TSV because there are blank cells
A0_path = "/content/A0.tsv"
P0_unflipped_col = ['ID','Date','Day','Stm']
# P0_vert = CSV_running(P0_path,P0_unflipped_col)
# B0_vert = CSV_running(B0_path,0)
# A0_vert = CSV_running(A0_path,0)
# Four months of July-October observations
# P1.csv contains the pain scale and B1.csv contains the food records
# P1_path = "/content/P1-Observations-PaperFigures.csv"
# B1_path = "/content/B1.csv"
# A1 is a tsv because of blank cells
A1_path = "/content/A1.tsv"
# List of columns to not be flipepd
# P1_unflipped_col = ['ID','Date','Day','Stm','Notes','Notes2']
# P1_vert = CSV_running(P1_path,P1_unflipped_col)
# B1_vert = CSV_running(B1_path,0)
A1_vert = CSV_running(A1_path,0)
'''

'''
# Part B: Get descriptive statistics
def stats_def(P1_vert,B1_vert):
  stats_class = Statistics()
  # The first three columns are skipped because they are ID, Date, and Day
  # These two loops calculate the means and moments
  P1_means_list = []
  P1_stnd_list = []
  B1_means_list = []
  B1_stnd_list = []
  # secondary todo: might make these functions
  for l in P1_vert[3:]:
    P1_means = stats_class.mu(l)
    P1_means_list.append(P1_means)
    P1_mnt2_4 = stats_class.mnt(P1_means[0],P1_means[1],l)
    P1_stnd_list.append(P1_mnt2_4[1])
  for m in B1_vert[2:]:
    B1_means = stats_class.mu(m)
    B1_means_list.append(B1_means)
    B1_mnt2_4 = stats_class.mnt(B1_means[0],B1_means[1],m)
    B1_stnd_list.append(B1_mnt2_4[1])
  # The nested loops calculates the covariance and correlations between B0 and P0
  for n in range(len(P1_vert[3:])):
    print("x: ", P1_vert[n+3][0])
    for o in range(len(B1_vert[2:])):
      print("    and ", B1_vert[o+2][0])
      P1B1_covar = stats_class.covar(P1_means_list[n],B1_means_list[o],P1_vert[n+3],B1_vert[o+2])
      P1B1_cor = stats_class.cor(P1B1_covar,P1_stnd_list[n],B1_stnd_list[o])
      print(P1B1_cor)
    print()

# Part C: Data visualization ASCII
def P1_ASCII_graph(P1_vert):
  title_full = ['Stamina',
                'Feet','Ankle','Calves',
                'Knees','Quadriceps','Gluteus','Groin',
                'Abdominals','Lower Back',
                'Latissimus Dorsi','Trapezius','Shoulders',
                'Chest','Triceps','Biceps',
                'Neck','Head']
  graph_count = 3
  for p in P1_vert[3:]:
    #if graph_count == 4:
    #  break
    # Initialize graph class
    P1_graph = Graph(P1_vert, 1, graph_count)
    # ASCII Graphs
    # date_col_num = 1 # data_col_num = each successive column
    # this would be a loop over columns 3-20, 1st column is the date
    # print(p[0])
    # print()
    P1_hi_lo = P1_graph.hi_lo(graph_count)
    date_hi_lo = P1_graph.hi_lo(1)
    P1_binned = P1_graph.binned(P1_hi_lo)
    P1_time_series = P1_graph.time_series(date_hi_lo,P1_binned)
    # P1_graph.time_series_print(P1_time_series[0],P1_time_series[1])
    # P1_file_out = "/content/P1_" + p[0] + ".txt"
    # P1_time_series_write = P1_graph.time_series_write(p[0],P1_file_out,P1_time_series[0],P1_time_series[1])
    # print("\n")
    graph_count += 1

def B1_ASCII_graph(B1_vert):
  # Did not finish
  graph_count = 2
  for p in B1_vert[2:]:
    #if graph_count == 4:
    #  break
    # Initialize graph class
    B1_graph = Graph(B1_vert, 1, graph_count)
    # ASCII Graphs
    # date_col_num = 1 # data_col_num = each successive column
    # this would be a loop over columns 3-20, 1st column is the date
    # print(p[0])
    # print()
    B1_hi_lo = B1_graph.hi_lo(graph_count)
    date_hi_lo = B1_graph.hi_lo(1)
    B1_binned = B1_graph.binned(B1_hi_lo)
    B1_time_series = B1_graph.time_series(date_hi_lo,B1_binned)
    # B0_graph.time_series_print(B0_time_series[0],B0_time_series[1])
    # print()
    # B0_file_out = "/content/B0_" + p[0] + ".txt"
    # B0_time_series_write = B0_graph.time_series_write(p[0],B0_file_out,B0_time_series[0],B0_time_series[1])
    # print("\n")
    graph_count += 1

# Part D: Data visualization RGB
def P1_RGB_graph(P1_vert):

  title_full = ['Stamina',
                'Feet','Ankle','Calves',
                'Knees','Quadriceps','Gluteus','Groin',
                'Abdominals','Lower Back',
                'Latissimus Dorsi','Trapezius','Shoulders',
                'Chest','Triceps','Biceps',
                'Neck','Head']
  P1_rgb = Graphs_rgb(P1_vert)
  P1_B1 = 0
  start_val = 3
  # Draws the bar charts
  P1_rgb_bar = P1_rgb.rgb_timeseries_bar(title_full,start_val,P1_B1)
  # RGB Line Graphs by Group
  # Uses the position of each body part name in the title_full list
  P1_groups_num = [3,4,7,11,13,16,19,21]
  P1_title_label = ['Stamina','Lower Legs','Upper Legs','Core','Upper Back','Arms','Head']
  # P1_rgb_line = P1_rgb.rgb_timeseries_line(title_full,start_val,P1_groups_num,P1_title_label,P1_B1)

  # Line graphs by upper/lower body group means
  def small():
    csv_groups_list = [[3,4],[4,7,11,13],[13,16,19,21]]
    legend_label = [['Stamina'],['Lower Legs','Upper Legs','Core'],['Upper Back','Arms','Head']]
    k0 = 0
    for csv_groups_num in csv_groups_list:
      fig, ax = plt.subplots(1, 1, layout='constrained', figsize=(15, 5))
      P1_rgb_line_smallest = P1_rgb.rgb_timeseries_small(csv_groups_num,legend_label[k0],ax)
      # Plot formatting
      plt.margins()
      plt.grid()
      plt.yticks(range(1,6))
      if sum(csv_groups_num) == sum(csv_groups_list[1]):
        ax.legend()
        plt.title("Lower Body")
        plt.ylabel("Pain")
        #plt.savefig("Lower Body Pain.jpg")
      elif sum(csv_groups_num) == sum(csv_groups_list[2]):
        ax.legend()
        plt.title("Upper Body")
        plt.ylabel("Pain")
        #plt.savefig("Upper Body Pain.jpg")
      else:
        plt.ylabel("Stamina")
        #plt.savefig("Stamina.jpg")
      k0 += 1

  # Smallest on one graph
  def smallest():
    # csv_groups_list = [[3,4],[4,12],[13,21]]
    # legend_label = [['Stamina'],['Lower Body'], ['Upper Body']]
    csv_groups_list = [[4,21]]
    legend_label = [['Pain']]
    fig, ax = plt.subplots(1, 1, layout='constrained', figsize=(15, 5))
    k1 = 0
    for csv_groups_num in csv_groups_list:
      P1_rgb_line_smallest = P1_rgb.rgb_timeseries_small(csv_groups_num,legend_label[k1],ax)
      k1 += 1
    # Plot formatting
    plt.margins()
    plt.grid()
    # plt.legend()
    plt.yticks(range(1,6))
    plt.ylabel("Pain")
    plt.savefig('P1_smallerest.jpg')
  # small()
  # smallest()

def B1_RGB_graph(B1_vert):
  title_full = ['Calories','Exercise',            # Group 0
              'Salt', 'Fat', 'Protein',           # Group 1
              'Carbohydrates', 'Alcohol Servings' # Group 3
              ]                                   # etc
  B1_rgb = Graphs_rgb(B1_vert)
  P1_B1 = 1
  start_val = 2
  # Part D RGB Graphs: B1.csv
  B1_rgb_bar = B1_rgb.rgb_timeseries_bar(title_full,start_val,P1_B1)
  # RGB Line Graphs by Group for B0.csv
  # Uses the position of each title in the title_full list
  B1_groups_num = [2,3,4,8,9]
  B1_title_label = ['Calories','Exercise','Nutrients','Alcohol Servings']
  # Line graph is not appropriate for calories, exercise, and alcohol servings
  #B1_rgb_line = B1_rgb.rgb_timeseries_line(title_full,start_val,B1_groups_num,B1_title_label,P1_B1)

# A0_vert
def A0_RGB_graph(A0_vert):
  # Part D RGB Graphs: A0.tsv
  A0_sort = Graphs_sort(A0_vert)
  # Calculates the duration of each activity.
  A0_sort_duration = A0_sort.sort_time(A0_sort.data[6],A0_sort.data[4],A0_sort.data[5])
  # Removes endings for similar words such as: 'Walk', 'Walks', 'Walked', 'Walking'.
  A0_activity_filter = A0_sort.filter_stop(A0_sort.data[6])
  # Sorts the list using an implementation of merge sort.
  ord_list = ['ord_list'] + [ord(A0_activity_filter[x][0]) for x in range(1,len(A0_activity_filter))]
  A0_sort_merged = A0_sort.sort_ascii(ord_list,A0_activity_filter,A0_sort.data[1],A0_sort_duration)
  # Finds the unique occurances of each word in 'Activity'.
  A0_sort_unique = A0_sort.sort_unique_words(A0_sort_merged[0])
  # Bins the sorted list using the unique words.
  A0_sort_bin = A0_sort.sort_unique_bin(A0_sort_unique,A0_sort_merged)
  # Merges the bins based on if the first word in the string are the same.
  # i.e. 'Eat' <- 'Eat 1' <- 'Eat 2' <- 'Eat 3'
  A0_sort_similar = A0_sort.merge_similar_activities(A0_sort_bin)
  A0_sort_similar_splice = A0_sort.merge_activities_splice(A0_sort_similar)
  # Graphs
  A0_sort_graph = Graphs_rgb(A0_sort_similar_splice)
  A0_sort_graph.rgb_timeseries_frequency()
  A0_sort_graph.rgb_timeseries_duration()

# A1_vert v0

def A1_RGB_graph(A1_vert):
  # Part D RGB Graphs: A0.tsv
  A1_sort = Graphs_sort(A1_vert)
  # Calculates the duration of each activity.
  A1_sort_duration = A1_sort.sort_time(A1_sort.data[6],A1_sort.data[4],A1_sort.data[5])
  # Removes endings for similar words such as: 'Walk', 'Walks', 'Walked', 'Walking'.
  A1_activity_filter = A1_sort.filter_stop(A1_sort.data[6])
  # Sorts the list using an implementation of merge sort.
  ord_list = ['ord_list'] + [ord(A1_activity_filter[x][0]) for x in range(1,len(A1_activity_filter))]
  A1_sort_merged = A1_sort.sort_ascii(ord_list,A1_activity_filter,A1_sort.data[1],A1_sort_duration)
  # Finds the unique occurances of each word in 'Activity'.
  A1_sort_unique = A1_sort.sort_unique_words(A1_sort_merged[0])
  # Bins the sorted list using the unique words.
  A1_sort_bin = A1_sort.sort_unique_bin(A1_sort_unique,A1_sort_merged)
  # Merges the bins based on if the first word in the string are the same.
  # i.e. 'Eat' <- 'Eat 1' <- 'Eat 2' <- 'Eat 3'
  A1_sort_similar = A1_sort.merge_similar_activities(A1_sort_bin)
  A1_sort_similar_splice = A1_sort.merge_activities_splice(A1_sort_similar)

  # Sort the values for each horizontal bar graph.
  A1_sort_similar_2 = A1_sort.merge_sort_int(A1_sort_similar_splice[2],A1_sort_similar_splice[0])
  A1_sort_graph = Graphs_rgb(0)
  # A1_sort_graph.rgb_timeseries_frequency(A1_sort_similar_2)                     # ( 2, 0 )
  A1_sort_similar_1 = A1_sort.merge_sort_int(A1_sort_similar_splice[1],A1_sort_similar_splice[0])
  # A1_sort_graph.rgb_timeseries_duration(A1_sort_similar_1)                      # ( 0, 1 )

  # Total activity mean.
  A1_sort_duration_mean = []
  for i in range(len(A1_sort_similar_splice[1])):
    duration_mean = A1_sort_similar_splice[1][i] / A1_sort_similar_splice[2][i]
    A1_sort_duration_mean.append(duration_mean)
  A1_sort_similar_3 = A1_sort.merge_sort_int(A1_sort_duration_mean,A1_sort_similar_splice[0])
  # A1_sort_graph.rgb_timeseries_mean(A1_sort_similar_3)                          # ( 0,(1/2) )


  # Daily mean.
  A1_sort_daily_mean = []
  for i in range(len(A1_sort_similar_splice[1])):
    duration_mean = (A1_sort_similar_splice[2][i] / 100) * 60
    A1_sort_daily_mean.append(duration_mean)
  A1_sort_similar_4 = A1_sort.merge_sort_int(A1_sort_daily_mean,A1_sort_similar_splice[0])
  # A1_sort_graph.rgb_timeseries_daily_mean(A1_sort_similar_4)                    # ( 0,((1/2) / 100) * 60)

# A1_vert v1
# A1_vert
def A1_RGB_graph(A1_vert):
  # Part D RGB Graphs: A0.tsv
  A1_sort = Graphs_sort(A1_vert)

  # Calculates the duration of each activity.
  # A1_sort_duration = A1_sort.sort_time(A1_sort.data[6],A1_sort.data[4],A1_sort.data[5])

  # Removes endings for similar words such as: 'Walk', 'Walks', 'Walked', 'Walking'.
  A1_activity_filter = A1_sort.filter_stop(A1_sort.data[6])
  # Fill in the blank days of the week for 'A1_sort.data[2]' i.e. ''
  A1_sort_day = []
  for i in A1_sort.data[2]:
    if len(i) > 0:
      check = i
    if i == '':
      A1_sort_day.append(check)
    else:
      A1_sort_day.append(i)

  # Binning the start time.
  start_time = []
  time_bins = ['0000-0659', '0700-0859', '0900-1059', '1100-1259', '1300-1459', '1500-1659', '1700-1859', '1900-2359']
  for zero in A1_sort.data[4]:
    # Appends the header or the '0' value.
    if zero == A1_sort.data[4][0]:
      start_time.append(zero)
    else:
      # 'time_bins' is the categories.
      for time_splice in time_bins:
        # Split each value into the the max and min value of the bin.
        time_split = time_splice.split('-')
        # If the start time is between the max and min value, append the bin start.
        if int(zero) >= int(time_split[0]) and int(zero) <= int(time_split[1]):
          # '0' has to be greater than length 1: 'sort_ascii()' -> 'merge()' -> 'for k in range(1,length):'
          # This is a data collection issue where '0' is entered as '0000' but Google Sheets
          # defaults to one decimal from formatting.
          if zero == '0':
            start_time.append('0000')
          else:
            start_time.append(time_split[0])

  # Sorts the list using an implementation of merge sort.
  ord_list = ['ord_list'] + [ord(start_time[x][0]) for x in range(1,len(A1_sort.data[4]))]

  # 'A1_sort_duration' is the duration used for days of the week with 'sort_ascii()',
  # 'A1_sort.data[4]' is the start column.

  A1_sort_merged = A1_sort.sort_ascii(ord_list,start_time,A1_sort_day,A1_activity_filter)

  # Finds the unique occurances of each word in 'Activity'.
  A1_sort_unique = A1_sort.sort_unique_words(A1_sort_merged[0])
  # Bins the sorted list using the unique words.
  A1_sort_bin = A1_sort.sort_unique_bin(A1_sort_unique,A1_sort_merged)

  # Orders the days of the week.
  # A1_sort_bin_day = [A1_sort_bin[0],A1_sort_bin[4],A1_sort_bin[2],A1_sort_bin[6],A1_sort_bin[7],A1_sort_bin[5],A1_sort_bin[1],A1_sort_bin[3]]
  # The start time bins are already ordered.
  A1_sort_bin_day = A1_sort_bin

  # Loop over each day and standardize the categories.
  A1_week_dur = []
  A1_week_freq = []

  # The binned weekdays code to generate HeatMaps is in 202504251421-HeatmapDays-GraphsExerciseStatistics.ipynb.
  # This version is almost identical but does it for start times.
  # Time X Activity Frequency
  for day in A1_sort_bin_day[1:]:
    weekday_activity = ['Activity'] # Weekday
    weekday_duration = ['Duration'] # Activity, because of ordering in sort_ascii().
    for j in day[1:]:
      weekday_activity.append(j[2])
      weekday_duration.append(j[1]) # Day of the week
    if day[0][0] == '0000':
      weekday_activity.append('Juggle')
      weekday_duration.append('Thursday') # Day of the week
    weekday_ord = ['weekday_ord'] + [ord(weekday_duration[x][0]) for x in range(1,len(weekday_duration))]
    weekday_foo_str = ['foo']
    weekday_foo = weekday_foo_str + [str(0) for y in range(len(weekday_activity))] # 'weekday_foo' can be any of the spreadsheet columns.
    A1_weekday_sort = A1_sort.sort_ascii(weekday_ord,weekday_duration,weekday_activity,weekday_foo)
    A1_weekday_unique = A1_sort.sort_unique_words(A1_weekday_sort[0])
    # Bins the sorted list using the unique words.
    A1_weekday_bin = A1_sort.sort_unique_bin(A1_weekday_unique,A1_weekday_sort)
    # Merges the bins based on if the first word in the string are the same.
    # i.e. 'Eat' <- 'Eat 1' <- 'Eat 2' <- 'Eat 3'
    A1_weekday_similar = A1_sort.merge_similar_activities(A1_weekday_bin)
    '''
    # Used for 'Activity Frequency' (Start Time) Heatmap graph.
    if A1_weekday_similar[3] == []:
      A1_weekday_similar_splice = A1_weekday_similar
    else:
      A1_weekday_similar_splice = A1_sort.merge_activities_splice(A1_weekday_similar)
    '''
    A1_weekday_similar_splice = A1_weekday_similar

    # Standardize the 'Activity' values for the heatmap.
    # A1_weekday_standard = ['Guitar', 'Juggle', 'Longboard', 'Run', 'Skateboard', 'Skateboard\npaper', 'Stretch', 'Walk']
    # A1_weekday_standard = ['Walk','Stretch','Skateboard\npaper','Skateboard','Run','Longboard','Juggle','Guitar']
    # A1_weekday_standard = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    A1_weekday_standard = ['Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday', 'Sunday']
    A1_standard_activity = []
    A1_standard_duration = []
    A1_standard_frequency = []
    # Results in Day (Y) by Activity (X)
    for k in range(len(A1_weekday_standard)):
      A1_standard_activity.append(A1_weekday_standard[k])
      A1_standard_duration.append(0)
      A1_standard_frequency.append(0)
      for m in range(len(A1_weekday_similar_splice[0])):
        if A1_weekday_similar_splice[0][m] == 'Longboard\nL':
          A1_weekday_similar_splice[0][m] = 'Longboard'
        if A1_weekday_similar_splice[0][m] == A1_weekday_standard[k]: # otherwise skip the 'Activity'
          A1_standard_duration[k] = A1_weekday_similar_splice[1][m]
          A1_standard_frequency[k] = A1_weekday_similar_splice[2][m]
    A1_week_dur.append(A1_standard_duration)
    A1_week_freq.append(A1_standard_frequency)
  # Flip the columns so that weekdays are X and values are Y.
  A1_dur_week_rev = A1_sort.direction_flipper(A1_week_dur)
  A1_freq_week_rev = A1_sort.direction_flipper(A1_week_freq)
  A1_freq_week_rev[2][0] = 0
  for m in range(len(A1_freq_week_rev)):
    print(A1_freq_week_rev[m], ' / ', A1_dur_week_rev[m]) # 6 0 != 1
  print()
  # 'weekdays' for the week graphing.
  # weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
  weekdays = ['0000', '0700', '0900', '1100', '1300', '1500', '1700', '1900']
  A1_sort_graph = Graphs_rgb(0)
  # A1_heatmap_dur = A1_sort_graph.heatmap_graph_0(weekdays, A1_weekday_standard, A1_dur_week_rev, 'Activity Duration (Hours)', 0)
  # A1_heatmap_freq = A1_sort_graph.heatmap_graph_0(weekdays, A1_weekday_standard, A1_freq_week_rev, 'Weekday Activity Frequency', 0)

  '''
  # Total activity mean.
  A1_total_duration_mean = []
  for dur_act in range(len(A1_dur_week_rev)):
    A1_dur_weekly_mean = []
    for dur_day in range(len(A1_dur_week_rev[0])):
      if A1_freq_week_rev[dur_act][dur_day] > 0 and A1_dur_week_rev[dur_act][dur_day] > 0:
        duration_mean = A1_dur_week_rev[dur_act][dur_day] / A1_freq_week_rev[dur_act][dur_day]
      else:
        duration_mean = 0
      A1_dur_weekly_mean.append(duration_mean)
    print(A1_dur_weekly_mean)
    A1_total_duration_mean.append(A1_dur_weekly_mean)
  print()
  A1_heatmap_dur_mean = A1_sort_graph.heatmap_graph_0(weekdays, A1_weekday_standard, A1_total_duration_mean, 'Duration Mean (Hours)', 0)
  # Daily mean
  A1_daily_duration_mean = []
  for dur_act in range(len(A1_dur_week_rev)):
    A1_daily_weekly_mean = []
    for dur_day in range(len(A1_dur_week_rev[0])):
      #if A1_freq_week_rev[dur_act][dur_day] > 0 and A1_dur_week_rev[dur_act][dur_day] > 0:
      duration_mean = (A1_dur_week_rev[dur_act][dur_day] / 100 ) * 60
      #else:
      #  duration_mean = 0
      A1_daily_weekly_mean.append(duration_mean)
    print(A1_daily_weekly_mean)
    A1_daily_duration_mean.append(A1_daily_weekly_mean)
  print()
  A1_heatmap_dur_mean = A1_sort_graph.heatmap_graph_0(weekdays, A1_weekday_standard, A1_daily_duration_mean, 'Daily Mean (Minutes)', 0)
  '''

  '''
  # Calculates the duration of each activity.
  A1_sort_duration = A1_sort.sort_time(A1_sort.data[6],A1_sort.data[4],A1_sort.data[5])
  # Removes endings for similar words such as: 'Walk', 'Walks', 'Walked', 'Walking'.
  A1_activity_filter = A1_sort.filter_stop(A1_sort.data[6])
  # Sorts the list using an implementation of merge sort.
  ord_list = ['ord_list'] + [ord(A1_activity_filter[x][0]) for x in range(1,len(A1_activity_filter))]
  A1_sort_merged = A1_sort.sort_ascii(ord_list,A1_activity_filter,A1_sort.data[1],A1_sort_duration)
  # Finds the unique occurances of each word in 'Activity'.
  A1_sort_unique = A1_sort.sort_unique_words(A1_sort_merged[0])
  # Bins the sorted list using the unique words.
  A1_sort_bin = A1_sort.sort_unique_bin(A1_sort_unique,A1_sort_merged)

  # Merges the bins based on if the first word in the string are the same.
  # i.e. 'Eat' <- 'Eat 1' <- 'Eat 2' <- 'Eat 3'
  A1_sort_similar = A1_sort.merge_similar_activities(A1_sort_bin)
  A1_sort_similar_splice = A1_sort.merge_activities_splice(A1_sort_similar)

  # Sort the values for each horizontal bar graph.
  A1_sort_similar_2 = A1_sort.merge_sort_int(A1_sort_similar_splice[2],A1_sort_similar_splice[0])

  A1_sort_graph = Graphs_rgb(0)

  # A1_sort_graph.rgb_timeseries_frequency(A1_sort_similar_2)                     # ( 2, 0 )
  A1_sort_similar_1 = A1_sort.merge_sort_int(A1_sort_similar_splice[1],A1_sort_similar_splice[0])
  # A1_sort_graph.rgb_timeseries_duration(A1_sort_similar_1)                      # ( 0, 1 )
  # Total activity mean.
  A1_sort_duration_mean = []
  for i in range(len(A1_sort_similar_splice[1])):
    duration_mean = A1_sort_similar_splice[1][i] / A1_sort_similar_splice[2][i]
    A1_sort_duration_mean.append(duration_mean)
  A1_sort_similar_3 = A1_sort.merge_sort_int(A1_sort_duration_mean,A1_sort_similar_splice[0])
  # A1_sort_graph.rgb_timeseries_mean(A1_sort_similar_3)                          # ( 0,(1/2) )
  # Daily mean.
  A1_sort_daily_mean = []
  for i in range(len(A1_sort_similar_splice[1])):
    duration_mean = (A1_sort_similar_splice[1][i] / 100) * 60
    A1_sort_daily_mean.append(duration_mean)
  A1_sort_similar_4 = A1_sort.merge_sort_int(A1_sort_daily_mean,A1_sort_similar_splice[0])
  A1_sort_graph.rgb_timeseries_daily_mean(A1_sort_similar_4)                    # ( 0,(1 / 100) * 60)
  '''

# P1_RGB_graph(P1_vert)
# B1_RGB_graph(B1_vert)
# A0_RGB_graph(A0_vert)
# A1_RGB_graph(A1_vert)
'''

# This method looks like a giant waste of time but the details of Tim sort were
# revealed that combines insert (bubble in this case) and merge sort depending on the
# length of the list since small lists perform similar regardless of if bubble or merge
# sort are used. This class contains functions that originally appeared in 'Graphs_Sort()'
# in Part E: Part D visualization helper functions and example usage is 'A1_daily_RGB_graph'.
'''
class TimSort:
  # Sorts a list using bubble sort.
  def bubble_sort(self,list0,count):
    list0_len = len(list0)
    for i in range(list0_len-1):
      swapped = False
      for j in range(list0_len-i-1):
        if list0[j][2] > list0[j+1][2]:
          list0[j], list0[j+1] = list0[j+1], list0[j]
          swapped = True
          count += 1
      if not swapped:
        break
    return [list0, count]

  # Returns abnormal pain or stamina day with reverse days.
  def day_ID_range(self,day_list,reverse_days):
    # minus the number of days of interest [30,10,7,5,3 ... n].
    header = reverse_days[0]
    day_start_end = [['minus_one',-1,-1,-1]]
    # The range of 'Day_ID' adding the frequency for [30,10,7,5,3 ... n] for each
    # successive 'reverse_days' then skip those 30 for the total frequency.
    for day in day_list:
      # Skips the header.
      for reverse in range(1,len(reverse_days)):
        # Check if there are enough days to reverse.
        day_start = reverse_days[reverse][1] - day
        if day_start > -1:
          day_end = reverse_days[reverse][1]
          day_start_end.append([header[0],day,day_start,day_end])
    return day_start_end

  # The main function is to return the number of activities before a day with erroneous pain.
  # Returns: 'Body_Part', 'Days_reverse', 'Day_ID_start', 'Day_ID_end', 'Time_ID_start' (or 'count_0'), 'Time_ID_end' (or 'count_1'), 'time_difference', 'id'
  def dayid_2_timeid(self,ordered_days_bubble):
    # Calculates activity frequencies before the erroneous pain value by converting
    # the P1.csv 'Day_ID' (0-99 rows) 'start' and 'end' (contained in
    # ordered_days_bubble[0]) to A1.csv 'Time_ID' (0-525 from self.data[0])).
    # Returns the difference between start and end.

    # Worst case is len(ordered_days_bubble[0]),len(self.data[0]) or 102 X 525 = ~53,000.
    # This method is increments the second loop to the 'start' called
    # ordered_days_bubble[0][i][2]. Since ordered_days_bubble[0] is already
    # sorted, it avoids looping through the entire 525 rows in A1.csv len(self.data[0])
    # and reduces iterations to ~13,000.
    counter = 0
    activity_frequency_list = []
    # Skipping the first 7 values is hardcoded because they are boilerplate
    # returns from a previous function. A more elegant solution is an 'if value == -1'.
    for i in range(7,len(ordered_days_bubble[0])):
      for j in range(ordered_days_bubble[0][i][2],len(self.data[0])):
        # Found the start value, 'count_0' is set to 'j'.
        if str(self.data[0][j]) == str(ordered_days_bubble[0][i][2]): # str, int

          # The goal is to find 'activity' frequency of overlapping ranges to avoid
          # looping over each range and each day as a different number of activities.
          # i.e. [start:end] = [0:7], [3:10] shares the values [3:7], the counter already
          # knows the number of activity values for [3:7] is 5 so it only loops over
          # [0:2] equals 2 and [8:10] equals 3.

          # These if/else reduce the iterations to 12,374 and you could reduce by
          # another few hundred by using greater than the 'start' and same as the 'end'
          # but is redundant.
          if ordered_days_bubble[0][i][2] == ordered_days_bubble[0][i-1][2]:
            # The erroneous values occured on the same day, the start and end are
            # the same, use the alrady calculated frequency and break the iteration.
            if ordered_days_bubble[0][i][3] == ordered_days_bubble[0][i-1][3]:
              # print('Same')
              # print('No calculation needed: ', ordered_days_bubble[0][i-1][2], ':', ordered_days_bubble[0][i-1][3])
              # print(ordered_days_bubble[0][i],ordered_days_bubble[0][i-1])
              # print(i,i-1)
              count_0 = count_0
              count_1 = count_1
              break
            # If the previous days 'end' is less than the current days 'end'
            # add it onto the already calculated frequency.
            elif ordered_days_bubble[0][i-1][3] < ordered_days_bubble[0][i][3]:
              # print('End is less than')
              # print('Already know this one: ', ordered_days_bubble[0][i-1][2], ':', ordered_days_bubble[0][i-1][3])
              # The start is the same as the previous one.
              count_0 = count_0
              # print('Trying to get this frequency: ', ordered_days_bubble[0][i][2], ':', ordered_days_bubble[0][i][3])
              # print('Calculate by adding this range onto the already known: ', ordered_days_bubble[0][i-1][3], ':', ordered_days_bubble[0][i][3])
              # print(ordered_days_bubble[0][i],ordered_days_bubble[0][i-1])
              # print(i,i-1)
              count_1_end = 0
              # Calculate the additional frequency.
              for k in range(count_1, len(self.data[0])):
                count_1_end += 1
                # When the range between the previous 'end' and the new 'end
                # are the same, that is the additional frequencies and add
                # it onto the already known frequency which has the same start.
                # print(self.data[0][k],ordered_days_bubble[0][i][3])
                counter += 1
                if str(self.data[0][k]) == str(ordered_days_bubble[0][i][3]):
                  count_1 = count_1 + count_1_end - 1
                  break
              break
            # If the previous days 'end' is greater than the current days 'end'
            # add it onto the already calculated frequency.
            #else:
              # You have to calculate the frequency as normal.
              #print('Greater, doesnt help. Have to calculate range.')
          else:
            count_0 = j

        # Found the 'end' value, 'count_1' is set to 'j' minus 1.
        if str(self.data[0][j]) == str(ordered_days_bubble[0][i][3]): # str, int
          count_1 = j
          # Breaks the loop and starts a new one at the next 'start' value at
          # ordered_days_bubble[0][i][2] avoiding unneccessary iterations.
          break
        # 'counter' is incremented for performance evaluations.
        counter += 1
      # 'count_0' through 'count_1' is A1.csv 'start' and 'end'.
      # print(ordered_days_bubble[0][i])
      # print(count_0, ':', count_1)
      # These are the original P1.csv 'Day_ID'.
      # print(self.data[0][count_0], ' : ', self.data[0][count_1])
      # A1.csv 'count_0' and 'count_1' are the start and end 'Time_ID'
      # similar to P1.csv 'Day_ID'. 'activity_frequency' is the difference
      # between 'count_1' and 'count_0'.
      time_difference = count_1 - count_0
      ordered_days_bubble[0][i].append(count_0)
      ordered_days_bubble[0][i].append(count_1)
      ordered_days_bubble[0][i].append(time_difference)
      activity_frequency_list.append(ordered_days_bubble[0][i])
    # print(counter)
    # print(len(ordered_days_bubble[0]),len(self.data[0]))
    return activity_frequency_list

  # Function to find the mean of each painful day group.
  def mean_reverse_days(self,frequency_day_sort):
    # The loop requires a boilerplate value to complete all iterations.
    frequency_day_sort.append(['z',0,0,0,0,0,0])
    # print(frequency_day_sort[0],0)
    # The sum and count starts at the first value, otherwise it's not included.
    frequency_sum = frequency_day_sort[0][6]
    frequency_count = 1
    mean_list = []
    splice_list = [0]
    # Find the mean of each day before the pain.
    for j in range(len(frequency_day_sort)):
      # Skip the last value
      if frequency_day_sort[j-1] == frequency_day_sort[-1]:
        continue
      # If the reverse day column is different than the previous, calculate the mean.
      elif frequency_day_sort[j-1][1] != frequency_day_sort[j][1]:
        splice_list.append(j)
        frequency_mean = round(frequency_sum / frequency_count,2)
        mean_list.append([frequency_day_sort[j-1][1],frequency_mean])
        # print(frequency_sum, frequency_count, frequency_mean)
        # print()
        # print(frequency_day_sort[j],j)
        # Reset the 'frequency_sum' and 'frequency_count' to the current value.
        frequency_sum = frequency_day_sort[j][6]
        frequency_count = 1
      # If the reverse days are the same, increment
      # the 'frequency_sum' and 'frequency_count'.
      elif frequency_day_sort[j-1][1] == frequency_day_sort[j][1]:
        # print(frequency_day_sort[j],j)
        frequency_sum += frequency_day_sort[j][6]
        frequency_count += 1
    return [mean_list,splice_list]

# Usage.
def A1_daily_RGB_graph(P1_vert,P1_vert_predictions,A1_vert):
  A1_Graphs_sort = Graphs_sort(A1_vert)
  # Attempting to save time in calculating frequency of activiites before
  # the erroneous value observation.
  # day_list = [3,5,7,10,30]
  day_list = [30,10,7,5,3]
  count = 0
  days_pain = []
  days_not_pain = []

  # Loop returns the bodily part, number of days, and erroneous pain or
  # stamina values start and end from the erroneous observation minus
  # number of days.
  for i in P1_vert[3:]:
    reverse_days = A1_Graphs_sort.erroneous_values(i)

    if len(reverse_days[0]) > 2:
      days_pain += reverse_days[0]
      days_not_pain += reverse_days[1]

      # Returns 'day_list' before errouneous 'Pain' rows.
      A1_frequency_list = A1_Graphs_sort.day_ID_range(day_list,reverse_days[0])
      # Reverse by the group [n...,7,5,3] to [3,5,7...n].
      A1_frequency_group_sort = sorted(A1_frequency_list, key=lambda x: x[1])
      # Sort the categories by the day.
      A1_frequency_category_sort = sorted(A1_frequency_group_sort, key=lambda x: x[3])
      ordered_days_pain += A1_frequency_category_sort[1:]
      # Sorts the list for 'start' using bubble sort since it's already almost sorted.
      day_bubble = A1_Graphs_sort.bubble_sort(A1_frequency_list[0],A1_frequency_list[1])
      # day_bubble = sorted(A1_frequency_list[0], key=lambda x: x[2])
      ordered_days_pain += day_bubble[0]
      count += day_bubble[1]

    # Sorts each category using 'start'. Built-in 'sorted()' does the same thing.
    # ordered_days = sorted(ordered_days, key=lambda x: x[2])
    ordered_days_bubble = A1_Graphs_sort.bubble_sort(ordered_days_pain,count)
    # Python sort is nearly identical to Bubble Sort (or Insertion) in this case.
    # The lists already almost sorted and those algorithms are O(n) in best case
    # and uses less space than merge sort with O(1) vs O(n). At 10,000,000,000
    # 'activities', run time is around 35 hours.

    # print(ordered_days_bubble[0])
    # print(ordered_days_bubble[1]) # count = 2175

    # It's being sorted to save time calculating the frequency 'n' number of days
    # before the erroneous pain observation in A1.csv.
    # Saves from ~52,000 to ~12,000 iterations.
    A1_activity_frequency = A1_Graphs_sort.dayid_2_timeid(ordered_days_bubble)
    # Sort by number of days before pain to make iterations easier.
    A1_frequency_day_sort = sorted(A1_activity_frequency, key=lambda x: x[1])
    # Find the mean by 'day_list = [3,5,7,10,30]'
    A1_mean_reverse_day = A1_Graphs_sort.mean_reverse_days(A1_frequency_day_sort)
    # Sorts each 'Day' group alphabetically and from [30,10,7,5,3,] to the opposite.
    A1_sorted_category = []
    for j in range(len(A1_mean_reverse_day[1])):
      if j == (len(A1_mean_reverse_day[1])-1):
        break
      # Splicing at the days in reverse [3,5,7..etc] based on 'A1_mean_reverse_day'.
      start = A1_mean_reverse_day[1][j]
      end = A1_mean_reverse_day[1][j+1]
      data_slice = A1_activity_frequency[start:end]
      sorted_category = sorted(data_slice, key=lambda x: x[0])
      sorted_day_list = sorted(sorted_category, key=lambda x: x[1])
      A1_sorted_category += sorted_day_list
    # Sort the categories by the day.
    A1_frequency_category_sort = sorted(A1_sorted_category, key=lambda x: x[5])

A1_daily_RGB_graph(P1_vert,P1_vert_predictions,A1_vert)

# Part F: Predictions vs Observed pain values using classification metrics.
def P1_Classification_RGB_graph(P1_vert,P1_vert_predictions):

  # B1.csv - Nutrition - binary calories high and low -> above/below 2500
  # - Mean number of activities per day over 3-14 days
  #     - Exclude 09/09-09/13 since it was recorded with excessive detail.
  # - Not stretching in the one or two days afterward.
  # - Stretching too frequently in the one or two days afterward.

  # Days of Interest :
  # Stamina for 08/27-0903 (value 4) except 08/29 (value 2) and abs (4) on 08/31.
      # Stamina for 09/13. Exclude 09/09-09/13 since it was recorded with excessive detail.
  # Stamina for 09/19-09/22 (value 4) except 09/21 (value 2).
  # The goal is to find an appropriate balance for exercise and not moving
  # by examining the frequency of Activities before these decreases.

  # 'Day_ID' remove 49-53 for average graphing because they were recorded
  # differently and induce outliers. ['909','910','911','912','913']
  for P1 in range(len(P1_vert_predictions)):
    del P1_vert_predictions[P1][50:55]
    del P1_vert[P1][50:55]
  # Remove these dates: ['909','910','911','912','913']
  # in A1_vert[0], A1_vert[3]
  del A1_vert[0][271:326]
  del A1_vert[3][271:326]
  # Accuracy, Precision, Recall, F1
  # Uses F1 since RMSE is for regression prediction models. The pain scale
  # is numerical and is equivilent to nominal categories.
  title_full = ['','','',
  'Stamina',
  'Feet','Ankle','Calves',
  'Knees','Quadriceps','Gluteus','Groin',
  'Abdominals','Lower Back',
  'Latissimus Dorsi','Trapezius','Shoulders',
  'Chest','Triceps','Biceps',
  'Neck','Head']
  # todo classification_metrics
  # wilcoxon_rank_sum
  for i in range(3,len(P1_vert)):
    '''
    print('Pain Scale')
    print(P1_vert[i])
    print('Classification')
    class_met = classification_metrics(P1_vert[i],P1_vert_predictions[i])
    binary = class_met.binary_classification()
    print(binary[0])
    print()
    # i is the pain scale 'Day_ID' (1-101) for A1 (1-350ish) 'did'
    print(A1_vert[0]) # 'Day_ID
    print(A1_vert[1])
    print(A1_vert[6]) # 'Activity'
    print()
    '''

    A1_graphs_sort = eu.Graphs_sort(A1_vert)
    A1_filter = A1_graphs_sort.filter_stop(A1_graphs_sort.data[6])

    '''
    A1_graphs_sort = Graphs_sort(data)
    A1_graphs_sort.filter_stop(A1_graphs_sort.data[])
    acc_binary = class_met.accuracy(binary[0])
    # header : print(P1_vert[i][0])
    print('Accuracy', ' = ', acc_binary)
    precision_binary = class_met.precision(binary[2],binary[3]) # tsp fp
    print('Precision', ' = ', precision_binary)
    print('tsp', ' ', binary[2])
    print('fp', ' ', binary[3])
    print()
    recall_binary = class_met.recall(binary[2],binary[4]) # tsp fn
    print('Recall', ' = ', recall_binary)
    print('tsp', ' ', binary[2])
    print('fp', ' ', binary[3])
    print()
    f1_score_binary = class_met.f1_score(binary[2],binary[3],binary[4]) # tsp fp fn
    print('F1 Score', ' = ', f1_score_binary)
    print('tsp', ' ', binary[2])
    print('fp', ' ', binary[3])
    print('fn', ' ', binary[4])
    print()
    print()
    print()
    '''

  return

# Part E and F: P1.csv with part F accuracy metrics, activity reverse by group, 
# and activity reverse by entry.
def A1_daily_RGB_graph(P1_vert,P1_vert_predictions,A1_vert):
  # Edited five days to remove overly detailed entries called 'A1-small.csv'
  # original is 'A1.csv' - ['909','910','911','912','913']

  A1_Graphs_sort = Graphs_sort(A1_vert)
  days_pain = []
  days_not_pain = []
  all_days = []
  # Loop returns the bodily part, number of days, and erroneous pain or
  # stamina values start and end from the erroneous observation minus
  # number of days. Also returns the days that were not a pain.
  for i in P1_vert[3:]:
    reverse_days = A1_Graphs_sort.erroneous_values(i)
    if len(reverse_days[0]) > 2:
      days_pain += reverse_days[0]
      days_not_pain += reverse_days[1]
      all_days += reverse_days[2]

  # Returns the frequency of activities for every day (discards the first 10).
  A1_activity_splice = A1_Graphs_sort.activity_frequency_splice()
  A1_activity_pain = A1_Graphs_sort.activity_reverse(days_pain,A1_activity_splice)
  A1_activity_not_pain = A1_Graphs_sort.activity_reverse(days_not_pain,A1_activity_splice)
  A1_activity_all = A1_Graphs_sort.activity_reverse(all_days,A1_activity_splice)

  # Calcualtes the mean for each reverse day means, then graph '3' on x with the sum
  # of the erroneous means divided by their count on the y against non pain
  # means and all the days mean. 'y' is labeled 'Activity Frequency'.
  A1_pain_group_mean = A1_Graphs_sort.activity_group_mean(A1_activity_pain)
  A1_not_pain_group_mean = A1_Graphs_sort.activity_group_mean(A1_activity_not_pain)
  A1_all_group_mean = A1_Graphs_sort.activity_group_mean(A1_activity_all)

  # Graphing section.
  # Summarized pain, not pain, and all data means for 3,5,7,10,and 30 days before the event.
  A1_graph_rgb = Graphs_rgb([])
  A1_reverse_mean_category = A1_graph_rgb.rgb_reverse_category(A1_pain_group_mean,A1_not_pain_group_mean,A1_all_group_mean)

  # Mean of every reverse splice for each day.
  A1_day_mean_category = A1_graph_rgb.rgb_reverse_day_mean(A1_activity_pain,P1_vert_predictions)

  # Graphing the prediction and observation along with classification metrics.
  # Usage is from 'P1_Classification_RGB_graph()'
  title_full = [#'','','',
  'Stamina',
  'Feet','Ankle','Calves',
  'Knees','Quadriceps','Gluteus','Groin',
  'Abdominals','Lower Back',
  'Latissimus Dorsi','Trapezius','Shoulders',
  'Chest','Triceps','Biceps',
  'Neck','Head']
  for j in range(3,len(P1_vert_predictions)):
    class_met = classification_metrics(P1_vert[j],P1_vert_predictions[j])
    binary = class_met.binary_classification()
    acc_binary = class_met.accuracy(binary[0])
    precision_binary = class_met.precision(binary[2],binary[3]) # tsp fp
    recall_binary = class_met.recall(binary[2],binary[4]) # tsp fn
    f1_score_binary = class_met.f1_score(binary[2],binary[3],binary[4]) # tsp fp fn
    classification_list = [title_full[j-3],P1_vert[j][0],acc_binary,precision_binary,recall_binary,f1_score_binary]
    # P1_graph_rgb = Graphs_rgb([])
    # P1_graph_rgb.rgb_prediction_observation(P1_vert_predictions[j],P1_vert[j],P1_vert_predictions[1],classification_list)
  return

# One month of May, 2024 observations
P0_path = "/content/P0.csv"
B0_path = "/content/B0.csv"
# A0 is a TSV because there are blank cells
A0_path = "/content/A0.tsv"
P0_unflipped_col = ['ID','Date','Day','Stm']
# P0_vert = CSV_running(P0_path,P0_unflipped_col)
# B0_vert = CSV_running(B0_path,0)
# A0_vert = CSV_running(A0_path,0)
# Four months of July-October observations
# P1.csv contains the pain scale and B1.csv contains the food records
P1_path = "/content/P1-Observations-PaperFigures.csv"
P1_path_predictions = "/content/P1-Prediction-PaperFigures.csv"
# B1_path = "/content/B1.csv"
# A1 is a tsv because of blank cells
# A1_path = "/content/A1.tsv" # The full dataset.
A1_path = "/content/A1-small.tsv"
# List of columns to not be flipepd
P1_unflipped_col = ['ID','Date','Day','Stm','Notes','Notes2']
P1_vert = CSV_running(P1_path,P1_unflipped_col)
P1_vert_predictions = CSV_running(P1_path_predictions,P1_unflipped_col)
# B1_vert = CSV_running(B1_path,0)
A1_vert = CSV_running(A1_path,0)

# P1_RGB_graph(P1_vert)
# B1_RGB_graph(B1_vert)
# A0_RGB_graph(A0_vert)
# A1_RGB_graph(A1_vert)
# P1_Classification_RGB_graph(P1_vert,P1_vert_predictions)
A1_daily_RGB_graph(P1_vert,P1_vert_predictions,A1_vert)

'''





