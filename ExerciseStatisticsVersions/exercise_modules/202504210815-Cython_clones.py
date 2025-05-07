# Functions mimicking Python built in methods written with C-like syntax.
class c_python_clones:
  # Initialize the input variables
  # def __init__(self, data):
  #  self.data = data

  def sort(self):
    # if int or float: sort by ints or float

    '''
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

    '''
    # if string and/or int: sort_ascii() -> merge()

    '''
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

    # Accepts a list 'ord_column' ASCII representation of the first character
    # for the 'activity_column', the string list 'activity_column'
    # to be sorted, and 'data' or the original CSV or TSV spreadsheet.
    def sort_ascii(self,ord_column,activity_column,data):
      column_length = len(data[0]) - 1
      # data_length = len(data) - 1
      step = 1
      while step < column_length:
        for i in range(1, column_length, 2 * step):
          left_data = [dsl[i:i + step] for dsl in data]
          right_data = [dsr[i + step:i + 2 * step] for dsr in data]
          left = [ord_column[i:i + step],activity_column[i:i + step],left_data]
          right = [ord_column[i + step:i + 2 * step],activity_column[i + step:i + 2 * step],right_data]
          merged = self.merge(left, right)
          # Place the merged array back into the original array
          for j in range(len(merged[0])):
            ord_column[i + j] = merged[0][j]
            activity_column[i + j] = merged[1][j]
            # data[i + j] = merged[2][j]
        step *= 2  # Double the sub-array length for the next iteration
      return [ord_column, activity_column] + data
    '''
    return

  # Not used: Returns the length of the input similar to len(element).
  def c_len(self, input):
    if input.__class__ == str or input.__class__ == list:
      total = 0
      for i in input:
        total += 1
    elif input.__class__ == int or input.__class__ == float:
      print("TypeError: object of type 'int' has no len()")
    return total

  # Not used: Returns the split string at subword similar to word.split(sub_word).
  def c_split(self,word,sub_word):
    j = len(sub_word) # sub_word_len
    word_len = len(word)
    start = 0
    split_return = []
    # Testing each 'word' with the length of the 'sub_word'.
    for i in range(word_len):
      sub_word_test = word[i:j]
      # If they match, append the sub string of the 'word'.
      if sub_word_test == sub_word:
        split_return.append(word[start:(j - len(sub_word))])
        start = i + len(sub_word)
      if j == (word_len):
        j = word_len
      else:
        j += 1
    # Append the remaining string after the final 'sub_word'.
    split_return.append(word[start:])
    return split_return

  # Not used: Input string and replace the word with the sub_word.
  # Similar to Python's string.replace(word,subword)
  def c_replace(self,string,word,sub_word):
    str_replace = ""
    word_len = len(word)
    str_len = len(string)
    count = 0
    for i in range(str_len-word_len+1):
      if string[count:word_len] == word:
        str_replace += sub_word
        count += len(word)
        word_len += len(word)
      else:
        str_replace += string[count]
        count += 1
        word_len += 1
    return str_replace

  # For stability they are not used.
  def c_min(self,array):
    smallest = array[0]
    for i in array:
      if i < smallest:
        smallest = i
    return smallest

  def c_max(self,array):
    largest = array[0]
    for i in array:
      if i > largest:
        largest = i
    return largest
  def c_sum(self,array):
    total = 0
    for i in array:
      total += i
    return total

  # todo
  def c_round(num):

    return

  # todo
  def c_append(item):

    return

  # todo
  def c_pop(list):

    return

  # todo
  def c_range(list):

    return