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

# In development
###############################################
# Part D: Data visualization with a RGB graph #
###############################################
# Matplotlib for color because otherwise you would have
# to write hardware code to avoid using Python or C libraries.
class Graphs_rgb_dev:
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
