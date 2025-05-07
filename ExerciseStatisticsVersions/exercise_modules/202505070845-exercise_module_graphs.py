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
'''
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
'''

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
