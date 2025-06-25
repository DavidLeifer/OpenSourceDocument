# Interesting method to print callable methods on an object.
# print(dir(left_right))
# Example is obj.__class__ that prints the data type without using the type(obj) method
# type_check = str(left_right.__class__)

#####################################################################################
# Part A: CSV or TSV parser class to open the file and parse the values into a list #
#####################################################################################
class CSV_Parser:
  # Initialize the input variables
  def __init__(self, data_path):
    self.data_path = data_path

  def file_opener(self):
    with open(self.data_path, "r") as data_open:
      data_read = data_open.read()
      return data_read
  # Index the commas and line breaks
  def comma_index(self, open_file, path, column_len):
    data_comma_place = [0]
    column_pl_len = 0
    path_split = [ext for ext in path]
    path_ext = "".join(path_split[-3:])
    for i in range(len(open_file)):
      data1_col1 = open_file[i]
      if path_ext == "csv":
        if data1_col1 == ",":
          data_comma_place.append(i)
          data_comma_place.append(i+1)
      elif path_ext == "tsv":
        if data1_col1 == "\t":
          data_comma_place.append(i)
          data_comma_place.append(i+1)
      if data1_col1 == "\n":
        data_comma_place.append(i)
        data_comma_place.append(i+1)
        # If you want to use the function to get the column width, set to 1
        if column_len == 1:
          col_width = len(data_comma_place)
          return col_width
          break
    last_val = data_comma_place[-1] + 2
    data_comma_place.append(last_val)
    return data_comma_place
  # Splitting the csv characters into list of words based on indexed comma position
  def csv_value_list(self, data_comma_out, open_file, col_width, col_head):
    j = col_head
    data_val_list = []
    for i in range(len(data_comma_out)):
      if j >= len(data_comma_out):
        break
      comma_strt = data_comma_out[j]
      j += 1
      comma_end = data_comma_out[j]
      #print(comma_strt, "and ", comma_end)
      j += 1
      data_val_list.append(open_file[comma_strt:comma_end])
      j = j + (col_width * 2)
    return data_val_list
  # Flipping the columns from high to low for readability
  # If the original value was 5, set it to equal 0 (no pain)
  # If the original value was 0, set it to equal to 5 (high pain) etc.
  # If none of those things are true, append the string (for the column header)
  def csv_flipper(self, csv_list, col_width):
    csv_flipped = []
    for i in csv_list:
      if i == str(5):
        n = str(1)
        csv_flipped.append(n)
      elif i == str(4):
        n = str(2)
        csv_flipped.append(n)
      elif i == str(3):
        n = str(3)
        csv_flipped.append(n)
      elif i == str(2):
        n = str(4)
        csv_flipped.append(n)
      elif i == str(1):
        n = str(5)
        csv_flipped.append(n)
      else:
        csv_flipped.append(i)
    return csv_flipped

######################################################
# Part B: Get descriptive statistics of each column. #
######################################################
class Statistics:
  # Returns a dictionary with the header and mean
  def mu(self, col_list):
    total = 0
    counter = 0
    # Column has to have a header
    for i in col_list[1:]:
      if i == "NA":
        continue
      total = total + float(i)
      counter += 1
    mean = total / counter
    header_mean = [col_list[0], mean]
    return header_mean
  # Returns the 2-4 moment of the distribution
  # Different than Google Sheets sample vs population
  def mnt(self, header, mean, col_list):
    col_1 = len(col_list) - 1
    stn = 0
    skew = 0
    kurt = 0
    counter = 0
    for i in col_list[1:]:
      if i == "NA":
        continue
      # secondary todo: doesn't work with decimals
      n1 = int(i) - mean
      n1_sqr = n1 ** 2
      n1_cube = n1 ** 3
      n1_quad = n1 ** 4
      stn = stn + n1_sqr
      skew = skew + n1_cube
      kurt = kurt + n1_quad
      counter += 1
    # Sample variance (n-1)
    # Population variance (n)
    counter = (counter - 1)
    stn_small_sqr = float(stn) / counter
    stn_small = stn_small_sqr ** .5
    skew_small_sqr = float(skew) / counter
    skew_small = skew_small_sqr / (stn_small ** 3)
    kurt_small_sqr = float(kurt) / counter
    kurt_small = kurt_small_sqr / (stn_small ** 4)
    return [header, stn_small, skew_small, kurt_small]
  # Covariance and correlation
  def covar(self, x_mean, y_mean, col_1_list, col_2_list):
    col_len = len(col_1_list) - 1
    covar = 0
    x1y1_sum = 0
    counter = 0
    for i in range(col_len):
      #if i == col_len-2:
      #  break
      if col_1_list[i+1] == "NA":
        continue
      if col_2_list[i+1] == "NA":
        continue
      # print(i+3,i)
      # print("x_mean: ", x_mean[1], "x_value: ", col_1_list[i+1])
      x1 = float(col_1_list[i+1]) - x_mean[1]
      y1 = float(col_2_list[i+1]) - y_mean[1]
      x1y1 = x1 * y1
      x1y1_sum = x1y1_sum + x1y1
      counter += 1
    covar = x1y1_sum / counter
    return covar
  def cor(self, covar, col_1_stnd, col_2_stnd):
    stnd12 = col_1_stnd * col_2_stnd
    cor = covar / stnd12
    return cor

######################################################
# Part C: Data visualization with a timeseries graph #
######################################################
# 'Graph' class accepts three variables: verticle arranged 'data',
# the date column'date_col_num', and the data column 'data_col_num'
class Graph:
  # Initialize the input variables
  def __init__(self, data, date_col_num, data_col_num):
    self.data = data
    self.date_col_num = date_col_num
    self.data_col_num = data_col_num
  def hi_lo(self, data_col_num):
    # The date and date column to be used
    data_col = self.data[data_col_num]
    data_col_len = len(data_col)
    # High and low of values
    hi_lo_count = 1
    hi = data_col[1]
    lo = data_col[1]
    for e in range(len(data_col[1:])):
      hi_lo_count += 1
      if hi_lo_count == (len(data_col[1:]) + 1):
        break
      if hi < data_col[hi_lo_count]:
        hi = data_col[hi_lo_count]
      if lo > data_col[hi_lo_count]:
        lo = data_col[hi_lo_count]
    return [hi, lo]
  def binned(self, hi_lo):
    # high value (5 in this case or hi_lo[0])
    # The date and date column to be used
    # TODO it works but is not resuable for other data ranges
    date_col = self.data[self.date_col_num]
    data_col = self.data[self.data_col_num]
    data_col_len = len(data_col)

    fiver = []
    fourer = []
    threer = []
    twoer = []
    oner = []
    lol_stm_date = []
    counter = 1
    # Binned with date value
    for i in range(data_col_len):
      P0_column = self.data[self.data_col_num]
      if counter == len(self.data[0]):
        break
      # secondary todo:
      if P0_column[counter] == "NA":
        counter += 1
        continue
      if float(P0_column[counter]) == 5:
        fiver.append([date_col[counter], P0_column[counter]])
      elif float(P0_column[counter]) == 4:
        fourer.append([date_col[counter], P0_column[counter]])
      elif float(P0_column[counter]) == 3:
        threer.append([date_col[counter], P0_column[counter]])
      elif float(P0_column[counter]) == 2:
        twoer.append([date_col[counter], P0_column[counter]])
      elif float(P0_column[counter]) == 1:
        oner.append([date_col[counter], P0_column[counter]])
      counter += 1
    # Combining the binned data into one dictionary
    lol_date_stm = [fiver, fourer, threer, twoer, oner]
    return lol_date_stm

  def time_series(self, date_hi_lo, lol_date_stm):
    date_col = self.data[self.date_col_num]
    # Base of the month, plus 00 i.e. 500
    date_base = int(date_hi_lo[1]) - 1
    # The number of spaces is the 'day' (date - month) - 'prev_day_space_int'
    # The difference between the values is multiplied by ' ' for each 5,4,3,2,1
    # Value with a '+' character marking the position
    spacer = []
    prev_day_space_int = 0
    for i in lol_date_stm:
      spacer_mid = []
      for ii in i:
        # ii is [date, value] in order
        # an if else statement
        # 7 starts at 22, 31 days
        # 8 30 days
        # 9 30 days
        # 10 31 days
        day = int(ii[0]) - date_base
        # print(day)
        day_count = day - prev_day_space_int
        day_space_str = ((day_count-1)*2) * " "
        spacer_mid.append(day_space_str)
        prev_day_space_int = day
      prev_day_space_int = 0
      spacer.append(spacer_mid)
    y_val = [y for y in range(len(spacer),0,-1)]
    return [spacer, y_val]
  def time_series_print(self,spacer,y_val):
    date_col = self.data[self.date_col_num]
    for j,k in zip(spacer,y_val):
      # y values
      print(k,end=" ")
      for l in j:
        print(l,end="")
        print("+",end=" ")
      print()
    # x values
    for m in range(len(date_col[0])-1):
      print("  ",end="")
      for n in date_col[1:]:
        print(n[m], end=" ")
      print()
    return
  def time_series_write(self,header,txt_out,spacer,y_val):
    # Open the output file location and write data to the txt
    date_col = self.data[self.date_col_num]
    file_output = open(txt_out, "w")
    file_output.write(header)
    file_output.write("\n")
    file_output.write("\n")
    # y values
    for j,k in zip(spacer,y_val):
      file_output.write(str(k) + " ")
      for l in j:
        file_output.write(str(l))
        file_output.write("+" + " ")
      file_output.write("\n")
    # x values
    for m in range(len(date_col[0])-1):
      file_output.write("  ")
      for n in date_col[1:]:
        file_output.write(str(n[m]) + " ")
      file_output.write("\n")
    file_output.close()
    return

###############################################
# Part D: Data visualization with a RGB graph #
###############################################
# Matplotlib for color because otherwise you would have
# to write hardware code to avoid using Python or C libraries.
class Graphs_rgb:
  # Initialize the input variables
  def __init__(self, data):
    self.data = data

  # Four utility functions daisy chained to rgb_timeseries_bar()
  # Minor todo: unchain them lol
  def rgb_timeseries_mean(self,formatted_data_group):
    # Input is list (1-4) of lists (95) of each columns values without NA
    # i.e. [[dist1],[dist1],[dist1], etc]
    date_col_len = len(formatted_data_group[0])
    group_mean = []
    # Length of the column (95 without "NA" as filtered in rgb_date_time)
    for i in range(date_col_len):
      row_list = []
      # Length of columns to be summarized (1-4) 95 row_list values
      for j in range(len(formatted_data_group)):
        row_list.append(formatted_data_group[j][i])
      # Mean at each day for each group
      row_count = len(row_list)
      row_sum = sum(row_list)
      row_mean = row_sum / row_count
      group_mean.append(row_mean)
    return group_mean

  def rgb_date_time(self,csv_groups,date_col):
    day_count = len(self.data[1])
    k = 0
    group_dist = []
    for i in csv_groups:
      dist0 = []
      dist1 = []
      dist2 = []
      for j in range(day_count):
        if j == (day_count-1):
          break
        if i[j+1] == "NA":
          continue
        else:
          # Formatting the date
          # year = 2024
          date_length = date_col[j+1]
          if len(date_length) < 4:
            month = date_length[:1]
            day = date_length[1:]
          else:
            month = date_length[:2]
            day = date_length[2:]
          date_format0 = month + "/" + day
          dist0.append(date_format0)
          dist1.append(int(i[j+1]))
          date_format1 = month + "/" + day
          if int(day) % 5 == 0:
            dist2.append(date_format1)
          else:
            dist2.append(" ")
            continue
      group_dist.append([dist0,dist1,dist2])
      k += 1
    return group_dist

  def rgb_P1_style(self,final_title,line):
    plt.yticks(range(1,6))
    if final_title == 'Stamina':
      plt.ylabel(final_title)
    else:
      plt.title(final_title)
      plt.ylabel("Pain")
      if line == 1:
        plt.legend()
    return

  def rgb_B1_style(self,final_title,line):
    if final_title == 'Calories':
      plt.yticks(range(1200,4500,400))
      plt.ylabel("Intake")
      plt.title(final_title)
    elif final_title == 'Alcohol Servings':
      plt.yticks(range(0,16))
      plt.title("Alcohol")
      plt.ylabel("Servings")
    elif final_title == 'Exercise':
      plt.yticks(range(0,3))
      plt.title(final_title)
      # plt.ylabel("Calories Out")
      plt.text(.1,.5, "Calories Out \n2 = 250+ \n1 = 1-249",
         bbox={'facecolor': 'white', 'alpha': .75, 'pad': 10})
    else:
      plt.yticks(range(1,6))
      if line == 1:
        plt.title("Nutrients")
      else:
        plt.title(final_title)
      plt.ylabel("Intake")
      plt.legend()
    return

  # Bar plots for each column
  def rgb_timeseries_bar(self,title_full,start_val,P1_B1):
    for i in range(start_val,len(title_full)+start_val):
      formatted_csv_group = self.rgb_date_time([self.data[i]],self.data[1])
      fig, ax = plt.subplots(1, 1, layout='constrained', figsize=(15, 5))
      ax.bar(formatted_csv_group[0][0], formatted_csv_group[0][1], width=0.8, align='edge')
      final_title = title_full[i-start_val]
      # Format the title, yticks, and ylabel
      if P1_B1 == 0:
        self.rgb_P1_style(final_title,0)
      elif P1_B1 == 1:
        self.rgb_B1_style(final_title,0)
      elif P1_B1 == 2:
        pass
        # self.rgb_A0_style(final_title,0)
      plt.xticks(formatted_csv_group[0][0], labels=formatted_csv_group[0][2])
      plt.margins()
      plt.grid()
      # plt.savefig(final_title + '.jpg')
    return

  # Returns a date list without blanks
  def rgb_date_list(self):
    # date_literal is 0-30 days
    date_literal = []
    # Makes a list with only the dates
    for i in range(1,len(self.data[2])):
      if len(self.data[2][i]) > 0:
        date_literal.append(self.data[2][i])
    return date_literal

  # Multiple lines same graphs.
  def rgb_timeseries_line(self,title_full,start_val,groups_num,title_label,P1_B1):
    data = self.data
    # secondary todo: name instead of number position
    j = 1
    # Adding multiple lines to a single plot by group with formatting
    for i in range(len(groups_num)):
      subset0 = groups_num[i:j][0]
      if subset0 == groups_num[-1]:
        break
      subset1 = groups_num[i+1:j+1][0]
      csv_groups = data[subset0:subset1]
      formatted_csv_group = self.rgb_date_time(csv_groups,self.data[1])
      # Format subplot
      fig, ax = plt.subplots(1, 1, layout='constrained', figsize=(15, 5))
      # Get the formatted_csv_group second list of values in each group
      dist1_list = [dist1[1] for dist1 in formatted_csv_group]
      # First 3 columns in data are ID, while the title list isn't.
      # Subtract each subset by the start_val of the values (excluding date, id, etc)
      title_group = title_full[(subset0-start_val):(subset1-start_val)]
      # y = each dist1 in formatted_csv_group, x = every date value, x labels = every 5th date value
      for k in range(len(dist1_list)):
        ax.plot(formatted_csv_group[0][0], dist1_list[k], label=title_group[k], linewidth=4)
        # Format the title, yticks, and ylabel
        if P1_B1 == 0:
          self.rgb_P1_style(title_label[j-1],1)
        elif P1_B1 == 1:
          self.rgb_B1_style(title_label[j-1],1)
      # Chart formatting and save
      plt.xticks(formatted_csv_group[0][0], labels=formatted_csv_group[0][2])
      plt.grid()
      plt.margins()
      #plt.savefig(title_label[j-1] + '.jpg')
      j += 1
    return

  # Summarized with mean
  def rgb_timeseries_small(self,csv_groups_num,legend_label,ax):
    csv = self.data
    j = 1
    for i in range(len(csv_groups_num)):
      subset0 = csv_groups_num[i:j][0]
      if subset0 == csv_groups_num[-1]:
        break
      subset1 = csv_groups_num[i+1:j+1][0]
      csv_groups = csv[subset0:subset1]
      # Builds an array to skip NA and format the date
      # [[[dist0],[1],[2]],[[dist0],[1],[2]], etc]]]
      formatted_csv_group = self.rgb_date_time(csv_groups,self.data[1])
      # Get the formatted_csv_group second list of values in each group
      dist1_list = [dist1[1] for dist1 in formatted_csv_group]
      # Summarize each body part's group with mean
      dist1_group_mean = self.rgb_timeseries_mean(dist1_list)
      # y = group mean, x = every date value, x labels = every 5th date value
      # Specified in rgb_date_time function
      ax.plot(formatted_csv_group[0][0], dist1_group_mean, label=legend_label[j-1], linewidth=4)
      plt.xticks(formatted_csv_group[0][0], labels=formatted_csv_group[0][2])
      j += 1
    return

  # A01.csv frequency of merged 'Activity'.
  def rgb_timeseries_frequency(self,data):
    y = data[0][-11:]
    x = data[1][-11:]
    fig, ax = plt.subplots(figsize=(15, 17))
    bars = ax.barh(x,y,height=.5)
    for i in range(len(y)):
      plt.text(y[i]-2.5, x[i], str(y[i]), color='White', fontsize=12, ha='center', va='center', bbox={'facecolor': 'none','linewidth': 0})
    plt.title('Activity Frequency July-October, 2024', pad=50, fontsize=20)
    ax.tick_params(axis='both', labelsize=14)
    ax.tick_params(axis='y', pad=50)
    ax.xaxis.set_ticks_position('top')
    plt.yticks(x, labels=x, ha='center')
    plt.grid(axis='x')
    plt.margins(y=0.01)
    # plt.savefig('A1-0 Activity Frequency July-October, 2024' + '.jpg')
    return

  # A01.csv duration of merged 'Activity' hours.
  def rgb_timeseries_duration(self,data):
    y = [round(j) for j in data[0][-11:]]
    x = data[1][-11:]
    fig, ax = plt.subplots(figsize=(15, 17))
    bars = ax.barh(x,y,height=.5)
    for i in range(len(y)):
      plt.text(y[i]-2.5, x[i], str(y[i]), color='White', fontsize=12, ha='center', va='center', bbox={'facecolor': 'C0','linewidth': 0})
    plt.title('Activity Duration July-October, 2024', pad=50, fontsize=20)
    plt.xlabel('Hours', fontsize=14)
    ax.tick_params(axis='y', pad=50, labelsize=14)
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')
    plt.yticks(x, labels=x, ha='center')
    plt.grid(axis='x')
    plt.margins(y=0.01)
    # plt.savefig('A1-0 Activity Duration July-October, 2024' + '.jpg')
    return

  # A01.csv mean of merged 'Activity' frequency / (sum of minutes)
  def rgb_timeseries_mean(self,data):
    y = [round(j,2) for j in data[0][-11:]]
    x = data[1][-11:]
    fig, ax = plt.subplots(figsize=(15, 17))
    bars = ax.barh(x,y,height=.5)
    for i in range(len(y)):
      plt.text(y[i]-.25, x[i], str(y[i]), color='White', fontsize=12, ha='center', va='center', bbox={'facecolor': 'C0','linewidth': 0})
    plt.title('Total Activity Average\nJuly-October, 2024', pad=50, fontsize=20)
    plt.xlabel('Hours', fontsize=14)
    ax.tick_params(axis='y', pad=50, labelsize=14)
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')
    plt.yticks(x, labels=x, ha='center')
    plt.grid(axis='x')
    plt.margins(y=0.01)
    # plt.savefig('A1-0 Total Activity Average July-October, 2024' + '.jpg')

  # A01.csv daily mean.
  def rgb_timeseries_daily_mean(self,data):
    y = [round(j) for j in data[0][-11:]]
    x = data[1][-11:]
    fig, ax = plt.subplots(figsize=(15, 17))
    bars = ax.barh(x,y,height=.5)
    for i in range(len(y)):
      plt.text(y[i]-1.15, x[i], str(y[i]), color='White', fontsize=12, ha='center', va='center', bbox={'facecolor': 'C0','linewidth': 0})
    plt.title('Daily Activity Average\nJuly-October, 2024', pad=50, fontsize=20)
    plt.xlabel('Minutes', fontsize=14)
    ax.tick_params(axis='y', pad=50, labelsize=14)
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')
    plt.yticks(x, labels=x, ha='center')
    plt.grid(axis='x')
    plt.margins(y=0.01)
    # plt.savefig('A1-0 Daily Activity Average July-October, 2024' + '.jpg')

  ##############################################################################'
  # Early iterations of A0 graphs.
  # Graph 0) Occurrence of each activity. Includes every Activity.
  def graph_0_frequency(self):
    '''
    # The activities with multiple same day were inconsistently collected.
    x = [i[0][0] for i in A0_sort_bin[1:]] # or A0_sort_unique
    y = [len(k[1:]) for k in A0_sort_bin[1:]] # number of each activity
    fig, ax = plt.subplots(figsize=(12, 15))
    ax.bar(x, y, linewidth=2)
    plt.title('Number of Activities, May 2024')
    plt.xticks(x, labels=x, rotation=90, ha='right', fontsize=10)
    plt.grid()
    plt.margins()
    # plt.xlabel('Activity')
    # plt.legend()
    # plt.savefig('AZ Activity' + '.jpg')
    plt.show()
    '''
    return
  # Graph 1) Duration of each activity. Includes every Activity duration in hours.
  def graph_1_duration(self):
    '''
    # One option is to sort by the number in each bin to arrange by frequency.
    # sort_unique_len = []
    # for i in range(len(A0_sort_bin)):
    #   sort_unique_len.append([A0_sort_bin[i][0][0],len(A0_sort_bin[i][1:])])
    # sort_unique_int = sorted(sort_unique_len, key=lambda sort_sub: sort_sub[1],
                               # reverse=True

    # todo use a list of lists in the sort functions (i.e. [x,y])
    # sort_int = merge_sort_int(A0_sort_bin)
    # x = [i[0] for i in sort_unique_int[1:]] # or A0_sort_unique
    # y = [k[1] for k in sort_unique_int[1:]]

    x = [i[0][0] for i in A0_sort_bin[1:]] # or A0_sort_unique
    y = []
    for j in A0_sort_bin[1:]:
      y_labeled = []
      for m in j[1:]:
        y_labeled.append(int(m[2]))
      y.append(round(sum(y_labeled) / 60,4))

    # Remove rest and read
    y_count = len(y)
    y_sum = sum(y)
    y_mean = round(y_sum / y_count, 4)
    yy = y
    count_2 = 0
    for xx in yy:
      num = round(xx - y_mean, 4)
      # Outliers greater than or less than 30
      if num > 30 or num < -30:
        # print(count_2, xx, '-', y_mean, num)
        x.pop(count_2)
        y.pop(count_2)
      count_2 += 1

    fig, ax = plt.subplots(figsize=(15, 12))
    ax.bar(x, y, linewidth=2)
    plt.title('Duration of Activities, May 2024')
    plt.xticks(x, labels=x, rotation=90, ha='center', fontsize=10)
    plt.grid()
    plt.margins()
    plt.ylabel('Hours')
    plt.text(.1,33.5, "Exceeded 50 hours: Rest and Sleep",
          bbox={'facecolor': 'white', 'alpha': .75, 'pad': 10})
    # plt.legend()
    # plt.savefig('AZ Activity Duration' + '.jpg')
    plt.show()
    '''
    return

  def heatmap_graph_0(self,x,y,values,title,save):
    fig, ax = plt.subplots()
    # Create the heatmap using pcolormesh
    heatmap = ax.pcolormesh(values, cmap='gist_earth')
    # Add a colorbar
    fig.colorbar(heatmap)
    # Show all ticks and label them with the respective list entries
    ax.set_xticks(range(len(x)), labels=x, ha='left')
    ax.set_yticks(range(len(y)), labels=y, va='bottom')
    # Loop over data dimensions and create text annotations. e for spacing.
    # plt.figure(figsize=(30,30), dpi=500)
    fig.set_dpi(300)
    e = .5
    for i in range(len(y)):
      for j in range(len(x)):
        text = ax.text(j+e, i+e, round(values[i][j],1), ha="center", va="center", fontsize=12, fontweight=500
                       , color="#FFFFFF", path_effects=[matplotlib.patheffects.withStroke(linewidth=1, foreground="#000000")]
                       )
    ax.set_title(title)
    if save == 1:
      plt.savefig('A1-0 ' + title + '.jpg')
    return

  ##############################################################################'
  # Graphing section to visualize the average number of activities before pain.
  
  # Mean of all days using the daily mean by 3,5,7,...etc. before pain.
  def rgb_reverse_category(self,pain,not_pain,all_data):

    x = [i[1] for i in pain]
    y1 = [j[0] for j in pain]
    y1n = [j[2] for j in pain]

    y2 = [k[0] for k in not_pain]
    y2n = [k[2] for k in not_pain]

    y3 = [l[0] for l in all_data]
    y3n = [l[2] for l in all_data]

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y1, label='Pain', marker='+')
    plt.scatter(x, y2, label='Not Pain', marker='_')
    plt.scatter(x, y3, label='All Data', marker='.')
    plt.xlabel('Days in Reverse', fontsize=10)
    plt.ylabel('Mean Daily Activities', fontsize=10)
    plt.title('Activites Before Pain',fontsize=12)
    for iter, mean in enumerate(y1):
      if mean > 6.5:
        bx_pos = x[iter] - 1.5
        by_pos = mean - .1
      else:
        bx_pos = x[iter] + 1.5
        by_pos = mean + .1
      box_str = 'N. ' + str(y1n[iter])
      plt.text(
          bx_pos,
          by_pos,
          box_str,
          ha="center",
          va="bottom",
          size=8,
          bbox=dict(facecolor="white", edgecolor="black", boxstyle="round", alpha=0.75),
      )
    plt.xticks(x)
    plt.ylim(5.1,6.75)
    plt.grid()
    plt.margins(y=0.01)
    plt.legend(loc='upper center')
    plt.show()

    # plt.savefig('P1-0 Activity Frequency Mean July-October, 2024' + '.jpg')
    return

  # Prediction vs observation and accuracy, precision, F1 score.
  # Input is prediction, observation, date, classification scores.
  def rgb_prediction_observation(self,prediction,observation,date,classification_list):
    x = []
    y1 = []
    y2 = []
    y3 = []
    # Filter 'NA'.
    for j in range(1,len(prediction)):
      if len(date[j]) == 3:
        month = date[j][0:1]
        day = date[j][1:]
      else:
        month = date[j][0:2]
        day = date[j][2:]
      split_date = month + '/' + day
      if prediction[j] == 'NA' or observation[j] == 'NA':
        y1.append(None)
        y2.append(None)
        y3.append(None)
        x.append(split_date)
      else:
        if prediction[j] == observation[j]:
          #print(prediction[j],observation[j],date[j])
          y1.append(int(prediction[j]))
          y2.append(None)
          y3.append(None)
          x.append(split_date)
        else : # prediction[j] != observation[j]
          y1.append(None)
          y2.append(int(prediction[j]))
          y3.append(int(observation[j]))
          x.append(split_date)

    plt.figure(figsize=(18, 6))
    plt.scatter(x, y1, label='Same', marker='.')
    plt.scatter(x, y2, label='Prediction', marker='o')
    plt.scatter(x, y3, label='Observation', marker='o')
    plt.ylim(0,6)
    x_label = [i for i in x[::5]]
    plt.xticks(x_label, fontsize=8)
    plt.xlabel('Date (2024)', fontsize=10)
    if prediction[0] == 'Stm':
      by_pos = .8
      plt.ylabel('Stamina', fontsize=10)
      plt.legend(loc='lower left',fontsize=8,borderaxespad=1.2)
    else:
      by_pos = 5.75
      plt.ylabel('Pain', fontsize=10)
      plt.title(classification_list[0])
      plt.legend(loc='upper left',fontsize=8,borderaxespad=1.2)

    bx_pos = '10/26' # x[-1]
    box_label = ['','','Accuracy: ', 'Precision: ', 'Recall: ', 'F1 Score: ']
    box_str = ''
    for k in range(2,len(classification_list)):
      box_subset_str = box_label[k] + str(round(classification_list[k],2))
      if k < len(classification_list) - 1:
        box_str += box_subset_str + '\n'
      else:
        box_str += box_subset_str

    plt.text(
        bx_pos,
        by_pos,
        box_str,
        ha="left",
        va="top",
        size=8,
        bbox=dict(facecolor="white", edgecolor="grey", boxstyle="round,pad=0.5", alpha=0.5))
    plt.grid()
    plt.margins(y=0.01)
    return

  # All the erroneous pain dates with each daily mean for 3,5,7..etc.
  def rgb_reverse_day_mean(self,input_data,P1_data):
    # x = [i[1] for i in input_data] # Day_ID
    # Return the date
    # Sort the 'input_data' chronologically and include the date.
    input_date = []
    input_data_id = sorted(input_data, key=lambda y:y[1])
    for j in range(len(input_data_id)):
      splice = input_data_id[j][1] + 1
      input_data_j = input_data_id[j]
      input_data_j.append(P1_data[1][splice])
      input_date.append(input_data_j)
    # Sorting 'input_date' based on the second value or the number of days in reverse.
    input_date_reverse = sorted(input_date, key=lambda x: x[2])
    y1 = []
    x1 = []
    reverse_days = [3,5,7,10,30]
    # 'y1' is a list of lists with the average activies per day as sorted by 'reverse_days'.
    for i in range(len(reverse_days)):
      y_input_day = []
      x_input_day = []
      for ii in range(len(input_date_reverse)):
        if input_date_reverse[ii][2] == reverse_days[i]:
          y_input_day.append(input_date_reverse[ii][4]) # input_date_reverse[ii]
          date = input_date_reverse[ii][5]
          if len(date) == 3:
            month = date[0:1]
            day = date[1:]
          else:
            month = date[0:2]
            day = date[2:]
          if day[0] == '0':
            day = day[1]
          split_date = input_date_reverse[ii][0] + '\n' + month + '/' + day
          x_input_day.append(split_date)
      y1.append(y_input_day)
      x1.append(x_input_day)

    plt.figure(figsize=(8,6))
    # y = [j[4] for j in input_data]
    # plt.scatter(x, y) # scatterplot version without sorting.

    # 20250616-... Google Drive takes forever to update changes
    # to the spreadsheet, these are hardcoded.
    y1[1][7] = 4    # 20 /  5 instead of 21 / 5  = 4.2
    y1[2][5] = 4    # 28 /  7 instaed of 29 / 7  = 4.14
    y1[3][4] = 4.1  # 41 / 10 instead of 42 / 10 = 4.2
    y1[4][2] = 5.6  # 168/ 30 instead of 169/ 30 = 5.63
    
    for sub in range(len(y1)):
      if reverse_days[sub] < 6:
        plt.plot(x1[sub],y1[sub])
      plt.scatter(x1[sub],y1[sub],label=reverse_days[sub])
    # plt.ylim(0,8.5)
    plt.text(
        6,
        4,
        box_str,
        ha="center",
        va="bottom",
        size=8,
        bbox=dict(facecolor="white", edgecolor="black", boxstyle="round", alpha=0.75),
    )

    plt.legend(title='Days Before\n      Pain',title_fontsize=10,alignment='left',loc='upper left',fontsize=8,borderaxespad=1.2)
    plt.xlabel('Date (2024)', fontsize=10)
    plt.ylabel('Average per Day', fontsize=10)
    plt.title('Activities Before Pain')
    plt.grid()
    plt.margins(y=0.01)
    return

#################################################
# Part E: Part D visualization helper functions #
#################################################
# Merge sort is the fastest for worst case scenario sorting: N log(n)
# Implementation is from W3 and modified for AZ with ascii ord():
# https://www.w3schools.com/dsa/dsa_algo_mergesort.php
# Bubble sort is the fastest for almost sorted lists O(n)
# https://www.w3schools.com/dsa/dsa_timecomplexity_bblsort.php
# Python's built-in sort() function uses Tim Sort which uses a hybrid
# Insertion and Merge. Insertion is similar to Bubble with the same
# Time and Space complexity with worst case O(n^2) and best O(n).
class Graphs_sort:
  # Initialize the input variables
  def __init__(self, data):
    self.data = data

  # Filters the verb endings using c_replace().
  def filter_stop(self,column):
    filtered_column = []
    for i in column:
      if 'Walked' in i:
        filtered_column.append("Walk")
      elif 'Juggling' in i:
        filtered_column.append("Juggle")
      elif 'Driving' in i:
        filtered_column.append("Drive")

      # english hard idk
      elif 'Reading' in i:
        filtered_column.append("Read")
      elif 'Writing' in i:
        filtered_column.append("Write")
      elif 'No juggling' in i:
        filtered_column.append("No juggling")
      elif 'Running' in i:
        filtered_column.append("Run")
      elif 'Hiking' in i:
        filtered_column.append("Hike")
      elif 'Rested' in i:
        filtered_column.append("Rest")
      elif 'Stretched' in i:
        filtered_column.append("Stretch")

      elif i == 'Lifts':
        # Could append since this is hard coded but I wanted to test.
        verb_less = i.replace("s", "")
        # verb_less = self.c_replace(i, "s", "")
        filtered_column.append(verb_less)
      elif 'ing' in i:
        verb_less = i.replace("ing", "")
        # verb_less = self.c_replace(i, "ing", "")
        filtered_column.append(verb_less)
      else:
        filtered_column.append(i)
    return filtered_column

  # Calculates duration using end - start.
  def sort_time(self,activity,start,end):
    duration = ['Duration']
    for i in range(1,len(start)):
      # Checks to see if the Activity or Start column is empty.
      # if len(activity[i]) == 0 or len(start[i]) == 0:
      #  continue
      # Estimates sleep at 7 hours.
      dur = 0
      if 'Sleep' == activity[i]:
        dur = str(7*60)
      else:
        # Converts the '100' digits to '60' minutes in hours.
        # Gets the end hour.
        if len(end[i]) == 4:      # handles 1030 4 digits
          end_sub = end[i][:2]
        elif len(end[i]) == 3:    # handles 0930 3 digits
          end_sub = end[i][0]
        else:                     # handles 0030 2 digits
          end_sub = 0
        # Gets the start hour.
        if len(start[i]) == 4:    # handles 1030 4 digits
          start_sub = start[i][:2]
        elif len(start[i]) == 3:  # handles 0930 3 digits
          start_sub = start[i][0]
        else:                     # handles 0030 2 digits
          start_sub = 0
        # Subtracts 40 minutes since there are 60 in an hour not 100.
        if start_sub == end_sub:
          if int(end[i]) == int(start[i]):
            dur = str(5)
          else:
            dur = str(int(end[i]) - int(start[i]))
        else:
          # Turn over from one day to another.
          if int(end[i]) < int(start[i]):
            # First day's amount of hours (24 - the start time hour)
            first_day = 23 - int(start_sub)
            first_day_minutes = 60 - int(start[i][2:]) # the last two digits are the minutes
            # Second day's hours added to the first day's hours as 'dur' as minutes.
            if len(end[i]) == 4:
              second_day_minutes = end[i][2:]
            elif len(end[i]) == 3:
              second_day_minutes = end[i][1:]
            else: # There are no extra hours
              second_day_minutes = end[i]
            end_sub = end_sub + first_day
            hunid = (int(end_sub)) * 60 # hour difference converted to minutes
            dur = hunid + first_day_minutes + int(second_day_minutes)
          else:
            hunid = (int(end_sub) - int(start_sub)) * 40
            dur = str( ( int(end[i]) - int(start[i]) ) - hunid)
      duration.append(dur)
    return duration

  # Merge sorts a list splice of strings from 'sort_ascii()' based on 'ord()'
  # and returns them to 'sort_ascii()'.
  def merge(self,left_in,right_in):
      result = []
      result_activity = []
      result_id = []
      result_dur = []
      i = j = 0
      while i < len(left_in[1]) and j < len(right_in[1]):
        left = left_in[0][i]
        right = right_in[0][j]
        left_activity = left_in[1][i]
        right_activity = right_in[1][j]
        left_id = left_in[2][i]
        right_id = right_in[2][j]
        left_dur = left_in[3][i]
        right_dur = right_in[3][j]
        if left < right: # or (left_activity_replace == right_activity and left < right) ?
          result.append(left)
          result_activity.append(left_activity)
          result_id.append(left_id)
          result_dur.append(left_dur)
          i += 1
        elif left > right: # or left_activity == right_activity ?
          result.append(right)
          result_activity.append(right_activity)
          result_id.append(right_id)
          result_dur.append(right_dur)
          j += 1
        else:
          if len(left_activity) > len(right_activity):
            length = len(right_activity)
          else: # same length?
            length = len(left_activity)
          # Find where the two words are different at k.
          for k in range(1,length):
            if left_activity[k] != right_activity[k]:
              break
          # Handles when the comparison first words are the same but
          # one of the comparisons have a space and second word.
          left_ord = ord(left_activity[k])
          right_ord = ord(right_activity[k])
          if left_activity[:length] == right_activity[:length]:
            if length < len(right_activity):
              if left_activity == right_activity[:length]:
                left_ord = -1
                # Comparison right_activity[length:] is longer and different.
                right_ord = ord(right_activity[length:][0])
          if left_activity[:k] == right_activity[:k] and left_ord < right_ord:
            result.append(left)
            result_activity.append(left_activity)
            result_id.append(left_id)
            result_dur.append(left_dur)
            i += 1
          else:
            result.append(right)
            result_activity.append(right_activity)
            result_id.append(right_id)
            result_dur.append(right_dur)
            j += 1
      result.extend(left_in[0][i:])
      result.extend(right_in[0][j:])
      result_activity.extend(left_in[1][i:])
      result_activity.extend(right_in[1][j:])
      result_id.extend(left_in[2][i:])
      result_id.extend(right_in[2][j:])
      result_dur.extend(left_in[3][i:])
      result_dur.extend(right_in[3][j:])

      return [result,result_activity,result_id,result_dur]

  # def sort_ascii(self,time_ID,ord_list,activity_filter,duration):
  # todo: avoid modification of the input variables with 'input[:]'
  def sort_ascii(self,ord_list,activity_filter,time_ID,duration):
    length = len(time_ID) - 1
    step = 1
    while step < length:
      for i in range(1, length, 2 * step):
        # Time vs space trade off: if you want less space calculate the duration
        # with another loop before sorting. Otherwise, the End and Start columns
        # are included in sorting and space is linear * number of columns (4).
        left = [ord_list[i:i + step],activity_filter[i:i + step], time_ID[i:i + step], duration[i:i + step]]
        right = [ord_list[i + step:i + 2 * step],
                 activity_filter[i + step:i + 2 * step], time_ID[i + step:i + 2 * step], duration[i + step:i + 2 * step]]
        merged = self.merge(left, right)
        # Place the merged array back into the original array
        for j in range(len(merged[0])):
          ord_list[i + j] = merged[0][j]
          activity_filter[i + j] = merged[1][j]
          time_ID[i + j] = merged[2][j]
          duration[i + j] = merged[3][j]
      step *= 2  # Double the sub-array length for the next iteration
    return [activity_filter,time_ID,duration]

  # Returns the time_id and unique activity lists.
  def sort_unique_words(self,activity_col):
    # A0_length is 0-225
    activity_unique = []
    # Unique words in Activity
    for i in range(len(activity_col)):
      if activity_col[i] not in activity_unique:
        if len(activity_col[i]) == 0:
          continue
        else:
          activity_unique.append(activity_col[i])
    return activity_unique

  # Returns the sorted list into AZ bins. C esque syntax.
  # Dimensions: 'sort_unique_words' by the number of occurances in 'sort_ascii'.
  def sort_unique_bin(self,sort_unique_words,sort_ascii):

    # Once the word is different than the next word, bin the next
    # word (or words) since the list is already sorted.

    # Empty 'unique_bin' is generated with int. Could use '0's but these
    # are 0,1,2,...n!
    unique_bin = [
        [[x],[x]] for x in range(len(sort_unique_words))
        ]
    count = 0
    for i in range(len(sort_ascii[0])):
      # Avoids checking 'sort_ascii' past the length of the list.
      # print(count, unique_bin[count], len(sort_unique_words))
      if i == (len(sort_ascii[0])-1):
        # If there are exactly one entry in the final 'sort_unique_words',
        # 'count' of type 'int' is placed as two lists into the identifier list.
        if unique_bin[-1][0][0].__class__ == int:
          unique_bin[-1] = [[sort_unique_words[count]]]
        break
      if sort_ascii[0][i] == sort_ascii[0][i+1]:
        # Words are the same, 'count' does not get incremented.
        if unique_bin[count][0][0].__class__ == str:
          # If first key or 'unique_bin[count]' is str, don't include it.
          unique_bin[count].append([sort_ascii[0][i],sort_ascii[1][i],sort_ascii[2][i]])
        else:
          unique_bin[count] = [
              [sort_unique_words[count]],
              [sort_ascii[0][i],sort_ascii[1][i],sort_ascii[2][i]]
              ]
      elif (sort_ascii[0][i-1] != sort_ascii[0][i]) and (sort_ascii[0][i] != sort_ascii[0][i+1]):
        # Previous word and next word are different.
        unique_bin[count] = [
            [sort_unique_words[count]],
            [sort_ascii[0][i],sort_ascii[1][i],sort_ascii[2][i]]
            ]
        count += 1
      elif (sort_ascii[0][i-1] == sort_ascii[0][i]) and (sort_ascii[0][i] != sort_ascii[0][i+1]):
        # Previous word is the same, next word is different.
        unique_bin[count].append([sort_ascii[0][i],sort_ascii[1][i],sort_ascii[2][i]])
        count += 1
      else:
        count += 1
    # Append last element of sorted list onto the bin list at end
    unique_bin[-1].append([sort_ascii[0][-1],
                           sort_ascii[1][-1],
                           sort_ascii[2][-1]])
    return unique_bin

  # Orders 'int' or 'float' instead of strings.
  # secodnary todo use one list instead of several lists (also for sort_ascii())
  def merge_int(self, left, right):
    result_int = []
    result_activity = []
    i = j = 0
    while i < len(left[0]) and j < len(right[0]):
      if left[0][i] < right[0][j]:
        result_int.append(left[0][i])
        result_activity.append(left[1][i])
        i += 1
      else:
        result_int.append(right[0][j])
        result_activity.append(right[1][j])
        j += 1
    result_int.extend(left[0][i:])
    result_int.extend(right[0][j:])
    result_activity.extend(left[1][i:])
    result_activity.extend(right[1][j:])
    return [result_int, result_activity]
  
  # Orders list of only 'int' or 'float'. From W3 schools.
  def merge_sort_int(self,int_in,activity_in):
    # The splice everything is used to avoid modification
    # of the input variables.
    array_int = int_in[:]
    activity = activity_in[:]
    step = 1  # Starting with sub-arrays of length 1
    length = len(array_int) - 1
    while step < length:
      for i in range(0, length, 2 * step):
        left = [array_int[i:i + step],activity[i:i + step]]
        right = [array_int[i + step:i + 2 * step],activity[i + step:i + 2 * step]]
        merged = self.merge_int(left, right)
        # Place the merged array back into the original array
        for j in range(len(merged[0])):
          array_int[i + j] = merged[0][j]
          activity[i + j] = merged[1][j]
      step *= 2  # Double the sub-array length for the next iteration
    return [array_int,activity]

  # todo: use multiple variables
  # Merges entries if the first word in the string is the same. Uses C syntax.
  # If you're a stickler, replace 'for i in range()' with 'while iterator <= len(data)'
  def merge_similar_activities(self, sorted_list):
    # Specific formatting for this dataset.
    ######################################################################
    x = [i[0][0] for i in sorted_list[1:]] # or A0_sort_unique
    z = [len(k[1:]) for k in sorted_list[1:]] # frequency of each activity
    y = []
    # Calculate the hours for duration.
    for j in sorted_list[1:]:
      y_label = []
      for m in j[1:]:
        y_label.append(float(m[2]))
      y.append(round(sum(y_label) / 60, 4))
    # This is a bad method to avoid binning 'Skateboard paper' into
    # 'Skateboard' but I want to do the graphing.
    for ayy in range(len(x)):
      if x[ayy] == 'Skateboard paper':
        x[ayy] = 'paper Skateboard'
      if x[ayy] == 'Skateboard videos':
        x[ayy] = 'videos Skateboard'

    ######################################################################

    # Combining similar Activities. The dataset uses the same word plus
    # a number to denote multiple of the same activities on the same day.
    y_mean = round(sum(y) / float(len(y)), 4)
    count_0 = 0
    count_1 = 1
    root_bool = False

    # Time complexity is the number of Activities.
    #for count_0 in range(len(y)):
    x[count_0] = x[count_0]
    y[count_0] = y[count_0]
    z[count_0] = z[count_0]
    spliced = []
    while True:
      if count_1 == len(y):
        x[count_0] = x[count_0]
        y[count_0] = y[count_0]
        z[count_0] = z[count_0]
        break
      x[count_1] = x[count_1]
      y[count_1] = y[count_1]
      z[count_1] = z[count_1]
      x_0 = x[count_0].split(' ') # c_split
      x_1 = x[count_1].split(' ') # c_split
      # Comparison operators to find the first instance of the word.
      # i.e. 'Eat' followed by 'Eat 0', 'Eat 1', etc.
      if x_0[0] == x_1[0]:
        if x_1[1] != 'outside':
          if ' ' not in x[count_0]:
            #if len(x_1) < 3:
            if root_bool == False:
              root_pos = count_0
              root_bool = True
      if root_bool == True:
        # Skip merging 'Skateboard paper' and 'Skateboard videos'.
        if y[root_pos] != y[count_0]:
          # 'y' value at 'count_0' is cumulative
          y[root_pos] += y[count_0]
          z[root_pos] += z[count_0]
        # The first 'y' value at 'root_pos' is the same as the total.
        x[count_0] = x[root_pos]
        y[count_0] = y[root_pos]
        z[count_0] = z[root_pos]
      else:
        x[count_0] = x[count_0]
        y[count_0] = y[count_0]
        z[count_0] = z[count_0]
      # This checks to see if the word and next word are different or the next
      # word is the same and is has three or more words, 'root_bool' is False.
      if x_0[0] != x_1[0] or len(x_1) >= 3:
        if root_bool == True:
          extra_numbers = (count_0+1) - (root_pos+1)
          # 'spliced' numbers list gets three values that slice the remaining
          # identical words in another loop.
          spliced = spliced + [[(count_0-extra_numbers),count_0, extra_numbers]]
          # The values at 'root_pos' get set to the current value at 'count_0'.
          x[count_0-extra_numbers] = x[count_0]
          y[count_0-extra_numbers] = y[count_0]
          z[count_0-extra_numbers] = z[count_0]
          root_bool = False
      count_0 += 1
      count_1 += 1

    ######################################################################
    # Reorganizing the strings (bad method)
    # Also inserts '\n' breaks if the string is longer than 10 characters
    # and more than one word.
    for bay in range(len(x)):
      if x[bay] == 'paper Skateboard':
        x[bay] = 'Skateboard paper'
      if x[bay] == 'videos Skateboard':
        x[bay] = 'Skateboard videos'
      string_count = 0
      for cay in x[bay]:
        if string_count > 9:
          string_break = x[bay].split(' ')
          string_word_count = len(string_break)
          if string_word_count > 1:
            string_word_mid = round(string_word_count / 2)
            string_0_half = " ".join(string_break[:string_word_mid]) + '\n'
            string_1_half = " ".join(string_break[string_word_mid:])
            x[bay] = string_0_half + string_1_half
          break
        string_count += 1
    return [x,y,z,spliced]

  # Uses 'merge_similar_activities' to splice the data.
  def merge_activities_splice(self,merged_activiites):
    # Time complexities is the number of repeated words that are being merged.
    x = []
    y = []
    z = []
    spler = []
    for k in range(len(merged_activiites[3])+1): # or while the length is less than the
      # The end splice.
      if k == len(merged_activiites[3]):
        # spler = spler + [[middle_0,0]] <- checks that the numbers are correct
        x = x + merged_activiites[0][middle_0:]
        y = y + merged_activiites[1][middle_0:]
        z = z + merged_activiites[2][middle_0:]
        break
      # The first splice.
      if x == []:
        # spler = [[0,merged_activiites[3][k][0]+1]]
        x = merged_activiites[0][0:merged_activiites[3][k][0]+1]
        y = merged_activiites[1][0:merged_activiites[3][k][0]+1]
        z = merged_activiites[2][0:merged_activiites[3][k][0]+1]
        # This part is carried into the next splice.
        middle_0 = merged_activiites[3][k][0]+1 + merged_activiites[3][k][2]
      else: # The middle splices.
        # spler = spler + [[middle_0, merged_activiites[3][k][0]+1]]
        x = x + merged_activiites[0][middle_0:merged_activiites[3][k][0]+1]
        y = y + merged_activiites[1][middle_0:merged_activiites[3][k][0]+1]
        z = z + merged_activiites[2][middle_0:merged_activiites[3][k][0]+1]
        # This part is carried into the next splice.
        middle_0 = merged_activiites[3][k][0]+1 + merged_activiites[3][k][2]
    return [x,y,z]

  # Flips Horizontal list of lists to vertical. Similar to NumPy reshape().
  # Input test dimensions are seven days by eight categories.
  def direction_flipper(self, input):
    # Get some vert.
    count = 0
    count_ct = 0
    count_br = 0
    output = []
    activity_count = []
    while True:
      if count == len(input):
        # When 'count' reaches the length of the list of horizontal lists input,
        # append the vertical list.
        output.append(activity_count)
        # 'count' resets, 'count_ct' increases by one,
        # and a new nested list is declared.
        count = 0
        count_ct += 1
        activity_count = []
        if count_br == ((len(input[0])) * (len(input))):
          break
      # 'count_ct' stays the same each time and 'count' is incremented each
      # time to get the first value of each list.
      activity_count.append(input[count][count_ct])
      count += 1
      count_br += 1
    return output

  # Series of functions to find erroneous pain values in P1.csv and calculate the
  # number of activities before each pain.
  # Returns the abnormal pain entry.
  def erroneous_values(self,P1_vert_column):
    erroneous_values = [[P1_vert_column[0],'NA']]
    non_erroneous_values = [[P1_vert_column[0],'NA']]
    all_values = [[P1_vert_column[0],'NA']]
    for i in range(len(P1_vert_column)):
      if len(P1_vert_column[i]) > 1:
        continue
      # Append all values to calculate overall mean.
      all_values.append([P1_vert_column[i], i-1])
      # Not stamina and greater than 4 pain values and 'Day_ID' get sent
      # to the list of lists.
      if P1_vert_column[0] != 'Stm' and int(P1_vert_column[i]) > 3:
        erroneous_values.append([P1_vert_column[i], i-1])
      # If it is stamina, check for values 2 and less.
      elif P1_vert_column[0] == 'Stm' and int(P1_vert_column[i]) < 3:
        erroneous_values.append([P1_vert_column[i], i-1])
      else:
        # Otherwise it is a normal value.
        non_erroneous_values.append([P1_vert_column[i], i-1])
    return [erroneous_values,non_erroneous_values,all_values]

  # Calculates the activity frequency for each day in ~ 500 iterations.
  # Returns 'Day_ID', 'start', and 'end' for splicing in 'activity_reverse()'.
  def activity_frequency_splice(self):
    # Skips the first ten values, 'Day_ID' is '10' in P1.csv and
    # 'start' is the 'Time_ID' in A1.tsv. The first 10 days are discarded
    # because they are why the information was collected.
    start = 53
    activity_frequency = []
    # The 'data' is from the function's class and needs a boilerplate
    # value appended to return the entire length of the 'data' list.
    data = self.data[0]
    data.append('100')
    for i in range(start,len(data)):
      # Checks 'Day_ID' P1.csv against 'Time_ID' from A1.tsv.
      # If 'Day_ID' is not '' or the values in A1.tsv,
      # they must by an integer (as long as the first value
      # header 'Day_ID' is ignored).
      if len(data[i]) > 0:
        day_id = int(data[i])
        activity_frequency.append([day_id-1, start, i])
        # 'start' is set to the 'i' or the iterator, which resumes checking
        # the length of A1.tsv.
        start = i
    # Deletes the null first value.
    del activity_frequency[0]
    return activity_frequency

  # Function to find the number of activities [30,10,7,5,3] and
  # returns the ['Category', 'Day_ID', 'Number of Days', 'Activity Frequency', 'Frequency per Day']
  def activity_reverse(self,day_id,activity_frequency):
    counter = 0
    known_ID = int(day_id[2][1])
    activity_reverse = []
    for i in range(len(day_id)):
      if type(day_id[i][1]) == str:
        category = day_id[i][0] # the category
      elif type(day_id[i][1]) == int:
        if day_id[i][1] > 9:
          # The number of days in reverse.
          reverse_days = [3,5,7,10,30]
          # 'Day_ID' ignores the first 10 days by subtracting 10 from 'start' and 'end'.
          # activity_by_category = []
          for k in range(len(reverse_days)):
            # 'end' is set to the 'Day_ID' when calculating the first reverse day '3'
            # Otherwise, it is a subtracted 'known_ID' that is the previous 'start' value below.
            if reverse_days[k] == 3:
              end = day_id[i][1]
            else:
              end = known_ID
            start = day_id[i][1] - reverse_days[k]
            # print('start: ', start, ' = ', day_id[i][1], ' - ', reverse_days[k])
            # print('end: ', end)
            # Avoids calculating frequencies for the first 10 days.
            if start > 9:
              # The number of activities 'reverse_days[k]' from the pain observation.
              activity_total = 0
              for j in range(start-10,end-10):
                # Summation for the number of activities, 'reverse_days' (k) from pain observation.
                activity_difference = activity_frequency[j][2] - activity_frequency[j][1]
                # print('Activity calculating : ', activity_difference, ' = ', activity_frequency[j][2], ' - ', activity_frequency[j][1])
                activity_total += activity_difference
                counter += 1
              # 'known_ID' is used to avoid calculating frequencies that are already known
              # by using the previous start to avoid duplicated iterations.
              known_ID = start
              # If 'k' is greater than '0', the previous day range frequency difference
              # was already calcualted and is used to calculate the frequency, reducing
              # unnecessary iterations. If 'reverse_days[k]' is '5' the frequency is already
              # known for '3', the difference for days '4' and '5' are calculated and added
              # onto 'activity_previous'.
              if k > 0:
                activity_previous = activity_intermediate + activity_total
              else:
                activity_previous = activity_total
              # The previous total is held for the next iteration.
              # print('Activity Total = ', activity_previous)
              activity_intermediate = activity_previous
              # Calculate the 'Activity Frequency' and 'Days' to get the the average of each day.
              activity_day_mean = round(activity_previous / reverse_days[k],2)
              activity_reverse.append([category,day_id[i][1],reverse_days[k],activity_previous,activity_day_mean])
          # print(category,day_id[i][1],reverse_days[k],activity_previous)
          if i+1 == len(day_id):
            break
          # May or may not need this depending on the oscillatory mean of meridians along Neptune reflecting Sun farts.
          # known_ID = day_id[i+1][1]
          # Avoids when the only 'reverse_days[k]' is '30' and is the only
          # 'start' that's less than '9'. [3,5,7,10] have already been
          # calculated.
          #if known_ID == 'NA':
          #  known_ID = day_id[i+2][1]
          #print('known ID: ', known_ID)
    # print(counter) # ~472 iterations without skips or 250 with skipping already calculated differences.
    return activity_reverse

  # Function to find the mean for each day group [3,5,7,10,30] mean.
  def activity_group_mean(self,input_data):
    group_day = [3,5,7,10,30]
    group_mean_list = []

    for i in range(len(group_day)):
      group_sum = 0
      group_count = 0
      for j in range(len(input_data)):
        # When the 'group_day' is the same as the group day value in
        # the 'activity_frequency' as calculate by 'Day_ID', that '3' '5', etc
        # group sum and count is incremented by the frequency and count respectively.
        if group_day[i] == input_data[j][2]:
          group_sum += input_data[j][4]
          group_count += 1
      # Once all the '3', '5', or ... n is summized, that group day's mean is calculated.
      # Subtract one because there's an extra '0' value appended from 'activity_day_mean()'.
      group_mean = group_sum / (group_count - 1)
      group_mean_list.append([round(group_mean,2),group_day[i],group_count])

    return group_mean_list

#################################################
# Part F: Non-parametric Classification Metrics #
#################################################
# Inputs are observations and prediction columns.
# Assumes input has a header.
class classification_metrics:
  # true_positive  = true_positive   1  (true_positive 1 / true_positive 1 + fn4) or recall
  # true_negative  = true_negative   0  (true_negative 0 / true_negative 0 + false_positive 3)
  # false_positive = false_positive  3  predicted soreness, was not sore.
  #                                     false positive rate = false_positive 3 / false_positive 3 + true_negative 0
  # false_negative = false_negative  4  predicted not soreness, was sore
  # https://www.geeksforgeeks.org/metrics-for-machine-learning-model/#regression-evaluation-metrics
  # https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall
  '''
  print(P1_vert[0])
  print(P1_vert[1])
  print(P1_vert[2])
  # 0 6 7 8
  print(A1_vert[0]) # Day_ID
  print(A1_vert[6]) # Activity
  # print(A1_vert[7]) # Notes
  # print(A1_vert[8]) # Explaination
  '''
  def __init__(self,observations,predictions):
    # The input scale is 5-1 high pain to low pain (or stamina).
    # The original data was 1-5 high pain to low pain and was flipped
    # since it was confusing (except for stamina).
    self.observations = observations
    self.predictions = predictions

  def binary_classification(self):
    # Returns 0 (True Negative) 1 (True Positive) if prediction
    # matches observation. False Positive when prediction was soreness
    # and observation was no soreness (3). False Negative when the prediction
    # was no soreness and there was soreness (4).
    # Also returns the count for the classifications.
    true_negative = 0
    true_positive = 0
    false_positive = 0
    false_negative = 0
    binary = []
    for i in range(1,len(self.observations)):
      if self.observations[i] == self.predictions[i]:
        result = 1
        true_positive += 1
      else:
        if self.predictions[i] == 'NA' or self.observations[i] == 'NA':
          result = 0
        # False positive predicted 4 or 5 (high soreness) and was 1,2,3.
        elif int(self.predictions[i]) > 3 and int(self.observations[i]) <= 3:
          result = 3
          false_positive += 1
        # False negative predicted 1,2,3 (low soreness) and was 4 or 5.
        elif int(self.predictions[i]) <= 3 and int(self.observations[i]) > 3:
          result = 4
          false_negative += 1
        else:
          result = 0
          true_negative += 1
      binary.append(result)
    return [binary,true_negative,true_positive,false_positive,false_negative]

  def accuracy(self,binary):
    # Number of correct predictions / total, input is False/True 0/1.
    count = 0
    for i in binary:
      if i == 1:
        count += 1
    total = len(binary)
    result = count / total
    return result

  def precision(self,true_positive,false_positive):
    # precision = true_positive 1 / (true_positive 1 + false_positive 3)
    result = true_positive / (true_positive + false_positive)
    return result

  def recall(self,true_positive,false_negative):
    # (true_positive / true_positive + false_negative 4) or recall
    result = true_positive / (true_positive + false_negative)
    return result

  def f1_score(self,true_positive,false_positive,false_negative):
    # 2 * (precision * recall) / (precision + recall)
    # (2 true_positive) / (2 true_positive + false_positive 3 + false_negative)
    result = (2 * true_positive) / ((2*true_positive) + false_positive + false_negative)
    return result

  # After the previous n (10,7,5,3) days of activity frequency, use the non parametric
  # Wilcoxon's rank sum test to compare the two dependent or paired samples. The two
  # samples being compared are n days activity frequency with the entire dataset's activity
  # frequency. It is non-parametric because it is categorical or ordinal dataset and
  # not real world measurements, despite having over 30 observations.
  # https://www.stat.purdue.edu/~tqin/system101/method/method_wilcoxon_rank_sum_sas.htm
  # https://pmc.ncbi.nlm.nih.gov/articles/PMC4754273/
  
  # I think non-parametric statistics are stupid outside of a learning exercise and I elected
  # to do other things.
  def wilcoxon_rank_sum(self):
    return



