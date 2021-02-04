sample_indices = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

hts = ([203., 191., 185., 203., 193., 185., 173., 178., 191., 188.])

wts = ([441.,  65.,  90., 441., 122.,  88.,  61.,  81., 104., 108.])

# perform calculations using list comprehension
def calc_bmi_lists(sample_indices, hts, wts):

  # gather sample heights and weights as lists 
  s_hts = [hts[i] for i in sample_indices]
  s_wts = [wts[i] for i in sample_indices]

  # convert heights from cm to m and square with list comprehension 
  s_hts_m_sqr = [(ht / 100) ** 2 for ht in s_hts]

  # calculate bmi as list with list comprehension
  bmis  = [s_wts[i] / s_hts_m_sqr[i] for i in range(len(sample_indices))]

  return bmis 
